#! /usr/bin/env python3
# coding: utf-8


from modelsp04.tournament import Tournament
from modelsp04.tournament import TournamentFinished

from viewsp04.tournamentview import TournamentView
from viewsp04.tournamentview import StartTournamentView
from viewsp04.tournamentview import ManagerTournamentView
from viewsp04.tournamentview import FinishedTournamentView


class TournamentController:
    """Le controlleur de tournoi."""

    def __init__(self, master_controller):
        """Initialisation de la classe TournamentController."""
        self.model = Tournament(self)
        self.model_finished = TournamentFinished(self)
        self.view = TournamentView(self)
        self.view_start = StartTournamentView(self)
        self.view_manage = ManagerTournamentView(self)
        self.view_finished = FinishedTournamentView(self)
        self.controller = master_controller

    def get_unserial_list_players(self):
        """Demande la désérialisation de la liste des joueurs."""
        return self.controller.get_unserial_list_players()

    def get_unserial_tournament_in_progress(self):
        """Demande la désérialisation du tournoi en cours."""
        in_progress = self.controller.get_tournament_in_progress()
        return self.model.unserial_tournament_in_progress(in_progress)

    def get_unserial_tournaments_finished(self):
        """Demande la désérialisation des tournois terminés."""
        list_finished = self.controller.get_tournaments_finished()
        return self.model_finished.unserial_tournaments_finished(list_finished)

    def get_len_tournaments_finished(self):
        """
        Demande le nombre de tournois terminés enregistrés.
        Sert pour déterminer l'index du prochain tournoi.
        """
        return self.controller.get_len_tournaments_finished()

    def get_player_exists(self, index_to_check):
        """
        Demande si les index joueurs renseignés par l'utilisateur (pour la
        création d'un nouveau tournoi) existent.
        """
        return self.controller.get_player_exists(index_to_check)

    def get_data_player(self, index_participant):
        """Demande les données d'un joueur selon son index."""
        return self.controller.get_data_player(index_participant)

    def display_view_home_page(self):
        """Demande la vue de la page d'accueil."""
        return self.controller.display_view_home_page()

    def display_view_start_tournament(self):
        """Demande la vue de création d'un nouveau tournoi."""
        return self.view_start.display_view_start_tournament()

    def display_winner_tournament(self, winner):
        # mettre un input pour permettre une pause dans l'affichage
        # quelque soit l'input, passer à la suite du script
        self.view_manage.display_winner_tournament(winner)
        pass

    def display_view_list_finished_tournaments(self):
        """Demande la vue de la lieste des tournois terminés."""
        return self.view_finished.display_view_list_finished_tournaments()

    def display_view_manage_tournament(self):
        """Demande la vue de management de tournoi."""
        return self.view_manage.display_view_manager_tournament()

    def add_tournament_in_progress(self, new_tournament):
        """Pour création et enregistrement d'un tournoi."""
        tournament_in_progress = self.model.add_tournament(new_tournament)
        return self.controller.add_tournament(tournament_in_progress)

    def new_tournament(self):
        """
        Récupére les différents inputs pour la création d'un nouveau tournoi.
        """
        new_tournament = []
        self.display_view_start_tournament()
        new_tournament.append(self.view_start.input_name())
        new_tournament.append(self.view_start.input_place())
        new_tournament.append(self.view_start.input_participant())
        new_tournament.append(self.view_start.input_round())
        new_tournament.append(self.view_start.input_time_control())
        new_tournament.append(self.view_start.input_description())
        return self.add_tournament_in_progress(new_tournament)

    def check_name(self, input_name):
        """Demande la validité de l'input_name."""
        check = self.model.check_name(input_name)
        if check == "true":
            return self.view_start.input_name("true")
        else:
            return check

    def check_place(self, input_place):
        """Demande la validité de l'input_place."""
        check = self.model.check_place(input_place)
        if check == "true":
            return self.view_start.input_place("true")
        else:
            return check

    def check_participant(self, input_participants):
        """Demande la validité de l'input participant."""
        check = self.model.check_participant(input_participants)
        if check == "true":
            return self.view_start.input_participant("true")
        else:
            return check

    def check_round(self, input_round):
        """Demande la validité de l'input round."""
        check = self.model.check_round(input_round)
        if check == "true":
            return self.view_start.input_round("true")
        else:
            return check

    def check_time_control(self, input_time_control):
        """Demande la validité de l'input time_control."""
        check = self.model.check_time_control(input_time_control)
        if check == "true":
            return self.view_start.input_time_control("true")
        else:
            return check

    def check_description(self, input_description):
        """Demande la validité de l'input description."""
        check = self.model.check_description(input_description)
        if check == "true":
            return self.view_start.display_description_default()
        else:
            return check

    def adding_score_round(self, matchs_round_to_close):
        """
        Pour affecter le score de match des participants, au score de round des
        participants (score non cumulés).
        """
        return self.model.adding_score_round(matchs_round_to_close)

    def designate_winner_tournament(self):
        """Pour désigner le vainqueur du tournoi."""
        # À faire.
        return self.model.designate_winner_tournament()

    def save_tournament(self, tournament_to_update):
        """Sauvegarde de tournoi dans la base de données (mise à jour)."""
        return self.controller.save_tournament(tournament_to_update)
