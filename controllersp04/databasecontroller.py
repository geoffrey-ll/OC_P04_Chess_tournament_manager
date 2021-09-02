#! /usr/bin/env python3
# coding: utf-8


from modelsp04.database import DataBase


class DataBaseController:
    """Le contrôlleur de la base de données."""

    def __init__(self, master_controller):
        """
        Initialise le contrôlleur de la base de données.
        """
        self.model = DataBase(self)
        self.controller = master_controller

    def get_list_players(self):
        """
        Demande la liste de tous les joueurs enregistrés dans la base de données.
        """
        return self.model.get_list_players()

    def get_len_players_in_db(self):
        """Demande le nombre de joueurs enregistrées dans la base de données."""
        return self.model.get_len_players_in_db()

    def get_tournament_in_progress_or_not(self):
        """Demande si un tournoi est en cours ou non."""
        return self.model.get_tournament_in_progress_or_not()

    def get_tournament_in_progress(self):
        """Demande les données du tournoi en cours."""
        return self.model.get_tournament_in_progress()

    def get_list_round(self):
        return self.model.get_list_round()

    def get_round_to_do(self):
        return self.model.get_round_to_do()

    def get_round_in_progress(self):
        return self.model.get_round_in_progress()
        pass

    def get_participants(self):
        return self.model.get_participants()
        pass

    def get_player_exists(self, index_to_check):
        return self.model.get_player_exists(index_to_check)
        pass


    def add_player(self, new_player):
        """
        Envoi le nouveau joueur dans le model de la base de données, pour
        l'ajouter à la base de données.
        """
        return self.model.add_player(new_player)

    def add_tournament_in_progress(self, tournament_in_progress):
        """Envoi les données du tournoi en cours vers la base de données."""
        return self.model.add_tournament_in_progress(tournament_in_progress)

    def add_round(self, round_in_progress):
        return self.model.add_round(round_in_progress)

    def closing_tournament(self):
        """Demande de transférer le tournoi clôturé vers les tournois finis."""
        return self.model.closing_tournament()

    def save_round(self, round_update):
        return self.model.save_round(round_update)