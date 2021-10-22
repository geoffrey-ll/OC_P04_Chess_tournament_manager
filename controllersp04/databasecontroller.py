#! /usr/bin/env python3
# coding: utf-8


from modelsp04.database import DataBase


class DataBaseController:
    """Le contrôlleur de la base de données."""

    def __init__(self, master_controller):
        """Initialisation de la classe DataBaseController"""
        self.model = DataBase(self)
        self.controller = master_controller

    def get_list_players(self):
        """Demande la liste de tous les joueurs enregistrés"""
        return self.model.get_list_players()

    def get_data_player(self, index_participant):
        """Demande les données d'un joueur selon son index"""
        return self.model.get_data_player(index_participant)

    def get_len_players_in_db(self):
        """
        Demande le nombre de joueurs enregistrées.
        Sert pour déterminer l'index du prochain nouveau joueur.
        """
        return self.model.get_len_players_in_db()

    def get_tournament_in_progress_or_not(self):
        """Pour savoir si un tournoi est en cours ou pas."""
        return self.model.get_tournament_in_progress_or_not()

    def get_round_to_do_or_not(self):
        """Pour savoir si il reste un round à faire."""
        return self.model.get_round_to_do_or_not()

    def get_tournament_in_progress(self):
        """Demande les données du tournoi en cours."""
        return self.model.get_tournament_in_progress()

    def get_tournaments_finished(self):
        """Demande la liste des tourrnois terminés."""
        return self.model.get_tournaments_finished()

    def get_len_tournaments_finished(self):
        """
        Demande le nombre de tournois terminés enregistrés.
        Sert pour déterminer l'index du prochain tournoi.
        """
        return self.model.get_len_tournaments_finished()

    def get_list_rounds(self):
        """Demande la liste des rounds du tournoi en cours."""
        return self.model.get_list_rounds()

    def get_round_to_do(self):
        """Demande les données du prochain round à faire (s'il en reste un)."""
        return self.model.get_round_to_do()

    def get_round_in_progress(self):
        """Demande les données du round en cours."""
        return self.model.get_round_in_progress()

    def get_matchs_current_round(self):
        """
        Demande les données des matchs de la round en cours (s'il y en a).
        """
        return self.model.get_matchs_current_round()

    def get_status_participants(self):
        """Demande le status des participants du tournoi en cours."""
        return self.model.get_status_participants()

    def get_players_participants(self):
        """Demande les données des joueurs participants au tournoi en cours."""
        return self.model.get_players_participants()

    def get_index_participants(self):
        """Demande l'index des joueurs participants au tournoi en cours."""
        return self.model.get_index_participants()

    def get_elo_participants(self):
        """Demande l'Elo des joueurs participants au tournoi en cours."""
        return self.model.get_elo_participants()

    def get_player_exists(self, index_to_check):
        """
        Demande si les index joueurs renseignés par l'utilisateur (pour la
        création d'un nouveau tournoi) existent.
        """
        return self.model.get_player_exists(index_to_check)

    def add_player(self, new_player):
        """Enregistrement d'un player dans la base de données."""
        return self.model.add_player(new_player)

    def add_tournament_in_progress(self, tournament_in_progress):
        """
        Enregistrement du nouveau tournoi créé dans la base de données, en tant
        que tournoi en cours.
        """
        return self.model.add_tournament_in_progress(tournament_in_progress)

    def add_round(self, round_in_progress):
        """Enregistrement des rounds du tournoi dans la base de données."""
        return self.model.add_round(round_in_progress)

    def add_matchs(self, list_matchs_in_round):
        """Enregistrement des matchs de round dans la base de données."""
        return self.model.add_matchs(list_matchs_in_round)

    def save_match(self, match_to_update):
        """Sauvegarde d'un match dans la base de données (mise à our)."""
        return self.model.save_match(match_to_update)

    def save_round(self, round_to_update):
        """Sauvegarde d'un round dans la base de données (mise à jour)."""
        return self.model.save_round(round_to_update)

    def save_tournament(self, tournament_to_update):
        """Sauvegarde de tournoi dans la base de données (mise à jour)."""
        return self.model.save_tournament(tournament_to_update)

    def transfer_tournament_to_finished(self):
        """
        Pour enregistrer le tournoi en cours dans a table des tournois terminés
        (à la clôture du tournoi en cours).
        """
        return self.model.transfer_tournament_to_finished()

    def purge_tournament_in_progress(self):
        """
        Purge la table de tournoi en cours (après sa fin et son enregistrement
        dans la table des tournois terminés).
        """
        return self.model.purge_tournament_in_progress()

    def reinitialize_for_test(self):
        """
        Pour purger des tables dans la base de données (utile pendant dev).
        """
        return self.model.reinitialize_for_test()
