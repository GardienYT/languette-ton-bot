#           ______               ___        __  ________        #
#          / ____/___ __________/ (_)__  ___\ \/ /_  __/        #
#         / / __/ __ `/ ___/ __  / / _ \/ __ \  / / /           #
#        / /_/ / /_/ / /  / /_/ / /  __/ / / / / / /            #
#        \____/\__,_/_/   \__,_/_/\___/_/ /_/_/ /_/             #
#                                                               #

import json
import os

CLASSES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classes.json")


def charger_classes(path=CLASSES_PATH) -> dict:
    """Charge les informations des classes depuis le fichier JSON."""
    with open(path, encoding="utf-8") as json_data:
        return json.load(json_data)


def creer_combattant(classes: dict, classe: str) -> dict:
    """Construit un combattant (vie et pouvoirs) à partir du nom de sa classe."""
    infos = classes[classe.lower()]
    return {
        "classe": classe,
        "vie": infos["vie"],
        "pouvoirs": [infos["power1"], infos["power2"]],
    }


def attaquer(cible: dict, pouvoir: dict) -> int:
    """Applique un pouvoir à la cible (sa vie ne descend pas sous 0) et renvoie les dégâts."""
    cible["vie"] = max(0, cible["vie"] - pouvoir["value"])
    return pouvoir["value"]


def est_vaincu(combattant: dict) -> bool:
    return combattant["vie"] <= 0
