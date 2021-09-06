#! /usr/bin/env python3
# coding: utf-8


from operator import itemgetter
from math import floor as arrinf
from math import ceil as arrsup
from pprint import pprint as pp
import random


class Round:
    round_in_progress = []


    def __init__(self, round_controller, name="",  match_in_round=int(), status_round="", status_participants=dict):
        self.controller = round_controller

        self.name = name
        self.match_in_round = match_in_round
        self.status_round = status_round
        self.status_participants = status_participants

        pass

    def get_list_round(self):
        return self.controller.get_list_round()

    def get_round_to_do(self):
        return self.controller.get_round_to_do()

    def get_round_in_progress(self):
        return self.controller.get_round_in_progress()
        pass

    def get_status_participants(self):
        return self.controller.get_status_participants()
        pass


    def add_round(self):
        return self.controller.add_round(self.round_in_progress)
        pass


    def initialize_round(self, in_progress):

        count_round = int(in_progress[0].get("round"))
        for count in range(count_round):
            name = "round_" + str(count + 1)
            match_in_round = in_progress[0].get("match_in_round")
            status_round = "TO_DO"
            status_participants = in_progress[0].get("status_participants")

            round = Round("round_controller", name, match_in_round, status_round, status_participants)
            self.round_in_progress.append(round)


        return self.add_round()



    def change_status_round(self):
        round_to_do = self.get_round_to_do()
        round_to_do["status_round"] = "IN_PROGRESS"
        return self.save_round(round_to_do)


    def save_round(self, round_update):
        return self.controller.save_round(round_update)
        pass



    def in_progress(self):
        pass


    def data_participants(self):
        status_participants = self.controller.get_status_participants()
        players_participants = self.controller.get_players_participants()
        data_participants = []
        for player in players_participants:
            for key, value in status_participants["player_index_{}".format(player["index"])].items():
                player[key] = value
            data_participants.append(player)
        return data_participants
        pass

    def point_levels(self, data_participants):
        point_levels = {}
        for player in data_participants:
            key = "point_levels_{}".format(player["score"])
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
            players_level.sort(key=itemgetter("score", "current_elo", "last_name", "first_name", "date_of_birth"))

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
                    # player["colors"] = self.random_test()
                    if player["colors"] == []:
                        player["pref_color"] = self.random_color()
                    else:
                        player["pref_color"] = self.difference_between_color(player)

                    print("pref", player["pref_color"], "\n")
                # print("en cours", subgroup_levels[level])
            # for player, tseu in subgroup_levels[level][group][0].items():
                # print(subgroup_levels[level][group][0])
                pass
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

        # test à l'aide de self.random_test()
        # a controler en situation réel.
        count_white = player["colors"].count("white")
        count_black = player["colors"].count("black")
        last_2_colors = []

        if len(player["colors"]) >= 2:
            last_2_colors = player["colors"][-2:]

        if last_2_colors.count("black") == 2:
            return "absolute_white"
        elif last_2_colors.count("white") == 2:
            return "absolute_black"
        else:
            difference_between_color = count_white - count_black
            if difference_between_color == -2:
                return "absolute_white"
            elif difference_between_color == 2:
                return "absolute_black"
            elif difference_between_color == -1:
                return "strong_white"
            elif difference_between_color == 1:
                return "strong_black"
            elif difference_between_color == 0:
                if player["colors"][-1] == "black":
                    return "soft_white"
                elif player["colors"][-1] == "white":
                    return "soft_black"

        pass

    def matching_no(self):
        """Officiellement, après le tri selon le classement elo, le tri se fait selon le titre du joueur. Pour ce projet, le titre d'un joeur ne sera pas utilisé."""


        # sorting_participants.sort(key=itemgetter("score", "current_elo", "last_name", "first_name", "date_of_birth"))



        # trop tot !!!! D'abord faire niveaux de points


        # for element in group_s1:
        #     print(element["index"])
        # print("\n")
        # for element in group_s2:
        #     print(element["index"])
        pass

    def matching(self):
        print("participants IN round\n", self.get_status_participants())

        # round_in_progress = ''
        # for round in self.round_in_progress:
        #     if round.round_status == "IN_PROGRESS":
        #         round_in_progress = round
        #         print(round_in_progress)
        #     else:
        #         pass
        # if round_in_progress.name == "round_1":
        #     participants = self.controller.get_participants()
        #     participants.sort(key=attrgetter("current_elo"), reverse=True)
        #
        #     for participant in participants:
        #         print("elo", participant.current_elo)
        #
        #     count = len(participants) // 2
        #
        #     top_elo = participants[:count]
        #     lower_elo = participants[count:]
        #     exempt_elo = []
        #     if len(participants) % 2 != 0:
        #         lower_elo = participants[count:-1]
        #         exempt_elo = participants[-1]
        #
        #     # matchs = []
        #     for number in range(round_in_progress.match_in_round):
        #         # initialise match ???
        #         # Match(top_elo[number], lower_elo[number])
        #         # matchs.append([top_elo[number], lower_elo[number]])
        #         # for elmt in matchs:
        #         #     print("matchs", elmt.current_elo)
        #         self.controller.new_match(top_elo[number], lower_elo[number])
        #
        #
        #     pass
        # for round in self.round_in_progress:
        #     print("\nlist round\n", round.round_status)
        # pass