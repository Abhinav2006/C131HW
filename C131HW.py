import pandas as pd
import csv

df = pd.read_csv('allstars.csv')
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()

gravity = []

def gravityformula(mass, radius):
    G = 6.674e-11
    for i in range(0, len(mass)):
        g = (mass[i]*G)/((radius[i])**2)
        gravity.append(g)

gravityformula(mass, radius)

df["gravity"] = gravity
df.to_csv("starswithgravity.csv")