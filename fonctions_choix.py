#           ______               ___        __  ________        #
#          / ____/___ __________/ (_)__  ___\ \/ /_  __/        #
#         / / __/ __ `/ ___/ __  / / _ \/ __ \  / / /           #
#        / /_/ / /_/ / /  / /_/ / /  __/ / / / / / /            #
#        \____/\__,_/_/   \__,_/_/\___/_/ /_/_/ /_/             #
#                                                               #

from enum import Enum
import sys
import time

from pick import pick
from rich.console import Console


def pretty_print(message, color):
    """
    Affiche un message dans la console.
    Couleurs possibles : green, yellow, red, blue ou un code hexadécimal.
    """
    Console().print(message, style=color)


class LancementApplicationChoix(Enum):
    Lancer = 1
    Quitter = 2


def lancement_application() -> str:
    title = "Languette ton Bot 💩"
    options = [choix.name for choix in LancementApplicationChoix]
    option, _ = pick(options, title)
    return option


def lancer_game():
    pretty_print("Lancement de la game..", "green")


def quitter_game():
    pretty_print("Deconnexion..", "red")
    time.sleep(1.5)
    sys.exit()


class Classe(Enum):
    Guerrier = 1
    Mage = 2
    Voleur = 3
    Pretre = 4


def choix_classe(title: str) -> str:
    options = [classe.name for classe in Classe]
    option, _ = pick(options, title)
    return option


def choix_classe_player() -> str:
    return choix_classe("Quelle classe voulez vous choisir ?")


def choix_classe_bot() -> str:
    return choix_classe("Choisir une classe pour l'adversaire")


def choix_pouvoir(noms_pouvoirs) -> str:
    option, _ = pick(list(noms_pouvoirs), "Choisir une attaque")
    return option
