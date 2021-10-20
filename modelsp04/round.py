#! /usr/bin/env python3
# coding: utf-8


from operator import itemgetter
from operator import attrgetter
from math import floor as arrinf
from math import ceil as arrsup
from pprint import pprint as pp
import random
import re


class Round:
    rounds_in_progress = []


    def __init__(self, round_controller, name="",  match_in_round=int(), status_round="", status_participants=dict):
        self.controller = round_controller

        self.name = name
        self.match_in_round = match_in_round
        self.status_round = status_round
        self.status_participants = status_participants

        pass

    def unserial_list_rounds(self, list_rounds_in_db):
        self.rounds_in_progress = []
        for round in list_rounds_in_db:
            name = round["name"]
            match_in_round = round["match_in_round"]
            status_round = round["status_round"]
            status_participants = round["status_participants"]
            round_in_db = Round("round_controller", name, match_in_round, status_round, status_participants)
            self.rounds_in_progress.append(round_in_db)
        return self.rounds_in_progress

    def unserial_round(self, round_in_db):
        try:
            name = round_in_db["name"]
            match_in_round = round_in_db["match_in_round"]
            status_round = round_in_db["status_round"]
            status_participants = round_in_db["status_participants"]
            if status_round == "TO_DO":
                round_to_do = Round("round_controller", name, match_in_round, status_round, status_participants)
                return round_to_do
            elif status_round == "IN_PROGRESS":
                round_in_progress = Round("round_controller", name, match_in_round, status_round, status_participants)
                return round_in_progress
        except:
           print("aucun round ici")


        pass


    def get_list_rounds(self):
        return self.controller.get_list_rounds()

    def get_round_to_do(self):
        return self.controller.get_round_to_do()

    def get_round_in_progress(self):
        return self.controller.get_round_in_progress()
        pass

    def get_status_participants(self):
        return self.controller.get_status_participants()
        pass


    def add_round(self):
        return self.controller.add_round(self.rounds_in_progress)
        pass


    def initialize_round(self, in_progress):
        self.rounds_in_progress = []
        count_round = in_progress.round
        for count in range(count_round):
            name = "round_" + str(count + 1)
            match_in_round = in_progress.match_in_round
            status_round = "TO_DO"
            status_participants = in_progress.status_participants

            round = Round("round_controller", name, match_in_round, status_round, status_participants)
            self.rounds_in_progress.append(round)


        return self.add_round()



    def change_status_round(self):
        round_to_do = self.controller.get_unserial_round_to_do()
        round_to_do.status_round = "IN_PROGRESS"
        self.save_round(round_to_do)
        return round_to_do.name


    def change_status_round_finished(self):
        round_to_finished = self.controller.get_unserial_round_in_progress()
        round_to_finished.status_round = "FINISHED"
        return self.save_round(round_to_finished)
        pass


    def save_round(self, round_update):
        return self.controller.save_round(round_update)
        pass


    def data_participants(self):
        status_participants = self.controller.get_status_participants()
        players_participants = \
            self.controller.get_unserial_players_participants()
        data_participants = []

        for player in players_participants:
            for key, value in status_participants["player_index_{}".format(player.index)].items():
                setattr(player, key, value)
            player.current_elo = -player.current_elo
            data_participants.append(player)

        return data_participants
        pass

    def sorting_participants(self, data_participants):
        data_participants.sort(key=attrgetter("score", "current_elo", "last_name", "first_name", "date_of_birth"), reverse=True)
        sorted_participants = data_participants
        return sorted_participants
        pass




    def subgroups(self, sorted_participants):
        subgroup_participants = {}

        count_group_s1 = int(arrinf(len(sorted_participants) / 2))
        subgroup_participants["group_s1"] = sorted_participants[:count_group_s1]
        subgroup_participants["group_s2"] = sorted_participants[count_group_s1:]

        return subgroup_participants
        pass

    def matching_round_1(self, subgroup_participants):
        matching = []

        for participant in range(len(subgroup_participants["group_s1"])):
            self.assigment_color(subgroup_participants["group_s1"][participant],
                                 subgroup_participants["group_s2"][participant])
            self.assigment_opponent(subgroup_participants["group_s1"][participant],
                                    subgroup_participants["group_s2"][participant])
            matching.append((subgroup_participants["group_s1"][participant],
                             subgroup_participants["group_s2"][participant]))

        if len(subgroup_participants["group_s1"]) \
                < len(subgroup_participants["group_s2"]):
            self.assigment_color(subgroup_participants["group_s2"][-1],
                                 "exempt")
            self.assigment_opponent(subgroup_participants["group_s2"][-1],
                                    "exempt")
            self.assigment_score_exempt(subgroup_participants["group_s2"][-1])
            matching.append((subgroup_participants["group_s2"][-1], "exempt"))

        return matching
        pass

    def assigment_color(self, participant_a, participant_b):
        random_color = random.randint(0, 1)
        if participant_b == "exempt":
            participant_a.colors.append("exempt")
        else:
            if random_color == 0:
                participant_a.colors.append("white")
                participant_b.colors.append("black")
            if random_color == 1:
                participant_a.colors.append("black")
                participant_b.colors.append("white")

        pass

    def assigment_opponent(self, participant_a, participant_b):
        if participant_b == "exempt":
            participant_a.opponent_index.append("exempt")
        else:
            participant_a.opponent_index.append(participant_b.index)
            participant_b.opponent_index.append(participant_a.index)
        pass

    def assigment_score_exempt(self, participant_exempt):
        participant_exempt.score = 1

        pass

    def matching_other_round(self, sorted_participants):
        matching = []

        for count_a in range(len(sorted_participants)):
            match = "no_ok"
            count_b = count_a + 1
            while match == "no_ok" and count_b < len(sorted_participants):
                response_1 = self.check_no_in_match(matching, sorted_participants[count_a], sorted_participants[count_b])
                if response_1 == "pass":
                    match = "ok"
                elif response_1 == "continue":
                        count_b += 1
                elif response_1 == "no_in_match":
                    response_2 = self.check_no_meet(sorted_participants[count_a], sorted_participants[count_b])
                    if response_2 == "continue":
                        count_b += 1
                    elif response_2 == "no_meet":
                        self.assigment_color(sorted_participants[count_a],
                                             sorted_participants[count_b])
                        self.assigment_opponent(sorted_participants[count_a],
                                                sorted_participants[count_b])
                        matching.append((sorted_participants[count_a],
                                         sorted_participants[count_b]))
                        match = "ok"
            if len(matching) != arrsup(len(sorted_participants)/2):
                if match == "no_ok" and count_b >= len(sorted_participants):
                    self.assigment_color(sorted_participants[count_a], "exempt")
                    self.assigment_opponent(sorted_participants[count_a], "exempt")
                    self.assigment_score_exempt(sorted_participants[count_a])
                    matching.append((sorted_participants[count_a], "exempt"))

        return matching
        pass

    def check_no_in_match(self, matching, participant_a, participant_b):
        if matching == []:
            return "no_in_match"
        else:
            for match in matching:
                for participant in match:
                    if participant_a.index == participant.index:
                        return "pass"
                    elif participant_b.index == participant.index:
                        return "continue"
            else:
                return "no_in_match"
        pass

    def check_no_meet(self, participant_a, participant_b):
        for opponent in participant_a.opponent_index:
            if opponent == participant_b.index:
                return "continue"

        return "no_meet"
        pass



    def adding_score_match(self, matchs_round_to_close):
        round_to_close = self.controller.get_unserial_round_in_progress()

        for match in matchs_round_to_close:
            try:
                idx_a = match.participant_a["index"]
                score_a = match.participant_a["score"]
                round_to_close.status_participants["player_index_{}".format(idx_a)]["score"] = score_a
            except:
                continue

            try:
                idx_b = match.participant_b["index"]
                score_b = match.participant_b["score"]
                round_to_close.status_participants["player_index_{}".format(idx_b)]["score"] = score_b
            except:
                continue

        return self.controller.save_round(round_to_close)

        pass

