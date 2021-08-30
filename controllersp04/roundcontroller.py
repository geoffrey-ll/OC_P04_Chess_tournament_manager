#! /usr/bin/env python3
# coding: utf-8


from modelsp04.round import Round


class RoundController:
    def __init__(self, master_controller):
        self.model = Round(self)
        self.controller = master_controller
        pass

    def get_list_round(self):
        return self.controller.get_list_round()

    def add_round(self, round_in_progress):
        return self.controller.add_round(round_in_progress)
        pass


    def initialize_round(self, in_progress):
        self.model.initialize_round(in_progress)
        pass

    def get_round(self):
        return self.model.get_round()
        pass

    def get_participants(self):
        return self.controller.get_participants()

    def new_round(self):
        return self.model.new_round()
        pass

    def new_match(self, participant_1, participant_2):
        return self.controller.new_match(participant_1, participant_2)

    def save_round(self, round_update):
        return self.controller.save_round(round_update)

    def closing_round(self):
        pass

    def matching(self):
        return self.model.matching()