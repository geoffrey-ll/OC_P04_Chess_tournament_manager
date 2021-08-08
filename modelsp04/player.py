#! /usr/bin/env python3
# coding: utf-8


from operator import attrgetter


class Player:
    """Ceci est ma classe Players."""

    list_all_player = []

    def __init__(self, player_controller, index=int(), first_name="", last_name="", date_of_birth="", gender="", current_elo=int()):
        """Initialissation de la classe Players."""
        self.controller = player_controller
        self.index = index
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.current_elo = current_elo

                 # index, first_name, last_name, date_of_birth, gender, current_elo):

        # self.index = index
        # self.first_name = first_name
        # self.last_name = last_name
        # self.date_of_birth = date_of_birth
        # self.gender = gender
        # self.current_elo = current_elo

    def sorting_default(self):
        self.list_all_player.sort(key=attrgetter('index'))
        return self.list_all_player

    def sorting_alphabetical(self):
        self.list_all_player.sort(key=attrgetter("last_name", "first_name", "current_elo", "index"))
        list_all_player_alphabetical = []
        for player in self.list_all_player:
            list_all_player_alphabetical.append(player)
        return list_all_player_alphabetical

    def sorting_elo(self):
        self.list_all_player.sort(key=attrgetter("current_elo", "last_name", "first_name", "index"))
        list_all_player_elo = []
        for player in self.list_all_player:
            list_all_player_elo.append(player)
        return list_all_player_elo

    def new_player(self, input_new_player):
        """Cette méthode instancie un joueur et l'ajoute à la liste des joueurs."""
        index = len(self.list_all_player)
        first_name = input_new_player[0]
        last_name = input_new_player[1]
        date_of_birth = input_new_player[2]
        gender = input_new_player[3]
        current_elo = int(input_new_player[4])
        new_player = Player('player_controller', index, first_name, last_name, date_of_birth, gender, current_elo) # Le premier argument '' correspond à l'argument player_controller


        self.list_all_player.append(new_player)



