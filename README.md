# Languette ton Bot


## GardienYT.exe
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
