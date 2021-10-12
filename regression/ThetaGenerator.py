# kod för regression på svenska
from sklearn.model_selection import train_test_split
import nltk
import re
#import random
import math
import numpy as np


# ------------------------- OPTIONS -------------------------------------
SPANISH = 'train/train_spanish.txt'
ENGLISH = 'train/train_english.txt'
FRENCH = 'train/train_french.txt'
GERMAN = 'train/train_german.txt'
SWEDISH= 'train/train_swedish.txt'

# insert one of the options
Language_to_train = SPANISH


#------------------------------------------------------------------------------
class BinaryLogisticRegression(object):

    def __init__(self, x=None, y=None):
        self.number_of_func = 4
        self.theta = np.random.uniform(-1, 1, self.number_of_func)
        x_tr, y_tr, x_val, y_val = self.train_val_split(np.array(x), np.array(y))
        self.xtrain = x_tr
        self.ytrain = y_tr
        self.xval = x_val
        self.yval= y_val
        self.alpha = 0.6
        self.gradient = np.zeros(self.number_of_func)
#------------------------------------------------------------------------------
    def train_val_split(self, x, y):
        xtr,xval,ytr,yval = train_test_split(x,y,test_size=0.1)
        return xtr, ytr, xval, yval
#------------------------------------------------------------------------------
    def sigmoid(self, z):
        return 1.0 / ( 1 + math.exp(-z) )


    def X(self,func,text):
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
        if func == 3: #kryliska
            match = re.search(r"'",text)
            if match != None:
                x = 1
            else:
                x = 0
        return x

#------------------------------------------------------------------------------
    def fit(self):
        i = 0
        for i in range(100000):
            i +=1
            sum = 0
            for k in range(self.number_of_func):
                x_sigH_Y_sum = 0
                for ord in range(len(self.xtrain)):
                    thetaTX = self.theta[0]*self.X(0,self.xtrain[ord]) + self.theta[1]*self.X(1,self.xtrain[ord]) + self.theta[2]*self.X(2,self.xtrain[ord])+self.theta[3]*self.X(3,self.xtrain[ord])
                    x_sigH_Y_it = self.X(k,self.xtrain[ord])*(self.sigmoid(thetaTX) - float(self.ytrain[ord]))
                    x_sigH_Y_sum = x_sigH_Y_sum + x_sigH_Y_it
                self.gradient[k] = x_sigH_Y_sum/len(self.xtrain)

            for k in range(self.number_of_func):
                self.theta[k] = self.theta[k] - self.alpha * self.gradient[k]
            #loss = self.loss()

            if i%100 == 0:
                print(self.theta)
                #print(loss)



#------------------------------------------------------------------------------

    def loss(self):
        x = self.xtrain
        y = self.ytrain
        sum = 0
        for m in range(len(self.xtrain)):
            thetaTX = self.theta[0]*self.X(0,self.xtrain[m]) + self.theta[1]*self.X(1,self.xtrain[m]) + self.theta[2]*self.X(2,self.xtrain[m])+self.theta[3]*self.X(3,self.xtrain[m])
            loss_per_it = -int(y[m])*np.log(self.sigmoid(thetaTX))-(1-int(y[m]))*np.log(1-self.sigmoid(thetaTX))
            sum = sum + loss_per_it
            res = sum/len(self.xtrain)
        return res
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
def main():
    x = []
    y = []
    with open(Language_to_train,'r') as f:
        for i in f.readlines():
            rad = nltk.word_tokenize(i)
            x.append(rad[0])
            y.append(rad[1])

    b = BinaryLogisticRegression(x, y)
    b.fit()


if __name__ == '__main__':
    main()
