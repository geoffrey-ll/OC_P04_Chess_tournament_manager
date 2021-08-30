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

    def display_options(self, status):
        """Affichage des options."""
        if status == "empty":
            list_options = ["Start a tournament",
                            "Finished tournaments",
                            "Players list",
                            "Quit"]
        elif status == "no empty":
            list_options = ["Tournament in progress",
                            "Finished tournaments",
                            "Players list",
                            "Quit"]

        for idx, value in enumerate(list_options):
            print("{:>85}{}] : {}".format('[', idx, value))
        return status

    def display_view_home_page(self, status):
        """Affichage de la vue de la page d'accueil."""
        self.display_title_1()
        self.display_title_2()
        self.display_options(status)
        return self.option_choice(status)

    def option_choice(self, status):
        """
        Instructions selon l'option choisit dans la vue de la page d'accueil.
        """
        user_input = input()

        if user_input == "0":
            if status == "empty":
                return self.controller.new_tournament()
            elif status == "no empty":
                return self.controller.manage_tournament()
        elif user_input == "1":
            pass
        elif user_input == "2":
            return self.controller.display_view_list_players()

        elif user_input == "3":
            quit()
        else:
            print("Option invalide.")
