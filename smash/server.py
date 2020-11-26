import cherrypy
import random
import os
var = "ptdr t ki"

class MonSiteWeb(object):  # Classe maîtresse de l'application
    def index(self):  # Méthode invoquée comme URL racine (/)

        list_nbr = []

        if os.path.exists("data.txt"):
            with open("data.txt", "r+") as file:
                list_chara = file.readlines()
                for n in range(1, 78):
                    list_nbr.append(n)

                choice = random.choice(list_nbr)

            with open("skins.txt", "r+") as file:
                list_img = file.readlines()


        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SSBU Random</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>SSBU RANDOM CHOICE</h1>
    <p>Cliquez sur le boutton pour découvrir votre personnage !</p>
    <img src=''',list_img[choice],'''>
</body>
</html>'''
    index.exposed = True  # la méthode doit être ?publiée'

###### Programme principal : #############
cherrypy.quickstart(MonSiteWeb(), config="tutoriel.conf")