#! /usr/bin/env python3
# coding: utf-8


from modelsp04.player import Player
from viewsp04.playerview import PlayerView


class PlayerController:
    """Le controller des players."""

    def __init__(self, master_controller):
        """Initialisation de la classe PlayerController."""
        self.model = Player(self)
        self.view = PlayerView(self)
        self.controller = master_controller

    def get_unserial_list_players(self):
        """Demande la désérialisation de la liste des joueurs."""
        list_players_in_db = self.controller.get_list_players()
        return self.model.unserial_list_players(list_players_in_db)

    def get_unserial_players_participants(self, players_participants_in_db):
        """Demande la désérialisation des participants du tournoi en cours."""
        return self.model.unserial_list_players(players_participants_in_db)

    def get_list_players(self):
        """Demande la liste de tous les joueurs enregistrés."""
        return self.controller.get_list_players()

    def get_len_players_in_db(self):
        """
        Demande le nombre de joueurs enregistrés.
        Sert pour déterminer l'index du prochain nouveau joueur.
        """
        return self.controller.get_len_players_in_db()

    def display_view_list_players(self):
        """Demande la vue liste des joueurs."""
        return self.view.display_view_list_players()

    def display_view_home_page(self):
        """Demande la vue de la page d'accueil."""
        return self.controller.display_view_home_page()

    def add_player(self, new_player, sorting_option):
        """
        Instructions pour créer et enregistrer un nouveau joueur et actualiser
        l'affichage de la liste des joueurs.
        """
        player = self.model.add_player(new_player)
        self.controller.add_player(player)
        return self.view.display_view_list_players(sorting_option)

    def new_player(self, sorting_option):
        """
        Récupére les différents inputs pour la création d'un nouveau joueur.
        """
        new_player = []
        new_player.append(self.view.input_first_name())
        new_player.append(self.view.input_last_name())
        new_player.append(self.view.input_date_birth())
        new_player.append(self.view.input_gender())
        new_player.append(self.view.input_current_elo())
        return self.add_player(new_player, sorting_option)

    def check_first_name(self, input_first_name):
        """Demande la validité de l'input_first_name."""
        check = self.model.check_first_name(input_first_name)
        if check == "true":
            return self.view.input_first_name("true")
        else:
            return check

    def check_last_name(self, input_last_name):
        """Demande la validité de l'input_last_name."""
        check = self.model.check_last_name(input_last_name)
        if check == "true":
            return self.view.input_last_name("true")
        else:
            return check

    def check_date_birth(self, input_date_birth):
        """Demande la validité de l'input_date_birth."""
        check = self.model.check_date_birth(input_date_birth)
        if check == "true":
            return self.view.input_date_birth("true")
        else:
            return check

    def check_gender(self, input_gender):
        """Demande la validité de l'input_gender."""
        check = self.model.check_gender(input_gender)
        if check == "true":
            return self.view.input_gender("true")
        else:
            return check

    def check_current_elo(self, input_current_elo):
        """Demande la validité de d'input_current_elo."""
        check = self.model.check_current_elo(input_current_elo)
        if check == "true":
            return self.view.input_current_elo("true")
        elif check == "inhuman":
            return self.view.input_current_elo("inhuman")
        else:
            return check

    def sort_players(self, sorting_option):
        """Instructions pour récupérer et trier la liste des joueurs."""
        list_players = self.get_unserial_list_players()
        if sorting_option == "default":
            return self.model.sorting_default(list_players)
        elif sorting_option == "alphabetical":
            return self.model.sorting_alphabetical(list_players)
        elif sorting_option == "elo":
            return self.model.sorting_elo(list_players)
        else:
            pass
