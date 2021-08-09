#! /usr/bin/env python3
# coding: utf-8


from .databasecontroller import DataBaseController
from .playercontroller import PlayerController


class MasterController:
    """Le contrôlleur pour les contrôller tous."""

    def __init__(self):
        """
        Initialise le MastetrContrôlleur.
        Les différents controllers du projet sont initialisés ici.
        """
        self.data_base_controller = DataBaseController(self)
        self.player_controller = PlayerController(self)

    def import_db_players(self):
        """
        Retourne une liste de dictionnaires contenant les players de la base de
        données, vers le player_controller.
        """
        dict_all_player = self.data_base_controller.import_data_base()
        if dict_all_player == []:
            pass
        else:
            return self.player_controller.import_data_base(dict_all_player)

    def display_view_list_players(self):
        """Demande la vue liste des joueurs au player_controller."""
        return self.player_controller.display_view_list_players()

    def add_player(self, new_player):
        """
        Demande au data_base_controller d'ajouter un player à la base de données.
        """
        return self.data_base_controller.add_player(new_player)
