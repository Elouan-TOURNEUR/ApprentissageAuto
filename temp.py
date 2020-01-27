# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
"""
from PIL import Image
import os, sys

size = 500, 500
im = Image.open('Data/Mer/cali65d.jpeg')
im.thumbnail(size, Image.ANTIALIAS)
im.save('Test/test.jpeg')
print ("test")
"""



from PIL import Image
import os, sys
import numpy as np



############Déclaration###########
size = 700, 500
extension = "JPEG"


#######Fonctions##############
def decouperMot(mot):
    motretour = ""
    for lettre in mot:
        if (lettre == "."):
            return motretour
        else:
            motretour += lettre
"""
def recupererImages():
    données = 0
    for infile in os.listdir('./Data/images/'):
        données += infile
    return données
"""
def recupererMatriceImage():
    données = []  
    for infile in os.listdir('./Data/images/'):
        nom = "./Data/images/" + infile
        img = Image.open(nom)
        matrice = np.array(img)
        matrice.flatten()
        données.append(matrice)
    return données
        
def labelliser():
    tableau = []
    for infile in os.listdir('./Data/images/'):
        tableau.append(reconnaitreMot(infile))
    return tableau
        
def reconnaitreMot(mot):
    if ((mot[len(mot)-5]) == 'r'):
        return 1
    else:
        return 0
############Programme############



############Code borne sup dimension#############
"""
compteur = "0"
for infile in os.listdir('./Data/Mer'):
    compteur += "1"
    debut = 'Data/Mer/'
    outfile = decouperMot(infile)
    outfile += "test"
    nom = debut + infile
    #outfile = compteur
    #print (outfile)
    outfile += ".jpeg"
    if nom != outfile:
        #print(nom)
        #print (outfile)
        
        im = Image.open(nom)
        im.thumbnail(size, Image.ANTIALIAS)
        chemin = 'Test/' + outfile
        im.save(chemin)données
"""


##########Code image carrée#############
"""
import PIL
from PIL import Image
import numpy as np


for infile in os.listdir('./Data/Mer'):
    compteur += "1"
    debut = 'Data/Mer/'
    outfile = decouperMot(infile)
    outfile += "mer"
    nom = debut + infile
    outfile += ".jpg"
    if nom != outfile:
        #print(nom)
        #print (outfile)
        img = Image.open(nom)
        img = img.convert("RGB")
        img = img.resize((300, 300), PIL.Image.ANTIALIAS)
        #matrice = np.array(img)
        #print(matrice)
        #im.thumbnail(size, Image.ANTIALIAS)
        chemin = 'Data/images/' + outfile
        img.save(chemin)
   


im = Image.open('Data/Mer/cuir-noir-blanc-les-georgettes.jpg')
im = im.resize((300, 300), PIL.Image.ANTIALIAS)
matrice = np.array(im)
im.save('Test/test.jpeg')
print(matrice)
"""


#donnees = recupererImages()
X = np.array(recupererMatriceImage())
y = np.array(labelliser())
print (type(y))

#print (y)
#print (X)
from sklearn.model_selection import train_test_split
X_train, X_test , y_train, y_test = train_test_split(X,y,test_size=0.20)

from sklearn.naive_bayes import GaussianNB
classifieur = GaussianNB()

classifieur.fit(X_train, y_train)
y_predits= classifieur.predict(X_test)

from sklearn.metrics import accuracy_score
print("Taux de reussite:", accuracy_score(y_test, y_predits))

          
    