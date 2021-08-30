#! /usr/bin/env python3
# coding: utf-8


from operator import attrgetter


class Round:
    round_in_progress = []


    def __init__(self, round_controller, name="",  match_in_round=int(), participants_status=dict, round_status="TO_DO", participants_idx=list(), participant_score=0):
        self.controller = round_controller

        self.name = name
        self.match_in_round = match_in_round
        self.participants_status = participants_status
        self.round_status = round_status
        # self.participants_idx = participants_idx
        # self.participant_score = participant_score
        pass

    def get_list_round(self):
        return self.controller.get_list_round()



    def initialize_round(self, in_progress):
        for count_round in range(in_progress.round):
            name = "round_" + str(count_round + 1)
            match_in_round = in_progress.match_in_round
            participants_status = {}
            for participant in in_progress.participants.keys():
                participants_status["idx_" + str(participant)] = "score_0"
            round = Round("round_controller", name, match_in_round, participants_status)
            self.round_in_progress.append(round)


        self.add_round()


    def add_round(self):
        return self.controller.add_round(self.round_in_progress)
        pass

    def save_round(self, round_update):
        return self.controller.save_round(round_update)
        pass

    def get_round(self):
        return self.round_in_progress

    def in_progress(self):
        pass

    def new_round(self):
        for round in self.round_in_progress:
            if round.round_status == "TO_DO":
                round.round_status = "IN_PROGRESS"
                self.save_round(round)
                return self.matching()#round)
            else:
                pass
        pass

    def matching(self):
        round_in_progress = ''
        for round in self.round_in_progress:
            if round.round_status == "IN_PROGRESS":
                round_in_progress = round
                print(round_in_progress)
            else:
                pass
        if round_in_progress.name == "round_1":
            participants = self.controller.get_participants()
            participants.sort(key=attrgetter("current_elo"), reverse=True)

            for participant in participants:
                print("elo", participant.current_elo)

            count = len(participants) // 2

            top_elo = participants[:count]
            lower_elo = participants[count:]
            exempt_elo = []
            if len(participants) % 2 != 0:
                lower_elo = participants[count:-1]
                exempt_elo = participants[-1]

            # matchs = []
            for number in range(round_in_progress.match_in_round):
                # initialise match ???
                # Match(top_elo[number], lower_elo[number])
                # matchs.append([top_elo[number], lower_elo[number]])
                # for elmt in matchs:
                #     print("matchs", elmt.current_elo)
                self.controller.new_match(top_elo[number], lower_elo[number])


            pass
        for round in self.round_in_progress:
            print("\nlist round\n", round.round_status)
        pass