# -*- coding: iso-8859-1 -*-
"""
MIT License

Copyright (c) 2017 marrakchino (nabilelqatib@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pylab import *
import Tkinter as Tk
import tkFileDialog
import pickle
import itertools as it
import time
from plot import Plot


fenetre_taille=Tk.Tk() 
taille_mathdoku=Tk.IntVar() 
fenetre_taille.title('Mathdoku solver')
fenetre_taille.geometry('300x120')
Tk.Label(fenetre_taille,text='Bienvenue !',fg="Brown",font="Underline").grid(column=0,row=0)
Tk.Label(fenetre_taille,text='Enter the grid size (4 - 9), 0 to load a saved grid.').grid(column=0,row=1)
Tk.Entry(fenetre_taille,textvariable=taille_mathdoku).grid(column=0,row=2)
Tk.Button(fenetre_taille,text='Fill',command=fenetre_taille.destroy).grid(row=3)
Tk.Button(fenetre_taille,text='Exit', fg='Red',command=fenetre_taille.destroy).grid(row=4)
fenetre_taille.mainloop()
taille=taille_mathdoku.get()

liste_domaine=list() 
coordonnee_bilan=list()

def cancel():
    suppression=liste_domaine.pop()[1]
    for ligne in range(0,taille):
        for colonne in range(0,taille):
            if (ligne,colonne) in suppression:
                coordonnee_bilan.remove((ligne,colonne))
    matrice_affichage=zeros((taille,taille),int)
    for domaine in liste_domaine:
        liste_coordonnee=domaine[1]
        for coordonnee in liste_coordonnee:
            ligne=coordonnee[0]
            colonne=coordonnee[1]
            matrice_affichage[ligne,colonne]=domaine[0]
    print("__________________________________")
    print(matrice_affichage) # Affiche les domaines avec leur coordonnees;
    print("__________________________________")
    print('Le dernier domaine a ete supprime.')
    print("__________________________________")



def sift():
    fenetre.quit()
    coordonnee=[]
    for i in range(0,taille*taille): # pour verifier
        if (liste_variable[i].get()==1)&((i//taille,i%taille) not in coordonnee)&((i//taille,i%taille) not in coordonnee_bilan):
        # Dans ce cas, le bouton est coche et la coordonnee n'est pas deja  dans les listes
            coordonnee.append((i//taille,i%taille))
        # entre la ligne, ie le quotient du numero de variable par la taille, et le reste comme colonne.
            coordonnee_bilan.append((i//taille,i%taille))
    total=total_domaine.get() # recupere la valeur dans le champ de saisie
    tuple_domaine=(total,coordonnee)
    # Pour creer le tuple qui apparaitra dans la liste finale (liste_domaine)
    if coordonnee==[]:
        print('Veuillez selectionner les cases du domaine !')
    else:
        liste_domaine.append(tuple_domaine) # complete la liste finale
        matrice_affichage=zeros((taille,taille),int)
        for domaine in liste_domaine:
            liste_coordonnee=domaine[1]
            for coordonnee in liste_coordonnee:
                ligne=coordonnee[0]
                colonne=coordonnee[1]
                matrice_affichage[ligne,colonne]=domaine[0]
        print("_____________________________________________________________________")
        print('Ce domaine a ete enregistre, pour l\'instant, voici votre grille :')
        print("_____________________________________________________________________")
        print(matrice_affichage) # domaines + coordonnees
        print("_____________________________________________________________________")
        print('Veuillez remplir les domaines restants.')
        print("_____________________________________________________________________")


if (taille_mathdoku.get() < 10) and (taille_mathdoku.get() > 3): 
    saisie_domaine=True
    fenetre=Tk.Tk()
    fenetre.title('Saisie de la grille')
    var='variable'
    liste_variable=[] # Pour les checkbox
    for nombre in range(0,taille*taille): # creation d'une liste du type : var_1, var_2 ... var_n
        chaine=str(nombre)  # Concatenation
        liste_variable.append(var+chaine)
        liste_variable[nombre]=Tk.IntVar() # Conversion du type pour exploiter dans les checkbox

    # Grille aux dimensions voulues i.e : n*n ( en utilisant les checkbox) a l'aide de 2boucles for
    for ligne in range(0,taille):
        for colonne in range(0,taille):
            Tk.Checkbutton(fenetre,
                        variable=liste_variable[ligne*taille+colonne]).grid(column=colonne,row=ligne)

    Tk.Label(fenetre,
             text="Total du domaine :",
             font='Bold').grid(column=taille,row=1)
    Tk.Label(fenetre,
             text="Remarque : Votre grille s'actualise dans la console",
             font='Bold', fg='Red').grid(column=taille+1,row=taille)
    total_domaine=Tk.IntVar() # Entier a recuperer
    Tk.Entry(fenetre,textvariable=total_domaine).grid(column=taille+1,row=1)# champ de saisie du total

    Tk.Button(fenetre,
           text='Quitter',command=fenetre.destroy,
           fg='Red').grid(column=taille+2,row=taille-3)
    Tk.Button(fenetre,
           text='Valider',command=sift).grid(column=taille,row=taille-3)
    Tk.Button(fenetre,
           text='Annuler',command=cancel).grid(column=taille+1,row=taille-3)


elif taille_mathdoku.get()==0: 
    saisie_domaine=False # On sort du while
    p = Plot()
    liste_domaine=p.load()

# TODO: FIX
else :
    fenetre_taille.quit()
    print("Veuillez entrer une dimension conforme !") 
    exit()

while saisie_domaine==True : # Plus rapide en saisissant tout les domaines dans une même fenêtre
    compteur=0
    for ligne in range(0,taille):
        for colonne in range(0,taille):
            if (ligne,colonne) in coordonnee_bilan: # Dans ce cas, tous les checkbox ont ete remplis
                compteur+=1
    if compteur==taille*taille:
        saisie_domaine=False
        print('Veuillez repondre par "oui" ou "non"')
        grille_finie=raw_input("-Voulez-vous confirmer la grille rentree ? ")
        if grille_finie=='oui':
            question_sauvegarde=raw_input("-Souhaitez vous sauvegarder la grille ? ")
        else:
            saisie_domaine=True
            cancel()
            question_sauvegarde='non'
        if question_sauvegarde=='oui': 
            fenetre.destroy()
            p = Plot()
            p.save(liste_domaine)

    else: # S'il reste des checkbox.
        fenetre.mainloop()
print(liste_domaine)


cpt=0 # Compteur d'iterations
for domaine in liste_domaine:
    cpt+=len(domaine[1])
cpt=cpt**0.5
taille=int(cpt)
# print('mathdoku de taille',taille)

def test_ligne_colonne(domaine,combinaison): # Test ligne et colonne en même temps.
    Matrice=zeros((taille,taille),int)
    for iteration in range(0,len(domaine)):  # Remplissage du domaine avec la combinaison.
        Matrice[domaine[iteration][0],domaine[iteration][1]]=combinaison[iteration]
    for element,coordonnee in zip(combinaison,domaine): # pour chaque element de la combinaison et sa coordonnee.
        for n in range(0,taille): # test colonne
            if (Matrice[coordonnee[0],n]==element)&(n!=coordonnee[1]):
                return False
                break
        for n in range(0,taille): # test ligne
            if(Matrice[n,coordonnee[1]]==element)&(n!=coordonnee[0]):
                return False
                break
        return True
    

def combinaison(total,domaine): #  Fonction " corps " du programme.
    liste_combinaison=[] # liste retournee.
    possibilite=[]
    var='element'
    liste_element=[]
    for nombre in range(0,len(domaine)): # creation de la combinaison pour addition, soustraction et division.
        chaine=str(nombre)
        liste_element.append(var+chaine)
        liste_element[nombre]=1
    for i in range(1,taille+1): # pour la fonction it.product.
        possibilite.append(i)
    if len(domaine)==1: # Dans ce cas il n'y a qu'une seule combinaison envisageable.
        liste_tuple=[total]
        tup=tuple(liste_tuple)
        liste_combinaison.append(tup)
        return liste_combinaison
    elif len(domaine)==2: # Si on peut faire une division ou une soustraction.

        tourne=True
        while tourne:
            element1=liste_element[0]
            element2=liste_element[1]

            if (element1/element2)==total: # Division
                solution1_div=(element1,element2)
                solution2_div=(element2,element1)
                if (test_ligne_colonne(domaine,solution1_div))&(solution1_div not in liste_combinaison):
                    liste_combinaison.append(solution1_div)
                if test_ligne_colonne(domaine,solution2_div)&(solution2_div not in liste_combinaison):
                    liste_combinaison.append(solution2_div)
            if (element1-element2)==total: # soustraction
                solution1_sous=(element1,element2)
                solution2_sous=(element2,element1)
                if (test_ligne_colonne(domaine,solution1_sous))&(solution1_sous not in liste_combinaison):
                    liste_combinaison.append(solution1_sous)
                if (test_ligne_colonne(domaine,solution2_sous))&(solution2_sous not in liste_combinaison):
                    liste_combinaison.append(solution2_sous)

            if liste_element[0]<taille: # Incrementation du 1er element.
                liste_element[0]+=1
            elif (liste_element[0]==taille)&(liste_element[1]<taille): # 2eme element.
                liste_element[0]=1
                liste_element[1]+=1
            else: # On a atteint le maximum, donc on sort du while.
                tourne=False

    # Multiplication.

    for combi_lineaire in it.product(possibilite,repeat=len(domaine)):
        produit_domaine=1
        for chiffre in combi_lineaire: # Produit de tous les chiffres de la combinaison.
            produit_domaine=produit_domaine*chiffre
        if produit_domaine==total:
            if (test_ligne_colonne(domaine,combi_lineaire))&(combi_lineaire not in liste_combinaison):
                liste_combinaison.append(combi_lineaire)

   # addition. Ca avance ..

    if taille*len(domaine)>=total: # L'addition est possible.
        for nombre in range(0,len(domaine)): # Creation de la combinaison.
            liste_element[nombre]=1 # Au cas cas où il y aurait eu une soustraction.

        somme=0
        while somme!=taille*len(domaine):
            somme=0 # Re-initialisation.
            for element in liste_element: # Verification.
                somme+=element
            if (somme==total): # Combinaison royale.

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

# On va maintenant creer et ordonner la liste pour la resolution.
def genese(liste):
    var='info_domaine'
    liste_info=[]
    for i in range(0,len(liste)):
        chaine=str(i)
        liste_info.append(var+chaine)
        liste_info[i]=(liste[i][1],combinaison(liste[i][0],liste[i][1])) # Coordonnee puis combinaison.
    liste_domaine_ordonnee=sorted(liste_info,key=lambda x:len(x[1]))
    return liste_domaine_ordonnee

liste_domaine_ordonnee=genese(liste_domaine)
print(liste_domaine_ordonnee)

# etape de la resolution.

def test_remplissage(domaine,combinaison,Matrice):
    matrice=Matrice.copy()
    for iteration in range(0,len(domaine)):
        matrice[domaine[iteration][0],domaine[iteration][1]]=combinaison[iteration]
    for element,coordonnee in zip(combinaison,domaine):

        # Tests respectifs des lignes et des colonnes.

        for n in range(0,taille):
            if (matrice[coordonnee[0],n]==element)&(n!=coordonnee[1]):
                return False
                break
        for n in range(0,taille):
            if(matrice[n,coordonnee[1]]==element)&(n!=coordonnee[0]):
                return False
                break

    return True

def fill_in(tuple_ordonne,indice,M): # Combinaison par combinaison.
    liste_parcours[indice]+=1
    liste_coordonnee=tuple_ordonne[0]
    liste_combinaison=tuple_ordonne[1]
    while liste_parcours[indice]<len(liste_combinaison): # Boucle tant qu'il y a toujours des combinaisons a essayer.
        if test_remplissage(liste_coordonnee,liste_combinaison[liste_parcours[indice]],M): # Si ça colle, on remplit.
            for iteration in range(0,len(liste_coordonnee)):
                M[liste_coordonnee[iteration][0],liste_coordonnee[iteration][1]]=liste_combinaison[liste_parcours[indice]][iteration]
            return True
        liste_parcours[indice]+=1
    liste_parcours[indice]=-1
    return False


def effacer_domaine(liste_coordonnee,M):
    for coordonnee in liste_coordonnee:
        M[coordonnee[0],coordonnee[1]]=0


liste_parcours=[]
debut = time.time()
def resolution(liste_domaine_ord):
    for iteration in range(0,len(liste_domaine_ord)):
        liste_parcours.append(-1) # -1 pour aucune combinaison.
    M=zeros((taille,taille),int)
    indice=0
    print("La grille est en cours de resolution ... Veuillez patienter. " )
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


result=resolution(liste_domaine_ordonnee)
print(result)
