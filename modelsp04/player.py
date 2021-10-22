#! /usr/bin/env python3
# coding: utf-8

import re
from operator import attrgetter


class Player:
    """Le model pour les joueurs."""

    list_all_players = []

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

    def unserial_list_players(self, list_players):
        """Désérialisation des joueurs."""
        self.list_all_players = []

        for player in list_players:
            index = player["index"]
            first_name = player["first_name"]
            last_name = player["last_name"]
            date_of_birth = player["date_of_birth"]
            gender = player["gender"]
            current_elo = player["current_elo"]

            player_in_db = Player("player_controller", index, first_name,
                                  last_name, date_of_birth, gender,
                                  current_elo)
            self.list_all_players.append(player_in_db)
        return self.list_all_players

    def add_player(self, input_new_player):
        """
        Créer un nouveau joueur à partir des inputs, puis envoi les données
        pour son insertion dans la base de données.
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

    @staticmethod
    def check_first_name(input_first_name):
        """Vérifie la validité de l'input first_name."""
        if input_first_name == '':
            return "true"
        else:
            return input_first_name

    @staticmethod
    def check_last_name(input_last_name):
        """Vérifie la validité de l'input last_name."""
        if input_last_name == '':
            return "true"
        else:
            return input_last_name

    @staticmethod
    def check_date_birth(input_date_birth):
        """Vérifie la validité de l'input date_birth."""
        number = re.findall("[0-9]+", input_date_birth)
        if len(number) == 3:
            if \
                    len(number[0]) == 4 \
                    and int(number[0]) >= 1900 \
                    and 0 < int(number[1]) < 13 \
                    and 0 < len(number[1]) < 3 \
                    and 0 < int(number[2]) < 32 \
                    and 0 < len(number[2]) < 3:

                if len(number[1]) == 1:
                    number[1] = str(0) + number[1]
                if number[1] == "02":
                    if int(number[2]) > 29:
                        return "true"
                if len(number[2]) == 1:
                    number[2] = str(0) + number[2]
                date_birth = number[0] + '.' + number[1] + '.' + number[2]
                return date_birth
            else:
                return "true"
        else:
            return "true"

    @staticmethod
    def check_gender(input_gender):
        """Vérifie la validité de l'input gender."""
        if input_gender == "M" or input_gender == "F":
            return input_gender
        else:
            return "true"

    @staticmethod
    def check_current_elo(input_current_elo):
        """Vérifie la validité de l'input current_elo."""
        number = re.findall("[0-9]+", input_current_elo)
        if len(number) == 1:
            if 0 < int(number[0]) < 2900:
                return -int(number[0])
            elif int(number[0]) >= 2900:
                return "inhuman"
            else:
                return "true"
        else:
            return "true"

    @staticmethod
    def sorting_default(list_players):
        """
        Tri la liste des joueurs de la base de données, par ordre croissant de
        leur index.
        """
        list_players.sort(key=attrgetter("index"))
        return list_players

    @staticmethod
    def sorting_alphabetical(list_players):
        """
        Tri la liste des joueurs de la base de données, par ordre croissant de
        leur last_name.
        """
        list_players.sort(key=attrgetter("last_name", "first_name",
                                         "current_elo", "index"))
        return list_players

    @staticmethod
    def sorting_elo(list_players):
        """
        Tri la liste des joueurs de la base de données, par ordre croissant de
        leur classement elo.
        """
        list_players.sort(key=attrgetter("current_elo", "last_name",
                                         "first_name", "index"))
        return list_players
