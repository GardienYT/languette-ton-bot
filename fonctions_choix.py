from enum import Enum
from pick import pick
import time
from rich.console import Console

def pretty_print(message, color):
    """
    Print message to console using Console
    Possible colors are: green, yellow, red or hexadecimal code
    :param message:
    :param color:
    :return:
    """
    console = Console()
    console.print(message, style=color)

class LancementApplicationChoix(Enum):
    Lancer = 1
    Quitter = 2

def lancement_application() -> LancementApplicationChoix:
    title = "Languette ton Bot 💩"
    options = [LancementApplicationChoix.Lancer.name, LancementApplicationChoix.Quitter.name]
    option, index = pick(options, title)

    return option


def lancer_game():
    pretty_print("Lancement de la game..", "green")


def quitter_game():
    pretty_print("Deconnexion..", "red")
    time.sleep(1.5)
    quit()

# Choix de la classe du Joueur
class ChoixClassePlayer(Enum):
    Guerrier = 1
    Mage = 2
    Voleur = 3
    Pretre = 4

def choix_classe_player() -> ChoixClassePlayer:
    title = "Quelle classe voulez vous choisir ?"
    options = [ChoixClassePlayer.Guerrier.name, ChoixClassePlayer.Mage.name, ChoixClassePlayer.Voleur.name, ChoixClassePlayer.Pretre.name]
    option, index = pick(options, title)

    return option

# Choix de la classe du Bot
class ChoixClasseBot(Enum):
    Guerrier = 1
    Mage = 2
    Voleur = 3
    Pretre = 4

def choix_classe_bot() -> ChoixClasseBot:
    title = "Choisir une classe pour l'adversaire"
    options = [ChoixClasseBot.Guerrier.name, ChoixClasseBot.Mage.name, ChoixClasseBot.Voleur.name, ChoixClasseBot.Pretre.name]
    option, index = pick(options, title)

    return option
    
