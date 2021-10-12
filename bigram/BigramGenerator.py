
# Kod för att skriva en txt-fil med givet textsdokuments bigram sanolikheter
# det krävs att man har klassen för alphabetet!

# in arg -f "filnamnet.txt" som inehåller träningscorpus"
# ut arg -d "filnamnet.txt " som skall inehålla bigram sannolikheterna

from alphabet import alphabet
import argparse
import sys
import re
from collections import defaultdict
import math
parser = argparse.ArgumentParser(description='UnigramBuilder')
parser.add_argument('--file', '-f', type=str,  required=True, help='textfil')
parser.add_argument('--destination', '-d', type=str, help='sparad textfil')
argument = parser.parse_args()


#----------------- Bygger unigram ocg bigra COUNTER ---------------------------
alphabet = alphabet()
alphabet.alphabetBuilder()
index_2_bokstav = alphabet.alphabet_i2w
bokstav_2_index = alphabet.alphabet_w2i
unigram_count = {}
bigram_count = defaultdict(lambda: defaultdict(int))




for i in range(len(bokstav_2_index)+1):
    unigram_count[i] = 0

with open(argument.file, 'r') as t:
    text =t.read()
    text= re.sub(r'[\n]','',text)
    text = list(text)
    prev_alphabet_index = int(bokstav_2_index['space'])
    for bokstav in text:
        if bokstav == ' ':
            alphabet_index = int(bokstav_2_index['space'])
        else:
            alphabet_index = int(bokstav_2_index[bokstav])
        unigram_count[alphabet_index] += 1

        try:
            bigram_count[prev_alphabet_index][alphabet_index] += 1
        except KeyError:
            bigram_count[prev_alphabet_index][alphabet_index] = 1
        prev_alphabet_index = alphabet_index


# ----------------------- Skriver en fil med BigramProbs---------------------------------------

with open(argument.destination,'w') as w:
    for first_ord in bigram_count:
        for secound_ord in bigram_count[first_ord]:
            p =format(math.log(bigram_count[first_ord][secound_ord] / unigram_count[first_ord]),'.15f')
            line = "{} {} {}\n".format(first_ord,secound_ord,p)
            w.write(line)
