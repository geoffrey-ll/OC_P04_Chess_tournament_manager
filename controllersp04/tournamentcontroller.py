#! /usr/bin/env python3
# coding: utf-8


from modelsp04.tournament import Tournament

from viewsp04.tournamentview import TournamentView
from viewsp04.tournamentview import StartTournamentView
from viewsp04.tournamentview import ManagerTournamentView


class TournamentController:

    def __init__(self, master_controller):
        """"""
        self.model = Tournament(self)
        self.view = TournamentView(self)
        self.view_son1 = StartTournamentView(self)
        self.view_son2 = ManagerTournamentView(self)
        self.controller = master_controller
        pass

    def import_db_tournaments(self):
        pass

    def display_view_start_tournament(self):
        input_new_tournament = self.view_son1.display_view_start_tournament()
        return self.add_tournament(input_new_tournament)

    def display_view_finished_tournaments(self):
        pass

    def add_tournament(self, input_new_tournament):
        tournament_in_progress = self.model.add_tournament(input_new_tournament)
        return self.view_son2.display_view_manager_tournament()