#! /usr/bin/env python3
# coding: utf-8


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
        # round_ = self.model.change_status_round()

        data_participants = self.model.data_participants()
        point_levels = self.model.point_levels(data_participants)
        sorting_levels = self.model.sorting_levels(point_levels)
        subgroup_levels = self.model.subgroups(sorting_levels)
        data_participants_ready = self.model.prefered_colors(subgroup_levels)
        matchs_in_round = self.model.matching_manager(data_participants_ready)

        return matchs_in_round
        pass

    def round_manager(self):
        test = self.get_round_in_progress()

        if test == "NO_ROUND_IN_PROGRESS":
            round_to_start = self.get_unserial_round_to_do()
            matchs_in_round = self.start_round()
            print("me voilàb, ", matchs_in_round)
            self.updates(matchs_in_round)
            self.controller.initialize_matchs(matchs_in_round)
        else:
            # TEMPORAIRE c'est pour tester le script sans recréer un tournoi.
            # c'est instructions devront être déplacées dans self.start_round()
            # ici doivent aller les instructions en cours de round (donc après l'appariement) et permettre la gestion de la round et des matchs (vainqueur, vaincu etc)
            print("méthode round_manager IN roundcontroller")
            return self.start_round()
            # return self.model.matching()
        pass

    def updates(self, matchs_in_round):
        # à terme, il faudra que ce soit avec round_in_progress
        round_to_update = self.get_unserial_round_to_do()
        tournament_to_update = self.get_unserial_tournament_in_progress()

        for match in matchs_in_round[0]:
            for player in match:
                try:
                    attr_round = round_to_update.status_participants["player_index_{}".format(player.index)]
                    attr_tourn = tournament_to_update.status_participants["player_index_{}".format(player.index)]

                    attr_round["score"] = player.score
                    attr_round["colors"] = player.colors[0]
                    attr_round["opponent_index"] = player.opponent_index[0]

                    attr_tourn["score"] += player.score
                    attr_tourn["colors"].append(player.colors[0])
                    attr_tourn["opponent_index"].append(player.opponent_index[0])
                except:
                    continue

        return self.save_round(round_to_update), self.save_tournament(tournament_to_update)

        pass

    def save_round(self, round_to_update):
        return self.controller.save_round(round_to_update)

    def save_tournament(self, tournament_to_update):

        return self.controller.save_tournament(tournament_to_update)
        pass

    def closing_round(self):
        pass

