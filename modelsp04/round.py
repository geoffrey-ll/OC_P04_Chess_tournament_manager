#! /usr/bin/env python3
# coding: utf-8


from operator import attrgetter
from math import floor as arrinf
from math import ceil as arrsup
import random


class Round:
    """Le model pour les rounds."""
    rounds_in_progress = []

    def __init__(self, round_controller, name="",
                 status_round="", status_participants=dict):
        """Initialisation de la classe Round."""
        self.controller = round_controller

        self.name = name
        self.status_round = status_round
        self.status_participants = status_participants

    def unserial_list_rounds(self, list_rounds_in_db):
        """"Désérialisation des rounds du tournoi en cours."""
        self.rounds_in_progress = []
        for round in list_rounds_in_db:
            name = round["name"]
            status_round = round["status_round"]
            status_participants = round["status_participants"]

            round_in_db = Round("round_controller", name,
                                status_round, status_participants)
            self.rounds_in_progress.append(round_in_db)
        return self.rounds_in_progress

    @staticmethod
    def unserial_round(round_in_db):
        """Désérialisation d'une round du tournoi en cours."""
        try:
            name = round_in_db["name"]
            status_round = round_in_db["status_round"]
            status_participants = round_in_db["status_participants"]
            if status_round == "To do":
                round_to_do = Round("round_controller", name,
                                    status_round,
                                    status_participants)
                return round_to_do
            elif status_round == "In progress":
                round_in_progress = Round("round_controller", name,
                                          status_round,
                                          status_participants)
                return round_in_progress
        except Exception as e:
            osef = []
            osef.append(e)
            print("No round here")

    def get_list_rounds(self):
        """Demande la liste de rounds du tournoi en cours."""
        return self.controller.get_list_rounds()

    def get_round_to_do(self):
        """Demande les données du prochain round à faire (s'il en reste un)."""
        return self.controller.get_round_to_do()

    def get_round_in_progress(self):
        """Demanade les données du round en cours."""
        return self.controller.get_round_in_progress()

    def get_status_participants(self):
        """Demande le status des participants du tournoi en cours."""
        return self.controller.get_status_participants()

    def add_round(self):
        """Enregistrement des rounds du tournoi dans la base de données."""
        return self.controller.add_round(self.rounds_in_progress)

    def initialize_round(self, in_progress):
        """Initialisation des rounds du tournoi."""
        self.rounds_in_progress = []
        count_round = in_progress.round
        for count in range(count_round):
            name = "round_" + str(count + 1)
            status_round = "To do"
            status_participants = in_progress.status_participants

            round = Round("round_controller", name,
                          status_round, status_participants)
            self.rounds_in_progress.append(round)
        return self.add_round()

    def change_status_round(self):
        """Change le status du round de "To do" à "In progress"."""
        round_to_do = self.controller.get_unserial_round_to_do()
        round_to_do.status_round = "In progress"
        self.save_round(round_to_do)
        return round_to_do.name

    def change_status_round_finished(self):
        """Change le status du round de "In progress" à "Finished"."""
        round_to_finished = self.controller.get_unserial_round_in_progress()
        round_to_finished.status_round = "Finished"
        return self.save_round(round_to_finished)

    def save_round(self, round_update):
        """Sauvegarde d'un round dasns la base de données (mise à jour)."""
        return self.controller.save_round(round_update)

    def data_participants(self):
        """
        Demande et compile les données des participants nécessaires pour les
        matchs.
        """
        status_participants = self.controller.get_status_participants()
        players_participants = \
            self.controller.get_unserial_players_participants()

        data_participants = []
        for player in players_participants:
            for key, value in (status_participants
                               ["player_index_{}".format(player.index)]
                               .items()):
                setattr(player, key, value)
            player.current_elo = -player.current_elo
            data_participants.append(player)
        return data_participants

    @staticmethod
    def sorting_participants(data_participants):
        """Tri des participants en vue de leur appariement."""
        data_participants.sort(key=attrgetter("score", "current_elo",
                                              "last_name", "first_name",
                                              "date_of_birth"),
                               reverse=True)
        sorted_participants = data_participants
        return sorted_participants

    @staticmethod
    def subgroups(sorted_participants):
        """
        Répartition des participants en deux groupes pour leur appariements.
        """
        subgroup_participants = {}
        count_group_s1 = int(arrinf(len(sorted_participants) / 2))
        subgroup_participants["group_s1"] = sorted_participants[:count_group_s1
                                                                ]
        subgroup_participants["group_s2"] = sorted_participants[count_group_s1:
                                                                ]
        return subgroup_participants

    def matching_round_1(self, subgroup_participants):
        """Appariements des participants lors du premier round."""
        matching = []
        for participant in range(len(subgroup_participants["group_s1"])):
            self.assigment_color(
                subgroup_participants["group_s1"][participant],
                subgroup_participants["group_s2"][participant]
                                 )
            self.assigment_opponent(
                subgroup_participants["group_s1"][participant],
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

    @staticmethod
    def assigment_color(participant_a, participant_b):
        """Attribution des couleurs aux participants d'un match."""
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

    @staticmethod
    def assigment_opponent(participant_a, participant_b):
        """
        Ajout de l'adversaire d'un participant, à la liste des adversaire
        rencontrés.
        """
        if participant_b == "exempt":
            participant_a.opponent_index.append("exempt")
        else:
            participant_a.opponent_index.append(participant_b.index)
            participant_b.opponent_index.append(participant_a.index)

    @staticmethod
    def assigment_score_exempt(participant_exempt):
        """Gain d'un point pour un participant exempté."""
        participant_exempt.score = 1

    def matching_other_round(self, sorted_participants):
        """Appariement des participants à partir du deuxième round."""
        matching = []
        for count_a in range(len(sorted_participants)):
            match = "no_ok"
            count_b = count_a + 1
            while match == "no_ok" and count_b < len(sorted_participants):
                response1 = \
                    self.check_no_in_match(matching,
                                           sorted_participants[count_a],
                                           sorted_participants[count_b])
                if response1 == "pass":
                    match = "ok"
                elif response1 == "continue":
                    count_b += 1
                elif response1 == "no_in_match":
                    response2 = \
                        self.check_no_meet(sorted_participants[count_a],
                                           sorted_participants[count_b])
                    if response2 == "continue":
                        count_b += 1
                    elif response2 == "no_meet":
                        self.assigment_color(sorted_participants[count_a],
                                             sorted_participants[count_b])
                        self.assigment_opponent(sorted_participants[count_a],
                                                sorted_participants[count_b])
                        matching.append((sorted_participants[count_a],
                                         sorted_participants[count_b]))
                        match = "ok"
            if len(matching) != arrsup(len(sorted_participants)/2):
                if match == "no_ok" and count_b >= len(sorted_participants):
                    self.assigment_color(sorted_participants[count_a],
                                         "exempt")
                    self.assigment_opponent(sorted_participants[count_a],
                                            "exempt")
                    self.assigment_score_exempt(sorted_participants[count_a])
                    matching.append((sorted_participants[count_a],
                                     "exempt"))
        return matching

    @staticmethod
    def check_no_in_match(matching, participant_a, participant_b):
        """
        Vérifie qu'un des participants n'est pas déjà affectés à un match.
        """
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

    @staticmethod
    def check_no_meet(participant_a, participant_b):
        """Vérifi que les participants ne se sont pas déjà affrontés."""
        for opponent in participant_a.opponent_index:
            if opponent == participant_b.index:
                return "continue"
        return "no_meet"

    def adding_score_match(self, matchs_round_to_close):
        """
        À la fin d'un round, enregistrement du résultat des matchs dans les
        données de la round (score non cumulé).
        """
        round_to_close = self.controller.get_unserial_round_in_progress()
        for match in matchs_round_to_close:
            try:
                idx_a = match.participant_a["index"]
                score_a = match.participant_a["score"]
                (round_to_close.status_participants
                 ["player_index_{}".format(idx_a)]["score"]) = score_a
            except Exception as e:
                osef = []
                osef.append(e)
                continue

            try:
                idx_b = match.participant_b["index"]
                score_b = match.participant_b["score"]
                (round_to_close.status_participants
                 ["player_index_{}".format(idx_b)]["score"]) = score_b
            except Exception as e:
                osef = []
                osef.append(e)
                continue
        return self.controller.save_round(round_to_close)
