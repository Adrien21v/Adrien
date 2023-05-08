#CARTES

import random

nbF=[1, 2, 3, 4, 5, 6]
nbI=[10, 11, 12, 13, 14]
nbpaire=[1, 2, 3, 4, 5, 6]


lcouleurs=['bleu','jaune','rouge']

def Bienvenue():
    print ('Bienvenue dans DICYCLE!')
    id=input('Avant de commencer, comment vous appelez vous ?')
    print('Bonjour',id, '!')
    

def choisir_cartes():
    '''
    CODEUR : ADRIEN
    '''
    
    cards = {'Facile': 12, 'Intermédiaire': 12, 'Difficile': 12}
    player_cards = {}

    while sum(player_cards.values()) < 12:
        for level in cards.keys():
            max_cards = min(12 - sum(player_cards.values()), cards[level])
            while True:
                try:
                    num_cards = int(input(f"Choisissez un nombre de cartes {level} compris entre 0 et {max_cards} : "))
                    if num_cards < 0 or num_cards > max_cards:
                        print(f"Nombre de cartes {level} invalide, veuillez réessayer.")
                    else:
                        player_cards[level] = num_cards
                        cards[level] -= num_cards
                        break
                except ValueError:
                    print("Veuillez entrer un nombre valide entre 0 et 12.")
                    continue

    if sum(player_cards.values()) != 12:
        print("Vous devez choisir exactement 12 cartes. Veuillez recommencer.")
        return choisir_cartes()

    return player_cards

def disposer_cartes(player_cards):
    '''
    CODEUR : ADRIEN
    '''
    
    cards = []
    for level, num_cards in player_cards.items():
        cards.extend([level] * num_cards)

    random.shuffle(cards)

    return cards


def gen_carteF():
    ''' 
    Cette fonction génère des cartes faciles. Elle n'a pas d'entrée et ressort un dictionnaire(qui correspond à une carte).
    CODEUR : LUNA
    '''
    
    lsymb=['<','=']
    
    var_s=[random.choice(lsymb)]
    var_n=[random.choice(nbF)]
    var_c=[random.choice(lcouleurs)]
    var_spe=['N']                   #dans le cas ou le num est 1, on ne peut avoir qu'un ">"      
    carteF={'couleurs':var_c, 'symbole':var_s, 'spécialité':var_spe, 'nombre':var_n}
    if var_n==1 and var_s==['<']:
        var_s=['>'] 
    return carteF
    
def gen_carteI():
    ''' 
    Cette fonction génère des cartes intermédiaires. Elle n'a pas d'entrée et ressort un dictionnaire(qui correspond à une carte).
    CODEUR : LUNA
    '''
    lsymb=['>','==','===']
    
    var_s=[random.choice(lsymb)]
    var_n=[]
    var_c=[]
    var_spe=[]
    
    if var_s==['==']:
        var_n=[random.choice(nbpaire)]
        var_c=[random.choice(lcouleurs),random.choice(lcouleurs)]
        var_spe=['XX']
        
    elif var_s==['===']:
        var_c=[random.choice(lcouleurs)]
        var_n=[]
        var_spe=['ABC']
    else:
        var_c=[random.choice(lcouleurs)]
        var_n=[random.choice(nbI)]
        var_spe=['S']
        
    
    carteI={'couleurs':var_c, 'symbole':var_s, 'spécialité':var_spe, 'nombre':var_n}
    return carteI
        
def gen_carteD():
    ''' 
    Cette fonction génère des cartes difficiles. Elle n'a pas d'entrée et ressort un dictionnaire(qui correspond à une carte).
    CODEUR : LUNA
    '''
    lsymb=['==','===','====']
    
    var_s=[random.choice(lsymb)]
    var_c=[]
    var_n=[]
    var_spe=[]
    
    if var_s==['==']:
        var_n=[0,random.choice(nbF)]
        var_c=[random.choice(lcouleurs)]
        var_spe=['XX','N']
    elif var_s==['===']:
        var_spe=['XXX']
        c3=['bleu', 'jaune','rouge','BJR']
        var_c=[random.choice(c3)]
        var_n=[random.choice(nbpaire)]
    elif var_s==['====']:
        spe4=['XXXX','ABCD']
        var_spe=[random.choice(spe4)]
        if var_spe==['XXXX']:
            var_c=[random.choice(lcouleurs)]
            var_n=[random.choice(nbpaire)]
        elif var_spe==['ABCD']:
            var_c=['BJR']
            var_n=[0]
            
    carteD={'couleurs':var_c, 'symbole':var_s, 'spécialité':var_spe, 'nombre':var_n}
    return carteD




