#! /usr/bin/env python3
# coding: utf-8

import re

from modelsp04.player import Player

from viewsp04.playerview import PlayerView


class PlayerController:
    """Le controller des players."""

    def __init__(self, master_controller):
        """Initialise le player_ontroller."""
        self.view = PlayerView(self)
        self.model = Player(self)
        self.controller = master_controller

    def get_list_players(self):
        """
        Demande la liste de tous les joueurs enregistrés dans la base de données.
        """
        return self.controller.get_list_players()

    def get_len_players_in_db(self):
        """Demande le nombre de joeurs enregistrés dans la base de données."""
        return self.controller.get_len_players_in_db()

    def display_view_list_players(self):
        """Demande la vue list des players."""
        return self.view.display_view_list_players()

    def display_view_home_page(self):
        """Demande la vue de la page d'accueil."""
        return self.controller.display_view_home_page()

    def add_player(self, new_player, sorting_option):
        """
        Envoi les données d'un nouveau joueur pour l'ajouter à la base de données.
        """
        player = self.model.add_player(new_player)
        self.controller.add_player(player)
        return self.view.display_view_list_players(sorting_option)


    def new_player(self, sorting_option):
        """
        Récupére les différents inputs pour la création d'un nouveau joueur.
        """
        new_player = []
        new_player.append(self.view.input_first_name())
        new_player.append(self.view.input_last_name())
        new_player.append(self.view.input_date_birth())
        new_player.append(self.view.input_gender())
        new_player.append(self.view.input_current_elo())
        return self.add_player(new_player, sorting_option)


    def check_first_name(self, input_first_name):
        """Vérifie la validité de l'input first_name."""
        if input_first_name == '':
            return self.view.input_first_name("TRUE")
        else:
            return input_first_name

    def check_last_name(self, input_last_name):
        """Vérifie la validité de l'input last_name."""
        if input_last_name == '':
            return self.view.input_last_name("TRUE")
        else:
            return input_last_name

    def check_date_birth(self, input_date_birth):
        """Vérifie la validité de l'input date_birth."""
        number = re.findall("[0-9]+", input_date_birth)
        if len(number) == 3:
            if len(number[0]) == 4 and 0 < int(number[1]) < 13 and 0 < int(number[2]) < 32:
                if len(number[1]) == 1:
                    number[1] = str(0) + number[1]
                if len(number[2]) == 1:
                    number[2] = str(0) + number[2]
                date_birth = number[0] + '.' + number[1] + '.' + number[2]
                return date_birth
            else:
                return self.view.input_date_birth("TRUE")
        else:
            return self.view.input_date_birth("TRUE")

    def check_gender(self, input_gender):
        """Vérifie la validité de l'input gender."""
        if input_gender == "M" or input_gender == "F":
            return input_gender
        else:
            return self.view.input_gender("TRUE")

    def check_current_elo(self, input_current_elo):
        """Vérifie la validité de d'input current_elo."""
        number = re.findall("[0-9]+", input_current_elo)
        if len(number) == 1:
            if 0 < int(number[0]) < 2900:
                return -int(number[0])
            elif int(number[0]) >= 2900:
                return self.view.input_current_elo("INHUMAN")
            else:
                return self.view.input_current_elo("TRUE")
        else:
            return self.view.input_current_elo("TRUE")


    def sort_players(self, sorting_option):
        """Instructions pour récupérer et trier la liste des joueurs."""
        list_players = self.get_list_players()
        if sorting_option == "DEFAULT":
            return self.model.sorting_default(list_players)
        elif sorting_option == "ALPHABETICAL":
            return self.model.sorting_alphabetical(list_players)
        elif sorting_option == "ELO":
            return self.model.sorting_elo(list_players)
        else:
            pass


