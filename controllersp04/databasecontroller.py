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

    def import_data_base(self):
        """
        Retourne une liste de dictionnaires contenant les players de la base de
        données, vers le master_controller.
        """
        dict_all_player = self.model.import_db_players()
        tournament_in_progress = self.model.import_db_tournament_in_progress()
        return dict_all_player, tournament_in_progress

    def add_player(self, new_player):
        """
        Envoi le nouveau joueur dans le model de la base de données, pour
        l'ajouter à la base de données.
        """
        return self.model.add_player(new_player)

    def add_tournament_in_progress(self, tournament_in_progress):
        return self.model.add_tournament_in_progress(tournament_in_progress)
        pass

    def closing_tournament(self):
        0
        return self.model.closing_tournament()