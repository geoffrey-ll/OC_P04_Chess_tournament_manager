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

    def import_data_base(self, dict_all_player):
        """
        Envoi la liste de dictionnaires, contenant les players de la base de
        données, vers le model player, afin de les ajouter à la liste des
        players du script.
        """
        return self.model.import_db_players(dict_all_player)

    def display_view_list_players(self):
        """Demande la vue list des players."""
        return self.view.display_view_list_players()

    def get_list_players(self, sorting_option):
        """Instructions pour récupérer la liste des joueurs."""
        if sorting_option == "DEFAULT":
            return self.model.sorting_default()
        elif sorting_option == "ALPHABETICAL":
            return self.model.sorting_alphabetical()
        elif sorting_option == "ELO":
            return self.model.sorting_elo()
        else:
            pass

    def add_player(self, sorting_option):
        """Instructions pour l'ajout d'un player."""
        input_new_player = self.view.add_player()
        new_player = self.model.add_player(input_new_player)
        self.controller.add_player(new_player)
        return self.view.display_view_list_players(sorting_option)
