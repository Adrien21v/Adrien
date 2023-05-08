# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:41:23 2023

@author: lunac
"""
import cartes 
import random



def Bloquer_Des(desj,des_tire):
    
    # Demander si le joueur veut bloquer certains dés
    blocked_dice = {}  # initialiser un dictionnaire pour stocker les dés bloqués
    
    block = input("Voulez-vous bloquer certains dés ? (oui/non) ")
    if block.lower() == "oui":
        # Demander les dés à bloquer
        while True:
            choice = input("Quels dés voulez-vous bloquer ? (ex: jaune 1) (non pour sortir) :  ")
            if choice.lower() == "non":
                break
            try:
                color, index = choice.split()
                index = int(index)
                if color not in desj.keys() or index < 1 or index > desj[color]:
                    print("Choix invalide. Veuillez réessayer.")
                    continue
                key = f"{color} {index}"
                blocked_dice[key] = des_tire[key]  # stocker le dé bloqué dans le dictionnaire
                del des_tire[key]  # supprimer le dé de la liste des dés à relancer
            except ValueError:
                print("Choix invalide. Veuillez réessayer.")
                continue
    
        print("Dés bloqués :")
        for key, value in blocked_dice.items():
            print(f"{key} : {value}")
        print()

    # Relancer les dés non bloqués
    for key in des_tire.keys():
        des_tire[key] = random.randint(1, 6)
    
    print("Résultats du tirage :")
    for key, value in des_tire.items():
        print(f"{key} : {value}")
    
    return des_tire
    
          
    
    
    
def Boucle_Tour(parcours):
    
    cartesTour=[]
    cartes_verif=[]
    #jeu_joueur=cartes.choisir_cartes()
    print()
    #parcours=cartes.parcours_cartes(cartes.disposer_cartes(jeu_joueur))
    for i in range(3):
            cartei=parcours[i]
            cartesTour+=[cartei]
    
    print("Voici les 3 prochaines cartes:")
    print()
    print(cartesTour)
    print('Choisissez les des avec lesquels vous souhaitez jouer.') 
    desj=cartes.choisir_dés()    
    
   
    des_tire=cartes.roll_dice(desj)
    
    
    
    carteV1=cartes.Verif_carte(cartesTour[0],des_tire)
    print (carteV1)
    carteV2=cartes.Verif_carte(cartesTour[1],des_tire)
    print(carteV2)
    carteV3=cartes.Verif_carte(cartesTour[2],des_tire)
    print(carteV3)
    cartes_verif=[carteV1,carteV2,carteV3]   
    
    if carteV1=="Bien joué! Vous avez validé ce niveau. Pédalez jusqu'à la carte suivante!":
        parcours.remove(parcours[0])
        for i in range(3):
                cartei=parcours[i]
                cartesTour+=[cartei]
                print("Voici vos nouvelles prochaines cartes:")
                print(cartesTour)
                break
        
    else:
        print()
        print('Ne vous inquiétez pas, il vous reste 2 lancers !')
    
    new_d=Bloquer_Des(desj, des_tire)
    
    print()
    
    print('Relançons les dés maintenant.')
    print()
    carteV1=cartes.Verif_carte(cartesTour[0],new_d)
    print (carteV1)
    carteV2=cartes.Verif_carte(cartesTour[1],new_d)
    print(carteV2)
    carteV3=cartes.Verif_carte(cartesTour[2],new_d)
    print(carteV3)
    
    
    cartes_verif=[carteV1,carteV2,carteV3]
    
    if carteV1=="Bien joué! Vous avez validé ce niveau. Pédalez jusqu'à la carte suivante!":
        parcours.remove(parcours[0])
        for i in range(3):
                cartei=parcours[i]
                cartesTour+=[cartei]
                print("Voici vos nouvelles prochaines cartes:")
                print(cartesTour)
                break
        
    else:
        print()
        print('Ne vous découragez pas, il vous reste 1 lancer !')
    
    
    
    new_d2=Bloquer_Des(desj, des_tire)
    
    
    carteV1=cartes.Verif_carte(cartesTour[0],new_d2)
    print (carteV1)
    carteV2=cartes.Verif_carte(cartesTour[1],new_d2)
    print(carteV2)
    carteV3=cartes.Verif_carte(cartesTour[2],new_d2)
    print(carteV3)
    cartes_verif=[carteV1,carteV2,carteV3]
   
    if cartes_verif[0]=="Bien joué! Vous avez validé ce niveau. Pédalez jusqu'à la carte suivante!":
        parcours.remove(parcours[0])
        
        if cartes_verif[1]=="Bien joué! Vous avez validé ce niveau. Pédalez jusqu'à la carte suivante!":
            parcours.remove(parcours[0])
            
            if cartes_verif[2]=="Bien joué! Vous avez validé ce niveau. Pédalez jusqu'à la carte suivante!":
                parcours.remove(parcours[0])
                
    return (parcours)

            
#Boucle_Tour()           



def Boucle_Jeu():
    
    cartes.Bienvenue()
    jeu_joueur=cartes.choisir_cartes()
    print()
    parcours=cartes.parcours_cartes(cartes.disposer_cartes(jeu_joueur))
    print ()
    print('Vous êtes actuellement sur la case Départ.', end=' ')
    print('Voici votre parcours:')
    print()
    print()
    print(parcours)
    
    while parcours!=[]:
        print()
        Boucle_Tour(parcours)
        print()
        print("Vous avez fini ce tour. Un nouveau va commencer.")
    
    
Boucle_Jeu()