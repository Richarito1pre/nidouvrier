import random

def generer_mot_de_passe():
    mot_de_passe = ""
    for _ in range(6):
        chiffre = random.randint(1, 9)
        mot_de_passe += str(chiffre)
    return mot_de_passe

# Demander le nombre de mots de passe à générer
nombre_mots_de_passe = int(input("Combien de mots de passe souhaitez-vous générer ? "))

# Générer les mots de passe demandés
for i in range(nombre_mots_de_passe):
    mot_de_passe = generer_mot_de_passe()
    print("Mot de passe", i+1, ":", mot_de_passe)
