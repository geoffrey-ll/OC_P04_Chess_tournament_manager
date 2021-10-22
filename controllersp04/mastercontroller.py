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
        """Demande la désérialisation de la liste des joueurs."""
        return self.player_controller.get_unserial_list_players()

    def get_unserial_players_participants(self, players_participants_in_db):
        """Demande la désérialisation des participants du tournoi en cours."""
        return self.player_controller\
            .get_unserial_players_participants(players_participants_in_db)

    def get_unserial_tournament_in_progress(self):
        """Demande la désérialisation du tournoi en cours."""
        return self.tournament_controller.get_unserial_tournament_in_progress()

    def get_unserial_round_to_do(self):
        """Demande la désérialisation du prochain round à faire."""
        return self.round_controller.get_unserial_round_to_do()

    def get_unserial_round_in_progress(self):
        """Demande la désérialisation du round en cours."""
        return self.round_controller.get_unserial_round_in_progress()

    def get_tournament_in_progress_or_not(self):
        """Pour savoir si un tournoi est en cours ou pas."""
        return self.data_base_controller.get_tournament_in_progress_or_not()

    def get_round_to_do_or_not(self):
        """Pour savoir si il reste un round à faire."""
        return self.data_base_controller.get_round_to_do_or_not()

    def get_list_players(self):
        """Demande la liste de tous les joueurs enregistrés."""
        return self.data_base_controller.get_list_players()

    def get_data_player(self, index_participant):
        """Demande les données d'un joueur selon son index."""
        return self.data_base_controller.get_data_player(index_participant)

    def get_len_players_in_db(self):
        """
        Demande le nombre de joueurs enregistrés.
        Sert pour déterminer l'index du prochain nouveau joueur.
        """
        return self.data_base_controller.get_len_players_in_db()

    def get_tournament_in_progress(self):
        """Demande les données du tournoi en cours."""
        return self.data_base_controller.get_tournament_in_progress()

    def get_tournaments_finished(self):
        """Demande la liste des tournois terminés."""
        return self.data_base_controller.get_tournaments_finished()

    def get_len_tournaments_finished(self):
        """
        Demande le nombre de tournois terminés enregistrés.
        Sert pour déterminer l'index du prochain tournoi.
        """
        return self.data_base_controller.get_len_tournaments_finished()

    def get_list_rounds(self):
        """Demande la liste des rounds du tournoi en cours."""
        return self.data_base_controller.get_list_rounds()

    def get_round_to_do(self):
        """Demande les données du prochain round à faire (s'il en reste un)."""
        return self.data_base_controller.get_round_to_do()

    def get_round_in_progress(self):
        """Demande les données du round en cours."""
        return self.data_base_controller.get_round_in_progress()

    def get_matchs_current_round(self):
        """
        Demande les données des matchs de la round en cours (s'il y en a).
        """
        return self.data_base_controller.get_matchs_current_round()

    def get_status_participants(self):
        """Demande le status des participants du tournoi en cours."""
        return self.data_base_controller.get_status_participants()

    def get_players_participants(self):
        """Demande les données des joueurs participants au tournoi en cours."""
        return self.data_base_controller.get_players_participants()

    def get_index_participants(self):
        """Demande l'index des joueurs participants au tournoi en cours."""
        return self.data_base_controller.get_index_participants()

    def get_elo_participants(self):
        """Demande l'Elo des joueurs participants au tournoi en cours."""
        return self.data_base_controller.get_elo_participants()

    def get_player_exists(self, index_to_check):
        """
        Demande si les index joueurs renseignés par l'utilisateur (pour la
        création d'un nouveau tournoi) existent.
        """
        return self.data_base_controller.get_player_exists(index_to_check)

    def display_view_home_page(self):
        """
        Demande la vue de la page d'accueil.
        Les options de la page d'accueil diffèrent selon qu'un tournoi est en
        cours ou non.
        status est la pour ça.
        """
        return self.home_page_controller.display_view_home_page()

    def display_view_start_tournament(self):
        """Demande la vue de création d'un nouveau tournoi."""
        return self.tournament_controller.display_view_start_tournament()

    def display_view_list_finished_tournaments(self):
        """Demande la vue de la liste des tournois terminés."""
        return \
            self.tournament_controller.display_view_list_finished_tournaments()

    def display_view_list_players(self):
        """Demande la vue liste des joueurs."""
        return self.player_controller.display_view_list_players()

    def display_view_manage_tournament(self):
        """Demande la vue de mangement de tournoi."""
        return self.tournament_controller.display_view_manage_tournament()

    def display_view_matchs_in_progress_round(self):
        """Demande la vue des matchs de la round en cours."""
        return self.match_controller.display_view_matchs_in_progress_round()

    def add_player(self, new_player):
        """Enregistrement d'un player dans la base de données."""
        return self.data_base_controller.add_player(new_player)

    def add_tournament(self, tournament_in_progress):
        """
        Enregistrement du nouveau tournoi créé dans la base de données, en tant
        que tournoi en cours.
        """
        return self.data_base_controller\
            .add_tournament_in_progress(tournament_in_progress)

    def add_round(self, round_in_progress):
        """Enregistrement des rounds du tournoi dans la base de données."""
        return self.data_base_controller.add_round(round_in_progress)

    def add_matchs(self, list_matchs_in_round):
        """Enregistrement des matchs de round dans la base de données."""
        return self.data_base_controller.add_matchs(list_matchs_in_round)

    def new_tournament(self):
        """Demande les inputs pour créer un nouveau tournoi."""
        self.tournament_controller.new_tournament()
        in_progress = self.get_unserial_tournament_in_progress()
        self.initialize_round(in_progress)
        return self.tournament_manager()

    def initialize_round(self, in_progress):
        """Pour l'initialisation des rounds du tournoi."""
        return self.round_controller.initialize_round(in_progress)

    def initialize_matchs(self, matchs_in_round):
        """Initialisation des matchs de round."""
        return self.match_controller.initialize_matchs(matchs_in_round)

    def start_round(self):
        """Demande le démarrage d'un round."""
        return self.round_controller.start_round()

    def round_manager(self):
        """Demande le round manager."""
        return self.round_controller.round_manager()

    def tournament_manager(self):
        """Demande le tournament manager."""
        self.display_view_manage_tournament()
        return self.round_manager()

    def round_to_close(self, matchs_round_to_close):
        """Instructions pour la clôture du round."""
        self.round_controller.round_to_close(matchs_round_to_close)
        self.tournament_controller.adding_score_round(matchs_round_to_close)
        return self.round_manager()

    def save_match(self, match_to_update):
        """Sauvagarde d'un match dans la base de données (mise à jour)."""
        return self.data_base_controller.save_match(match_to_update)

    def save_round(self, round_to_update):
        """Sauvegarde d'un round dans la base de données (mise à jour)."""
        return self.data_base_controller.save_round(round_to_update)

    def save_tournament(self, tournament_to_update):
        """Sauvegarde de tournoi dans la base de données (mise à jour)."""
        return self.data_base_controller.save_tournament(tournament_to_update)

    def designate_winner_tournament(self):
        """Pour déterminer le vainqueur du tournoi."""
        return self.tournament_controller.designate_winner_tournament()

    def closing_tournament(self):
        """Instruction pour clôturer le tournoi en cours."""
        # winner = self.tournament_controller.designate_winner_tournament()
        self.data_base_controller.transfer_tournament_to_finished()
        self.data_base_controller.purge_tournament_in_progress()
        # self.tournament_controller.display_winner_tournament(winner)
        return self.display_view_home_page()

    def reinitialize_for_test(self):
        """
        Pour purger des tables dans la base de données (utile pendant dev).
        """
        return self.data_base_controller.reinitialize_for_test()
