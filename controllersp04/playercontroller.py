#! /usr/bin/env python3
# coding: utf-8


from modelsp04.player import Player

from viewsp04.playerview import PlayerView


class PlayerController:
    """Controller du projet."""

    def __init__(self):
        """Initialise le Controller."""

        self.view = PlayerView(self)
        self.model = Player(self)


    def display_view_list_players(self):
        return self.view.display_view_list_players()
        # input = PlayerView.display_view_list_players()
        # if input == 'N':
        #     PlayerController.new_player()
    def get_list_players(self, sorting_option):
        """Récupére la liste des joueurs."""
        if sorting_option == "DEFAULT":
            return self.model.sorting_default()
        elif sorting_option == "ALPHABETICAL":
            return self.model.sorting_alphabetical()
        elif sorting_option == "ELO":
            return self.model.sorting_elo()
        else:
            pass

    def new_player(self, sorting_option):
        input_new_player = self.view.new_player()
        self.model.new_player(input_new_player)

        return self.view.display_view_list_players(sorting_option)

    # def sorting_alphabetical(self):
    #     self.model.sorting_alphabetical()






# player1 = Players("0" ,"Geoffrey", "Llopis", "Inconnue", "M", "1100")

control1 = PlayerController()
control1.display_view_list_players()



