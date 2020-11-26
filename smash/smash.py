import random
import os
import cherrypy


if os.path.exists("data.txt"):
    with open("data.txt", "r+") as file:
        list = file.readlines()
        choice = random.choice(list)


    for color in range(1, 9):
        list_color.append(color)
        skin = random.choice(list_color)
    print("Tu vas jouer", choice, "avec le", skin, "ème skin !")
