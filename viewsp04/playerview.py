#! /usr/bin/env python3
# coding: utf-8


class PlayerView:
    """Ceci est ma classe ListOfPlayers."""

    def __init__(self, player_controller):
        """Initialisation de la classe ListOfPlayers."""
        self.controller = player_controller
        # self.title1 = title_1
        # self.title2 = title_2
        # self.header = header
        # self. lines_player = lines_player
        # self. options = options

    def display_title_1(self):
        """Affichage du titre niveau 1."""
        display_title_1 = "Tournoi du club OpenClassRooms"
        return print("{:^202}".format(display_title_1))

    def display_title_2(self):
        """Affichage du titre niveau 2."""
        display_title_2 = "Liste des joueurs"
        return print("{:^202}".format(display_title_2))

    def display_headers(self):
        """Affichage des headers."""
        list_headers = ["Index", "First name", "Last name", "Date of birth", "Gender", "Current Elo"]
        print(("{0}"*133).format('-'))
        print('|', end='')
        for values in list_headers:
            print("{:^20} |".format(values), end='')
        print(("\n" + "{0}"*133).format('-'))

    def display_player(self):
        """Affichage des joueurs."""
        pass

    def display_options(self):
        """Affichage des options."""
        list_options = ["New player", "Data player", "Alphabetical sorting", "Index sorting", "Elo sorting", "Return to home page"]
        print("\n[N] : {}\n".format(list_options[0]))
        print("[#] : {}".format(list_options[1]))
        print("[A] : {}".format(list_options[2]))
        print("[I] : {}".format(list_options[3]))
        print("[E] : {}\n".format(list_options[4]))
        print("[R] : {}".format(list_options[5]))

    def display_view_list_players(self, sorting_option="DEFAULT"):
        """Affichage de la vue list_of_player."""
        self.display_title_1()
        self.display_title_2()
        self.display_headers()
        list_players = self.controller.get_list_players(sorting_option)
        for idx, player, in enumerate(list_players):
            if list_players == []:
                pass
            else:
                print('|', end='')
                # print(" {:<19} |".format(idx), end='')
                for value in player.__dict__.values():
                    if value == 'player_controller':
                        pass
                    else:
                        print(" {:<19} |".format(str(value)), end='')
                print(("\n" + "{0}"*133).format('-'))

        self.display_options()
        return self.option_choice(sorting_option)

    def option_choice(self, sorting_option):

        user_input = input().capitalize()
        if user_input == 'N':
            return self.controller.new_player(sorting_option)
        elif user_input == 'A':
            return self.display_view_list_players("ALPHABETICAL")
        # ou return self.controller.display_view_list_players(sorting_option) ????
        elif user_input == 'I':
            return self.display_view_list_players("DEFAULT")
        elif user_input == 'E':
            return self.display_view_list_players("ELO")
        else:
            return print("Option invalide")

    def new_player(self):
        input_new_player = [input("First name : ").capitalize(),
                    input("Last name : ").capitalize(), input("Date of birth : "),
                    input("Gender : "), input("Current Elo : ")]
        return input_new_player


