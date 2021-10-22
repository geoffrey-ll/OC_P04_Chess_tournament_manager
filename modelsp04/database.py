#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, where, Query
import re


class DataBase:
    """Base de données."""

    db = TinyDB("db.json")
    player = db.table("player")
    tournament_in_progress = db.table("tournament_in_progress")
    round_tournament = db.table("round_tournament")
    matchs_tournament = db.table("matchs_tournament")
    tournaments_finished = db.table("tournament_finished")

    def __init__(self, database_controller):
        """Initialisation de la base de données"""
        self.controller = database_controller

    def get_list_players(self):
        """Renvoi la liste de tous les joueurs de la base de données."""
        return self.player.search(Query().controller == "player_controller")

    def get_data_player(self, index_participant):
        """Renvoi les données des joueurs qui participent au tournoi."""
        return self.player.search(Query().index == int(index_participant))

    def get_len_players_in_db(self):
        """
        Renvoi le nombre de joueurs présent dans la base de données.
        Pour la bonne association joueur/index.
        """
        return len(self.player)

    def get_tournament_in_progress_or_not(self):
        """Renvoi si un tournoi est en cours ou pas."""
        if len(self.tournament_in_progress) == 0:
            return "empty"
        else:
            return "no empty"

    def get_round_to_do_or_not(self):
        """Renvoi s'il reste un round à faire pour le tournoi en cours."""
        count = 0
        for round in self.round_tournament:
            if round["status_round"] == "To do":
                count += 1
        if count != 0:
            return "yes"
        if count == 0:
            return "not"

    def get_tournament_in_progress(self):
        """Renvoi les données du tournoi en cours."""
        for element in self.tournament_in_progress:
            return element

    def get_tournaments_finished(self):
        """Renvoi les données des tournois terminés."""
        return self.tournaments_finished\
            .search(Query().controller == "finished_controller")

    def get_len_tournaments_finished(self):
        """
        Renvoi le nombre de tournois terminés dans la base de données.
        Pour la bonne association tournoi_terminés/index.
        """
        if self.tournaments_finished == []:
            return 0
        else:
            return len(self.tournaments_finished)

    def get_list_rounds(self):
        """Renvoi les rounds du tournoi en couns."""
        return self.round_tournament\
            .search(Query().controller == "round_controller")

    def get_round_to_do(self):
        """Renvoi le prochain round à faire du tournoi en cours."""
        for round in self.round_tournament:
            if round["status_round"] == "To do":
                return round
            else:
                continue
        return "no round to do"

    def get_round_in_progress(self):
        """Renvoi le round en cours du tournoi en cours."""
        for round in self.round_tournament:
            if round["status_round"] == "In progress":
                return round
            else:
                continue
        return "no_round_in_progress"

    def get_matchs_current_round(self):
        """Renvoi les matchs du round en cours du tournoi en cours."""
        current_round = self.get_round_in_progress()
        number_current_round = re.findall("[0-9]+", current_round["name"])[0]
        matchs_current_round = []
        for match in self.matchs_tournament:
            try:
                if match["name"] == re.findall(
                        "match_{}.+".format(number_current_round),
                        match["name"])[0]:
                    matchs_current_round.append(match)
            except Exception as e:
                osef = []
                osef.append(e)
                continue
        if matchs_current_round != []:
            return matchs_current_round
        else:
            return "no_matchs_current_round"

    def get_status_participants(self):
        """
        Renvoi le status des participants de la table tournament_in_progress.
        """
        dico_tournament = self.tournament_in_progress\
            .search(Query().controller == "tournament_controller")
        return dico_tournament[0]["status_participants"]

    def get_players_participants(self):
        """
        Renvoi les donnése des joueurs participants au tournoi.
        Remarque : dans la base de données, les scores elo sont stockés comme
        entier négatifs.
        """
        index_participants = self.get_index_participants()
        players_participants = []
        for idx in index_participants:
            players_participants\
                .append(self.player.search(Query().index == int(idx))[0])
        return players_participants
        pass

    def get_index_participants(self):
        """Renvoi les index des participants du tournoi en cours."""
        index_participants = []
        dico_tournament = self.tournament_in_progress\
            .search(Query().controller == "tournament_controller")
        for key in dico_tournament[0]["status_participants"]:
            index_participants.append(re.findall("[0-9]+", key)[0])
        return index_participants

    def get_elo_participants(self):
        """Renvoi le classement Elo des participants du tournoi en cours."""
        index_participants = self.get_index_participants()
        elo_participants = []
        for index in index_participants:
            elo_participant = {}
            player = self.player.search(Query().index == int(index))
            elo_participant["index_player"] = index
            elo_participant["current_elo"] = -player[0]["current_elo"]
            elo_participants.append(elo_participant)
        return elo_participants

    def get_player_exists(self, index_to_check):
        """
        Vérifie que les index renseignés pour la création d'un tournoi aient
        une correspondance dans la base de données.
        Si tous les index existent, initialise un dictionnaire de données des
        participants pour le tournoi.
        """
        participants_validate = {}
        for indexx in index_to_check:
            if self.player.search(Query().index == int(indexx)):
                participants_validate["player_index_{}".format(indexx)] = {}
                (participants_validate["player_index_{}".format(indexx)]
                 ["score"]) = 0
                (participants_validate["player_index_{}".format(indexx)]
                 ["colors"]) = []
                (participants_validate["player_index_{}".format(indexx)]
                 ["opponent_index"]) = []
        if len(participants_validate) == len(index_to_check):
            return participants_validate
        else:
            return "true"

    def add_player(self, new_player):
        """Enregistre le nouveau joueur dans la base de données."""
        dic = {}
        for key, value in new_player.__dict__.items():
            dic[key] = value
        self.player.insert(dic)

    def add_tournament_in_progress(self, tournament_in_progress):
        """
        Enregistre les données du tournoi en cours dans la base de dnnées.
        """
        dic = {}
        for key, value in tournament_in_progress.__dict__.items():
            dic[key] = value
        self.tournament_in_progress.insert(dic)

    def add_round(self, round_in_progress):
        """
        Enregistre les rounds du tournoi en cours dans la base de données.
        """
        dic = {}
        for round in round_in_progress:
            for key, value in round.__dict__.items():
                dic[key] = value
            self.round_tournament.insert(dic)

    def add_matchs(self, list_matchs_in_round):
        """
        Enregistre les matchs de la round en cours dans la base de donnnées.
        """
        dic = {}
        for match in list_matchs_in_round:
            for key, value in match.__dict__.items():
                if key == "participant_a" or key == "participant_b":
                    dic[key] = {}
                    try:
                        for subkey, data in value.items():
                            if subkey == "current_elo":
                                dic[key][subkey] = -data
                            else:
                                dic[key][subkey] = data
                    except Exception as e:
                        osef = []
                        osef.append(e)
                        continue
                else:
                    dic[key] = value
            self.matchs_tournament.insert(dic)

    def save_match(self, match_to_update):
        """Sauvegarde le match dans la base de données (mise à jour)."""
        update = {}
        for key, value in match_to_update.__dict__.items():
            update[key] = value
        self.matchs_tournament.update(update, where("name") == update["name"])

    def save_round(self, round_to_update):
        """Sauvegarde la round dans la base de données (mise à jour)."""
        update = {}
        for key, value in round_to_update.__dict__.items():
            update[key] = value
        self.round_tournament.update(update, where("name") == update["name"])

    def save_tournament(self, tournament_to_update):
        """Sauvegarde le tournoi dans la base de données (mise à jour)."""
        update = {}
        for key, value in tournament_to_update.__dict__.items():
            update[key] = value
        self.tournament_in_progress.update(update,
                                           where("name") == update["name"])

    def transfer_tournament_to_finished(self):
        """
        Enregistre le tournoi en cours dans la table des tournois terminés
        (à la clôture du tournoi en cours).
        """
        tournament_to_close = self.tournament_in_progress\
            .search(Query().controller == "tournament_controller")
        rounds_tournament = self.round_tournament\
            .search(Query().controller == "round_controller")
        matchs_tournament = self.matchs_tournament\
            .search(Query().controller == "match_controller")

        return self.tournaments_finished\
            .insert({"controller": "finished_controller",
                     "tournament": tournament_to_close[0],
                     "rounds": rounds_tournament, "matchs": matchs_tournament})

    def purge_tournament_in_progress(self):
        """
        Purge la table de tournoi en cours (après sa fin et son enregistrement
        dans la table des tournois terminés.
        """
        self.tournament_in_progress.truncate()
        self.round_tournament.truncate()
        return self.matchs_tournament.truncate()

    def reinitialize_for_test(self):
        """
        Pour purger des tables dans la base de données (utile pendant dev).
        """
        self.round_tournament.truncate()
        self.matchs_tournament.truncate()
        self.tournament_in_progress.truncate()
        # return self.tournaments_finished.truncate()
