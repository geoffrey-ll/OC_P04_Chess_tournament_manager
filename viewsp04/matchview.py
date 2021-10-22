#! /usr/bin/env python3
# coding: utf-8


import re


class MatchView:
    """La vue des matchs."""

    def __init__(self, match_controller):
        """Initialisation de la classe MatchView."""
        self.controller = match_controller

    def get_unserial_matchs_current_round(self):
        """Demande la désérialisation des matchs du round en cours."""
        return self.controller.get_unserial_matchs_current_round()

    def display_view_matchs_in_progress_round(self, invalide=False):
        """Affichage des matchs du round en cours."""
        list_matchs = self.get_unserial_matchs_current_round()
        number_match = len(list_matchs)
        count = 0

        print("Round n°{}"
              .format(re.findall("[0-9]+", list_matchs[0].name)[0][0]))
        while count <= number_match - 2:
            print("{0}{1}{2}{1}".format(' '*5, '_'*70, ' '*20))
            print("{0}|{1:^68}|{2}|{3:^68}|"
                  .format(' '*5,
                          "[{}] "
                          .format(
                              re.findall("[0-9]+",
                                         list_matchs[count].name)[-1])
                          + list_matchs[count].name[:5].capitalize()
                          + ' '
                          + list_matchs[count].name[6:],
                          ' '*20,
                          "[{}] "
                          .format(
                              re.findall("[0-9]+",
                                         list_matchs[count+1].name)[-1])
                          + list_matchs[count+1].name[:5].capitalize()
                          + ' '
                          + list_matchs[count+1].name[6:]))

            try:
                print("{0}| {1:<31}[N]{2:>32} |{3}| {4:<32}[N]{5:>31} |"
                      .format(' '*5,
                              list_matchs[count].participant_a["last_name"]
                              + ' '
                              + list_matchs[count].participant_a["first_name"]
                              + "  [G]",
                              "[D]  "
                              + list_matchs[count].participant_b["last_name"]
                              + ' '
                              + list_matchs[count].participant_b["first_name"],
                              ' '*20,
                              list_matchs[count+1].participant_a["last_name"]
                              + ' '
                              + list_matchs[count+1].participant_a["first_name"
                                                                   ]
                              + "  [G]",
                              "[D]  "
                              + list_matchs[count+1].participant_b["last_name"]
                              + ' '
                              + list_matchs[count+1].participant_b["first_name"
                                                                   ]
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<31}[N]{2:>32} |{3}| {4:<33}{5:>33} |"
                      .format(' '*5,
                              list_matchs[count].participant_a["last_name"]
                              + ' '
                              + list_matchs[count].participant_a["first_name"]
                              + "  [G]",
                              "[D]  "
                              + list_matchs[count].participant_b["last_name"]
                              + ' '
                              + list_matchs[count].participant_b["first_name"],
                              ' '*20,
                              list_matchs[count+1].participant_a["last_name"]
                              + ' '
                              + list_matchs[count+1].participant_a["first_name"
                                                                   ],
                              list_matchs[count+1].participant_b["exempt"]
                              ))

            try:
                print("{0}| {1:<33}{2:>33} |{3}| {4:<33}{5:>33} |"
                      .format(' '*5,
                              str(- list_matchs[count]
                                  .participant_a["current_elo"])
                              + "  (Elo)",
                              "(Elo)  "
                              + str(- list_matchs[count]
                                    .participant_b["current_elo"]),
                              ' '*20,
                              str(- list_matchs[count+1]
                                  .participant_a["current_elo"])
                              + "  (Elo)",
                              "(Elo)  "
                              + str(- list_matchs[count+1]
                                    .participant_b["current_elo"])
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<33}{2:>33} |{3}| {4:<66} |"
                      .format(' ' * 5,
                              str(- list_matchs[count]
                                  .participant_a["current_elo"])
                              + "  (Elo)",
                              "(Elo)  "
                              + str(- list_matchs[count]
                                    .participant_b["current_elo"]),
                              ' ' * 20,
                              str(- list_matchs[count+1]
                                  .participant_a["current_elo"])
                              + "  (Elo)",
                              ))

            try:
                print("{0}| {1:<33}{2:>33} |{3}| {4:<33}{5:>33} |"
                      .format(' '*5,
                              str(list_matchs[count].participant_a["score"])
                              + "  (Score)",
                              "(Score)  "
                              + str(list_matchs[count].participant_b["score"]),
                              ' '*20,
                              str(list_matchs[count+1].participant_a["score"])
                              + "  (Score)",
                              "(Score)  "
                              + str(list_matchs[count+1].participant_b["score"]
                                    )
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<33}{2:>33} |{3}| {4:<66} |"
                      .format(' ' * 5,
                              str(list_matchs[count].participant_a["score"])
                              + "  (Score)",
                              "(Score)  "
                              + str(list_matchs[count].participant_b["score"]),
                              ' ' * 20,
                              str(list_matchs[count+1].participant_a["score"])
                              + "  (Score)",
                              ))

            try:
                print("{0}| {1:<33}{2:>33} |{3}| {4:<33}{5:>33} |"
                      .format(' '*5,
                              str(list_matchs[count].participant_a["colors"])
                              + "  (Color)",
                              "(Color)  "
                              + str(
                                  list_matchs[count].participant_b["colors"]),
                              ' '*20,
                              str(list_matchs[count+1].participant_a["colors"])
                              + "  (Color)",
                              "(Color)  "
                              + str(
                                  list_matchs[count+1].participant_b["colors"]
                                    )
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<33}{2:>33} |{3}| {4:<66} |"
                      .format(' ' * 5,
                              str(list_matchs[count].participant_a["colors"])
                              + "  (Color)",
                              "(Color)  "
                              + str(
                                  list_matchs[count].participant_b["colors"]),
                              ' ' * 20,
                              str(list_matchs[count+1].participant_a["colors"])
                              + "  (Color)",
                              ))

            print("{0}|{1:^68}|{2}|{3:^68}|"
                  .format(' '*5,
                          list_matchs[count].status_match,
                          ' '*20,
                          list_matchs[count+1].status_match
                          ))
            print("{0}{1}{2}{1}".format(' '*5, '_'*70, ' '*20))
            print("\n")
            count += 2

        while count == number_match - 1:
            print("{0}{1}".format(' '*5, '_'*70))
            print("{0}|{1:^68}|"
                  .format(' '*5,
                          "[{}] ".format(
                              re.findall("[0-9]+",
                                         list_matchs[count].name)[-1])
                          + list_matchs[count].name[:5].capitalize()
                          + ' '
                          + list_matchs[count].name[6:]
                          ))

            try:
                print("{0}| {1:<31}[N]{2:>32} |"
                      .format(' ' * 5,
                              list_matchs[count].participant_a["last_name"]
                              + ' '
                              + list_matchs[count].participant_a["first_name"]
                              + "  [G]",
                              "[D]  "
                              + list_matchs[count].participant_b["last_name"]
                              + ' '
                              + list_matchs[count].participant_b["first_name"]
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<33}{2:>33} |"
                      .format(' '*5,
                              list_matchs[count].participant_a["last_name"]
                              + ' '
                              + list_matchs[count].participant_a["first_name"],
                              list_matchs[count].participant_b["exempt"]
                              ))

            try:
                print("{0}| {1:<33}{2:>33} |"
                      .format(' '*5,
                              str(- list_matchs[count]
                                  .participant_a["current_elo"])
                              + "  (Elo)",
                              "(Elo)  "
                              + str(- list_matchs[count]
                                    .participant_b["current_elo"])
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<66} |"
                      .format(' '*5,
                              str(- list_matchs[count]
                                  .participant_a["current_elo"])
                              + "  (Elo)"
                              ))

            try:
                print("{0}| {1:<33}{2:>33} |"
                      .format(' ' * 5,
                              str(list_matchs[count].participant_a["score"])
                              + "  (Score)",
                              "(Score)  "
                              + str(list_matchs[count].participant_b["score"])
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<66} |"
                      .format(' '*5,
                              str(list_matchs[count].participant_a["score"])
                              + "  (Score)"
                              ))

            try:
                print("{0}| {1:<33}{2:>33} |"
                      .format(' ' * 5,
                              str(list_matchs[count].participant_a["colors"])
                              + " (Color)  ",
                              "(Color)  "
                              + str(list_matchs[count].participant_b["colors"])
                              ))
            except Exception as e:
                osef = []
                osef.append(e)
                print("{0}| {1:<66} |"
                      .format(' '*5,
                              str(list_matchs[count].participant_a["colors"])
                              + "  (Color)"
                              ))

            print("{0}|{1:^68}|".format(' '*5,
                                        list_matchs[count].status_match))
            print("{0}{1}".format(' '*5, '_'*70))
            count += 1

        if invalide is True:
            print("\nInvalide option")
        self.display_options()
        return self.option_choice()

    def display_options(self):
        """Affichage des options (option selection match)."""
        print("\n")
        round_finish_or_not = self.controller.check_status_round()
        if round_finish_or_not == "Finished":
            print("\n[C] : {}".format("Close the round"))
        print("\n[#] : {}".format("Choose a match"))
        return print("\n[R] : {}".format("Return to home page"))

    def option_choice(self):
        """Option choisit par l'utilisateur (option sélection match)."""
        user_input = input().capitalize()
        if re.findall("[0-9]+", user_input) != []:
            selected_match = \
                self.controller.check_input_number_match(user_input)
            if selected_match == "match_no_exist":
                return \
                    self.display_view_matchs_in_progress_round(invalide=True)
            if selected_match != []:
                return self.display_designate_winner(selected_match)
            else:
                return \
                    self.display_view_matchs_in_progress_round(invalide=True)
        elif user_input == "R":
            return self.controller.display_view_home_page()
        elif user_input == "C":
            return self.controller.round_to_close()
        else:
            return self.display_view_matchs_in_progress_round(invalide=True)

    def display_designate_winner(self, selected_match):
        """
        Affichage des options (option délection vainqueur).
        &
        Option choisit par l'utilisateur (option sélection vainqueur).
        """
        winner = input("\n[G] : Winner is player left\n"
                       "[N] : Match is nul\n"
                       "[D] : Winer is player right\n"
                       "\n"
                       "[R] : Return to matchs view\n").capitalize()
        if winner == "G" or winner == "N" or winner == "D":
            self.controller.designate_winner(selected_match, winner)
            return self.display_view_matchs_in_progress_round()
        elif winner == "R":
            return self.display_view_matchs_in_progress_round()
        else:
            return self.display_view_matchs_in_progress_round(invalide=True)

    def save_match(self, match):
        """Sauvegarde d'un match dans la base de données (mise à jour)."""
        return self.controller.save_match(match)
