#! /usr/bin/env python3
# coding: utf-8


from tinydb import TinyDB, where , Query


class DataBase:
    """Ceci est la base de données."""

    db = TinyDB("db.json")
    player = db.table("player")
    tournament_in_progress = db.table("tournament_in_progress")
    tournament_finished = db.table("tournament_finished")
    round_in_progress = db.table("round_in_progress")

    def __init__(self, database_controller):
        """Initialisation de la base de données"""
        self.controller = database_controller

    def get_list_players(self):
        """Renvoi la liste de tous les joueurs de la base de données."""
        list_players = []
        for idx, player in enumerate(self.player):
            list_players.append(player)

        return list_players

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
        tournament_in_progress = []
        for idx, value in enumerate(self.tournament_in_progress):
            tournament_in_progress.append(value)
        return tournament_in_progress

    def get_list_round(self):
        list_round = []
        for idx, round in enumerate(self.round_in_progress):
            list_round.append(round)

        return list_round





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
            if key == "participants":
                dic[key] = {}
                for sub_key, sub_value in value.items():
                    dic[key][sub_key] = str(sub_value)
            else:
                dic[key] = value
        self.tournament_in_progress.insert(dic)

    def add_round(self, round_in_progress):
        dic = {}
        for round in round_in_progress:
            for key, value in round.__dict__.items():
                dic[key] = value
            self.round_in_progress.insert(dic)
        pass

    def closing_tournament(self):
        """Pour transférer le tournoi clôturé vers les tournois finis."""
        # self.tournament_finished.insert(self.tournament_in_progress)
        self.round_in_progress.truncate()
        return self.tournament_in_progress.truncate()

    def save_round(self, round_update):
        update = {}
        for key, value in round_update.__dict__.items():
            update[key] = value
        self.round_in_progress.update(update, where("name") == round_update.name)
        pass