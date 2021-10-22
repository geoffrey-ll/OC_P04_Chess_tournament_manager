#! /usr/bin/env python3
# coding: utf-8


class TournamentView:
    """La vue tournoi parent."""

    def __init__(self, tournament_controller):
        """Initialisation de la classe TournamentView."""
        self.controller = tournament_controller

    @staticmethod
    def display_title_1():
        """Affichage du titre niveau 1."""
        display_title_1 = "OpenClassrooms chess club"
        return print("{:^202}".format(display_title_1))


class StartTournamentView(TournamentView):
    """La vue création de tournoi (enfant)."""

    def __init__(self, tournament_controller):
        """Initialisation de la classe StartTournamentView."""
        super().__init__(tournament_controller)

    def get_len_tournaments_finished(self):
        """
        Demande le nombre de tournois terminés enregistrés.
        Sert pour déterminer l'index du prochain tournoi.
        """
        len_finished = self.controller.get_len_tournaments_finished()
        return len_finished

    @staticmethod
    def display_title_2():
        """Affichage du titre niveau 2 (création tournoi)."""
        display_title_2 = "Sart a tournament"
        return print("{:^202}".format(display_title_2))

    def display_view_start_tournament(self):
        """
        Affichage de la vue de création d'un nouveau tournoi. (hors inputs).
        """
        self.display_title_1()
        return self.display_title_2()

    @staticmethod
    def display_time_control():
        """Affichage des choix de time_control."""
        list_time_control = ["Bullet", "Blitz", "Quick"]
        print("Time control : ", end='')
        for idx, value in enumerate(list_time_control):
            if idx == 0:
                print("[{}] : {}".format(idx, value))
            else:
                print("{:15}[{}] : {}".format('', idx, value))
        return ''

    def display_description_default(self):
        """Affichage de la description par défaut."""
        len_finished = self.get_len_tournaments_finished()
        len_in_progress = len_finished + 1
        return "Tournament n°{} of 2021.".format(len_in_progress)

    def input_name(self, invalide="false"):
        """Demande à l'utilisateur le nom du tournoi à créer."""
        if invalide == "false":
            input_name = input("Name of tournament : ").capitalize()
            return self.controller.check_name(input_name)
        elif invalide == "true":
            print("\nNo entry")
            return self.input_name()

    def input_place(self, invalide="false"):
        """Demande à l'utilisateur le lieu du tournoi à créer."""
        if invalide == "false":
            input_place = input("Place of tournament : ").capitalize()
            return self.controller.check_place(input_place)
        elif invalide == "true":
            print("\nNo entry")
            return self.input_place()

    def input_participant(self, invalide="false"):
        """
        Demande à l'utilisateur les index des participants au tournoi à créer.
        """
        if invalide == "false":
            input_participants = input("Participants (player index) : ")
            return self.controller.check_participant(input_participants)
        elif invalide == "true":
            print("\nSome participants were not found")
            return self.input_participant()

    def input_round(self, invalide="false"):
        """Demande à l'utilisateur le nombre de round du tournoi à créer."""
        if invalide == "false":
            input_round = input("Round : 4 ")
            return self.controller.check_round(input_round)
        elif invalide == "true":
            print("\nInvalid answer")
            return self.input_round()

    def input_time_control(self, invalide="false"):
        """Demande à l'utilisateur le genre de match (durée) du tournoi à créer."""
        if invalide == "false":
            input_time_control = input(self.display_time_control())
            return self.controller.check_time_control(input_time_control)
        elif invalide == "true":
            print("\nInvalide answer")
            return self.input_time_control()

    def input_description(self):
        """Demande à l'utilisateur une description du tournoi à créer."""
        input_description = input("Description : {}\n"
                                  .format(self.display_description_default()))
        return self.controller.check_description(input_description)


class ManagerTournamentView(TournamentView):
    """La vue pour le management du tournoi (enfant)."""

    def __init__(self, tournament_controller):
        """Initialisation de la classe ManagerTournamentView."""
        super().__init__(tournament_controller)

    @staticmethod
    def display_title_manager():
        """Affichage du titre niveau 2 (management tournoi)."""
        display_title_manager = "Tournament manager"
        return print("{:^202}".format(display_title_manager))

    def display_view_manager_tournament(self):
        """Affichage de la vue management de tournoi."""
        self.display_title_1()
        return self.display_title_manager()

    def display_winner_tournament(self, winner):
        """Affichage du vainqueur du tournoi."""
        self.display_view_manager_tournament()
        print(winner)
        return input("Press any key to continue")


class FinishedTournamentView(TournamentView):
    """La vue des tournois terminés (enfant)."""

    def __init__(self, tournament_controller):
        """Initialisation da la classe FinishedTournamentView."""
        super().__init__(tournament_controller)

    def get_unserial_tournaments_finished(self):
        """Demande la désérialisation des tournois terminés."""
        return self.controller.get_unserial_tournaments_finished()

    @staticmethod
    def display_title_finished():
        """Affichage du titre de niveau 2 (tournoi terminés)."""
        display_title_finished = "List of tournaments finished"
        return print("{:^202}".format(display_title_finished))

    def display_view_no_tournament_finished(self):
        """Affichage quand aucun tournoi terminé dans la base de données."""
        print("No finished tournaments in the database")
        self.display_options()
        return self.option_choice()

    @staticmethod
    def display_headers():
        """Affichage des en-têtes."""
        headers_line_1 = ["Index", "Name", "Place", "Round", "Time control",
                          "List participants", "Description"]
        headers_line_2 = "(Id Last First Score)"
        print(("{0}"*152).format('-'))
        print('|', end='')
        for header in headers_line_1:
            if header == "Index" or header == "Round":
                print(" {:^5} |".format(header), end='')
            elif header == "List participants" or header == "Description":
                print(" {:^30} |".format(header), end='')
            else:
                print(" {:^20} |".format(header), end='')
        print("\n|{0}|{1}|{1}|{0}|{1}|{2:^32}|{3}|"
              .format(' '*7, ' '*22, headers_line_2, ' '*32))
        return print(("{0}"*152).format('-'))

    @staticmethod
    def display_options():
        """Affichage des options."""
        list_options = ["Return to home page"]
        print("\n")
        return print("[R] : {}".format(list_options[0]))

    def option_choice(self):
        """Option choisit par l'utilisateur."""
        user_input = input().capitalize()

        if user_input == "R":
            return self.controller.display_view_home_page()
        else:
            return self.display_view_list_finished_tournaments(True)

    def display_view_list_finished_tournaments(self, invalide=False):
        """Affichage de la liste des tournois terminés."""
        self.display_title_1()
        self.display_title_finished()
        self.display_headers()
        list_finished_tournaments = self.get_unserial_tournaments_finished()

        if list_finished_tournaments == "empty":
            return self.display_view_no_tournament_finished()
        else:
            for tournament in list_finished_tournaments:
                for count in range(len(tournament.index)):
                    for attribut in tournament.__dict__.keys():
                        if attribut == "len_participants" \
                                or attribut == "controller":
                            continue
                        else:
                            values = tournament.__getattribute__(attribut)
                            print(values[count], end='')
                    print("")
                print(("{0}"*152).format('-'))

            self.display_options()
            if invalide is True:
                print("\nInvalide option")
            return self.option_choice()
