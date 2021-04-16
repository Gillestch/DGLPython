# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:42:34 2021

@author: Gilles
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
import unicodedata # pour enlever les accents

with open('E:\AI\jours\jour3\data.txt', "r") as filin:
    ch = filin.read()
#print(ch)

nbLettres = len(ch)
tabLettreNb = []
i = 0

for lettre in "abcdefghijklmnopqrstuvwxyz" :
    i = i + 1 # i ne sert pas en fait
    #print (lettre)
    #print(lettre.upper())
    lettreMaj = lettre.upper()
    tabLettreNb.append( 100*len(re.findall("(["+lettre+lettreMaj+"]+)",ch))/nbLettres )
    
print(tabLettreNb)







lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
X = list(range(26))
Y = tabLettreNb

"""
N = 5
menMeans = (20, 35, 30, 35, -27)
womenMeans = (25, 32, 34, 20, -25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

#Stacked bar plot with error bars

fig, ax = plt.subplots()

p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
p2 = ax.bar(ind, womenMeans, width,
            bottom=menMeans, yerr=womenStd, label='Women')

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()

# Label with label_type 'center' instead of the default 'edge'
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p2)

plt.show()


# Fixing random state for reproducibility
np.random.seed(19680801)

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()
"""
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.bar(lettres, tabLettreNb)  # Plot some data on the axes.

"""

#plt.bar(X,Y,tick_label=lettres)
#plt.show()
x = [1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]
plt.bar(x, range = (0, 5), bins = 5, color = 'yellow',
            edgecolor = 'red', density = True, hatch = 'x',
            orientation = 'horizontal', rwidth = 0.8, log = True)
plt.ylabel('valeurs')
plt.xlabel('frequences')
plt.title('Histogramme horizontal')

"""