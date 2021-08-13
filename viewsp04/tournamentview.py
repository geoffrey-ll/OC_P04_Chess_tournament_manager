#! /usr/bin/env python3
# coding: utf-8


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

    # def add_tournament(self):
    #     input_new_tournament = [
    #         input("Name of tournament : ").capitalize(),
    #         input("Place of tournament : ").capitalize(),
    #         input("Participants (player index) : "),
    #         input("Round : 4 "),
    #         input("Match in round : "),
    #         input(StartTournamentView.time_control()),
    #         input("Description : {}"
    #               .format(StartTournamentView.description_default()))]
    #     return input_new_tournament


class StartTournamentView(TournamentView):

    def __init__(self, tournament_controller):
        super().__init__(tournament_controller)
        pass

    @staticmethod
    def display_title_2():
        display_title_2 = "Sart a tournament"
        return print("{:^202}".format(display_title_2))

    @staticmethod
    def time_control():
        list_time_control = ["Bullet", "Blitz", "Quick"]
        print("Time control : ", end='')
        for idx, value in enumerate(list_time_control):
            if idx == 0:
                print("[{}] : {}".format(idx, value))
            else:
                print("{:15}[{}] : {}".format('', idx, value))
        return ''

    @staticmethod
    def description_default():
        return "Tournament n°{} of 2021.".format("xx")

    def add_tournament(self):
        input_new_tournament = [input("Name of tournament : ").capitalize(),
                                input("Place of tournament : ").capitalize(),
                                input("Participants (player index) : "),
                                input("Round : 4 "),
                                input("Match in round : "),
                                input(self.time_control()),
                                input("Description : {}"
                                      .format(self.description_default()))]
        return input_new_tournament

    def display_view_start_tournament(self):
        self.display_title_1()
        self.display_title_2()
        input_new_tournament = self.add_tournament()
        return input_new_tournament


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
        print("")
        pass