#! /usr/bin/env python3
# coding: utf-8


import re

from modelsp04.tournament import Tournament

from viewsp04.tournamentview import TournamentView
from viewsp04.tournamentview import StartTournamentView
from viewsp04.tournamentview import ManagerTournamentView


class TournamentController:

    def __init__(self, master_controller):
        """Initialise le tournament_controller."""
        self.model = Tournament(self)
        self.view = TournamentView(self)
        self.view_son1 = StartTournamentView(self)
        self.view_son2 = ManagerTournamentView(self)
        self.controller = master_controller
        pass

    def get_list_players(self):
        """
        Demande la liste de tous les joueurs enregistrés dans la base de données.
        """
        return self.controller.get_list_players()

    def get_participants(self):
        return self.model.get_participants()

    def display_view_start_tournament(self):
        """Demande la vue de création d'un nouveau tournoi."""
        return self.view_son1.display_view_start_tournament()
        # input_new_tournament = self.view_son1.display_view_start_tournament()
        # return self.add_tournament_in_progress(input_new_tournament)

    def display_view_finished_tournaments(self):
        input_new_tournament = "todo"
        pass
        return self.add_tournament_finished(input_new_tournament)

    def add_tournament_in_progress(self, new_tournament):
        """
        Envoi les données du tournoi en cours pour l'ajouter à la base de données.
        """
        tournament_in_progress = self.model.add_tournament(new_tournament)
        self.controller.add_tournament(tournament_in_progress)
        self.initialize_round(tournament_in_progress)
        return self.manage_tournament()

    def add_tournament_finished(self, input_new_tournament):
        pass

    def new_tournament(self):
        """
        Récupére les différents input pour la création d'un nouveau tournoi.
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

    def new_round(self):
        return self.controller.new_round()
        pass



    def check_participant(self, input_participants):
        """Demande la validité de l'input participant."""
        return self.model.check_participant(input_participants)

    def check_round(self, input_round):
        """demande la validité de l'input round."""
        if input_round == '':
            return 4
        elif input_round != '':
            if input_round.isdigit() == True:
                return int(input_round)
            else:
                return self.view_son1.input_round("TRUE")

    def check_match_in_round(self, input_match_in_round):
        """Demande la validité de l'input match_in_round."""
        if input_match_in_round.isdigit() == True:
            return int(input_match_in_round)
        else:
            return self.view_son1.input_match_in_round("TRUE")

    def check_time_control(self, input_time_control):
        """Demande la validité de l'input time_control."""
        while input_time_control != "0" \
                and input_time_control != "1" \
                and input_time_control != "2":
            return self.view_son1.input_time_control("TRUE")
        else:
            return int(input_time_control)

    def check_description(self, input_description):
        """Demande la validité de l'input description."""
        if input_description == '':
            return self.view_son1.description_default()
        else:
            return input_description





    def manage_tournament(self):
        in_progress = self.controller.get_tournament_in_progress()
        # participants_in_progress = self.model.get_participants_in_progress()
        self.tempo_matching(in_progress)
        # self.new_round()

        return self.view_son2.display_view_manager_tournament()

    def initialize_round(self, in_progress):
        self.controller.initialize_round(in_progress)
        pass



    def tempo_matching(self, tournament_in_progress):
        self.controller.tempo_matching()
        pass