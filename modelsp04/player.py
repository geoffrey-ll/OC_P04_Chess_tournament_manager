#! /usr/bin/env python3
# coding: utf-8


from operator import attrgetter


class Player:
    """Ceci est la classe Player."""

    list_all_player = []

    def __init__(self, player_controller, index=int(), first_name="",
                 last_name="", date_of_birth="", gender="", current_elo=int()):
        """Initialisation de la classe Player."""
        self.controller = player_controller

        self.index = index
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.current_elo = current_elo

    def import_db_players(self, dict_all_player):
        """
        Ajoute les players de la base de données, à la liste des players du
        script.
        """
        for dict_player in dict_all_player:
            index = dict_player["index"]
            first_name = dict_player["first_name"]
            last_name = dict_player["last_name"]
            date_of_birth = dict_player["date_of_birth"]
            gender = dict_player["gender"]
            currend_elo = dict_player["current_elo"]
            player = Player("player_controller", index, first_name, last_name,
                            date_of_birth, gender, currend_elo)
            # OU faire plutôt comme ci-dessous ?????
            # player = Player("player_controller",
            #                 dict_player["index"],
            #                 dict_player["first_name"],
            #                 dict_player["last_name"]
            #                 dict_player["date_of_birth"]
            #                 dict_player["gender"]
            #                 dict_player["current_elo"])

            self.list_all_player.append(player)

    def sorting_default(self):
        """
        Retourne vers le player_controller, la liste des players du script
        ordonnés par leur index.
        """
        self.list_all_player.sort(key=attrgetter('index'))
        return self.list_all_player

    def sorting_alphabetical(self):
        """
        Retourne vers le player_controller, la liste des players du script
        ordonnés par leur last_name.
        """
        self.list_all_player.sort(key=attrgetter("last_name", "first_name",
                                                 "current_elo", "index"))
        list_all_player_alphabetical = []
        for player in self.list_all_player:
            list_all_player_alphabetical.append(player)
        return list_all_player_alphabetical

    def sorting_elo(self):
        """
        Retourne vers le player_controller, la liste des players du script
        ordonnés par leur current_elo.
        """
        self.list_all_player.sort(key=attrgetter("current_elo", "last_name",
                                                 "first_name", "index"))
        list_all_player_elo = []
        for player in self.list_all_player:
            list_all_player_elo.append(player)
        return list_all_player_elo

    def add_player(self, input_new_player):
        """
        Cette méthode instancie un joueur et l'ajoute à la liste des players du
        script, puis renvoi le nouveau player vers le player_controller pour
        qu'il soit ajouté à la base de données.
        """
        index = len(self.list_all_player)  # Faire un +1 pour que la valeur
        # corresponde à celle de l'index de la base de données ?
        first_name = input_new_player[0]
        last_name = input_new_player[1]
        date_of_birth = input_new_player[2]
        gender = input_new_player[3]
        current_elo = int(input_new_player[4])
        new_player = Player("player_controller", index, first_name, last_name,
                            date_of_birth, gender, current_elo)
        self.list_all_player.append(new_player)
        return new_player
