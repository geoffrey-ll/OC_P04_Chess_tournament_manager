#! /usr/bin/env python3
# coding: utf-8


import inspect


# def decorateur(func):
#     def inner(self, *args, **kwargs):
#         for param in inspect.signature(func).parameters.values():
#             print(param)
#             if str(param) == "invalide='False'":
#                 return func(self)
#             elif str(param) == "invalide='True'":
#                 print("\nRéponse invalide")
#                 return func(self)
#     return inner




class TournamentView:
    """"""

    def __init__(self, tournament_controller):
        self.controller = tournament_controller

    @staticmethod
    def display_title_1():
        display_title_1 = "Tournoi d'échec du club OpenClassrooms"
        return print("{:^202}".format(display_title_1))

    def display_view_finished_tournaments(self):
        pass



class StartTournamentView(TournamentView):

    def __init__(self, tournament_controller):
        super().__init__(tournament_controller)
        pass



    @staticmethod
    def display_title_2():
        """Affichage du titre niveau 2."""
        display_title_2 = "Sart a tournament"
        return print("{:^202}".format(display_title_2))

    def display_view_start_tournament(self):
        """Affichage de la vue de création d'un nouveau tournoi."""
        self.display_title_1()
        self.display_title_2()

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

    @staticmethod
    def display_description_default():
        """Affichage de la description par défaut."""
        return "Tournament n°{} of 2021.".format("xx")


    def input_name(self, invalide="FALSE"):
        """Demande à l'utilisateur le nom du tournoi à créer."""

        if invalide == "FALSE":
            input_name = input("Name of tournament : ").capitalize()
            return self.controller.check_name(input_name)
        elif invalide == "TRUE":
            print("\nNo entry")
            return self.input_name()

    def input_place(self, invalide="FALSE"):
        """Demande à l'utilisateur le lieu du tournoi à créer."""
        if invalide == "FALSE":
            input_place = input("Place of tournament : ").capitalize()
            return self.controller.check_place(input_place)
        elif invalide == "TRUE":
            print("\nNo entry")
            return self.input_place()

    def input_participant(self, invalide="FALSE"):
        """Demande à l'utilisateur les participants du tournoi à créer."""
        if invalide == "FALSE":
            input_participants = input("Participants (player index) : ")
            return self.controller.check_participant(input_participants)
        elif invalide == "TRUE":
            print("Some participants were not found")
            return self.input_participant()

    def input_round(self, invalide="FALSE"):
        """Demande à l'utilisateur le nombre de round du tournoi à créer."""
        if invalide == "FALSE":
            input_round = input("Round : 4 ")
            return self.controller.check_round(input_round)
        elif invalide == "TRUE":
            print("\nInvalid answer")
            return self.input_round()

    def input_match_in_round(self, invalide="FALSE"):
        """
        Demande à l'utilisateur le nombre de match par round du tournoi à créer.
        """
        if invalide == "FALSE":
            input_match_in_round = input("Match in round :")
            return self.controller.check_match_in_round(input_match_in_round)
        elif invalide == "TRUE":
            print("\nInvalide answer")
            return self.input_match_in_round()

    def input_time_control(self, invalide="FALSE"):
        """Demande à l'utilisateur le genre de match (durée) du tournoi à créer."""
        if invalide == "FALSE":
            input_time_control = input(self.display_time_control())
            return self.controller.check_time_control(input_time_control)
        elif invalide == "TRUE":
            print("\nInvalide answer")
            return self.input_time_control()

    def input_description(self):
        """Demande à l'utilisateur une description du tournoi à créer."""
        input_description = input("Description : {}\n"
                                  .format(self.display_description_default()))
        return self.controller.check_description(input_description)





class ManagerTournamentView(TournamentView):
    def __init__(self, tournament_controller):
        super().__init__(tournament_controller)

    @staticmethod
    def display_title2():
        display_title_2 = "Tournament manager"
        return print("{:^202}".format(display_title_2))

    def display_view_manager_tournament(self):
        self.display_title_1()
        self.display_title2()
        print("En cours de contruction !!")
        pass