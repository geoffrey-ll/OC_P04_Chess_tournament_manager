#! /usr/bin/env python3
# coding: utf-8


class Match:
    """"""

    list_matchs_in_round = []

    def __init__(self, match_controller, participant_1='', participant_2=''):
        self.controller = match_controller

        self.participant_1 = participant_1
        self.participant_2 = participant_2
        pass

    def new_match(self, participant_1, participant_2):
        match = Match("match_controller", participant_1, participant_2)
        self.list_matchs_in_round.append(match)

        for m in self.list_matchs_in_round:
            print(m.participant_1.last_name, m.participant_2.last_name)