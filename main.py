#           ______               ___        __  ________        #
#          / ____/___ __________/ (_)__  ___\ \/ /_  __/        #
#         / / __/ __ `/ ___/ __  / / _ \/ __ \  / / /           #
#        / /_/ / /_/ / /  / /_/ / /  __/ / / / / / /            #
#        \____/\__,_/_/   \__,_/_/\___/_/ /_/_/ /_/             #
#                                                               #

from fonctions_choix import *
from fonctions import *
import json
import random
import time

# Choix des classes
player = ""
bot = ""
choix_de_depart = lancement_application()

if choix_de_depart == LancementApplicationChoix.Lancer.name:
    lancer_game()
    player = player_classe(player=player)
    bot = bot_classe(bot=bot)

elif choix_de_depart == LancementApplicationChoix.Quitter.name:
    quitter_game()
else:
    print("kossa ou ve fé ?")

# Définir l'énergie et la vie des classes
health_player = 100     # 100 HP
health_bot = 100        # 100 HP

# Charger les informations des classes depuis le fichier JSON
with open('classes.json') as json_data:
    d = json.load(json_data)

power_player_1 = d[player.lower()]["power1"]["value"]
power_player_2 = d[player.lower()]["power2"]["value"]
name_power_player_1 = d[player.lower()]["power1"]["name"]
name_power_player_2 = d[player.lower()]["power2"]["name"]

power_bot_1 = d[bot.lower()]["power1"]["value"]
power_bot_2 = d[bot.lower()]["power2"]["value"]
name_power_bot_1 = d[bot.lower()]["power1"]["name"]
name_power_bot_2 = d[bot.lower()]["power2"]["name"]

def choix_power_player():
    title = "Choisir une attaque"
    options = [name_power_player_1, name_power_player_2]
    option, index = pick(options, title)
    return option

def health_info():
    pretty_print("-------- Vies --------", "green")
    pretty_print(f"Vie du joueur: {health_player}", "green")
    pretty_print(f"Vie du bot: {health_bot}", "green")
    time.sleep(5)

# Choix aléatoire de la personne qui attaque en premier
current_turn = random.choice([player, bot])

while True:
    health_info()
    if current_turn == player:
        pretty_print("-------- PLAYER --------", "blue")
        choix_poupou = choix_power_player()
        
        if choix_poupou == name_power_player_1:
            health_bot -= power_player_1
            pretty_print(f"Pouvoir: {name_power_player_1}", "blue")
            pretty_print(f"Dégat: {power_player_1}", "blue")
        elif choix_poupou == name_power_player_2:
            health_bot -= power_player_2
            pretty_print(f"Pouvoir: {name_power_player_2}", "blue")
            pretty_print(f"Dégat: {power_player_2}", "blue")

        # Vérifier si le bot est vaincu
        if health_bot <= 0:
            pretty_print("FINISH", "red")
            print("Le joueur a gagné !")
            break

        # Passer le tour au bot
        current_turn = bot

    else:  # Le tour du bot
        pretty_print("-------- BOT --------", "red")
        attack_choice = random.choice([1, 2])

        if attack_choice == 1:
            health_player -= power_bot_1
            pretty_print(f"Pouvoir: {name_power_bot_1}", "red")
            pretty_print(f"Dégat: {power_bot_1}", "red")
        else:
            health_player -= power_bot_2
            pretty_print(f"Pouvoir: {name_power_bot_2}", "red")
            pretty_print(f"Dégat: {power_bot_2}", "red")

        # Vérifier si le joueur est vaincu
        if health_player <= 0:
            pretty_print("FINISH", "red")
            print("Le bot a gagné !")
            break

        # Passer le tour au joueur
        current_turn = player

pretty_print("FINISH", "red")