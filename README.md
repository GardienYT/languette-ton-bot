# Languette ton Bot 💩

Petit jeu de combat au tour par tour dans le terminal : tu choisis ta classe, puis celle de ton adversaire (le bot), et vous vous attaquez jusqu'à ce que l'un des deux tombe à 0 PV.

## Lancer le jeu (terminal, sur ordinateur)
```
python -m venv env
source env/bin/activate      # Windows : .\env\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Jouer sur téléphone (version web)
La version web est dans `docs/index.html` : une seule page, sans installation, qui reprend les mêmes règles et les mêmes classes.

**Option 1 – GitHub Pages (recommandé, joue de n'importe où)**
1. Sur GitHub, ouvre le dépôt → **Settings** → **Pages**.
2. Dans *Build and deployment*, choisis **Deploy from a branch**, la branche **main** (fusionne d'abord la branche de travail) et le dossier **/docs**, puis **Save**.
3. Après une minute, l'adresse `https://gardienyt.github.io/languette-ton-bot/` est en ligne : ouvre-la sur ton téléphone.
4. Astuce : dans le navigateur, « Ajouter à l'écran d'accueil » donne une icône comme une vraie appli.

**Option 2 – Depuis ton ordinateur, sur le même Wi-Fi**
```
cd docs
python -m http.server 8000
```
Trouve l'IP de ton ordinateur (`ipconfig` sous Windows, `ip a` sous Linux, `ifconfig` sous macOS), puis ouvre `http://IP_DE_TON_PC:8000` sur le téléphone.

**Option 3 – Fichier direct** : envoie-toi `docs/index.html` et ouvre-le dans le navigateur du téléphone.

> Si tu modifies `classes.json`, reporte les changements dans la constante `CLASSES` de `docs/index.html`.

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
- `docs/index.html` : version web jouable sur téléphone
- `main.py` : boucle de jeu (version terminal)
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
