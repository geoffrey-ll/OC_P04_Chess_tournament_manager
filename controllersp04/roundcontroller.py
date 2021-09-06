#! /usr/bin/env python3
# coding: utf-8


from modelsp04.round import Round


class RoundController:
    def __init__(self, master_controller):
        self.model = Round(self)
        self.controller = master_controller
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
        # self.model.change_status_round()


        data_participants = self.model.data_participants()
        point_levels = self.model.point_levels(data_participants)
        sorting_levels = self.model.sorting_levels(point_levels)
        subgroup_levels = self.model.subgroups(sorting_levels)
        self.model.prefered_colors(subgroup_levels)
        #
        self.model.matching()
        # C'est ici que je dois faire l'appariements des joueurs pour les matchs
        # self.model.matching()
        pass

    def round_manager(self):
        test = self.get_round_in_progress()
        if test == "NO_ROUND_IN_PROGRESS":
            return self.start_round()
        else:
            # TEMPORAIRE c'est pour tester le script sans recréer un tournoi.
            # c'est instructions devront être déplacées dans self.start_round()
            # ici doivent aller les instructions en cours de round (donc après l'appariement) et permettre la gestion de la round et des matchs (vainqueur, vaincu etc)
            print("méthode round_manager IN roundcontroller")
            return self.start_round()
            # return self.model.matching()
        pass

    def save_round(self, round_update):
        return self.controller.save_round(round_update)

    def closing_round(self):
        pass

    def matching(self):
        return self.model.matching()
