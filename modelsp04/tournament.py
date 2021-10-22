#! /usr/bin/env python3
# coding: utf-8


import re


class Tournament:
    """Le model pour le tournoi en cours."""
    tournament_in_progress = []

    def __init__(self, tournament_oontroller, index=int(), name="", place="",
                 round=4, time_control=list, description="",
                 status_participants=list):
        """Initialisation de la classe Tournament."""
        self.controller = tournament_oontroller

        self.index = index
        self.name = name
        self.place = place
        self.round = round
        self.time_control = time_control
        self.description = description
        self.status_participants = status_participants

    def unserial_tournament_in_progress(self, in_progress):
        """Désérialisation du tournoi en cours."""
        self.tournament_in_progress = []

        index = in_progress["index"]
        name = in_progress["name"]
        place = in_progress["place"]
        round = in_progress["round"]
        time_control = in_progress["time_control"]
        description = in_progress["description"]
        status_participants = in_progress["status_participants"]

        self.tournament_in_progress = Tournament("tournament_controller",
                                                 index, name,
                                                 place, round,
                                                 time_control, description,
                                                 status_participants)

        return self.tournament_in_progress

    def add_tournament(self, new_tournament):
        """Création du tournoi en cours à partir des input utilisateur."""
        count_finished = self.controller.get_len_tournaments_finished()
        if count_finished == 0:
            index = 1
        else:
            index = count_finished + 1
        name = new_tournament[0]
        place = new_tournament[1]
        round = new_tournament[3]
        time_control = new_tournament[4]
        description = new_tournament[5]
        status_participants = new_tournament[2]

        self.tournament_in_progress = Tournament("tournament_controller",
                                                 index, name,
                                                 place, round,
                                                 time_control, description,
                                                 status_participants)
        return self.tournament_in_progress

    @staticmethod
    def check_name(input_name):
        """Vérifie la validité de l'input_name."""
        if input_name == '':
            return "true"
        else:
            return input_name

    @staticmethod
    def check_place(input_place):
        """Vérifie la validité de l'input_place."""
        if input_place == '':
            return "true"
        else:
            return input_place

    def check_participant(self, input_participant):
        """Vérifie la validité de l'input_participant."""
        index_to_check = re.findall("[0-9]+", input_participant)
        if index_to_check == []:
            return "true"
        check = self.controller.get_player_exists(index_to_check)
        return check

    @staticmethod
    def check_round(input_round):
        """Vérifie la validité de l'input_round."""
        if input_round == '':
            return 4
        elif input_round != '':
            if input_round.isdigit() is True:
                return int(input_round)
            else:
                return "true"

    @staticmethod
    def check_time_control(input_time_control):
        """Vérifie la validité de l'input_time_control."""
        while input_time_control != '0' \
                and input_time_control != '1' \
                and input_time_control != '2':
            return "true"
        else:
            return input_time_control

    @staticmethod
    def check_description(input_description):
        """Vérifie la lavalidité de l'input_description."""
        if input_description == '':
            return "true"
        else:
            return input_description

    def adding_score_round(self, matchs_round_to_close):
        """À la fin d'un round, ajout du score du round des participants,
        à leur score de tournoi (score cummulé)."""
        in_progress = self.controller.get_unserial_tournament_in_progress()
        for match in matchs_round_to_close:
            try:
                idx_a = match.participant_a["index"]
                score_a = match.participant_a["score"]
                short = "player_index_{}".format(idx_a)
                in_progress.status_participants[short]["score"] += score_a
            except Exception as e:
                osef = []
                osef.append(e)
                continue

            try:
                idx_b = match.participant_b["index"]
                score_b = match.participant_b["score"]
                short = "player_index_{}".format(idx_b)
                in_progress.status_participants[short]["score"] += score_b
            except Exception as e:
                osef = []
                osef.append(e)
                continue
        return self.controller.save_tournament(in_progress)

    def designate_winner_tournament(self):
        # tournament = self.controller.get_unserial_tournament_in_progress()
        # sorted_by_score = tournament.status_participants\
        #     .sort(key=attrgetter("score"), reverse=True)
        #
        # winner = sorted_by_score[0]
        pass


