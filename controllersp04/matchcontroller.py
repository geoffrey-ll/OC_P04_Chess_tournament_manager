#! /usr/bin/env python3
# coding: utf-8


import re

from modelsp04.match import Match
from viewsp04.matchview import MatchView


class MatchController:
    """Le controller de matchs."""

    def __init__(self, master_controller):
        """Initialisation de la classe MatchController."""
        self.model = Match(self)
        self.view = MatchView(self)
        self.controller = master_controller

    def get_unserial_round_to_do(self):
        """Demande la désérialisation du prochain round à faire."""
        return self.controller.get_unserial_round_to_do()

    def get_unserial_round_in_progress(self):
        """Demande la désérialisation du round en cours."""
        return self.controller.get_unserial_round_in_progress()

    def get_unserial_matchs_current_round(self):
        """Demande la désérialisation des matchs du round en corus."""
        matchs_current_round_in_db = self.controller.get_matchs_current_round()
        return \
            self.model.unserial_matchs_current_round(matchs_current_round_in_db)

    def display_view_home_page(self):
        """Demande la vue de la page d'accueil."""
        return self.controller.display_view_home_page()

    def display_view_matchs_in_progress_round(self):
        """Demande la vue des matchs du round en cours."""
        return self.view.display_view_matchs_in_progress_round()

    def add_matchs(self, list_matchs_in_round):
        """Pour l'enregistrement des matchs du round dans la base de données."""
        return self.controller.add_matchs(list_matchs_in_round)

    def initialize_matchs(self, matchs_in_round):
        """Demande l'initialisation des matchs du round."""
        return self.model.initialize_matchs(matchs_in_round)

    def check_input_number_match(self, user_input):
        """Demande que le match dont on veut désigner le vainqueur, existe."""
        return self.model.check_input_number(user_input)

    def check_status_round(self):
        """Demande si tous les matchs du round sont terminés ou pas."""
        return self.model.check_status_round()

    def designate_winner(self, selected_match, winner):
        """Instructions pour désigner le vainqueur d'un match."""
        list_matchs = self.get_unserial_matchs_current_round()
        for match in list_matchs:
            if [match.name] == re.findall(".+x{}".format(selected_match),
                                          match.name):
                self.assigment_winner(match, winner)
                self.awarding_points(match)
                self.save_match(match)
            continue

    def assigment_winner(self, match, winner):
        """
        Pour indiquer le résultat d'un match.
        Attention. Si le match est terminé et qu'un vainqueur est déjà assigné,
        choisir à nouveau un vainqueur remplacera le choix précédent.
        """
        return self.model.assigment_winner(match, winner)

    def awarding_points(self, match):
        """Pour attribution les poins de match aux participants d'un match."""
        return self.model.awarding_points(match)

    def round_to_close(self):
        """Instructions pour la clôture d'un round."""
        matchs_round_to_close = self.get_unserial_matchs_current_round()
        return self.controller.round_to_close(matchs_round_to_close)

    def save_match(self, match_to_update):
        """Sauvegarde d'un match dans la base de données (mise à jour)."""
        return self.controller.save_match(match_to_update)
