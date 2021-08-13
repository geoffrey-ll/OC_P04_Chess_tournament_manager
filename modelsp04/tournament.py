#! /usr/bin/env python3
# coding: utf-8


class Tournament:

    list_finished_tournaments = []
    tournament_in_progress = []

    def __init__(self, tournament_oontroller, index=int(), name="", place="", participants=list, round=4, match_in_round=int(), time_control=list, description=""):
        self.controller = tournament_oontroller

        self.index = index
        self.name = name
        self.place = place
        self.participants = participants
        self.round = round
        self.match_in_rond = match_in_round
        self.time_control = time_control
        self.description = description

    def import_db_tournaments(self, tournament_in_progress):
        self.tournament_in_progress.append(tournament_in_progress)
        print(self.tournament_in_progress)
        pass

    def add_tournament(self, input_new_tournament):
        if len(self.list_finished_tournaments) == 0:
            index = 1
        else:
            index = len(self.list_finished_tournaments + 1)
        name = input_new_tournament[0]
        place = input_new_tournament[1]
        participants = input_new_tournament[2]
        round = input_new_tournament[3]
        match_in_round = input_new_tournament[4]
        time_control = input_new_tournament[5]
        description = input_new_tournament[6]

        tournament = Tournament("tournament_controller", index, name, place, participants, round, match_in_round, time_control, description)
        self.tournament_in_progress.append(tournament)
        return tournament#, self.tournament_in_progress
