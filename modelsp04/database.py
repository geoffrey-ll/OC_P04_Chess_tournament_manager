#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB  # , Query


class DataBase:
    """Ceci est la base de données."""

    db = TinyDB('db.json')
    player = db.table('player')

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

    def add_player(self, new_player):
        """Ajoute le nouveau joueur dans la base de données."""
        dic = {}
        for key, value in new_player.__dict__.items():
            dic[key] = value
        self.player.insert(dic)
