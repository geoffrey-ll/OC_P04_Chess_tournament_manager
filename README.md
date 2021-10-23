![open_class_rooms](https://img.shields.io/badge/OpenClassRooms-Project04-limegreen?labelColor=blueviolet&style=plastic)
![built_by](https://img.shields.io/badge/Built%20by-Developers%20%3Cgeoffrey_ll%3E-black?labelColor=orange&style=plastic)


![made_with_python](https://img.shields.io/badge/Made%20With-Python_3.6.5-darkgreen?logo=python&labelColor=red&style=plastic)
![ide_use_pycharm](https://img.shields.io/badge/IDE%20use-PyCharm-darkgreen?logo=pycharm&labelColor=red&style=plastic)
![os_use_windowns](https://img.shields.io/badge/OS%20use-Windows-blue?labelColor=red&style=plastic&logo=windows)


![open_source](https://img.shields.io/badge/licence-libre-darkkhaki?labelColor=red&style=plastic)



# openclassrooms_chess_club.py #

1.  [Description](#description)
2.  [Utilisation](#utilisation)
    1.  [Page d'accueil](#PAGE-D-ACCUEIL)
    2.  [Start a tournament](#START-A-TOURNAMENT)
    3.  [Finished tournaments](#FINISHED-TOURNAMENTS)
    4.  [Players list](#PLAYERS-LIST)
    5.  [Tournament in progress](#TOURNAMENT-IN-PROGRESS)
    6.  [Rapport flake8](#FLAKE-8)
3.  [Installation](#installation)
    1.  [Environnement virtuel](#environnement-virtuel)
    2.  [Requierements](#requierements)
4.  [À propos](#a-propos)
    1.  [Packages](#packages)
    2.  [Bugs connus](#bugs-connus)
    3.  [Améliorations futures](#améliorations-futures)

 
## 1. Description <a name="description"></a> ##

    Ce script à été réalisé dans le cadre d'un projet du parcours
    'Développeur d'application - Python' d'OpenClassROoms.

\
\
OpenClassrooms_chess_club.py est un gestionnaire (simplifié) de tournoi d'échec, qui permet :
- La création d'une base de données joueurs.
- La création et la gestion de tournoi avec enregistrement en base de données.
- L'appariements pour les matchs est basé sur le système Suisse, sous une forme simplifié de l'appariement officiel de la Fédération Française d'Échecs (FFE) (ex : il n'y a pas d'équilibrage des couleurs).
- La visualisation de la liste des joueurs et des tournois terminés.

Le script s'utilise via une interface terminal.\
La base de données est en format .json.

 
## 2. Utilisation <a name="utilisation"></a> ##

**Attention :**
- L'affichage à été pensé pour du 16/9. Pour un affichage correct, il est nécessaire que la fenêtre du terminal soit large.

\
Pour lancer le script, la ligne de commande est :

![command_line_start_script](readme_png/command_line_start_script.png)

 
###### PAGE D'ACCUEIL : <a name="PAGE-D-ACCUEIL"></a> ######

![view_home_page](readme_png/view_home_page.png)

0. Création d'un nouveau tournoi (ou gestion du tournoi si un en cours ![view_home_page_only_option_tournament_in_progress](readme_png/view_home_page_only_option_tournament_in_progress.png))
1. Affichage des données des tournois terminés.
2. Affichage et enregistrement des joueurs en base de données.
3. Quitter le script.

 
###### START A TOURNAMENT : <a name="START-A-TOURNAMENT"></a> ######

**Attention :**
- Afin de pouvoir débuter un tournoi, il est nécessaire d'avoir des joueurs enregistrés dans la base de données.

![view_all_input_new_tournament](readme_png/view_all_input_new_tournament.png)

\
Succession d'inputs pour renseigner les paramètres du tournoi.\
Les paramètres avec une valeur, sont ceux qui ont une valeur par défaut.\
Utiliser la touche entrée pour conserver la valeur par défaut.

 
###### FINISHED TOURNAMENTS : <a name="FINISHED-TOURNAMENTS"></a> ######

Voici un affichage avec tournois terminés dans la base de données :

![view_finished_tournaments_(x2)](readme_png/view_finished_tournaments_(x2).png)

 
###### PLAYERS LIST : <a name="PLAYERS-LIST"></a> ######

Voici un affichage avec quelques joueurs dans la base de données :

![view_list_players_(x10)](readme_png/view_list_players_(x10).png)
- N : Ajout d'un joueur dans la base de données.
- A : Tri des joueurs par ordre alphabetique (nom de famille)
- I  : Tri des joueurs par défaut. L'index joueur en base de données.
- E : Tri des joueurs par classement Elo décroissant. 

L'option [N] initie une succesion d'inputs pour renseigner les informations du joueur :

![view_all_input_new_player](readme_png/view_all_input_new_player.png)

 
###### TOURNAMENT IN PROGRESS : <a name="TOURNAMENT-IN-PROGRESS"></a> ######

![view_tournament_manager_option_selection_match_(x2matchs)](readme_png/view_tournament_manager_option_selection_match_(x2matchs).png)

\
Durant un tournoi, la seule chose à faire est de désigner les vainqueurs des matchs.\
Pour cela, il suffit d'entrer le numéro d'un match (les numéros de match sont indiqués en première ligne).\
Puis de désigner le vainqueur.

\
![view_tournament_manager_option_selection_winner](readme_png/view_tournament_manager_option_selection_winner.png)

L'option pour clôturer le round sera disponible lorsque tous les matchs du round seront finis.

![view_tournament_manager_option_close_a_round](readme_png/view_tournament_manager_option_close_a_round.png)

Laissant place au round suivant.

 
###### RAPPORT FLAKE-8 : <a name="FLAKE-8"></a> ######

Pour générer les rapports flake-8, la commande est :

![command_line_flake-8](readme_png/command_line_flake-8.png)

Les rapports seront générés dans le dossier ![folder_flake-8](readme_png/folder_flake-8.png) du réportoire de travail.\
Dans lequel on trouve le fichier ![file_overview_flake-8](readme_png/file_overview_flake-8.png), qui est la table des rapports.

 
## 3. Installation <a name="installation"></a> ##

**Remarque**

Dans les sous-sections suivantes, les lignes de commande sont exécutée depuis le répertoire de travail :\
![working_directory](readme_png/working_directory.png)\
Les différents fichiers du script s'y trouvent.\
Pour utiliser les lignes de commandes, il faut que votre répertoire de travail, soit, celui où se trouvent les différents fichiers du script.

 
### i. Environnement virtuel <a name="environnement-virtuel"></a> ###

Sous Linux, avec l'IDE PyCharm.

- Pour créer l'environnement virtuel lancer la commande suivante :\
![command_line_create_env_linux](readme_png/command_line_create_env_linux.png)\
Cela créra un environnement virtuel nommé 'env'.

- Si l'environnement virtuel est actif, son nom apparaîtra au début de la ligne de commande, comme suit :\
![env_activate](readme_png/env_activate.png)

- Sinon, pour activer l'env, il faut lancer la commande :\
![command_line_activate_env_linux](readme_png/command_line_activate_env_linux.png)


\
Sous Windows, avec l'IDE PyCharm.

- Pour créer l'environnement virtuel lancer la commande suivante :\
![command_line_create_env_win](readme_png/command_line_create_env_win.png)\
Cela créra un environement virtuel nommé 'env'
- Si l'environnement virtuel est actif, son nom apparaîtra au début de la ligne de commande, comme suit :\
![env_activate](readme_png/env_activate.png)

- Sinon, pour activer l'env, il faut lancer la commande :\
![command_line_activate_env_win](readme_png/command_line_activate_env_win.png)


 
### ii. Requierements <a name="requierements"></a> ###

Une fois l'environnement virtuel activé, lancer la commande suivante :

![command_line_install_requierements](readme_png/command_line_install_requierements.png)

Cela installera tous les modules renseignés dans le fichier requierements.txt.


 
## 4. À propos <a name="a-propos"></a> ###
 
### i. Packages <a name="packages"></a> ###

La structure de openclassrooms_chess_club.py est basé sur le modèle MVC (Model View Controller).\

![structure_project_MVC_only](readme_png/structure_project_MVC_only.png)


- Les models, gèrent les transformations.
- Les views, gèrent les affichages et les inputs utilisateurs.
- Les controllers, coordonnent les différentes méthodes et fichiers. Permettent la liason entre les views et les models.

 
### ii. Bugs connus <a name="bugs-connus"></a> ###

- Le script se termine si l'on essai de désigner un vainqueur à un match exempté (match avec un joueur sans adversaire).
N'entraine pas d'erreur sur le tournoi en question. Relancer le script est suffissant pour revenir à la gestion du tournoi.
      
Si vous trouvez un bug, merci de me le signaler sur l'adresse\
gl_openclassrooms@laposte.net

 
### iii. Amélioration futures <a name="améliorations-futures"></a> ###

- Mise en évidence des vainqueurs de toursnois.
- Horodage des tournois/rounds/matchs.
- Mise à jour (simplifié) du score Elo des joueurs après victoire/nul/défaite d'un match. Respectivement +7/+0/-7.
- Afficher les détails d'un tournoi terminés (détails des matchs etc.).