def parcours_cartes(l_cartes):
    '''
    Cette fonction prend en entrée une liste comprenant le nombre de cartes par niveau de difficulté. Elle 
    sort un parcours de cartes sous la forme d'une liste de dictionnaires, correspondant chacun à une carte dont 
    le niveau est définit au hasard (il y a toujours le bon nombre de chaque difficulté choisit par le joueur). 
    Sa sortie est donc une liste.
    
    CODEUR : LUNA

    '''
    CF=0
    CI=0
    CD=0
    
    for i in range(len(l_cartes)):
        if l_cartes[i]=="Facile":
            CF+=1
        elif l_cartes[i]=="Intermédiaire":
            CI+=1
        elif l_cartes[i]=="Difficile":
            CD+=1

    cartesF=[]
    cartesI=[]
    cartesD=[]
    
    for i in range(CF):
        carteFi=[gen_carteF()]
        cartesF+=carteFi
     
    for i in range(CI):
        carteIi=[gen_carteI()]
        cartesI+=carteIi
        
    for i in range(CD):
        carteDi=[gen_carteD()]
        cartesD+=carteDi
        
    cartes=cartesF+cartesI+cartesD
    
    parcours=random.sample(cartes, len(cartes))
    return parcours
       

def choisir_dés():
    dices = {'jaune': 6, 'rouge': 6, 'bleu': 6}

    # Demander aux joueurs de choisir un nombre de dés pour chaque couleur
    player_dice = {}
    while sum(player_dice.values()) < 6:
        for color in dices.keys():
            max_dice = min(6 - sum(player_dice.values()), dices[color])
            while True:
                try:
                 num_dice = int(input(f"Choisissez un nombre de dés {color} (0-{max_dice}) : "))
                 if num_dice < 0 or num_dice > max_dice:
                    print(f"Nombre de dés {color} invalide, veuillez réessayer.")
                 else:
                    player_dice[color] = num_dice
                    dices[color] -= num_dice
                    break
                except ValueError:
                    print("Veuillez entrer un nombre valide entre 0 et 6.")
                    continue

        if sum(player_dice.values()) == 0:
            print("Vous devez choisir au moins 6 dés. Veuillez recommencer.")
            return choisir_dés()
        if sum(player_dice.values()) != 6:
            print("Vous devez choisir au moins 6 dés. Veuillez recommencer.")
            return choisir_dés()

    return player_dice



def roll_dice(player_dice):
    # Tirer les dés choisis
    results = {}
    for color, num_dice in player_dice.items():
        for i in range(num_dice):
            result = random.randint(1, 6)
            key = f"{color} {i+1}"
            results[key] = result

    # Afficher les résultats
    print("Résultats du tirage :")
    for key, value in results.items():
        print(f"{key} : {value}")
    return results

    



#print (parcours_cartes(disposer_cartes(choisir_cartes())))
#player_dice = choisir_dés()
#print (roll_dice(player_dice))

