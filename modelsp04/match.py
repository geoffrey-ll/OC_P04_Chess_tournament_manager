#! /usr/bin/env python3
# coding: utf-8


import re


class Match:
    """Le model pour les matchs."""

    list_matchs_in_round = []

    def __init__(self, match_controller, name='', status_match='',
                 participant_a=dict, participant_b=dict, winner_index=int()):
        """Initialisation de la classe Match."""
        self.controller = match_controller

        self.name = name
        self.status_match = status_match
        self.participant_a = participant_a
        self.participant_b = participant_b
        self.winner_index = winner_index

    def unserial_matchs_current_round(self, matchs_current_round_in_db):
        """Désérialisation des matchs du round en cours."""
        self.list_matchs_in_round = []
        for match in matchs_current_round_in_db:
            name = match["name"]
            status_match = match["status_match"]
            participant_a = match["participant_a"]
            participant_b = match["participant_b"]
            winner_index = match["winner_index"]

            match_in_progress = Match("match_controller",
                                      name, status_match,
                                      participant_a, participant_b,
                                      winner_index)
            self.list_matchs_in_round.append(match_in_progress)
        return self.list_matchs_in_round

    def check_input_number(self, user_input):
        """Vérifie que le match dont on veut désigner le vainqueur, existe."""
        list_matchs = self.controller.get_unserial_matchs_current_round()
        count = 0
        for match in list_matchs:
            if user_input == re.findall("[0-9]+", match.name)[-1]:
                return user_input
            else:
                count += 1
        if count == len(list_matchs):
            return "match_no_exist"

    def check_status_round(self):
        """Pour prévenir si tous les matchs du round sont terminés."""
        list_matchs = self.controller.get_unserial_matchs_current_round()
        count_matchs = len(list_matchs)
        count_matchs_finished = 0
        for match in list_matchs:
            if match.status_match == "Finished":
                count_matchs_finished += 1
            else:
                continue
        if count_matchs_finished == count_matchs:
            return "Finished"

    def initialize_matchs(self, matching):
        """Sérialisation des matchs du round en cours."""
        self.list_matchs_in_round = []
        round_in_progress = self.controller.get_unserial_round_in_progress()
        count = int(re.findall("[0-9]+", round_in_progress.name)[0]) - 1

        for match in matching:
            name = self.name_of_match()
            if match[0] == "exempt" or match[1] == "exempt":
                status_match = "Finished"
            else:
                status_match = "In progress"
            participant_a = self.which_participant(match[0], count)
            participant_b = self.which_participant(match[1], count)
            if participant_a == "exempt":
                winner_index = participant_b["index"]
                participant_a["exempt"] = "exempt"
            elif participant_b == "exempt":
                winner_index = participant_a["index"]
                participant_b = {}
                participant_b["exempt"] = "exempt"
            else:
                winner_index = int()

            ini = Match("match_controller", name, status_match,
                        participant_a, participant_b, winner_index)
            self.list_matchs_in_round.append(ini)
        return self.add_matchs()

    def name_of_match(self):
        """Détermination du nom du match."""
        round_in_progress = self.controller.get_unserial_round_in_progress()
        number_round = re.findall("[0-9]+", round_in_progress.name)
        name = "match_{}x{}".format(number_round[0],
                                    len(self.list_matchs_in_round) + 1)
        return name

    @staticmethod
    def which_participant(participant_object, count):
        """Compilation des données du participant au match."""
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

    def add_matchs(self):
        """
        Pour l'enregistrement des matchs de round dans la base de données.
        """
        return self.controller.add_matchs(self.list_matchs_in_round)

    @staticmethod
    def assigment_winner(match, winner):
        """Assignation du vainqueur du match & changement statut du match."""
        if winner == "G":
            match.winner_index = match.participant_a["index"]
            match.status_match = "Finished"
        elif winner == "N":
            match.winner_index = "nul"
            match.status_match = "Finished"
        elif winner == "D":
            match.winner_index = match.participant_b["index"]
            match.status_match = "Finished"

    @staticmethod
    def awarding_points(match):
        """
        Assignation des points
        (hors participant exempté.
        Pour eux les points sont distribuer lors de l'appariement).
        """
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
