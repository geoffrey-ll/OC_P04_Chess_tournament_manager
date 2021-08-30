#! /usr/bin/env python3
# coding: utf-8


import re

class PlayerView:
    """Ceci est la vue de la liste des players du script."""

    def __init__(self, player_controller):
        """Initialisation de la vue de la liste des players du script."""
        self.controller = player_controller

    @staticmethod
    def display_title_1():
        """Affichage du titre niveau 1."""
        display_title_1 = "Tournoi d'échec du club OpenClassrooms"
        return print("{:^202}".format(display_title_1))

    @staticmethod
    def display_title_2():
        """Affichage du titre niveau 2."""
        display_title_2 = "Liste des joueurs"
        return print("{:^202}".format(display_title_2))

    @staticmethod
    def display_headers():
        """Affichage des headers."""
        list_headers = ["Index", "First name", "Last name",
                        "Date of birth", "Gender", "Current Elo"]
        print(("{0}"*133).format('-'))
        print('|', end='')
        for values in list_headers:
            print("{:^20} |".format(values), end='')
        print(("\n" + "{0}"*133).format('-'))

    def display_player(self):
        """Affichage des donnés d'un joueur."""
        pass

    @staticmethod
    def display_options():
        """Affichage des options."""
        list_options = ["New player", "Data player", "Alphabetical sorting",
                        "Index sorting", "Elo sorting", "Return to home page"]
        print("\n[N] : {}\n".format(list_options[0]))
        print("[#] : {}".format(list_options[1]))
        print("[A] : {}".format(list_options[2]))
        print("[I] : {}".format(list_options[3]))
        print("[E] : {}\n".format(list_options[4]))
        print("[R] : {}".format(list_options[5]))

    def display_view_list_players(self, sorting_option="DEFAULT", invalide_option=False):
        """Affichage de la vue list_of_player."""
        self.display_title_1()
        self.display_title_2()
        self.display_headers()
        list_players = self.controller.sort_players(sorting_option)
        for idx, player, in enumerate(list_players):
            if list_players == []:
                pass
            else:
                print('|', end='')
                for key, value in player.items():
                    if value == "player_controller":
                        pass
                    else:
                        print(" {:<19} |".format(str(value)), end='')
                print(("\n" + "{0}"*133).format('-'))
        self.display_options()
        if invalide_option is True:
            print("\nInvalide option")
        return self.option_choice(sorting_option)

    @staticmethod
    def add_player():
        """Les inputs relatifs à l'ajout d'un nouveau player."""
        input_new_player = [input("First name : ").capitalize(),
                            input("Last name : ").capitalize(),
                            input("Date of birth (yyyy.mm.dd) : "),
                            input("Gender : "),
                            input("Current Elo : ")]
        return input_new_player

    def option_choice(self, sorting_option):
        """
        Instructions selon l'option choisit dans la vue list des players du
        script.
        """
        user_input = input().capitalize()
        if user_input == 'N':
            return self.controller.add_player(sorting_option)
        elif user_input == 'A':
            return self.display_view_list_players("ALPHABETICAL")
        # ou return self.controller.display_view_list_players(sorting_option) ????
        elif user_input == 'I':
            return self.display_view_list_players("DEFAULT")
        elif user_input == 'E':
            return self.display_view_list_players("ELO")
        elif user_input == "R":
            return self.controller.display_view_home_page()
        else:
            invalide_option = True
            return self.display_view_list_players(sorting_option, invalide_option)

