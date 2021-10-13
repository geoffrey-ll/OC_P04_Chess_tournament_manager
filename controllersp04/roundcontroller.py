#! /usr/bin/env python3
# coding: utf-8


import re

from modelsp04.round import Round


class RoundController:
    def __init__(self, master_controller):
        self.model = Round(self)
        self.controller = master_controller
        pass

    def get_unserial_list_rounds(self):
        list_rounds_in_db = self.get_list_rounds()
        return self.model.unserial_list_rounds(list_rounds_in_db)
        pass

    def get_unserial_round_to_do(self):
        round_to_do_in_db = self.get_round_to_do()
        return self.model.unserial_round(round_to_do_in_db)
        pass

    def get_unserial_round_in_progress(self):
        round_in_progress_in_db = self.get_round_in_progress()
        return self.model.unserial_round(round_in_progress_in_db)
        pass

    def get_unserial_players_participants(self):
        players_participants_in_db = self.get_players_participants()
        return self.controller.get_unserial_players_participants(players_participants_in_db)
        pass

    def get_unserial_tournament_in_progress(self):
        return self.controller.get_unserial_tournament_in_progress()
        pass

    def get_list_rounds(self):
        return self.controller.get_list_rounds()

    def get_round_to_do_or_not(self):
        return self.controller.get_round_to_do_or_not()
        pass

    def get_round_to_do(self):
        return self.controller.get_round_to_do()

    def get_round_in_progress(self):
        return self.controller.get_round_in_progress()
        pass

    def get_status_participants(self):
        return self.controller.get_status_participants()

    def get_players_participants(self):
        return self.controller.get_players_participants()
        pass

    def get_index_participants(self):
        return self.controller.get_index_participants()
        pass

    def get_elo_participants(self):
        return self.controller.get_elo_participants()
        pass


    def add_round(self, round_in_progress):
        return self.controller.add_round(round_in_progress)


    # def new_round(self):
    #     return self.model.start_round()
    #     pass

    def new_match(self, participant_1, participant_2):
        return self.controller.new_match(participant_1, participant_2)


    def initialize_round(self, in_progress):
        return self.model.initialize_round(in_progress)

    def start_round(self):
        """pour commencer un round, appariement et le reste."""
        # le self.model.change_status_round() doit rester en comm jusqu'à codage appariement terminé

        round_name = self.model.change_status_round()

        data_participants = self.model.data_participants()
        # point_levels = self.model.point_levels(data_participants)
        sorted_participants = self.model.sorting_participants(data_participants)
        if round_name == "round_1":
            subgroup_participants = self.model.subgroups(sorted_participants)
            matching = self.model.matching_round_1(subgroup_participants)
        else:
            matching = self.model.matching_other_round(sorted_participants)
        # data_participants_ready = self.model.prefered_colors(subgroup_levels)
        # matchs_in_round = self.model.matching_manager(data_participants_ready)


        return matching
        pass

    def round_manager(self):
        test = self.get_round_in_progress()


        if test == "NO_ROUND_IN_PROGRESS":
            test2 = self.get_round_to_do_or_not()
            if test2 == "yes":
                matching = self.start_round()
                self.updates(matching)
                self.controller.initialize_matchs(matching)
                self.controller.display_view_matchs_in_progress_round()
            elif test2 == "not":
                return self.controller.closing_tournament()
        else:
            return self.controller.display_view_matchs_in_progress_round()

        pass

    def updates(self, matching):
        # à terme, il faudra que ce soit avec round_in_progress
        round_to_update = self.get_unserial_round_in_progress()
        count = int(re.findall("[0-9]+", round_to_update.name)[0]) - 1
        tournament_to_update = self.get_unserial_tournament_in_progress()

        for match in matching:
            for player in match:
                try:
                    attr_round = round_to_update.status_participants["player_index_{}".format(player.index)]
                    attr_tourn = tournament_to_update.status_participants["player_index_{}".format(player.index)]

                    attr_round["score"] = 0
                    attr_round["colors"] = player.colors[count]
                    attr_round["opponent_index"] = player.opponent_index[count]

                    attr_tourn["score"] = player.score
                    attr_tourn["colors"].append(player.colors[count])
                    attr_tourn["opponent_index"].append(player.opponent_index[count])
                except:
                    continue

        return self.save_round(round_to_update), self.save_tournament(tournament_to_update)

        pass

    def round_to_close(self, matchs_round_to_close):
        self.model.adding_score_match(matchs_round_to_close)
        return self.model.change_status_round_finished()
        pass

    def save_round(self, round_to_update):
        return self.controller.save_round(round_to_update)

    def save_tournament(self, tournament_to_update):

        return self.controller.save_tournament(tournament_to_update)
        pass

    def closing_round(self):
        pass

