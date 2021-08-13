#! /usr/bin/env python3
# coding: utf-8


from controllersp04.mastercontroller import MasterController


def main():
    """Le point d'entré du script."""

    init = MasterController()
    init.import_data_base()
    # init.closing_tournament()

    pass


if __name__ == '__main__':
    main()

# TODO
# transformer les add_player du data_base en export_db_players. À faire à
# chaque nouvel ajout de joueur comme maintenant ? Ou à la fin du script en
# export toutes la liste d'un coup (réalisable si script interrompu brutalement
# ?) ?
#
#
# Réfléchir à une MasterView, pour les élèments communs à chaque vues, tel le
# titre de niveau etc.
# TODO
