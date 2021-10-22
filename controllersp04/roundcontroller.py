#! /usr/bin/env python3
# coding: utf-8


import re

from modelsp04.round import Round


class RoundController:
    """Le controller de round."""

    def __init__(self, master_controller):
        """Initialisation de la classe RoundController."""
        self.model = Round(self)
        self.controller = master_controller

    def get_unserial_list_rounds(self):
        """Demande la désérialisation des rounds du tournoi en cours."""
        list_rounds_in_db = self.get_list_rounds()
        return self.model.unserial_list_rounds(list_rounds_in_db)

    def get_unserial_round_to_do(self):
        """Demande la désérialisation du prochain round à faire."""
        round_to_do_in_db = self.get_round_to_do()
        return self.model.unserial_round(round_to_do_in_db)

    def get_unserial_round_in_progress(self):
        """Demande la désérialisation du round en cours."""
        round_in_progress_in_db = self.get_round_in_progress()
        return self.model.unserial_round(round_in_progress_in_db)

    def get_unserial_players_participants(self):
        """Demande la désérialisation des participants du tournoi en cours."""
        players_participants_in_db = self.get_players_participants()
        return self.controller\
            .get_unserial_players_participants(players_participants_in_db)

    def get_unserial_tournament_in_progress(self):
        """Demande la désérilisation du tournoi en cours."""
        return self.controller.get_unserial_tournament_in_progress()

    def get_list_rounds(self):
        """Demande la liste des rounds du tournoi en cours."""
        return self.controller.get_list_rounds()

    def get_round_to_do_or_not(self):
        """Pour savoir si il reste un round à faire."""
        return self.controller.get_round_to_do_or_not()

    def get_round_to_do(self):
        """Demande les données du prochain round à faire (s'il en reste un)."""
        return self.controller.get_round_to_do()

    def get_round_in_progress(self):
        """Demande les données du round en cours."""
        return self.controller.get_round_in_progress()

    def get_status_participants(self):
        """Demande le status des participants du tournoi en cours."""
        return self.controller.get_status_participants()

    def get_players_participants(self):
        """Demande les données des joueurs participants au tournoi en cours."""
        return self.controller.get_players_participants()

    def get_index_participants(self):
        """Demande l'index des joueurs participants au tournoi en cours."""
        return self.controller.get_index_participants()

    def get_elo_participants(self):
        """Demande l'Elo des joueurs participants au tournoi en cours."""
        return self.controller.get_elo_participants()

    def add_round(self, round_in_progress):
        """Enregistrement des rounds du tournoi dans la base de données."""
        return self.controller.add_round(round_in_progress)

    def initialize_round(self, in_progress):
        """Pour l'initialisation des rounds du tournoi."""
        return self.model.initialize_round(in_progress)

    def start_round(self):
        """Pour commencer un round, appariement et le reste."""
        round_name = self.model.change_status_round()
        data_participants = self.model.data_participants()
        sorted_participants = \
            self.model.sorting_participants(data_participants)

        if round_name == "round_1":
            subgroup_participants = self.model.subgroups(sorted_participants)
            matching = self.model.matching_round_1(subgroup_participants)
        else:
            matching = self.model.matching_other_round(sorted_participants)
        return matching

    def round_manager(self):
        """Le round manager."""
        test = self.get_round_in_progress()
        if test == "no_round_in_progress":
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

    def updates(self, matching):
        """Sauvegarde des matchs (mise à jour) et mise à jour du tournoi."""
        round_to_update = self.get_unserial_round_in_progress()
        count = int(re.findall("[0-9]+", round_to_update.name)[0]) - 1
        tournament_to_update = self.get_unserial_tournament_in_progress()

        for match in matching:
            for player in match:
                try:
                    short = "player_index_{}".format(player.index)
                    attr_round = round_to_update.status_participants[short]
                    attr_tourn = tournament_to_update.status_participants[short
                                                                          ]
                    attr_round["score"] = 0
                    attr_round["colors"] = player.colors[count]
                    attr_round["opponent_index"] = player.opponent_index[count]

                    attr_tourn["score"] = player.score
                    attr_tourn["colors"].append(player.colors[count])
                    attr_tourn["opponent_index"] \
                        .append(player.opponent_index[count])
                except Exception as e:
                    osef = []
                    osef.append(e)
                    continue
        return (self.save_round(round_to_update),
                self.save_tournament(tournament_to_update))

    def round_to_close(self, matchs_round_to_close):
        """Instruction pour la clôture du round."""
        self.model.adding_score_match(matchs_round_to_close)
        return self.model.change_status_round_finished()

    def save_round(self, round_to_update):
        """Sauvegarde de tournoi dans la base de données (mise à jour)."""
        return self.controller.save_round(round_to_update)

    def save_tournament(self, tournament_to_update):
        """Sauvegarde de tournoi dans la base de données (mise à jour)."""
        return self.controller.save_tournament(tournament_to_update)
