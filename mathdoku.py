# -*- coding: iso-8859-1 -*-
"""

"""
#Programme de résolution de Mathdoku (4x4 jusqu'à 9x9)
#Auteur: ELQATIB

"""J'ai décidé de ne pas utiliser les classes pour mon interface et inclure tout le code dans
un seul script en utilisant des fonctions 'plus simples' pour la partie interface .."""



from pylab import *
from tkinter import *
import tkinter as tk
import pickle # Manipuler les Grilles sauvegardées .. ;)
import itertools as it
import time


"""
Grille de Mathdoku, taille
"""
fenetre_taille=tk.Tk() #Création de la fenêtre.
taille_mathdoku=IntVar() #Variable de type 'integer' à récupérer.
fenetre_taille.title('Résolution de Mathdoku')#Titre de la fenêtre.
fenetre_taille.geometry('480x120') #Dimensions
tk.Label(fenetre_taille,text='Bienvenue !',fg="Brown",font="Underline").grid(column=0,row=0)
tk.Label(fenetre_taille,text='Entrez la taille de votre grille Mathdoku ( 4-9, ou 0 pour charger une grille sauvegardée )  :').grid(column=0,row=1)
tk.Entry(fenetre_taille,textvariable=taille_mathdoku).grid(column=0,row=2)
Button(fenetre_taille,text='Valider',command=fenetre_taille.destroy).grid(row=3)
Button(fenetre_taille,text='Quitter', fg='Red',command=fenetre_taille.destroy).grid(row=4)
fenetre_taille.mainloop() #Affichage.
taille=taille_mathdoku.get() # Variable à récupérer, ie : taille de la grille.

"""
"""

liste_domaine=list() #Très importante
coordonnee_bilan=list()


def cancel():
    suppression=liste_domaine.pop()[1]
    for ligne in range(0,taille):
        for colonne in range(0,taille):
            if (ligne,colonne) in suppression:
                coordonnee_bilan.remove((ligne,colonne))
    Matrice_affichage=zeros((taille,taille),int)
    for domaine in liste_domaine:
        liste_coordonnee=domaine[1]
        for coordonnee in liste_coordonnee:
            ligne=coordonnee[0]
            colonne=coordonnee[1]
            Matrice_affichage[ligne,colonne]=domaine[0]
    print("__________________________________")
    print(Matrice_affichage) #Affiche les domaines avec leur coordonnées;
    print("__________________________________")
    print('Le dernier domaine a été supprimé.')
    print("__________________________________")



