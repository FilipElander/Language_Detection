# Gör Binärklassificieringen enligt bigram för interface programmmet
# language labeler.

from alphabet.alphabet import alphabet
from bigram.Bigram import Bigram
from collections import defaultdict
import math


class Detection(object):

    def __init__(self,I2W,W2I):
        self.Lexikon = defaultdict(lambda:defaultdict(lambda: defaultdict()))
        self.antal_alphabet = 0
        self.sannolikhheter = []
        self.ind_2_word = I2W
        self.word_2_ind = W2I
        self.LanguageName = {}
        self.vikt = math.log(0.001)



    def Alfabeten(self,sprak_modellen,namn): # bygger en 4D dic med alphabeten
        self.Lexikon[self.antal_alphabet] = sprak_modellen
        self.LanguageName[self.antal_alphabet] = namn
        self.antal_alphabet +=1



    def Process(self,letters):
        letters = list(letters)
        # initierar den första sannolikhter (alltid start till första bokstaven)
        for i in range(self.antal_alphabet):
            try:
                P = float(self.Lexikon[i][self.word_2_ind['space']][self.word_2_ind[letters[0]]])
                self.sannolikhheter.append(P)
            except:
                P = self.vikt
                self.sannolikhheter.append(P)


        # fortsätter på bokstav 2 i in-argumentet
        prew = letters[0]
        for token_index in range(1,len(letters)):
            bokstav = letters[token_index]
            for sprak_index in range(len(self.Lexikon)): #går igenom varje språk
                try:
                    P = float(self.Lexikon[sprak_index][self.word_2_ind[prew]][self.word_2_ind[bokstav]])
                    self.sannolikhheter[sprak_index] =  self.sannolikhheter[sprak_index] + P

                except:

                    P = self.vikt
                    self.sannolikhheter[sprak_index] =  self.sannolikhheter[sprak_index] + P


            prew = bokstav
        res = []
        for row in self.sannolikhheter:
            res.append(math.exp(row))

        #print(res)
        res_language = res.index(max(res))
        res_sannolikhet = res[res_language]
        print("Texten är med störst sannolikhet skriven på {}".format(self.LanguageName[res_language]))
        return self.LanguageName[res_language]



def main(In_arg):

    alfabetet = alphabet()
    alfabetet.alphabetBuilder()

    detection = Detection(alfabetet.alphabet_i2w,alfabetet.alphabet_w2i)


    #------- Svenska ------------#
    Svenska = Bigram('bigram/models/swedish_bigrams.txt')
    Svenska.BigramBuilder()
    SWE = Svenska.Bigram
    detection.Alfabeten(SWE,'Svenska')
    #------------------------#
    #------- Engelska ------------#
    Engelska = Bigram('bigram/models/english_bigrams.txt')
    Engelska.BigramBuilder()
    ENG = Engelska.Bigram
    detection.Alfabeten(ENG,'Engelska')
    #------------------------#
    #------- Spanska ------------#
    Spanska = Bigram('bigram/models/spanish_bigrams.txt')
    Spanska.BigramBuilder()
    SPE = Spanska.Bigram
    detection.Alfabeten(SPE,'Spanska')
    #------------------------#
    #------- Tyska ------------#
    Tyska = Bigram('bigram/models/german_bigrams.txt')
    Tyska.BigramBuilder()
    GER = Tyska.Bigram
    detection.Alfabeten(GER,'Tyska')
    #------------------------#
    #------- Franska ------------#
    Franska = Bigram('bigram/models/french_bigrams.txt')
    Franska.BigramBuilder()
    FRA = Franska.Bigram
    detection.Alfabeten(FRA,'Franska')
    #------------------------#
    #------- Ryska ------------#
    Ryska = Bigram('bigram/models/russian_bigrams.txt')
    Ryska.BigramBuilder()
    RUS = Ryska.Bigram
    detection.Alfabeten(RUS,'Ryska')
    #------------------------#


    return detection.Process(In_arg)

if __name__ == "__main__":
    main()
