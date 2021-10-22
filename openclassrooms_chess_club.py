#! /usr/bin/env python3
# coding: utf-8


from controllersp04.mastercontroller import MasterController


def main():
    """Le point d'entré du script."""

    init = MasterController()
    return init.display_view_home_page()


if __name__ == '__main__':
    main()