class TournamentFinished:
    """Le model pour les tournois terminés."""

    list_finished_tournaments = []

    def __init__(self, finished_controller, len_participants=int(),
                 index=list(), name=list(), place=list(), round=list(),
                 time_control=list(), participants=list(), description=list()):
        """Initialisation de la classe TournamentFinished."""
        self.controller = finished_controller

        self.len_participants = len_participants
        self.index = index
        self.name = name
        self.place = place
        self.round = round
        self.time_control = time_control
        self.participants = participants
        self.description = description

    def get_data_player(self, index_participant):
        """demande les données d'un joueur selon son index."""
        return self.controller.get_data_player(index_participant)

    @staticmethod
    def unserial_index(tournament, len_participant):
        """Désérialisation de l'index du tournoi."""
        index = []
        index.append("| {:<5} |".format(tournament["tournament"]["index"]))
        for count in range(len_participant - 1):
            index.append("| {:<5} |".format(''))
        return index

    @staticmethod
    def unserial_name(tournament, len_participant):
        """Désérialisation du nom du tournoi."""
        name = []
        name.append(" {:<20} |".format(tournament["tournament"]["name"]))
        for count in range(len_participant - 1):
            name.append(" {:<20} |".format(''))
        return name

    @staticmethod
    def unserial_place(tournament, len_participant):
        """Désérialisation du lieu du tournoi."""
        place = []
        place.append(" {:<20} |".format(tournament["tournament"]["place"]))
        for count in range(len_participant - 1):
            place.append(" {:<20} |".format(''))
        return place

    @staticmethod
    def unserial_round(tournament, len_participants):
        """Désérialisation du nombre de rounds du tournoi."""
        round = []
        round.append(" {:<5} |".format(tournament["tournament"]["round"]))
        for count in range(len_participants - 1):
            round.append(" {:<5} |".format(''))
        return round

    @staticmethod
    def unserial_time_control(tournament, len_participants):
        """Désérialisation du time control du tournoi."""
        time_control = []
        t_c_string = ""
        if tournament["tournament"]["time_control"] == '0':
            t_c_string = "Bullet"
        elif tournament["tournament"]["time_control"] == '1':
            t_c_string = "Blitz"
        elif tournament["tournament"]["time_control"] == '2':
            t_c_string = "Quick"
        time_control.append(" {:<20} |".format(t_c_string))
        for count in range(len_participants - 1):
            time_control.append(" {:<20} |".format(''))
        return time_control

    def unserial_participants(self, tournament):
        """
        Désérialisation de l'index, nom de famille, prénom et score de chacun
        des participants.
        """
        participants = []
        for key in tournament["tournament"]["status_participants"]:
            index_participant = re.findall("[0-9]+", key)[0]
            score = \
                tournament["tournament"]["status_participants"][key]["score"]
            data_player = self.get_data_player(index_participant)[0]
            participants.append(" {:<30} |".format(str(data_player["index"]) +
                                                   ' ' +
                                                   data_player["last_name"] +
                                                   ' ' +
                                                   data_player["first_name"] +
                                                   ' ' +
                                                   str(score)
                                                   ))
        return participants

    @staticmethod
    def unserial_description(tournament, len_participant):
        """Désérialisation de la desscription du tournoi."""
        description = []
        description.append(" {:<30} |"
                           .format(tournament["tournament"]["description"]))
        for count in range(len_participant):
            description.append(" {:<30} |".format(''))
        return description

    def unserial_tournaments_finished(self, list_finished):
        """Désérialisation des tournois terminés."""
        self.list_finished_tournaments = []
        if list_finished == []:
            return "empty"
        for tournament in list_finished:
            len_participants = self.get_len_participants(tournament)

            index = self.unserial_index(tournament, len_participants)
            name = self.unserial_name(tournament, len_participants)
            place = self.unserial_place(tournament, len_participants)
            round = self.unserial_round(tournament, len_participants)
            time_control = \
                self.unserial_time_control(tournament, len_participants)
            participants = self.unserial_participants(tournament)
            description = \
                self.unserial_description(tournament, len_participants)

            self.list_finished_tournaments.append(
                TournamentFinished("finished_controller", len_participants,
                                   index, name, place, round, time_control,
                                   participants, description))
        return self.list_finished_tournaments

    @staticmethod
    def get_len_participants(tournament):
        """Demande le nombre de participants que le tournoi à eu."""
        return len(tournament["tournament"]["status_participants"])
