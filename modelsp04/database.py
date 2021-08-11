#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB  # , Query


class DataBase:
    """Ceci est la base de données."""

    db = TinyDB("db.json")
    player = db.table("player")
    tournament_in_progress = db.table("tournament_in_progress")

    def __init__(self, database_controller):
        """Initialisation de la base de données"""
        self.controller = database_controller

    def import_db_players(self):
        """
        Extrait de la base de données, une liste de dictionnaires contenant les
        players, et les retourne vers le data_base_controller.
        """
        player_in_db = self.player
        dict_all_player = []
        for idx, player in enumerate(player_in_db):
            dict_all_player.append(player)
        return dict_all_player

    def import_db_tournament_in_progress(self):
        if self.tournament_in_progress == {}:
            pass
        else:
            """A faire plus condenser"""
            test = self.tournament_in_progress
            dict_test = []
            for idx, value in enumerate(test):
                dict_test.append(value)
            return dict_test

    def add_player(self, new_player):
        """Ajoute le nouveau joueur dans la base de données."""
        dic = {}
        for key, value in new_player.__dict__.items():
            dic[key] = value
        self.player.insert(dic)

    def add_tournament_in_progress(self, tournament_in_progress):
        dic = {}
        for key, value in tournament_in_progress.__dict__.items():
            dic[key] = value
        self.tournament_in_progress.insert(dic)
        pass