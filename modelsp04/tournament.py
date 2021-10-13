#! /usr/bin/env python3
# coding: utf-8


import re
from operator import attrgetter


class Tournament:

    tournament_in_progress = []

    def __init__(self, tournament_oontroller, index=int(), name="", place="", status_participants=list, round=4, match_in_round=int(), time_control=list, description=""):
        self.controller = tournament_oontroller

        self.index = index
        self.name = name
        self.place = place
        self.status_participants = status_participants
        self.round = round
        self.match_in_round = match_in_round
        self.time_control = time_control
        self.description = description


    def unserial_tournament_in_progress(self, in_progress):
        self.tournament_in_progress = []

        index = in_progress["index"]
        name = in_progress["name"]
        place = in_progress["place"]
        status_participants = in_progress["status_participants"]
        round = in_progress["round"]
        match_in_round = in_progress["match_in_round"]
        time_control = in_progress["time_control"]
        description = in_progress["description"]

        self.tournament_in_progress = Tournament("tournament_controller", index, name, place, status_participants, round, match_in_round, time_control, description)

        return self.tournament_in_progress
        pass




    def add_tournament(self, new_tournament):
        count_finished = self.controller.get_len_tournaments_finished()
        if count_finished == 0:
            index = 1
        else:
            index = count_finished + 1
        name = new_tournament[0]
        place = new_tournament[1]
        status_participants = new_tournament[2]
        round = new_tournament[3]
        match_in_round = new_tournament[4]
        time_control = new_tournament[5]
        description = new_tournament[6]

        self.tournament_in_progress = Tournament("tournament_controller", index,
                                                 name, place, status_participants,
                                                 round, match_in_round,
                                                 time_control, description)
        return self.tournament_in_progress


    def new_round(self, tournament_in_progress):
        pass





    def adding_score_round(self, matchs_round_to_close):
        in_progress = self.controller.get_unserial_tournament_in_progress()

        for match in matchs_round_to_close:
            try:
                idx_a = match.participant_a["index"]
                score_a = match.participant_a["score"]
                in_progress.status_participants["player_index_{}".format(idx_a)]["score"] += score_a
            except:
                continue

            try:
                idx_b = match.participant_b["index"]
                score_b = match.participant_b["score"]
                in_progress.status_participants["player_index_{}".format(idx_b)]["score"] += score_b
            except:
                continue

        return self.controller.save_tournament(in_progress)


    def designate_winner_tournament(self):
        tournament = self.controller.get_unserial_tournament_in_progress()
        # sorted_by_score = tournament.status_participants\
        #     .sort(key=attrgetter("score"), reverse=True)
        #
        # winner = sorted_by_score[0]
        pass

        pass


class TournamentFinished:

    list_finished_tournaments = []

    def __init__(self, finished_controller, len_participants=int(), index=list(), name=list(), place=list(), round=list(), time_control=list(), participants=list(), description=list()):
        self.controller = finished_controller

        self.len_participants = len_participants
        self.index = index
        self.name = name
        self.place = place
        self.round = round
        self.time_control = time_control
        self.participants = participants
        self.description = description

        pass


    def get_data_player(self, index_participant):
        return self.controller.get_data_player(index_participant)
        pass

    def unserial_index(self, tournament, len_participant):
        index = []
        index.append("| {:<5} |".format(tournament["tournament"]["index"]))
        for count in range(len_participant - 1):
            index.append("| {:<5} |".format(''))
        return index

    def unserial_name(self, tournament, len_participant):
        name = []
        name.append(" {:<20} |".format(tournament["tournament"]["name"]))
        for count in range(len_participant - 1):
            name.append(" {:<20} |".format(''))
        return name
        pass

    def unserial_place(self, tournament, len_participant):
        place = []
        place.append(" {:<20} |".format(tournament["tournament"]["place"]))
        for count in range(len_participant - 1):
            place.append(" {:<20} |".format(''))
        return place
        pass

    def unserial_round(self, tournament, len_participants):
        round = []
        round.append(" {:<5} |".format(tournament["tournament"]["round"]))
        for count in range(len_participants - 1):
            round.append(" {:<5} |".format(''))
        return round
        pass

    def unserial_time_control(self, tournament, len_participants):
        time_control = []
        t_c_string = ""
        if tournament["tournament"]["time_control"] == 0:
            t_c_string = "Bullet"
        elif tournament["tournament"]["time_control"] == 1:
            t_c_string = "Blitz"
        elif tournament["tournament"]["time_control"] == 2:
            t_c_string = "Quick"
        time_control.append(" {:<20} |".format(t_c_string))
        for count in range(len_participants - 1):
            time_control.append(" {:<20} |".format(''))
        return time_control
        pass

    def unserial_participants(self, tournament, len_participants):
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
        pass

    def unserial_description(self, tournament, len_participant):
        description = []
        description.append(" {:<30} |".format(tournament["tournament"]["description"]))
        for count in range(len_participant):
            description.append(" {:<30} |".format(''))
        return description
        pass


    def unserial_tournaments_finished(self, list_finished):
        self.list_finished_tournaments = []

        if list_finished == []:
            self.controller.display_view_no_tournament_finished()

        for tournament in list_finished:
            len_participants = self.get_len_participants(tournament)


            index = self.unserial_index(tournament, len_participants)
            name = self.unserial_name(tournament, len_participants)
            place = self.unserial_place(tournament, len_participants)
            round = self.unserial_round(tournament, len_participants)
            time_control = self.unserial_time_control(tournament, len_participants)
            participants = self.unserial_participants(tournament, len_participants)
            description = self.unserial_description(tournament, len_participants)

            # data = [index, name, place, round, time_control, participants, description]

            self.list_finished_tournaments.append(
                TournamentFinished("finished_controller", len_participants, index, name, place, round, time_control, participants, description))

        return self.list_finished_tournaments
        # for i in range(3):
        #     for element in range(len(data)):
        #         print(data[element][i], end='')
        #     print("")
        # print(("{0}"*152).format('-'))
        # pass

    def get_len_participants(self, tournament):
        return len(tournament["tournament"]["status_participants"])
        pass
