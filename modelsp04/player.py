#! /usr/bin/env python3
# coding: utf-8


import operator as ope


class Player:
    """Ceci est la classe Player."""

    list_all_player = []

    def __init__(self, player_controller, index=int(), first_name="",
                 last_name="", date_of_birth="", gender="", current_elo=int()):
        """Initialisation de la classe Player."""
        self.controller = player_controller

        self.index = index
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.current_elo = current_elo

    def add_player(self, input_new_player):
        """
        Créer un nouveau joueur à partir des inputs, puis envoi les données pour
        son insertion dans la base de données.
        """
        index = self.controller.get_len_players_in_db() + 1
        first_name = input_new_player[0]
        last_name = input_new_player[1]
        date_of_birth = input_new_player[2]
        gender = input_new_player[3]
        current_elo = int(input_new_player[4])
        new_player = Player("player_controller", index, first_name, last_name,
                            date_of_birth, gender, current_elo)
        return new_player


    def sorting_default(self, list_players):
        """
        Tri la liste des joueurs de la base de données, par ordre croissant de
        leur index.
        """

        list_players.sort(key=ope.itemgetter('index'))
        return list_players


    def sorting_alphabetical(self, list_players):
        """
        Tri la liste des joueurs de la base de données, par ordre croissant de
        leur last_name.
        """

        list_players.sort(key=ope.itemgetter("last_name", "first_name", "current_elo", "index"))
        return list_players



    def sorting_elo(self, list_players):
        """
        Tri la liste des joueurs de la base de données, par ordre croissant de
        leur classement elo.
        """

        list_players.sort(key=ope.itemgetter("current_elo", "last_name", "first_name", "index"))
        return list_players


