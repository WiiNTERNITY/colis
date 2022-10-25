from math import dist
import math
from importlib.resources import path
from turtle import distance
from ast import literal_eval


# La saisi des points ce fait  sur la meme ligne et sur le modele suivant exemple : 48.6,12.5 44.84,-5.69 etc...

points = input(
    "entrer coordonnee comme suit x.01,y.02  x1.55,y1.63  etc ..,.. :").split()


points = [literal_eval(coord) for coord in points]

print(points)


def euclideanDistance(coordinate1, coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)


distances = []
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        distances += [euclideanDistance(points[i], points[j])]

print("nombre de points : ", len(distances))
print("poids entre noeud ", distances)
print("distance la plus courte ", min(distances))
print("itineraire: ", sorted(
    range(len(distances)), key=lambda k: distances[k]))

print("linterpretation de l itineraire considere le retour au point de depart  ")


# 0 50.63 3.07 # Lille
# 1 48.86 2.35 # Paris
# 2 44.84 -0.58 # Bordeaux
# 3 45.76 4.84 # Lyon
# 4 43.3 5.37 # Marseille
# 5 43.6 1.44 # Toulouse
