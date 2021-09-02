#! /usr/bin/env python3
# coding: utf-8


from .databasecontroller import DataBaseController
from .homepagecontroller import HomePageController
from .playercontroller import PlayerController
from .tournamentcontroller import TournamentController
from .roundcontroller import RoundController
from .matchcontroller import MatchController


class MasterController:
    """Le contrôlleur pour les contrôller tous."""

    def __init__(self):
        """
        Initialise le MastetrContrôlleur.
        Les différents controllers du projet sont initialisés ici.
        """
        self.data_base_controller = DataBaseController(self)
        self.home_page_controller = HomePageController(self)
        self.player_controller = PlayerController(self)
        self.tournament_controller = TournamentController(self)
        self.round_controller = RoundController(self)
        self.match_controller = MatchController(self)




    def get_tournament_in_progress_or_not(self):
        """Pour savoir si un tournoi est en cours ou pas."""
        return self.data_base_controller.get_tournament_in_progress_or_not()

    def get_list_players(self):
        """
        Demande au data_base_controller la liste de tous les joueurs enregistrés.
        """
        return self.data_base_controller.get_list_players()

    def get_len_players_in_db(self):
        """Demande au data_base_controller le nombre de joeurs enregistrées."""
        return self.data_base_controller.get_len_players_in_db()

    def get_tournament_in_progress(self):
        """Demande au data_base_controller, les données du tournoi en cours."""
        return self.data_base_controller.get_tournament_in_progress()

    def get_list_round(self):
        return self.data_base_controller.get_list_round()

    def get_round_to_do(self):
        return self.data_base_controller.get_round_to_do()

    def get_round_in_progress(self):
        return self.data_base_controller.get_round_in_progress()
        pass

    def get_participants(self):
        return self.data_base_controller.get_participants()

    def get_player_exists(self, index_to_check):
        return self.data_base_controller.get_player_exists(index_to_check)
        pass


    def display_view_home_page(self):
        """
        Demande la vue de la page d'accueil au home_page_controller.

        Les options de la page d'accueil diffèrent selon qu'un tournoi est en
        cours ou non.

        status est la pour ça.
        """
        status = self.get_tournament_in_progress_or_not()
        return self.home_page_controller.display_view_home_page(status)

    def display_view_start_tournament(self):
        """Demande la vue de démarrage d'un tournoi au tournament_controller."""
        return self.tournament_controller.display_view_start_tournament()

    def display_view_finished_tournaments(self):
        pass

    def display_view_list_players(self):
        """Demande la vue liste des joueurs au player_controller."""
        return self.player_controller.display_view_list_players()

    def display_view_manage_tournament(self):
        return self.tournament_controller.display_view_manage_tournament()


    def add_player(self, new_player):
        """
        Demande au data_base_controller d'ajouter un player à la base de données.
        """
        return self.data_base_controller.add_player(new_player)

    def add_tournament(self, tournament_in_progress):
        """
        Demande au data_base_controller d'ajouter le nouveau tournoi crée dans
        la base de données, en tant que tournoi en cours.
        """
        return self.data_base_controller\
            .add_tournament_in_progress(tournament_in_progress)

    def add_round(self, round_in_progress):
        return self.data_base_controller.add_round(round_in_progress)


    def new_tournament(self):
        """Demande les inputs pour créer un nouveau tournoi."""
        self.tournament_controller.new_tournament()
        in_progress = self.get_tournament_in_progress()
        self.initialize_round(in_progress)
        self.start_round()
        return self.tournament_controller.display_view_manage_tournament()

    def new_match(self, participant_1, participant_2):
        return self.match_controller.new_match(participant_1, participant_2)

    # def new_round(self):
    #     return self.round_controller.new_round()





    def initialize_round(self, in_progress):
        return self.round_controller.initialize_round(in_progress)

    def start_round(self):
        return self.round_controller.start_round()
        pass

    def round_manager(self):
        return self.round_controller.round_manager()
        pass


    def closing_tournament(self):
        """Demande au data_base_controller de supprimer le tournoi en cours."""
        return self.data_base_controller.closing_tournament()


    def tournament_manager(self):
        self.display_view_manage_tournament()
        print("le reste à faire IN master_controller")
        self.round_manager()
        self.get_tournament_in_progress()
        return self.tournament_controller.tournament_manager()


    def save_round(self, round_update):
        return self.data_base_controller.save_round(round_update)


    def test(self):
        return

    def tempo_matching(self):
        return self.round_controller.matching()