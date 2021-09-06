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
            if round["status_round"] == "TO_DO":
                return round
            else:
                pass

    def get_round_in_progress(self):
        for round in self.round_tournament:
            if round["status_round"] == "IN_PROGRESS":
                return round
            else:
                pass
        return "NO_ROUND_IN_PROGRESS"
        pass

    def get_status_participants(self):
        dico_tournament = self.tournament_in_progress.search(Query().controller == "tournament_controller")
        return dico_tournament[0]["status_participants"]

    def get_players_participants(self):
        """Remarque : dans la base de données, les scores elo sont stockés comme entier négatifs."""
        index_participants = self.get_index_participants() # utiliser get_status_participants juste au-dessus !!!!!!!!!!!!!!!!!
        players_participants = []
        for idx in index_participants:
            players_participants.append(self.player.search(Query().index == int(idx))[0])
        return players_participants
        pass

    def get_index_participants(self):
        index_participants = []
        dico_tournament = self.tournament_in_progress.search(Query().controller == "tournament_controller")
        for key in dico_tournament[0]["status_participants"]:
            index_participants.append(re.findall("[0-9]+", key)[0])
        return index_participants
        pass

    def get_elo_participants(self):
        """Remarque : dans la base de données, les scores elo sont stockés comme entier négatifs."""
        index_participants = self.get_index_participants()
        elo_participants = []
        for index in index_participants:
            elo_participant = {}
            player = self.player.search(Query().index == int(index))
            elo_participant["index_player"] = index
            elo_participant["current_elo"] = -player[0]["current_elo"]
            elo_participants.append(elo_participant)
        return elo_participants
        pass

    def get_player_exists(self, index_to_check):
        participants_validate = {}
        for indexx in index_to_check:
            if self.player.search(Query().index == int(indexx)):
                participants_validate["player_index_{}".format(indexx)] = {}
                participants_validate["player_index_{}".format(indexx)]["score"] = 0
                participants_validate["player_index_{}".format(indexx)]["colors"] = []
                participants_validate["player_index_{}".format(indexx)]["opponent_index"] = []
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