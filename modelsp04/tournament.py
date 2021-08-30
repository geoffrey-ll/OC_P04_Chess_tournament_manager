#! /usr/bin/env python3
# coding: utf-8


import re


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
        self.match_in_round = match_in_round
        self.time_control = time_control
        self.description = description


    def add_tournament(self, new_tournament):
        if len(self.list_finished_tournaments) == 0:
            index = 1
        else:
            index = len(self.list_finished_tournaments + 1)
        name = new_tournament[0]
        place = new_tournament[1]

        participants = new_tournament[2]
        round = new_tournament[3]
        match_in_round = new_tournament[4]
        time_control = new_tournament[5]
        description = new_tournament[6]

        self.tournament_in_progress = Tournament("tournament_controller", index, name, place, participants, round, match_in_round, time_control, description)
        return self.tournament_in_progress

    def check_participant(self, input_participants):
        list_players = self.controller.get_list_players()
        print("liste des joueurs dans tournament", list_players)
        participants = re.findall("([0-9]+)", input_participants)
        participants_validate = {}

        for participant in participants:
            for player in list_players:
                if int(participant) == player["index"]:
                    participants_validate["player_index.{}".format(int(participant))] = player
                else:
                    pass
        if len(participants_validate) == len(participants):
            return participants_validate
        else:
            print("il faut pouvoir rajouter un joueur")

    def get_tournament_in_progress(self):
        pass

    def get_participants(self):
        list_players = self.controller.get_list_players()
        participants_in_progress = []
        idx_participants = self.tournament_in_progress.participants
        for key in idx_participants.keys():
            for player in list_players:
                if player.index == int(key):
                    participants_in_progress.append(player)
        return participants_in_progress

    def new_round(self, tournament_in_progress):
        pass

    def matching(self):
        pass