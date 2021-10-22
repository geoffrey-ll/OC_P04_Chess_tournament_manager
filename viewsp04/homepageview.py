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
        display_title_1 = "OpenClassrooms chess club"
        return print("{:^202}".format(display_title_1))

    @staticmethod
    def display_title_2():
        """Affichage du titre niveau 2."""
        display_title_2 = "Home page"
        return print("{:^202}".format(display_title_2))

    @staticmethod
    def display_options(status):
        """Affichage des options."""
        list_options = []
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

    def display_view_home_page(self, invalide_option=False):
        """Affichage de la vue de la page d'accueil."""
        self.display_title_1()
        self.display_title_2()
        status = self.controller.get_tournament_in_progress_or_not()
        self.display_options(status)
        if invalide_option is True:
            print("\nInvalide option")
        return self.option_choice(status)

    def option_choice(self, status):
        """
        Instructions selon l'option choisit dans la vue de la page d'accueil.
        """
        user_input = input().lower()

        if user_input == "0":
            if status == "empty":
                return self.controller.new_tournament()
            elif status == "no empty":
                return self.controller.tournament_manager()
        elif user_input == "1":
            return self.controller.display_view_list_finished_tournaments()
        elif user_input == "2":
            return self.controller.display_view_list_players()
        elif user_input == "3" or user_input == '':
            return quit()
        elif user_input == "reset":
            self.controller.reinitialize_for_test()
            return self.display_view_home_page()
        else:
            return self.display_view_home_page(True)
