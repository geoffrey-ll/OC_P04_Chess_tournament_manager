#! /usr/bin/env python3
# coding: utf-8


from viewsp04.homepageview import HomePageView


class HomePageController:
    """Le controller de la page d'accueil."""

    def __init__(self, master_controller):
        """Initialise le home_page_controller."""
        self.view = HomePageView(self)
        self.controller = master_controller

    def display_view_home_page(self, status):
        """Demande la vue de la page d'accueil."""
        return self.view.display_view_home_page(status)

    def display_view_list_players(self):
        """Demande la vue list des players au master_controller."""
        return self.controller.display_view_list_players()

    def display_view_list_finished_tournaments(self):
        return self.controller.display_view_list_finished_tournaments()
        pass

    def tournament_manager(self):
        return self.controller.tournament_manager()

    def new_tournament(self):
        """Renvoi les inputs pour la création d'un nouveau tournoi."""
        return self.controller.new_tournament()

