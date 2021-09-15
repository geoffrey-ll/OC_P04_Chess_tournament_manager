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
        return print("ici", self.rounds_in_progress)

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
        return self.save_round(round_to_do)


    def save_round(self, round_update):
        return self.controller.save_round(round_update)
        pass



    def in_progress(self):
        pass


    def data_participants(self):
        status_participants = self.controller.get_status_participants()
        players_participants = self.controller.get_unserial_players_participants()
        data_participants = []

        for player in players_participants:
            for key, value in status_participants["player_index_{}".format(player.index)].items():
                setattr(player, key, value)
            data_participants.append(player)

        return data_participants
        pass

    def point_levels(self, data_participants):
        point_levels = {}
        for player in data_participants:
            key = "point_levels_{}".format(player.score)
            if key in point_levels:
                point_levels[key].append(player)
            else:
                point_levels[key] = []
                point_levels[key].append(player)
        return point_levels
        pass

    def sorting_levels(self, point_levels):
        sorting_levels = {}
        for key in point_levels.keys():
            players_level = point_levels.get(key)
            # rajouter une condition pour trouver les flotteurs, et, si possible, les faire joueur entre eux si il ont le même score.
            players_level.sort(key=attrgetter("score", "current_elo", "last_name", "first_name", "date_of_birth"))

            sorting_levels[key] = players_level

        return sorting_levels
        pass


    def subgroups(self, sorting_levels):
        subgroup_levels = {}
        for level, value in sorting_levels.items():

            count_group_s1 = int(arrinf(len(value) / 2))
            subgroup_levels[level] = {}
            subgroup_levels[level]["group_s1"] = value[:count_group_s1]
            subgroup_levels[level]["group_s2"] = value[count_group_s1:]

        return subgroup_levels
        pass

    def prefered_colors(self, subgroup_levels):
        # print("subgroup_levels IN round\n", subgroup_levels)
        #
        for level, group in subgroup_levels.items():
            for players in group.values():
                for player in players:
                    # player.colors = self.random_test()
                    if player.colors == []:
                        setattr(player, "pref_color", self.random_color())
                    else:
                        setattr(player, "pref_color", self.difference_between_color(player))
        return subgroup_levels
        pass

    def random_color(self):
        random_color = random.randint(0, 1)
        if random_color == 0:
            return "soft_white"
        else:
            return "soft_black"
        pass

    def random_test(self):
        # Là uniquement pour test self.difference_between_color()
        colors = []
        for i in range(3):
            random_test = random.randint(0, 1)
            if random_test == 0:
                colors.append("white")
            elif random_test == 1:
                colors.append("black")
        return colors
        pass

    def difference_between_color(self, player):
        """
        notes sur les pref_colors:
            - une pref_color = "2_white", indique une préférence "absolute_white"
                Le joueur devra absolument avoir la couleur white.
            - une pref_color = "1_black", indique une préférence "strong_black".
                 La couleur est à privilégier face à une "soft".
            - une pref_color = "0_white", indique une préférence "soft_white".
                Ne doit pas être privilégier face à une color "strong" ou "absolute"
        :param player:
        :return:
        """

        # testé à l'aide de self.random_test()
        # a controler en situation réel.
        count_white = player.colors.count("white")
        count_black = player.colors.count("black")
        last_2_colors = []

        if len(player.colors) >= 2:
            last_2_colors = player.colors[-2:]

        if last_2_colors.count("black") == 2:
            return "absolute_white"
        elif last_2_colors.count("white") == 2:
            return "absolute_black"
        else:
            difference_between_color = count_white - count_black
            if difference_between_color == -2: # or player["colors"][-2:] == ["black", "black"]
                return "absolute_white"
            elif difference_between_color == 2: # or player["colors"][-2:] == ["white", "white"]
                return "absolute_black"
            elif difference_between_color == -1:
                return "strong_white"
            elif difference_between_color == 1:
                return "strong_black"
            elif difference_between_color == 0:
                if player.colors[-1] == "black":
                    return "soft_white"
                elif player.colors[-1] == "white":
                    return "soft_black"

        pass

    def matching_manager(self, data_participants_ready):
        matchs_in_round = []
        for level, groups in data_participants_ready.items():
            mixed_or_not = self.check_homogeneity(groups)
            if mixed_or_not == "level_homogeneous":
                match_in_level = self.matching(groups)
                matchs_in_round.append(match_in_level)
            elif mixed_or_not == "level_heterogeneous":
                resorting_level = self.sorting_level_heterogeneous(groups)

        return matchs_in_round
        pass

    def check_homogeneity(self, groups):
        score_in_level = []
        for group, players in groups.items():
            for player in players:
                count_score = 0
                for score in score_in_level:
                    if score_in_level == []:
                        score_in_level.append(player.score)
                    elif player.score == score:
                        pass
                    else:
                        count_score += 1
                if count_score == len(score_in_level):
                    score_in_level.append(player.score)
        if len(score_in_level) == 1:
            return "level_homogeneous"
        else:
            return "level_heterogeneous"
        pass

    def sorting_level_heterogeneous(self, level):
        return print("Il faut construire la def pour le tri des niveaux de points hetérogène !!!!")
        pass

    def matching(self, groups):
        provisionnal_matching = []
        for player_s1 in groups["group_s1"]:
            for player_s2 in groups["group_s2"]:
                continue_or_not = self.player_in_match_or_not\
                    (player_s1, player_s2, provisionnal_matching)
                if continue_or_not == "continue":
                    continue
                else:
                    continue_or_not = self.player_meet_or_not(player_s1, player_s2)
                    if continue_or_not == "continue":
                        continue
                    else:
                        match_or_not = self.check_colors_compatibility(player_s1, player_s2)
                        if match_or_not == "continue":
                            continue
                        else:
                            provisionnal_matching.append(match_or_not)

        matching_ok_or_not = self.exempt_or_not(groups, provisionnal_matching)
        if matching_ok_or_not == "level_matching_ok":
            return provisionnal_matching
        else:
            return matching_ok_or_not

        pass


    def player_in_match_or_not(self, player_s1, player_s2, provisionnal_matching):
        for provi_match in provisionnal_matching:
            for player in provi_match:
                if player.index == player_s1.index or player.index == player_s2.index:
                    return "continue"
                else:
                    pass
        pass

    def player_meet_or_not(self, player_s1, player_s2):
        if player_s1.opponent_index != []:
            for opponent in player_s1.opponent_index:
                if player_s2.index == opponent:
                    return "continue"
            return "pass"
        else:
            return "pass"

        pass

    def check_colors_compatibility(self, player_s1, player_s2):
        power_str_s1 = re.findall(".+_", player_s1.pref_color)[0][:-1]
        power_str_s2 = re.findall(".+_", player_s2.pref_color)[0][:-1]

        power_s1 = self.power_str_to_int(power_str_s1)
        pref_color_s1 = player_s1.pref_color[-5:]


        power_s2 = self.power_str_to_int(power_str_s2)
        pref_color_s2 = player_s2.pref_color[-5:]


        if power_s1 > power_s2:
            player_s1.colors.append(pref_color_s1)
            player_s2.colors.append(self.assigment_color_opponent(pref_color_s1))
            self.assigment_opponent_index(player_s1, player_s2)
            return (player_s1, player_s2)

        elif power_s1 < power_s2:
            player_s1.colors.append(self.assigment_color_opponent(pref_color_s2))
            player_s2.colors.append(pref_color_s2)
            self.assigment_opponent_index(player_s1, player_s2)
            return (player_s1, player_s2)

        elif power_s1 == power_s2:
            if power_s1 == 2 and power_s2 == 2:
                return "continue"
            else:
                player_s1.colors.append(pref_color_s1)
                player_s2.colors.append(self.assigment_color_opponent(pref_color_s1))
                self.assigment_opponent_index(player_s1, player_s2)
                return (player_s1, player_s2)
        pass

    def power_str_to_int(self, power_str):
        if power_str == "absolute":
            return 2
        elif power_str == "strong":
            return 1
        elif power_str == "soft":
            return 0
        pass

    def assigment_color_opponent(self, pref_color_player):
        if pref_color_player == "black":
            return "white"
        elif pref_color_player == "white":
            return "black"
        pass

    def assigment_opponent_index(self, player_s1, player_s2):
        player_s1.opponent_index.append(player_s2.index)
        player_s2.opponent_index.append(player_s1.index)
        pass


    def exempt_or_not(self, groups, provisionnal_matching):
        if len(groups["group_s1"]) == len(groups["group_s2"]):
            if len(provisionnal_matching) == len(groups["group_s1"]):
                return "level_matching_ok"
            else:
                return print("Problème d'appariement dans méthode \"matching\" dans model \"round\"")
        else:
            player_have_match = []
            for match in provisionnal_matching:
                for participant in match:
                    player_have_match.append(participant.index)
            for group in groups.values():
                for player in group:
                    count = 0
                    for index in player_have_match:
                        if player.index == index:
                            count += 1
                        else:
                            continue
                    if count == 0:
                        provisionnal_matching.append(("exempt", player))
            return "level_matching_ok"


        pass