def Verif_carte(carte,des):
    
    
    verif_c1=False
    verif_c2=False
    verif_n=False
    print ('carte:', carte)
    
    print('dés:', des)
    
    
    somme=0
    couleur1=carte['couleurs'][0]
    print (couleur1)
    if len(carte['couleurs'])>=2:
        couleur2=carte['couleurs'][1]
        print(couleur2)
    n=[1,2,3,4,5,6]
    
    
    
    
    for cle,valeur in des.items() :
        if couleur1 in cle:
            verif_c1=True
            verif_c2=True
            if carte['spécialité']==['N']:
                if carte['symbole']==['<'] and [valeur]<carte['nombre']:
                            verif_n=True
                            break
                else:
                     verif_n=False
                    
                if carte['symbole']==['>'] and [valeur]>carte['nombre']:
                     verif_n=True
                     break
                else:
                      verif_n=False
                      
                if carte['symbole']==['='] and [valeur]==carte['nombre']:
                     verif_n=True
                     break
                else:
                      verif_n=False
    

                      
                          
    #cas des paires
    if carte['symbole']==['==']:
        if carte['spécialité']==['XX']:
            for cle,valeur in des.items():
                if [valeur]==carte['nombre']:
                    cle1=cle
                    for valeur in des.values():
                        if valeur in carte['nombre'] and cle!=cle1:
                            verif_n=True
                            break
                        else:
                            verif_n=False
                        if couleur1 in cle and couleur1 in cle1:
                            verif_c1=True
                            verif_c2=True
                            break
                    else:
                        verif_c1=False
                        
                    if couleur2 in cle:
                        verif_c2=True
                        break
                    else:
                        verif_c2=False
        
        if carte['spécialité']==['XX','N']:
            for cle in des.keys():
                if [0, des[cle]]==carte['nombre'] and couleur1 in cle:
                    verif_c1=True
                    verif_c2=True
                    for cle in des:
                        n=[des[cle]]
                        cle1=cle
                        for cle in des:
                            if [des[cle]]==n and cle!=cle1:
                                verif_n=True
                                break
    #cas symbole >            
    if carte['symbole']==['>']:
        if carte['spécialité']==['S']:
            for cle,valeur in des.items():
                if couleur1 in cle:
                    somme+=des[cle]
                if [somme]>carte['nombre']:
                    verif_n=True
                    break
                    
                else:
                    verif_n=False
                    
            if couleur1 in cle:
                verif_c1=True
                verif_c2=True
                
            else:
                verif_c1=False
                verif_c2=False 
            
    
    #cas triple et suite ABC                   
    if carte['symbole']==['===']:
        if carte['spécialité']==['XXX']:
            for cle,valeur in des.items():
                if [valeur]==carte['nombre']:
                    cle1=cle
                    for cle in des.keys():
                        if [des[cle]]==carte['nombre'] and cle!=cle1:
                            cle2=cle
                            for cle in des.keys():
                                if [des[cle]]==carte['nombre'] and cle!=cle1 and cle!=cle2:
                                    verif_n=True
                                    break
                             
                                else:
                                    verif_n=False
                            
                                if couleur1 in cle and couleur1 in cle1 and couleur1 in cle2:
                                    verif_c1=True
                                    verif_c2=True
                                    break
                                if couleur1=='BJR':
                                    verif_c1=True
                                    verif_c2=True
                                    break
                
                
    if carte['symbole']==['===']:
        if carte['spécialité']==['ABC']:
            verif_c1=True
            verif_c2=True
            for cle in des.keys():
               if carte['nombre']==des[cle]:
                    cle1=cle
                    for cle in des.keys():
                         if des[cle]==des[cle1]+1 and cle!=cle1:
                             
                             cle2=cle
                             
                             for cle in des:
                                 if des[cle]==des[cle2]+2 and cle!=cle1 and cle!=cle2:
                                     
                                     verif_n=True
                                     break 
                             if verif_n==True:    
                                 break
                    if verif_n==True:    
                        break
                    
    #cas des suites ABCD           
    if carte['symbole']==['====']:
        if carte['spécialité']==['ABCD']:
            verif_c1=True
            verif_c2=True
            for cle in des.keys():
                if des[cle]==1 or des[cle]==2 or des[cle]==3:
                    
                    cle1=cle
                    for cle in des.keys():
                         if des[cle]==des[cle1]+1 and cle!=cle1:
                             
                             cle2=cle
                             
                             for cle in des.keys():
                                 if des[cle]==des[cle1]+2 and cle!=cle1 and cle!=cle2:
                                     cle3=cle
                                     
                                     for cle in des.keys():
                                         if des[cle]==des[cle1]+3 and cle!=cle1 and cle!=cle2 and cle!=cle3:
                                             verif_n=True
                                             break
                                     
                                     verif_n=True
                                     break
                                     
                             if verif_n==True:
                                 break
                    if verif_n==True:
                        break
    
            
    if verif_c1==True and verif_c2==True and verif_n==True:
        return "Bien joué! Vous avez validé ce niveau. Pédalez jusqu'à la carte suivante!"
    else:
        return"Dommage, c'est raté ! Rejouez pour valider le niveau.",""

      



def asso_cartes():
    
    parcours=parcours_cartes(disposer_cartes(choisir_cartes()))
    print (parcours)
    
    for i in range(11):
    
        if i==0:
            carte1=parcours[0]
            desc1=roll_dice(choisir_dés())
        if i==1:
            carte2=parcours[1]
            desc2=roll_dice(choisir_dés())
        if i==2:
            carte3=parcours[2]
            desc3=roll_dice(choisir_dés())
        if i==3:
            carte4=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc4=roll_dice(choisir_dés())
        if i==4:
            carte5=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc5=roll_dice(choisir_dés())
        if i==5:
            carte6=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc6=roll_dice(choisir_dés())
        if i==6:
            carte7=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc7=roll_dice(choisir_dés())
        if i==7:
            carte8=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc8=roll_dice(choisir_dés())
        if i==8:
            carte9=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc9=roll_dice(choisir_dés())
        if i==9:
            carte10=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc10=roll_dice(choisir_dés())
        if i==10:
            carte11=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc11=roll_dice(choisir_dés())
        if i==11:
            carte12=parcours_cartes(disposer_cartes(choisir_cartes()))[i]
            desc12=roll_dice(choisir_dés())
        print (carte1)
        return [carte1, desc1]
'''
cartedes=asso_cartes()
carte1=cartedes[0]
des1=cartedes[1]

Verif_carte(carte1,des1)
'''

