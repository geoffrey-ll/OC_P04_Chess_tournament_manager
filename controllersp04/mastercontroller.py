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


    def get_unserial_list_players(self):
        return self.player_controller.get_unserial_list_players()
        pass

    def get_unserial_players_participants(self, players_participants_in_db):
        return self.player_controller.get_unserial_players_participants(players_participants_in_db)
        pass

    def get_unserial_tournament_in_progress(self):
        return self.tournament_controller.get_unserial_tournament_in_progress()
        pass

    def get_unserial_round_to_do(self):
        return self.round_controller.get_unserial_round_to_do()
        pass

    def get_unserial_round_in_progress(self):
        return self.round_controller.get_unserial_round_in_progress()
        pass


    def get_tournament_in_progress_or_not(self):
        """Pour savoir si un tournoi est en cours ou pas."""
        return self.data_base_controller.get_tournament_in_progress_or_not()

    def get_round_to_do_or_not(self):
        return self.data_base_controller.get_round_to_do_or_not()
        pass

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

    def get_list_rounds(self):
        return self.data_base_controller.get_list_rounds()

    def get_round_to_do(self):
        return self.data_base_controller.get_round_to_do()

    def get_round_in_progress(self):
        return self.data_base_controller.get_round_in_progress()
        pass

    def get_matchs_current_round(self):
        return self.data_base_controller.get_matchs_current_round()
        pass

    def get_status_participants(self):
        return self.data_base_controller.get_status_participants()

    def get_players_participants(self):
        return self.data_base_controller.get_players_participants()
        pass

    def get_index_participants(self):
        return self.data_base_controller.get_index_participants()
        pass

    def get_elo_participants(self):
        return self.data_base_controller.get_elo_participants()
        pass

    def get_player_exists(self, index_to_check):
        return self.data_base_controller.get_player_exists(index_to_check)
        pass

    def get_numbers_matchs_current_round(self):
        return self.data_base_controller.get_numbers_matchs_current_round()
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

    def display_view_list_finished_tournaments(self):
        return self.tournament_controller.display_view_list_finished_tournaments()
        pass

    def display_view_list_players(self):
        """Demande la vue liste des joueurs au player_controller."""
        return self.player_controller.display_view_list_players()

    def display_view_manage_tournament(self):
        return self.tournament_controller.display_view_manage_tournament()

    def display_view_matchs_in_progress_round(self):
        return self.match_controller.display_view_matchs_in_progress_round()
        pass



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

    def add_matchs(self, list_matchs_in_round):
        return self.data_base_controller.add_matchs(list_matchs_in_round)
        pass


    def new_tournament(self):
        """Demande les inputs pour créer un nouveau tournoi."""
        self.tournament_controller.new_tournament()
        in_progress = self.get_unserial_tournament_in_progress()
        self.initialize_round(in_progress)
        return self.tournament_manager()






    def initialize_round(self, in_progress):
        return self.round_controller.initialize_round(in_progress)

    def initialize_matchs(self, matchs_in_round):
        self.match_controller.initialize_matchs(matchs_in_round)
        pass

    def start_round(self):
        return self.round_controller.start_round()
        pass

    def round_manager(self):
        return self.round_controller.round_manager()
        pass





    def tournament_manager(self):
        print("le reste à faire IN master_controller")
        self.display_view_manage_tournament()
        return self.round_manager()
        pass


    def round_to_close(self, matchs_round_to_close):
        self.round_controller.round_to_close(matchs_round_to_close)
        self.tournament_controller.adding_score_round(matchs_round_to_close)
        self.round_manager()
        pass



    def save_match(self, match_to_update):
        return self.data_base_controller.save_match(match_to_update)
        pass

    def save_round(self, round_to_update):
        return self.data_base_controller.save_round(round_to_update)

    def save_tournament(self, tournament_to_update):
        return self.data_base_controller.save_tournament(tournament_to_update)
        pass

    def designate_winner_tournament(self):
        self.tournament_controller.designate_winner_tournament()
        pass

    def closing_tournament(self):
        """"""
        self.tournament_controller.designate_winner_tournament()
        self.data_base_controller.transfer_tournament_to_finished()
        self.data_base_controller.purge_tournament_in_progress()
        self.tournament_controller.display_winner_tournament()
        self.display_view_home_page()




    def reinitialize_for_test(self):
        return self.data_base_controller.reinitialize_for_test()
        pass
