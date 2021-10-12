#! /usr/bin/env python3
# coding: utf-8


import re

from modelsp04.tournament import Tournament

from viewsp04.tournamentview import TournamentView
from viewsp04.tournamentview import StartTournamentView
from viewsp04.tournamentview import ManagerTournamentView
from viewsp04.tournamentview import FinishedTournamentView


class TournamentController:

    def __init__(self, master_controller):
        """Initialise le tournament_controller."""
        self.model = Tournament(self)
        self.view = TournamentView(self)
        self.view_son1 = StartTournamentView(self)
        self.view_son2 = ManagerTournamentView(self)
        self.view_son3 = FinishedTournamentView(self)
        self.controller = master_controller
        pass

    def get_unserial_list_players(self):
        """
        Demande la liste de tous les joueurs enregistrés dans la base de données.
        """
        return self.controller.get_unserial_list_players()

    def get_unserial_tournament_in_progress(self):
        in_progress = self.controller.get_tournament_in_progress()
        return self.model.unserial_tournament_in_progress(in_progress)
        pass

    def get_player_exists(self, index_to_check):
        return self.controller.get_player_exists(index_to_check)
        pass


    def display_view_start_tournament(self):
        """Demande la vue de création d'un nouveau tournoi."""
        return self.view_son1.display_view_start_tournament()
        # input_new_tournament = self.view_son1.display_view_start_tournament()
        # return self.add_tournament_in_progress(input_new_tournament)

    def display_winner_tournament(self):
        # mettre un input pour permettre une pause dans l'affichage
        # quelque soit l'input, passer à la suite du script
        # self.view.display_winner_tournament()
        pass

    def display_view_list_finished_tournaments(self):
        return self.view
        pass
        # serait cool de pouvoir ajouter des tournois gérer sans le script
        # return self.add_tournament_finished(input_new_tournament)

    def display_view_manage_tournament(self):
        return self.view_son2.display_view_manager_tournament()


    def add_tournament_in_progress(self, new_tournament):
        """
        Envoi les données du tournoi en cours pour l'ajouter à la base de données.
        """
        tournament_in_progress = self.model.add_tournament(new_tournament)
        return self.controller.add_tournament(tournament_in_progress)


    def add_tournament_finished(self, input_new_tournament):
        pass


    def new_tournament(self):
        """
        Récupére les différents inputs pour la création d'un nouveau tournoi.
        """
        new_tournament = []
        self.display_view_start_tournament()
        new_tournament.append(self.view_son1.input_name())
        new_tournament.append(self.view_son1.input_place())
        new_tournament.append(self.view_son1.input_participant())
        new_tournament.append(self.view_son1.input_round())
        new_tournament.append(self.view_son1.input_match_in_round())
        new_tournament.append(self.view_son1.input_time_control())
        new_tournament.append(self.view_son1.input_description())

        return self.add_tournament_in_progress(new_tournament)


    def check_name(self, input_name):
        if input_name == '':
            return self.view_son1.input_name("TRUE")
        else:
            return input_name
        pass

    def check_place(self, input_place):
        if input_place == '':
            return self.view_son1.input_place("TRUE")
        else:
            return input_place
        pass


    def check_participant(self, input_participants):
        """Vérifie la validité de l'input participant."""
        index_to_check = re.findall("[0-9]+", input_participants)
        check = self.controller.get_player_exists(index_to_check)
        if check == "TRUE":
            return self.view_son1.input_participant("TRUE")
        else:
            return check

    def check_round(self, input_round):
        """Vérifie la validité de l'input round."""
        if input_round == '':
            return 4
        elif input_round != '':
            if input_round.isdigit() == True:
                return int(input_round)
            else:
                return self.view_son1.input_round("TRUE")

    def check_match_in_round(self, input_match_in_round):
        """Vérifie la validité de l'input match_in_round."""
        if input_match_in_round.isdigit() == True:
            return int(input_match_in_round)
        else:
            return self.view_son1.input_match_in_round("TRUE")

    def check_time_control(self, input_time_control):
        """Vérifie la validité de l'input time_control."""
        while input_time_control != '0' \
                and input_time_control != '1' \
                and input_time_control != '2':
            return self.view_son1.input_time_control("TRUE")
        else:
            return int(input_time_control)

    def check_description(self, input_description):
        """Vérifie la validité de l'input description."""
        if input_description == '':
            return self.view_son1.display_description_default()
        else:
            return input_description


    def adding_score_round(self, matchs_round_to_close):
        return self.model.adding_score_round(matchs_round_to_close)
        pass

    def tournament_manager(self):
        pass

        # in_progress = self.controller.get_tournament_in_progress()
        # participants_in_progress = self.model.get_participants_in_progress()
        # self.tempo_matching(in_progress)
        # self.new_round()


    # def initialize_round(self, in_progress):
    #
    #     return self.controller.initialize_round(in_progress)

    # def start_round(self):
    #     return self.controller.start_round()
    #     pass


    def designate_winner_tournament(self):
        return self.model.designate_winner_tournament()
        pass


    def tempo_matching(self, tournament_in_progress):
        self.controller.tempo_matching()
        pass


    def save_tournament(self, tournament_to_update):
        return self.controller.save_tournament(tournament_to_update)
        pass

