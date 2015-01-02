from tkinter import *
import goslate
import sys
#--------------------------------------------------------------
#Tkinter windows creation:
root = Tk()
root.geometry("500x300")
root.title("TransPy - Will Venn")
#--------------------------------------------------------------
#Functions:
def Translate_GB():
	s = Entry_1.get()
	gs = goslate.Goslate()
	translated = gs.translate(s, "gb")
	print (translated)

def Translate_FR():
	s = Entry_1.get()
	gs = goslate.Goslate()
	translated = gs.translate(s, "fr")
	print (translated)

def Translate_ES():
	s = Entry_1.get()
	gs = goslate.Goslate()
	translated = gs.translate(s, "es")
	print (translated)

def Translate_SV():
	s = Entry_1.get()
	gs = goslate.Goslate()
	translated = gs.translate(s, "sv")
	print (translated)
#--------------------------------------------------------------
#Labels:
Label_Intro = Label(root, text="Enter the text you would like to translate below")
Label_SupportedLang = Label(root, text="The supported languages are: ")

Label_ENG = Label(root, text="GB = English")
Label_FR = Label(root, text="FR = French")
Label_ES = Label(root, text="ES = Spanish")
Label_SV = Label(root, text="SV = Swedish")
#--------------------------------------------------------------
#Buttons:
Button_Submit_GB = Button(root, text="Translate to GB", bd=3, command=Translate_GB)
Button_Submit_FR = Button(root, text="Translate to FR", bd=3, command=Translate_FR)
Button_Submit_ES = Button(root, text="Translate_ES", bd=3, command=Translate_ES)
Button_Submit_SV = Button(root, text="Translate_SV", bd=3, command=Translate_SV)
#--------------------------------------------------------------
#Entry box:
Entry_1 = Entry(root)
Entry_1.delete(0, END)
Entry_1.insert(0, "Translate here: ")
##s = Entry_1.get()
#--------------------------------------------------------------
#Packings:
Label_Intro.pack()
Label_SupportedLang.pack()
Label_ENG.pack()
Label_FR.pack()
Label_ES.pack()
Label_SV.pack()
Entry_1.pack()
Button_Submit_GB.pack()
Button_Submit_FR.pack()
Button_Submit_ES.pack()
Button_Submit_SV.pack()
#--------------------------------------------------------------

#--------------------------------------------------------------
#Loops:
root.mainloop()
#--------------------------------------------------------------
