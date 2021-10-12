
from tkinter import *


###################### ENGINES ################
from Engines import LanguageLablerBigram
from Engines import LanguageLablerReg


# ansnätter roten
root = Tk()
root.title("Language Detection")
root.geometry("500x300")

#entering data
e = Entry(root,width=50)
e.grid(row=0,column=0,columnspan=2)

#funktion för Bigram
def bigram():
    mylabel2 = Label(root,text="mest sannolikt" + " " +LanguageLablerBigram.main(e.get()))
    mylabel2.grid(row=2,column=0,columnspan=2)
#funktion för regression
def regression():
    mylabel2 = Label(root,text="mest sannolikt" + " " +LanguageLablerReg.main(e.get()))
    mylabel2.grid(row=2,column=0,columnspan=2)
#knapp 1
mybutton = Button(root,text="Bigram",command = bigram,padx = 50,pady =25)
mybutton.grid(row=1,column=0)
#knapp2
mybutton2 = Button(root,text="Regressed",command=regression,padx =50,pady=25)
mybutton2.grid(row=1,column=1)

#loopen
root.mainloop()
