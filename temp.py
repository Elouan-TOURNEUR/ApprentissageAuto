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


############Déclaration###########
size = 500, 500
extension = "JPEG"


#######Fonctions##############
def decouperMot(mot):
    motretour = ""
    for lettre in mot:
        if (lettre == "."):
            return motretour
        else:
            motretour += lettre


############Programme############

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
        im.save(chemin)
        
        
        

            

            
        
