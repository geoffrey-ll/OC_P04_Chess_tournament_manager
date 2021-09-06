#! /usr/bin/env python3
# coding: utf-8


import re


class Tournament:

    list_finished_tournaments = []
    tournament_in_progress = []

    def __init__(self, tournament_oontroller, index=int(), name="", place="", status_participants=list, round=4, match_in_round=int(), time_control=list, description=""):
        self.controller = tournament_oontroller

        self.index = index
        self.name = name
        self.place = place
        self.status_participants = status_participants
        self.round = round
        self.match_in_round = match_in_round
        self.time_control = time_control
        self.description = description


    def get_tournament_in_progress(self):
        pass



    def add_tournament(self, new_tournament):
        if len(self.list_finished_tournaments) == 0:
            index = 1
        else:
            index = len(self.list_finished_tournaments + 1)
        name = new_tournament[0]
        place = new_tournament[1]
        status_participants = new_tournament[2]
        round = new_tournament[3]
        match_in_round = new_tournament[4]
        time_control = new_tournament[5]
        description = new_tournament[6]

        self.tournament_in_progress = Tournament("tournament_controller", index,
                                                 name, place, status_participants,
                                                 round, match_in_round,
                                                 time_control, description)
        return self.tournament_in_progress


    def new_round(self, tournament_in_progress):
        pass





    def matching(self):
        pass