#! /usr/bin/env python3
# coding: utf-8


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

    def add_player(self, sorting_option):
        """
        Envoi les données d'un nouveau joueur pour l'ajouter à la base de données.
        """
        input_new_player = self.view.add_player()
        new_player = self.model.add_player(input_new_player)
        self.controller.add_player(new_player)
        return self.view.display_view_list_players(sorting_option)

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


