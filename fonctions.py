from fonctions_choix import *

def  player_classe(player):
    choix_de_classe_player = choix_classe_player()

    if choix_de_classe_player == ChoixClassePlayer.Guerrier.name:
        player = choix_de_classe_player
    elif choix_de_classe_player == ChoixClassePlayer.Mage.name:
        player = choix_de_classe_player
    elif choix_de_classe_player == ChoixClassePlayer.Voleur.name:
        player = choix_de_classe_player
    elif choix_de_classe_player == ChoixClassePlayer.Pretre.name:
        player = choix_de_classe_player
    return player

def bot_classe(bot):
    choix_de_class_bot = choix_classe_bot()

    if choix_de_class_bot == ChoixClasseBot.Guerrier.name:
        bot = choix_de_class_bot
    elif choix_de_class_bot == ChoixClasseBot.Mage.name:
        bot = choix_de_class_bot
    elif choix_de_class_bot == ChoixClasseBot.Voleur.name:
        bot = choix_de_class_bot
    elif choix_de_class_bot == ChoixClasseBot.Pretre.name:
        bot = choix_de_class_bot
    return bot