def sift():
    fenetre.quit()
    coordonnee=[]
    for i in range(0,taille*taille): #pour vérifier
        if (liste_variable[i].get()==1)&((i//taille,i%taille) not in coordonnee)&((i//taille,i%taille) not in coordonnee_bilan):
        #Dans ce cas, le bouton est coché et la coordonnée n'est pas déjà  dans les listes
            coordonnee.append((i//taille,i%taille))
        #entre la ligne, ie le quotient du numéro de variable par la taille, et le reste comme colonne.
            coordonnee_bilan.append((i//taille,i%taille))
    total=total_domaine.get() #récupère la valeur dans le champ de saisie
    tuple_domaine=(total,coordonnee)
    # Pour créer le tuple qui apparaitra dans la liste finale (liste_domaine)
    if coordonnee==[]:
        print('Veuillez sélectionner les cases du domaine !')
    else:
        liste_domaine.append(tuple_domaine) #compléte la liste finale
        Matrice_affichage=zeros((taille,taille),int)
        for domaine in liste_domaine:
            liste_coordonnee=domaine[1]
            for coordonnee in liste_coordonnee:
                ligne=coordonnee[0]
                colonne=coordonnee[1]
                Matrice_affichage[ligne,colonne]=domaine[0]
        print("_____________________________________________________________________")
        print('Ce domaine a été enregistré, pour l\'instant, voici votre grille :')
        print("_____________________________________________________________________")
        print(Matrice_affichage) #domaines + coordonnées
        print("_____________________________________________________________________")
        print('Veuillez remplir les domaines restants.')
        print("_____________________________________________________________________")




"""Pour le chargement et la sauvegarde"""

def save(): #Sauvegarde d'une grille, là intervient la fonction pickle!
    num_sauve=numero_sauve.get() #L'entier qu'on récupère, pour lequel la grille est enregistrée .
    nom_sauve='sauvegarde mathdoku n°' + str(num_sauve)
    with open(nom_sauve,"wb") as fichier_sauvegarde: #Manipulations du fichier (création - sauvegarde)
        liste_sauvegarde=pickle.Pickler(fichier_sauvegarde) #Stockage de la liste grâce à la fonction 'pickle'
        liste_sauvegarde.dump(liste_domaine)
    sauvegarde.quit()

def upload(): #Chargement d'une grille, en cas d'existence :D
    num_charge=numero_charge.get() #valeur récupérée lors du clic sur le bouton
    nom_charge='sauvegarde mathdoku n° '+ str(num_charge)
    with open(nom_charge,'rb') as fichier_sauvegarde :
        lecture=pickle.load(fichier_sauvegarde)
    chargement.quit()
    return lecture #renvoie la liste sauvegardée dans le fichier

""" Saisie de la grille """


if (taille_mathdoku.get()<10)&(taille_mathdoku.get()>3): #On s'assure que la taille entrée est bien conforme aux règles du jeu
    saisie_domaine=True
    fenetre=tk.Tk()
    fenetre.title('Saisie de la grille')
    var='variable'
    liste_variable=[] #Pour les checkbox
    for nombre in range(0,taille*taille): #création d'une liste du type : var_1, var_2 ... var_n
        chaine=str(nombre)  #Concatenation
        liste_variable.append(var+chaine)
        liste_variable[nombre]=IntVar() #Conversion du type pour exploiter dans les checkbox

    #Grille aux dimensions voulues i.e : n*n ( en utilisant les checkbox) à l'aide de 2boucles for
    for ligne in range(0,taille):
        for colonne in range(0,taille):
            Checkbutton(fenetre,
                        variable=liste_variable[ligne*taille+colonne]).grid(column=colonne,row=ligne)

    tk.Label(fenetre,
             text="Total du domaine :",
             font='Bold').grid(column=taille,row=1)
    tk.Label(fenetre,
             text="Remarque : Votre grille s'actualise dans la console",
             font='Bold', fg='Red').grid(column=taille+1,row=taille)
    total_domaine=IntVar() #Entier à récupérer
    tk.Entry(fenetre,textvariable=total_domaine).grid(column=taille+1,row=1)#champ de saisie du total

    Button(fenetre,
           text='Quitter',command=fenetre.destroy,
           fg='Red').grid(column=taille+2,row=taille-3)
    Button(fenetre,
           text='Valider',command=sift).grid(column=taille,row=taille-3)
    Button(fenetre,
           text='Annuler',command=cancel).grid(column=taille+1,row=taille-3)



elif taille_mathdoku.get()==0: #Dans ce cas, il est nécessaire de charger une grille stockée
    saisie_domaine=False #On sort du while
    chargement=tk.Tk()
    chargement.title("Chargement d'une grille ")
    chargement.geometry('300x60')
    numero_charge=IntVar()

    tk.Label(chargement,
             text='Charger la grille numero :').grid(column=0,row=0)
    tk.Entry(chargement,
             textvariable=numero_charge).grid(column=1,row=0)
    Button(chargement,
           text='Quitter',command=chargement.destroy,
           fg='Red').grid(column=1,row=1)
    Button(chargement,
           text='Charger',command=upload).grid(column=0,row=1)

    chargement.mainloop()
    liste_domaine=upload()


else :
    fenetre_taille.quit()
    print("Veuillez entrer une dimension conforme !") #Un peu de respect ..!

while saisie_domaine==True : #Plus rapide en saisissant tout les domaines dans une même fenêtre
    compteur=0
    for ligne in range(0,taille):
        for colonne in range(0,taille):
            if (ligne,colonne) in coordonnee_bilan: #Dans ce cas, tous les checkbox ont été remplis
                compteur+=1
    if compteur==taille*taille:
        saisie_domaine=False
        print('Veuillez répondre par "oui" ou "non"')
        grille_finie=input(" -Voulez-vous confirmer la grille rentrée ? ")
        if grille_finie=='oui':
            question_sauvegarde=input(" -Souhaitez vous sauvegarder la grille ? ")
        else:
            saisie_domaine=True
            cancel()
            question_sauvegarde='non'
        if question_sauvegarde=='oui': #Sinon, il n'y a plus rien à faire !
            fenetre.destroy()
            sauvegarde=tk.Tk()
            numero_sauve=IntVar()
            tk.Label(sauvegarde,text='Sauvegarder sous le numéro :').grid(column=0,row=0)
            tk.Entry(sauvegarde,textvariable=numero_sauve).grid(column=1,row=0)
            Button(sauvegarde,text='Quitter',command=sauvegarde.destroy, fg='Red').grid(column=1,row=1)
            Button(sauvegarde,text='Sauvegarder',command=save).grid(column=0,row=1)
            sauvegarde.mainloop()
            #sauvegarde.destroy avec précaution ...

    else: #S'il reste des checkbox.
        fenetre.mainloop()
print(liste_domaine)

"""
Fin de l'interface

"""
"""

cpt=0 #Compteur d'itérations
for domaine in liste_domaine:
    cpt+=len(domaine[1])
cpt=cpt**0.5
taille=int(cpt)
#print('mathdoku de taille',taille)

"""

"""
def test_ligne_colonne(domaine,combinaison): #Test ligne et colonne en même temps.
    Matrice=zeros((taille,taille),int)
    for iteration in range(0,len(domaine)):  #Remplissage du domaine avec la combinaison.
        Matrice[domaine[iteration][0],domaine[iteration][1]]=combinaison[iteration]
    for element,coordonnee in zip(combinaison,domaine): #pour chaque élement de la combinaison et sa coordonnée.
        for n in range(0,taille): #test colonne
            if (Matrice[coordonnee[0],n]==element)&(n!=coordonnee[1]):
                return False
                break
        for n in range(0,taille): #test ligne
            if(Matrice[n,coordonnee[1]]==element)&(n!=coordonnee[0]):
                return False
                break
        return True
    #end def

def combinaison(total,domaine): # Fonction " corps " du programme.
    liste_combinaison=[] #liste retournée.
    possibilite=[]
    var='élement'
    liste_element=[]
    for nombre in range(0,len(domaine)): #création de la combinaison pour addition, soustraction et division.
        chaine=str(nombre)
        liste_element.append(var+chaine)
        liste_element[nombre]=1
    for i in range(1,taille+1): #pour la fonction it.product.
        possibilite.append(i)
    if len(domaine)==1: #Dans ce cas il n'y a qu'une seule combinaison envisageable.
        liste_tuple=[total]
        tup=tuple(liste_tuple)
        liste_combinaison.append(tup)
        return liste_combinaison
    elif len(domaine)==2: #Si on peut faire une division ou une soustraction.

        tourne=True
        while tourne:
            element1=liste_element[0]
            element2=liste_element[1]

            if (element1/element2)==total: #Division
                solution1_div=(element1,element2)
                solution2_div=(element2,element1)
                if (test_ligne_colonne(domaine,solution1_div))&(solution1_div not in liste_combinaison):
                    liste_combinaison.append(solution1_div)
                if test_ligne_colonne(domaine,solution2_div)&(solution2_div not in liste_combinaison):
                    liste_combinaison.append(solution2_div)
            if (element1-element2)==total: #soustraction
                solution1_sous=(element1,element2)
                solution2_sous=(element2,element1)
                if (test_ligne_colonne(domaine,solution1_sous))&(solution1_sous not in liste_combinaison):
                    liste_combinaison.append(solution1_sous)
                if (test_ligne_colonne(domaine,solution2_sous))&(solution2_sous not in liste_combinaison):
                    liste_combinaison.append(solution2_sous)

            if liste_element[0]<taille: #Incrémentation du 1er élement.
                liste_element[0]+=1
            elif (liste_element[0]==taille)&(liste_element[1]<taille): #2ème élement.
                liste_element[0]=1
                liste_element[1]+=1
            else: #On a atteint le maximum, donc on sort du while.
                tourne=False


    #Multiplication.
                #Cas le plus pénible..

    for combi_lineaire in it.product(possibilite,repeat=len(domaine)):
        produit_domaine=1
        for chiffre in combi_lineaire: #Produit de tous les chiffres de la combinaison.
            produit_domaine=produit_domaine*chiffre
        if produit_domaine==total:
            if (test_ligne_colonne(domaine,combi_lineaire))&(combi_lineaire not in liste_combinaison):
                liste_combinaison.append(combi_lineaire)

   #addition. Ca avance ..

    if taille*len(domaine)>=total: #L'addition est possible.
        for nombre in range(0,len(domaine)): #Création de la combinaison.
            liste_element[nombre]=1 #Au cas cas où il y aurait eu une soustraction.

        somme=0
        while somme!=taille*len(domaine):
            somme=0 #Ré-initialisation.
            for element in liste_element: #Vérification.
                somme+=element
            if (somme==total): #Combinaison royale. (Celle qui marche ^^)

                combinaison_gg=tuple(liste_element)
                if (test_ligne_colonne(domaine,combinaison_gg))&(combinaison_gg not in liste_combinaison):
                    liste_combinaison.append(combinaison_gg)
            for indice in range(0,len(liste_element)):
                if liste_element[indice]<taille:
                    liste_element[indice]+=1
                    break
                else:
                    liste_element[indice]=1

    return liste_combinaison

"""

"""

#On va maintenant créer et ordonner la liste pour la résolution.

def genèse(liste):
    var='info_domaine'
    liste_info=[]
    for i in range(0,len(liste)):
        chaine=str(i)
        liste_info.append(var+chaine)
        liste_info[i]=(liste[i][1],combinaison(liste[i][0],liste[i][1])) #Coordonnée puis combinaison.
    liste_domaine_ordonnee=sorted(liste_info,key=lambda x:len(x[1]))
    return liste_domaine_ordonnee

liste_domaine_ordonnee=genèse(liste_domaine)
print(liste_domaine_ordonnee)

"""

"""


#On va maintenant créer et ordonner la liste pour la résolution.

def genèse(liste):
    var='info_domaine'
    liste_info=[]
    for i in range(0,len(liste)):
        chaine=str(i)
        liste_info.append(var+chaine)
        liste_info[i]=(liste[i][1],combinaison(liste[i][0],liste[i][1])) #Coordonnée puis combinaison.
    liste_domaine_ordonnee=sorted(liste_info,key=lambda x:len(x[1]))
    return liste_domaine_ordonnee

liste_domaine_ordonnee=genèse(liste_domaine)
print(liste_domaine_ordonnee)

"""

"""

#Là commence les choses sérieuses, étape de la résolution.

def test_remplissage(domaine,combinaison,Matrice):
    matrice=Matrice.copy()
    for iteration in range(0,len(domaine)):
        matrice[domaine[iteration][0],domaine[iteration][1]]=combinaison[iteration]
    for element,coordonnee in zip(combinaison,domaine):

        #Tests respectifs des lignes et des colonnes.

        for n in range(0,taille):
            if (matrice[coordonnee[0],n]==element)&(n!=coordonnee[1]):
                return False
                break
        for n in range(0,taille):
            if(matrice[n,coordonnee[1]]==element)&(n!=coordonnee[0]):
                return False
                break

    return True

    #end def



def fill_in(tuple_ordonne,indice,M): #Combinaison par combinaison.
    liste_parcours[indice]+=1
    liste_coordonnee=tuple_ordonne[0]
    liste_combinaison=tuple_ordonne[1]
    while liste_parcours[indice]<len(liste_combinaison): #Boucle tant qu'il y a toujours des combinaisons à essayer.
        if test_remplissage(liste_coordonnee,liste_combinaison[liste_parcours[indice]],M): #Si ça colle, on remplit.
            for iteration in range(0,len(liste_coordonnee)):
                M[liste_coordonnee[iteration][0],liste_coordonnee[iteration][1]]=liste_combinaison[liste_parcours[indice]][iteration]
            return True
        liste_parcours[indice]+=1
    liste_parcours[indice]=-1
    return False

    #end def


def effacer_domaine(liste_coordonnee,M):
    for coordonnee in liste_coordonnee:
        M[coordonnee[0],coordonnee[1]]=0


liste_parcours=[]
debut = time.time()
def resolution(liste_domaine_ord):
    for iteration in range(0,len(liste_domaine_ord)):
        liste_parcours.append(-1) #-1 pour aucune combinaison.
    M=zeros((taille,taille),int)
    indice=0
    print("La grille est en cours de résolution ... Veuillez patienter. " )
    while True:
        if fill_in(liste_domaine_ord[indice],indice,M):
            indice+=1
        else:
            indice=indice-1
            effacer_domaine(liste_domaine_ord[indice][0],M)

        if indice==0:
            print('ERROR : Indice non valable, veuillez relancer le programme.')
            break

        if indice==len(liste_domaine_ord):
            break
    fin=time.time()
    return M
    return str(fin-debut)

    #end def


resultat=resolution(liste_domaine_ordonnee)
print(resultat)

#end prg



