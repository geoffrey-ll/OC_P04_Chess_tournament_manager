#! /usr/bin/env python3
# coding: utf-8


import re


class Match:
    """"""

    list_matchs_in_round = []

    def __init__(self, match_controller, name='', status_match='', participant_a=dict, participant_b=dict, winner_index=int()):
        self.controller = match_controller

        self.name = name
        self.status_match = status_match
        self.participant_a = participant_a
        self.participant_b = participant_b
        self.winner_index = winner_index
        pass

    def unserial_matchs_current_round(self, matchs_current_round_in_db):
        self.list_matchs_in_round = []
        for match in matchs_current_round_in_db:
            name = match["name"]
            status_match = match["status_match"]
            participant_a = match["participant_a"]
            participant_b = match["participant_b"]
            winner_index = match["winner_index"]

            match_in_progress = Match("match_controller", name, status_match, participant_a, participant_b, winner_index)

            self.list_matchs_in_round.append(match_in_progress)
        return self.list_matchs_in_round
        pass


    def initialize_matchs(self, matchs_in_round):
        self.list_matchs_in_round = []
        round_in_progress = self.controller.get_unserial_round_in_progress()
        count = int(re.findall("[0-9]+", round_in_progress.name)[0]) - 1
        for level_matchs in matchs_in_round:
            for match in level_matchs:

                name = self.name_of_match()
                if match[0] == "exempt" or match[1] == "exempt":
                    status_match = "FINISHED"
                else:
                    status_match = "IN_PROGRESS"

                participant_a = self.which_participant(match[0], count)
                participant_b = self.which_participant(match[1], count)

                if participant_a == "exempt":
                    winner_index = participant_b["index"]
                elif participant_b == "exempt":
                    winner_index = participant_a["index"]
                else:
                    winner_index = int()

                ini = Match("match_controller", name, status_match, participant_a, participant_b, winner_index)
                self.list_matchs_in_round.append(ini)

        return self.add_matchs()

        pass

    def name_of_match(self):
        round_in_progress = self.controller.get_unserial_round_in_progress()
        number_round = re.findall("[0-9]+", round_in_progress.name)
        name = "match_{}x{}".format(number_round[0],
                                    len(self.list_matchs_in_round) + 1)
        return name
        pass

    def which_participant(self, participant_object, count):
        participant_ = {}
        if participant_object != "exempt":
            player_ = participant_object
            for attr in player_.__dict__:
                if attr == "index":
                    participant_[attr] = player_.__getattribute__(attr)
                if attr == "first_name":
                    participant_[attr] = player_.__getattribute__(attr)
                if attr == "last_name":
                    participant_[attr] = player_.__getattribute__(attr)
                if attr == "current_elo":
                    participant_[attr] = player_.__getattribute__(attr)
                if attr == "score":
                    participant_[attr] = player_.__getattribute__(attr)
                if attr == "colors":
                    participant_[attr] = player_.__getattribute__(attr)[count]
                if attr == "opponent_index":
                    participant_[attr] = player_.__getattribute__(attr)[count]
        else:
            participant_ = "exempt"
        return participant_
        pass


    def add_matchs(self):
        return self.controller.add_matchs(self.list_matchs_in_round)
        pass

    def assigment_winner(self, match, winner):
        if winner == "G":
            match.winner_index = match.participant_a["index"]
            match.status_match = "FINISHED"
        elif winner == "N":
            match.winner_index = "nul"
            match.status_match = "FINISHED"
        elif winner == "D":
            match.winner_index = match.participant_b["index"]
            match.status_match = "FINISHED"

        pass

    def awarding_points(self, match):
        if match.winner_index == "nul":
            match.participant_a["score"] = 0.5
            match.participant_b["score"] = 0.5
        else:
            if match.participant_a["index"] == match.winner_index:
                match.participant_a["score"] = 1
            else:
                match.participant_a["score"] = 0
            if match.participant_b["index"] == match.winner_index:
                match.participant_b["score"] = 1
            else:
                match.participant_b["score"] = 0

            if match.participant_a["opponent_index"] == "exempt":
                match.participant_a["score"] = 1
            if match.participant_b["opponent_index"] == "exempt":
                match.participant_b["score"] = 1
        pass


    def check_status_round(self):
        list_matchs = self.controller.get_unserial_matchs_current_round()
        count_matchs = len(list_matchs)
        count_matchs_finished = 0
        for match in list_matchs:
            if match.status_match == "FINISHED":
                count_matchs_finished += 1
            else:
                continue
        if count_matchs_finished == count_matchs:
            return "FINISHED"
        pass
