
from collections import defaultdict

class Bigram(object):
    def __init__(self,model):
        self.Bigram = defaultdict(lambda: defaultdict())
        self.LanguageModel = model

    def BigramBuilder(self):    # bygger en klass för bigramet
        with open(self.LanguageModel,'r') as t:
            for i in t.readlines():
                i = i.split()
                self.Bigram[i[0]][i[1]]= i[2]
