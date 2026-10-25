#           ______               ___        __  ________        #
#          / ____/___ __________/ (_)__  ___\ \/ /_  __/        #
#         / / __/ __ `/ ___/ __  / / _ \/ __ \  / / /           #
#        / /_/ / /_/ / /  / /_/ / /  __/ / / / / / /            #
#        \____/\__,_/_/   \__,_/_/\___/_/ /_/_/ /_/             #
#                                                               #

import random
import time

from fonctions import attaquer, charger_classes, creer_combattant, est_vaincu
from fonctions_choix import (
    LancementApplicationChoix,
    choix_classe_bot,
    choix_classe_player,
    choix_pouvoir,
    lancement_application,
    lancer_game,
    pretty_print,
    quitter_game,
)

PAUSE_ENTRE_TOURS = 1.5


def afficher_vies(joueur, bot):
    pretty_print("-------- Vies --------", "green")
    pretty_print(f"Vie du joueur ({joueur['classe']}): {joueur['vie']}", "green")
    pretty_print(f"Vie du bot ({bot['classe']}): {bot['vie']}", "green")
    time.sleep(PAUSE_ENTRE_TOURS)


def jouer_tour(titre, couleur, pouvoir, cible):
    pretty_print(f"-------- {titre} --------", couleur)
    degats = attaquer(cible, pouvoir)
    pretty_print(f"Pouvoir: {pouvoir['name']}", couleur)
    pretty_print(f"Dégat: {degats}", couleur)


def combat(joueur, bot):
    # Le tour est suivi par un indicateur, pas par la classe (même classe des deux côtés possible)
    tour_du_joueur = random.choice([True, False])

    while True:
        afficher_vies(joueur, bot)

        if tour_du_joueur:
            noms = {p["name"]: p for p in joueur["pouvoirs"]}
            pouvoir = noms[choix_pouvoir(noms)]
            jouer_tour("PLAYER", "blue", pouvoir, bot)
            if est_vaincu(bot):
                return "joueur"
        else:
            jouer_tour("BOT", "red", random.choice(bot["pouvoirs"]), joueur)
            if est_vaincu(joueur):
                return "bot"

        tour_du_joueur = not tour_du_joueur


def main():
    if lancement_application() == LancementApplicationChoix.Quitter.name:
        quitter_game()
        return

    lancer_game()
    classes = charger_classes()
    joueur = creer_combattant(classes, choix_classe_player())
    bot = creer_combattant(classes, choix_classe_bot())

    gagnant = combat(joueur, bot)
    afficher_vies(joueur, bot)
    pretty_print("FINISH", "red")
    print("Le joueur a gagné !" if gagnant == "joueur" else "Le bot a gagné !")


if __name__ == "__main__":
    main()
