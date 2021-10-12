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


    def unserial_tournament_in_progress(self, in_progress):
        self.tournament_in_progress = []

        index = in_progress["index"]
        name = in_progress["name"]
        place = in_progress["place"]
        status_participants = in_progress["status_participants"]
        round = in_progress["round"]
        match_in_round = in_progress["match_in_round"]
        time_control = in_progress["time_control"]
        description = in_progress["description"]

        self.tournament_in_progress = Tournament("tournament_controller", index, name, place, status_participants, round, match_in_round, time_control, description)

        return self.tournament_in_progress
        pass



    def add_tournament(self, new_tournament):
        if len(self.list_finished_tournaments) == 0:
            index = 1
        else:
            # il faut demander le len à la base de données !!!!!
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





    def adding_score_round(self, matchs_round_to_close):
        in_progress = self.controller.get_unserial_tournament_in_progress()

        for match in matchs_round_to_close:
            try:
                idx_a = match.participant_a["index"]
                score_a = match.participant_a["score"]
                in_progress.status_participants["player_index_{}".format(idx_a)]["score"] += score_a
            except:
                continue

            try:
                idx_b = match.participant_b["index"]
                score_b = match.participant_b["score"]
                in_progress.status_participants["player_index_{}".format(idx_b)]["score"] += score_b
            except:
                continue

        return self.controller.save_tournament(in_progress)


    def designate_winner_tournament(self):
        tournament = self.controller.get_unserial_tournament_in_progress()
        for participant in tournament.status_participants:
            print("…")

        pass
