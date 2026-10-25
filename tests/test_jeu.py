import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fonctions import attaquer, charger_classes, creer_combattant, est_vaincu


def test_toutes_les_classes_ont_vie_et_deux_pouvoirs():
    classes = charger_classes()
    assert set(classes) == {"guerrier", "mage", "voleur", "pretre"}
    for infos in classes.values():
        assert infos["vie"] > 0
        assert infos["power1"]["value"] > 0 and infos["power2"]["value"] > 0


def test_meme_classe_des_deux_cotes_donne_deux_combattants_distincts():
    classes = charger_classes()
    a, b = creer_combattant(classes, "Mage"), creer_combattant(classes, "Mage")
    attaquer(b, b["pouvoirs"][0])
    assert a["vie"] > b["vie"]


def test_la_vie_ne_descend_pas_sous_zero():
    cible = {"vie": 5}
    attaquer(cible, {"name": "x", "value": 50})
    assert cible["vie"] == 0 and est_vaincu(cible)
