# Gör Binärklassificieringen enligt reggresed modell för interface-programmmet
# language labeler.

from alphabet import alphabet
#from bigram_classes.Bigram import Bigram
#import argparse
#import sys
import re
from collections import defaultdict
import math
import numpy as np
import operator

def X(func,text):
    #dummy
    if func == 0:
        x = 1
    #f1
    if func == 1:
        match = re.search(r'(\w)\1+',text)
        if match != None:
            x = 1
        else:
            x = 0
    #f2
    if func == 2:
        match = re.search(r'[^a-zA-Z]',text)
        if match != None:
            x = 1
        else:
            x = 0
    # f3
    if func == 3:
        match = re.search(r"'",text)
        if match != None:
            x = 1
        else:
            x = 0
    #f5
    if func == 4:
        match = re.search(r"[å|ä|ö]",text)
        if match != None:
            x = 1
        else:
            x = 0
    #f6
    if func == 5:
        match = re.search(r"[\u0400-\u04FF]",text)
        if match != None:
            x = 1
        else:
            x = 0
    #f6
    if func == 6:
        match = re.search(r"[ß|β]",text)
        if match != None:
            x = 1
        else:
            x = 0
    return x

def main(In_arg):
    modeller = {}
    modeller['Svenska'] = [ 0.14601027, 0.93009565,  0.82639244, -0.03092643, 1000, 0, 0]
    modeller['Engelska'] = [ 0.92969424 ,-0.58307614, -4.59818166,  0.19541981, 0,0,0]
    modeller['Tyska'] = [1.07453223,  0.33104029, -1.05536525 , 0.26345996,0,0,1000]
    modeller['Spanska'] = [ 0.45493518, -0.83723368,  0.722144,   -0.8934274,0,0,0 ]
    modeller['Franska'] = [ 0.79979773, -0.48735955,  0.32604579,  0.22527257,0,0,0]
    modeller['Ryska'] = [ 0.01, 0.1,  0.01, 0.01,0,1000,0]


    res = []
    for i in range(7): # antal funktioner
        holder = X(i,In_arg)
        res.append(holder)
    sannolikheter = {}
    for language in ["Svenska","Engelska","Tyska","Spanska","Franska","Ryska"]:
        P = modeller[language][0]*res[0] + modeller[language][1]*res[1] + modeller[language][2]*res[2] +modeller[language][3]*res[3]+modeller[language][4]*res[4]+modeller[language][5]*res[5]+modeller[language][6]*res[6]
        sannolikheter[language] = P

    Keymax = max(sannolikheter, key=sannolikheter.get)
    return Keymax

if __name__ == "__main__":
    main()
