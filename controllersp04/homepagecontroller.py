#! /usr/bin/env python3
# coding: utf-8


from viewsp04.homepageview import HomePageView


class HomePageController:
    """Le controller de la page d'accueil."""

    def __init__(self, master_controller):
        """Initialise le home_page_controller."""
        self.view = HomePageView(self)
        self.controller = master_controller

    def get_tournament_in_progress_or_not(self):
        """Pour savoir si un tournoi est en cours ou pas."""
        return self.controller.get_tournament_in_progress_or_not()

    def display_view_home_page(self):
        """Demande la vue de la page d'accueil."""
        return self.view.display_view_home_page()

    def display_view_list_players(self):
        """Demande la vue players list."""
        return self.controller.display_view_list_players()

    def display_view_list_finished_tournaments(self):
        """Demande la vue finished tournaments."""
        return self.controller.display_view_list_finished_tournaments()

    def tournament_manager(self):
        """Demande la vue du manager tournament."""
        return self.controller.tournament_manager()

    def new_tournament(self):
        """Renvoi les inputs pour la création d'un nouveau tournoi."""
        return self.controller.new_tournament()

    def reinitialize_for_test(self):
        """
        Pour purger des tables dans la base de données (utile pendant dev).
        """
        return self.controller.reinitialize_for_test()