# ancien matching, avant la dé-procéduralisation.
    # def matching(self, groups):
    #     provisional_matching = []
    #     players_s2_pass = []
    #     for player_s1 in groups["group_s1"]:
    #         count_matching = len(provisional_matching)
    #         print("player_s1", player_s1)
    #         for player_s2 in groups["group_s2"]:
    #             print("\nplayer_s2\n", player_s2)
    #             pass_or_not = ''
    #             for provi_match in provisional_matching:
    #                 for player_to_pass in provi_match:
    #                     if player_s2.index == player_to_pass.index:
    #                         pass_or_not = "pass"
    #
    #             if pass_or_not == "pass":
    #                 continue
    #
    #             if player_s1.opponent_index != []:
    #                 for opponent in player_s1.opponent_index:
    #                     if player_s2.index == opponent:
    #                         pass
    #             if player_s1.pref_color[:8] == "absolute":
    #                 if player_s2.pref_color[:8] == "absolute":
    #                     if player_s1.pref_color == player_s2.pref_color:
    #                         pass
    #                     else:
    #                         player_s1.colors.append(player_s1.pref_color[-5:])
    #                         player_s2.colors.append(player_s2.pref_color[-5:])
    #                         provisional_matching.append((player_s1, player_s2))
    #                         players_s2_pass.append(player_s2.index)
    #                 else:
    #                     player_s1.colors.append(player_s1.pref_color[-5:])
    #                     if player_s1.colors[-1] == "black":
    #                         player_s2.colors.append("white")
    #                     else:
    #                         player_s2.colors.append("black")
    #                     provisional_matching.append((player_s1, player_s2))
    #                     players_s2_pass.append(player_s2.index)
    #             elif player_s1.pref_color[:6] == "strong":
    #                 if player_s2.pref_color[:8] == "absolute":
    #                     player_s2.colors.append(player_s2.pref_color[-5:])
    #                     if player_s2.colors[-1] == "black":
    #                         player_s1.colors.append("white")
    #                     else:
    #                         player_s1.colors.append("black")
    #                     provisional_matching.append((player_s1, player_s2))
    #                     players_s2_pass.append(player_s2.index)
    #                 else:
    #                     player_s1.colors.append(player_s1.pref_color[-5:])
    #                     if player_s1.colors[-1] == "black":
    #                         player_s2.colors.append("white")
    #                     else:
    #                         player_s2.colors.append("black")
    #                     provisional_matching.append((player_s1, player_s2))
    #                     players_s2_pass.append(player_s2.index)
    #             else:
    #                 if player_s2.pref_color[:4] == "soft":
    #                     player_s1.colors.append(player_s1.pref_color[-5:])
    #                     if player_s1.colors[-1] == "black":
    #                         player_s2.colors.append("white")
    #                     else:
    #                         player_s2.colors.append("black")
    #                     provisional_matching.append((player_s1, player_s2))
    #                     players_s2_pass.append(player_s2.index)
    #                 else:
    #                     player_s2.colors.append(player_s2.pref_color[-5:])
    #                     if player_s2.colors[-1] == "black":
    #                         player_s1.colors.append("white")
    #                     else:
    #                         player_s1.colors.append("black")
    #                     provisional_matching.append((player_s1, player_s2))
    #                     players_s2_pass.append(player_s2.index)
    #             if len(provisional_matching) != count_matching:
    #                 print("je suis entré là")
    #                 break
    #
    #
    #     print("\nprovisional\n", provisional_matching)
    #
    #     pass


