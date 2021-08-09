#! /usr/bin/env python3
# coding: utf-8


class HomePageView:
    """Ceci est la vue de la page d'accueil."""

    def __init__(self, home_page_controller):
        """Initialise la vue de la page d'accueil."""
        self.controller = home_page_controller

    @staticmethod
    def display_title_1():
        """Affichage du titre niveau 1."""
        display_title_1 = "Tournoi d'échec du club OpenClassrooms"
        return print("{:^202}".format(display_title_1))

    @staticmethod
    def display_title_2():
        """Affichage du titre niveau 2."""
        display_title_2 = "Accueil"
        return print("{:^202}".format(display_title_2))

    @staticmethod
    def display_options():
        """Affichage des options."""
        list_options = ["Start a tournament", "Tournament in progress",
                        "Finished tournaments",
                        "Players list",
                        "Backup",
                        "Quit"]
        for idx, value in enumerate(list_options):
            print("{:>85}{}] : {}".format('[', idx, value))

    def display_view_home_page(self):
        """Affichage de la vue de la page d'accueil."""
        self.display_title_1()
        self.display_title_2()
        self.display_options()
        return self.option_choice()

    def option_choice(self):
        """
        Instructions selon l'option choisit dans la vue de la page d'accueil.
        """
        user_input = int(input())
        if user_input == 3:
            return self.controller.display_view_list_players()

        elif user_input == 5:
            quit()
        else:
            print("Option invalide.")
