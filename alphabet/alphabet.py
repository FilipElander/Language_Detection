#klass för alphabete

class alphabet(object):

    def __init__(self):
        self.alphabet_i2w = {}
        self.alphabet_w2i = {}

    def alphabetBuilder(self):    # bygger en dictionary i en klass med alphabetet
        with open('alphabet/alphabet.txt','r') as v:
            for i in v.readlines():
                i = i.split()
                self.alphabet_i2w[i[0]] = i[1]
                self.alphabet_w2i[i[1]] = i[0]
