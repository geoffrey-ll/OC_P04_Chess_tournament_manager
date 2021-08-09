#! /usr/bin/env python3
# coding: utf-8


from viewsp04.homepageview import HomePageView


class HomePageController:
    """Le controller de la page d'accueil."""

    def __init__(self, master_controller):
        """Initialise le home_page_controller."""
        self.view = HomePageView(self)
        self.controller = master_controller

    def display_view_home_page(self):
        """Demande la vue de la page d'accueil."""
        return self.view.display_view_home_page()

    def display_view_list_players(self):
        """demande la vue list des players au master_controller."""
        return self.controller.display_view_list_players()
