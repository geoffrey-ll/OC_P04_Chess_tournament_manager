![open_class_rooms](https://img.shields.io/badge/OpenClassRooms-Project04-limegreen?labelColor=blueviolet&style=plastic)
![built_by](https://img.shields.io/badge/Built%20by-Developers%20%3Cgeoffrey_ll%3E-black?labelColor=orange&style=plastic)



![made_with_python](https://img.shields.io/badge/Made%20With-Python_3.6.5-darkgreen?logo=python&labelColor=red&style=plastic)
![ide_use_pycharm](https://img.shields.io/badge/IDE%20use-PyCharm-darkgreen?logo=pycharm&labelColor=red&style=plastic)
![os_use_windowns](https://img.shields.io/badge/OS%20use-Windows-blue?labelColor=red&style=plastic&logo=windows)



![open_source](https://img.shields.io/badge/licence-libre-darkkhaki?labelColor=red&style=plastic)





# openclassrooms_chess_club.py #

AJOUTER SECTION RAPPORT FLAKE8

1.  [Description](#description)
2.  [Utilisation](#utilisation)
    1.  [Page d'accueil](#PAGE-D-ACCUEIL)
    2.  [Start a tournament](#START-A-TOURNAMENT)
    3.  [Finished tournaments](#FINISHED-TOURNAMENTS)
    4.  [Players list](#PLAYERS-LIST)
    5.  [Rapport flake8](#FLAKE-8)
3.  [Installation](#installation)
    1.  [Environnement virtuel](#environnement-virtuel)
    2.  [Requierements](#requierements)
4.  [À propos](#a-propos)
    1.  [Packages](#packages)
    2.  [Bugs connus](#bugs-connus)
    3.  [Idées d'améliorations](#idees-d-ameliorations)

AJOUTER SECTION RAPPORT FLAKE8


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

\
La base de données est en format .json.

\
Le script s'utilise via une interface terminal. 

\
\
**Attention :**
- L'affichage à été pensé pour du 16/9. Pour un affichage correct, il est nécessaire que la fenêtre du terminal soit large.




## 2. Utilisation <a name="utilisation"></a> ##


Pour lancer le script, la ligne de commande est :

![command_line_start_script](readme_png/command_line_start_script.png)



###### PAGE D'ACCUEIL : <a name="PAGE-D-ACCUEIL"></a> ######

![view_home_page](readme_png/view_home_page_L900.png)

0. Création d'un nouveau tournoi.
1. Affichage des données des tournois terminés.
2. Affichage et enregistrement des joueurs en base de données.
3. Quitter le script.



###### START A TOURNAMENT : <a name="START-A-TOURNAMENT"></a> ######

**Attention :**\
Afin de pouvoir débuter un tournoi, il est nécessaire d'avoir des joueurs enregistrés dans la base de données.

Initie une succession d'input pour renseigner les paramètres du tournoi.\
Les paramètres avec une valeur, sont ceux qui ont une valeur par défaut.\
Utiliser la touche entrée pour conserver la valeur par défaut.

![view_all_input_new_tournament_L900](readme_png/view_all_input_new_tournament_L900.png)



###### FINISHED TOURNAMENTS : <a name="FINISHED-TOURNAMENTS"></a> ######

Voici l'affichage lorsque la base de données est vide :

![view_finished_tournaments_L900](readme_png/view_finished_tournaments_L900.png)



###### PLAYERS LIST : <a name="PLAYERS-LIST"></a> ######

Voici l'affichage lorsque la base de données est vide :

![view_list_players](readme_png/view_list_players_L900.png)
- n : Ajout d'un joueur dans la base de données.
- \# : Pour une amélioration future.
- A : Tri des joueurs par ordre alphabetic (nom de famille)
- I : Tri des joueurs par défaut. L'index joueur en base de données.
- E : Tri des joueurs par classement Elo décroissant. 

L'option [N] initie une succesion d'input pour renseigner les informations du joueur :

![view_all_input_new_player](readme_png/view_all_input_new_player.png)



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


- Les models, gèrent 
- Les views, gèrent l'affichage et les inputs utilisateurs.
- Les controllers, coordonnent les différentes méthodes et fichiers.





### ii. Bugs connus <a name="bugs-connus"></a> ###


-   AJOUTER SECTION RAPPORT FLAKE8

    -   
    
        ![bug_option_input_espace_before_next_category](readme_jpg/bug_option_input_espace_before_next_category.jpg)
    
    -   
    
        ![bug_option_input_no_dash_before_firt_category](readme_jpg/bug_option_input_no_dash_before_first_category.jpg)

-   

Si vous trouvez un bug, merci de (ne pas) me le signaler sur l'adresse\
openclassrooms_chess_club@support.com




### iii. Idées d'amélioration <a name="idees-d-ameliorations"></a> ###



- 


- 


- 


- 

