#! /usr/bin/env python3
# coding: utf-8


from modelsp04.match import Match


class MatchController:
    """"""

    def __init__(self, master_controller):
        self.model = Match(self)
        self.controller = master_controller

    def new_match(self, participant_1, participant_2):
        return self.model.new_match(participant_1, participant_2)