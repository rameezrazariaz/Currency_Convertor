#import datetime module
import datetime
from tkinter import *
from tkinter import messagebox

def convertCurrency():
    inr=float(inputfield.get())
    usd.set(0.014*inr)
    aed.set(0.052*inr)
    gbp.set(0.011*inr)
    eur.set(0.013*inr)


#default window size
HEIGHT = 400
WIDTH = 600

#init the tkinter
root = Tk()
root.title("Currency Converter")

canvas=Canvas(root,width = WIDTH, height = HEIGHT)
canvas.pack()

#setup frontend
#set frame
frame = Frame(root,bg="#ececec")
frame.place(relheight=1,relwidth=1,relx=0,rely=0)
#set heading
headingLabel = Label(frame,text="Currency Converter",bg="#ececec",fg="#000000",font='DecoType 24')
headingLabel.pack(fill = X, expand =False, ipady = 18)
#input label
inputLabel = Label(frame,text="Enter amount in INR:",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel.place(relheight=.05,relwidth=.55,relx=.035,rely=.2)

inputLabel1 = Label(frame,text="Amount in  USD:",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel1.place(relheight=.05,relwidth=.55,relx=.01,rely=.33)

inputLabel2 = Label(frame,text="Amount in  AED:",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel2.place(relheight=.05,relwidth=.55,relx=.01,rely=.45)

inputLabel3 = Label(frame,text="Amount in  GBP:",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel3.place(relheight=.05,relwidth=.55,relx=.01,rely=.57)

inputLabel4 = Label(frame,text="Amount in  EUR:",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel4.place(relheight=.05,relwidth=.55,relx=.01,rely=.69)

#calculate button
calculateButton = Button(frame,text="Convert",font = 'AppleGothic 16',bg="#ffffff",fg="red",activebackground="#ffffff",command=convertCurrency)
calculateButton.place(relheight=.12,relwidth=.25,relx=.375,rely=.80)

#inputfield
inputfield = StringVar()
myInput = Entry(frame,font = 'AppleGothic 16 italic',textvariable = inputfield,bg="#fcfcfc",fg="#000000")
myInput.place(relheight = .10,relwidth=.30,relx=.52,rely=.18)

usd= StringVar()
usdOutput = Label(frame,font = 'AppleGothic 16 italic',textvariable = usd,bg="#fcfcfc",fg="#000000")
usdOutput.place(relheight = .10,relwidth=.30,relx=.52,rely=.305)

aed = StringVar()
aedOutput = Label(frame,font = 'AppleGothic 16 italic',textvariable = aed,bg="#fcfcfc",fg="#000000")
aedOutput.place(relheight = .10,relwidth=.30,relx=.52,rely=.43)

gbp = StringVar()
gbpOutput = Label(frame,font = 'AppleGothic 16 italic',textvariable = gbp,bg="#fcfcfc",fg="#000000")
gbpOutput.place(relheight = .10,relwidth=.30,relx=.52,rely=.55)

eur = StringVar()
eurOutput = Label(frame,font = 'AppleGothic 16 italic',textvariable = eur,bg="#fcfcfc",fg="#000000")
eurOutput.place(relheight = .10,relwidth=.30,relx=.52,rely=.67)


root.mainloop()