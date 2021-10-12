#! /usr/bin/env python3
# coding: utf-8


from modelsp04.database import DataBase


class DataBaseController:
    """Le contrôlleur de la base de données."""

    def __init__(self, master_controller):
        """
        Initialise le contrôlleur de la base de données.
        """
        self.model = DataBase(self)
        self.controller = master_controller

    def get_list_players(self):
        """
        Demande la liste de tous les joueurs enregistrés dans la base de données.
        """
        return self.model.get_list_players()

    def get_len_players_in_db(self):
        """Demande le nombre de joueurs enregistrées dans la base de données."""
        return self.model.get_len_players_in_db()

    def get_tournament_in_progress_or_not(self):
        """Demande si un tournoi est en cours ou non."""
        return self.model.get_tournament_in_progress_or_not()

    def get_round_to_do_or_not(self):
        return self.model.get_round_to_do_or_not()
        pass

    def get_tournament_in_progress(self):
        """Demande les données du tournoi en cours."""
        return self.model.get_tournament_in_progress()

    def get_list_rounds(self):
        return self.model.get_list_rounds()

    def get_round_to_do(self):
        return self.model.get_round_to_do()

    def get_round_in_progress(self):
        return self.model.get_round_in_progress()
        pass

    def get_matchs_current_round(self):
        return self.model.get_matchs_current_round()
        pass

    def get_status_participants(self):
        return self.model.get_status_participants()
        pass

    def get_players_participants(self):
        return self.model.get_players_participants()
        pass

    def get_index_participants(self):
        return self.model.get_index_participants()
        pass

    def get_elo_participants(self):
        return self.model.get_elo_participants()
        pass

    def get_player_exists(self, index_to_check):
        return self.model.get_player_exists(index_to_check)
        pass

    def get_numbers_matchs_current_round(self):
        return self.model.get_numbers_matchs_current_round()
        pass


    def add_player(self, new_player):
        """
        Envoi le nouveau joueur dans le model de la base de données, pour
        l'ajouter à la base de données.
        """
        return self.model.add_player(new_player)

    def add_tournament_in_progress(self, tournament_in_progress):
        """Envoi les données du tournoi en cours vers la base de données."""
        return self.model.add_tournament_in_progress(tournament_in_progress)

    def add_round(self, round_in_progress):
        return self.model.add_round(round_in_progress)

    def add_matchs(self, list_matchs_in_round):
        return self.model.add_matchs(list_matchs_in_round)
        pass



    def save_match(self, match_to_update):
        return self.model.save_match(match_to_update)
        pass

    def save_round(self, round_to_update):
        return self.model.save_round(round_to_update)

    def save_tournament(self, tournament_to_update):
        return self.model.save_tournament(tournament_to_update)
        pass

    def transfer_tournament_to_finished(self):
        """Demande de transférer le tournoi clôturé vers les tournois finis."""
        return self.model.transfer_tournament_to_finished()

    def purge_tournament_in_progress(self):
        return self.model.purge_tournament_in_progress()
        pass



    def reinitialize_for_test(self):
        return self.model.reinitialize_for_test()
        pass