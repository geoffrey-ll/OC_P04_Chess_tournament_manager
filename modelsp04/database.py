#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, where , Query
import re



class DataBase:
    """Ceci est la base de données."""

    db = TinyDB("db.json")
    player = db.table("player")
    tournament_in_progress = db.table("tournament_in_progress")
    tournament_finished = db.table("tournament_finished")
    round_tournament = db.table("round_tournament")

    def __init__(self, database_controller):
        """Initialisation de la base de données"""
        self.controller = database_controller

    def get_list_players(self):
        """Renvoi la liste de tous les joueurs de la base de données."""
        return self.player.search(Query().controller == "player_controller")

    def get_len_players_in_db(self):
        """
        Renvoi la nombre de joueurs présent dans la base de données.
        Pour la bonne association joueur/index.
        """
        return len(self.player)

    def get_tournament_in_progress_or_not(self):
        """Renvoi si un tournoi est en cours ou pas."""
        if len(self.tournament_in_progress) == 0:
            return "empty"
        else:
            return "no empty"

    def get_tournament_in_progress(self):
        """Renvoi les données du tournoi en cours."""
        return self.tournament_in_progress.search(Query().controller == "tournament_controller")

    def get_list_round(self):
        return self.round_tournament.search(Query().controller == "round_controller")

    def get_round_to_do(self):
        for round in self.round_tournament:
            if round["round_status"] == "TO_DO":
                return round
            else:
                pass

    def get_round_in_progress(self):
        for round in self.round_tournament:
            if round["round_status"] == "IN_PROGRESS":
                return round
            else:
                pass
        return "NO_ROUND_IN_PROGRESS"
        pass

    def get_participants(self):
        dico_tournament = self.tournament_in_progress.search(Query().controller == "tournament_controller")
        return dico_tournament[0]["participants_status"]

    def get_player_exists(self, index_to_check):
        participants_validate = []
        for indexx in index_to_check:
            if self.player.search(Query().index == int(indexx)):
                participants_validate.append(["player_index_{}".format(int(indexx)), "score_0"])

        if len(participants_validate) == len(index_to_check):
            return participants_validate
        else:
            return "TRUE"
        pass


    def add_player(self, new_player):
        """Ajoute le nouveau joueur dans la base de données."""
        dic = {}
        for key, value in new_player.__dict__.items():
            dic[key] = value
        self.player.insert(dic)

    def add_tournament_in_progress(self, tournament_in_progress):
        """Ajoute les données du tournoi en cours dans la base de dnnées."""
        dic = {}
        for key, value in tournament_in_progress.__dict__.items():
            if key == "participants_status":
                dic[key] = {}
                for participant in value:
                    dic[key][participant[0]] = participant[1]
            else:
                dic[key] = value
        self.tournament_in_progress.insert(dic)

    def add_round(self, round_in_progress):
        dic = {}
        for round in round_in_progress:
            for key, value in round.__dict__.items():
                dic[key] = value
            self.round_tournament.insert(dic)
        pass


    def closing_tournament(self):
        """Pour transférer le tournoi clôturé vers les tournois finis."""
        # self.tournament_finished.insert(self.tournament_in_progress)
        self.round_tournament.truncate()
        return self.tournament_in_progress.truncate()

    def save_round(self, round_update):

        # update = {}
        # for key, value in round_update.__dict__.items():
        #     update[key] = value
        self.round_tournament.update(round_update, where("name") == round_update["name"])
        pass