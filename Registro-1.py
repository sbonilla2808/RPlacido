from cProfile import label
from msilib.schema import CheckBox
from tkinter import*
from tokenize import String
#####
root = Tk()
root.geometry("400x400")
#####

def getvals():
    print("Accepted")

#Heading
Label(root, text="Ventana de Registro", font="ar 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="name")
phone = Label(root, text="phone")

#Packing Fields
name.grid(row=4, column=2)
phone.grid(row=5, column=2)

#Variable for storing data
namevalue = StringVar
phonevalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)

#This is a whiteWindow
nameentry.grid(row=4, column=3)
phoneentry.grid(row=5, column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=7, column= 3)

#Submit button
Button(text="Aceptar", command=getvals).grid(row=8, column= 3)

root.mainloop()




