# Languette ton Bot 💩

Petit jeu de combat au tour par tour dans le terminal : tu choisis ta classe, puis celle de ton adversaire (le bot), et vous vous attaquez jusqu'à ce que l'un des deux tombe à 0 PV.

## Lancer le jeu
```
python -m venv env
source env/bin/activate      # Windows : .\env\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Règles
- Le premier joueur est tiré au sort.
- À ton tour, tu choisis l'un des deux pouvoirs de ta classe ; le bot en choisit un au hasard.
- Chaque classe a ses propres points de vie et ses pouvoirs (voir `classes.json`).

| Classe | Vie | Pouvoir 1 | Pouvoir 2 |
|---|---|---|---|
| Guerrier | 120 | Coup d'épée (10) | Frappe puissante (15) |
| Mage | 90 | Boule de feu (14) | Éclair de glace (18) |
| Voleur | 100 | Coup dans le dos (12) | Poison (16) |
| Prêtre | 110 | Eau bénite (10) | Croix de saint Pierre (15) |

## Structure
- `main.py` : boucle de jeu
- `fonctions.py` : logique (chargement des classes, attaques)
- `fonctions_choix.py` : menus et affichage
- `classes.json` : données des classes
- `tests/` : tests (`pip install pytest` puis `pytest`)

---

## Aide-mémoire (Python, système, Git)
### Python
#### Initialiser un nouvel environnement virtuel
```
virtualenv env
# ou
python -m venv env
```

#### Activer l'environnement virtuel
```
source env/bin/activate
# ou
.\env\Scripts\activate
```

#### Enregistrer les dépendances python dans un fichier
```
pip freeze > requirements.txt
```

#### Installer les librairies d'un projet
```
pip install -r requirements.txt
```

### Système
#### Afficher le répertoire courant
```
ls
```

#### Se déplacer dans un répertoire
```
cd repertoire
```

### Git
#### Initialiser un répertoire pour commencer à versionner son projet
```
git init
```

#### Faire un état des lieux des fichiers à sauvegarder
```
git status
```

#### Ajouter des fichiers pour la sauvegarde
```
git add nom_du_fichier
```

#### Sauvegarder son travail avec les fichiers à sauvegarder
```
git commit -m "Mon message spécifique pour les fichiers que je sauvegarde actuellement"
```

#### S'assurer qu'il existe un lien entre son répertoire local et le répertoire sur github
```
git remote -v
```

#### Ajouter le répertoire distant si ce n'est pas le cas
- Se positioner sur le répertoire en ligne
- Suivre les instructions si le répertoire en ligne est vide
- Sinon, cliquer sur le bouton "Code" et récupérer le lien HTTPS
- Se positioner dans son répertoire local, puis :
```
git remote add origin lien
```

#### Mettre en ligne ses changements
```
git push origin main
```

#### Récupérer les changements effectués en ligne
```
git pull origin main
```
