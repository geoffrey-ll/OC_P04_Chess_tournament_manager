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


    def get_len_tournaments_finished(self):
        len_finished =  self.controller.get_len_tournaments_finished()
        return len_finished
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

    def display_description_default(self):
        """Affichage de la description par défaut."""
        len_finished = self.get_len_tournaments_finished()

        len_in_progress = len_finished + 1
        return "Tournament n°{} of 2021.".format(len_in_progress)


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
            print("\nSome participants were not found")
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
            input_match_in_round = input("Match in round : ")
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
    def display_title_manager():
        display_title_manager = "Tournament manager"
        return print("{:^202}".format(display_title_manager))

    def display_view_manager_tournament(self):
        self.display_title_1()
        self.display_title_manager()
        pass

    def display_winner_tournament(self, winner):
        self.display_view_manager_tournament()
        print(winner)
        input()

        pass


class FinishedTournamentView(TournamentView):
    def __init__(self, tournament_controller):
        super().__init__(tournament_controller)
        pass

    def get_unserial_tournaments_finished(self):
        return self.controller.get_unserial_tournaments_finished()
        pass

    @staticmethod
    def display_title_finished():
        display_title_finished = "List of tournaments finished"
        return print("{:^202}".format(display_title_finished))
        pass

    def display_view_no_tournament_finished(self):
        self.display_title_1()
        self.display_title_finished()
        print("No finished tournaments in the database")
        return self.display_options()

    def display_headers(self):
        headers_line_1 = ["Index", "Name", "Place", "Round", "Time control", "List participants", "Description"]
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
        print("\n|{0}|{1}|{1}|{0}|{1}|{2:^32}|{3}|".format(' '*7, ' '*22, headers_line_2, ' '*32))
        print(("{0}"*152).format('-'))
        pass

    def display_options(self):
        list_options = ["Return to home page"]

        print("\n")
        print("[R] : {}".format(list_options[0]))
        pass

    def option_choice(self):
        user_input = input().capitalize()

        if user_input == "R":
            return self.controller.display_view_home_page()
        pass


    def display_view_list_finished_tournaments(self):
        self.display_title_1()
        self.display_title_finished()
        self.display_headers()
        list_finished_tournaments = self.get_unserial_tournaments_finished()

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
        return self.option_choice()
        pass


