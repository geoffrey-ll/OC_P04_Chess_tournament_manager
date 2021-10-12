#! /usr/bin/env python3
# coding: utf-8


import re

from modelsp04.match import Match
from viewsp04.matchview import MatchView


class MatchController:
    """"""

    def __init__(self, master_controller):
        self.model = Match(self)
        self.view = MatchView(self)
        self.controller = master_controller

    def get_unserial_round_to_do(self):
        return self.controller.get_unserial_round_to_do()
        pass

    def get_unserial_round_in_progress(self):
        return self.controller.get_unserial_round_in_progress()
        pass

    def get_unserial_matchs_current_round(self):
        matchs_current_round_in_db = self.controller.get_matchs_current_round()
        return \
            self.model.unserial_matchs_current_round(matchs_current_round_in_db)
        pass


    def get_numbers_matchs_current_round(self):
        return self.controller.get_numbers_matchs_current_round()
        pass


    def display_view_home_page(self):
        return self.controller.display_view_home_page()
        pass

    def display_view_matchs_in_progress_round(self):
        return self.view.display_view_matchs_in_progress_round()
        pass


    def add_matchs(self, list_matchs_in_round):
        return self.controller.add_matchs(list_matchs_in_round)
        pass


    def initialize_matchs(self, matchs_in_round):
        return self.model.initialize_matchs(matchs_in_round)


    def check_input_number_match(self, user_input):
        list_matchs = self.get_unserial_matchs_current_round()
        count = 0
        for match in list_matchs:
            if user_input == re.findall("[0-9]+", match.name)[-1]:
                return user_input
            else:
                count += 1
        if count == len(list_matchs):
            return "MATCH_NO_EXIST"

        pass

    def check_status_round(self):
        return self.model.check_status_round()
        pass

    def designate_winner(self, selected_match, winner):
        list_matchs = self.get_unserial_matchs_current_round()
        for match in list_matchs:
            if [match.name] == re.findall(".+x{}".format(selected_match), match.name):
                self.assigment_winner(match, winner)
                self.awarding_points(match)
                self.save_match(match)

            continue
        pass

    def assigment_winner(self, match, winner):
        """Attention. Si le match est terminé et qu'un vainqueur est déjà assigné, choisir à nouveau un vainqueur remplacera le choix précédent."""
        return self.model.assigment_winner(match, winner)
        pass

    def awarding_points(self, match):
        return self.model.awarding_points(match)
        pass


    def round_to_close(self):
        matchs_round_to_close = self.get_unserial_matchs_current_round()
        return self.controller.round_to_close(matchs_round_to_close)
        pass

    def save_match(self, match_to_update):
        return self.controller.save_match(match_to_update)
        pass
