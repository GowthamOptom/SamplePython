from tkinter import *

root = Tk()

root.geometry("500x300")

def getval():
    print("Saved")

Label(root, text="regestration form", font="ar 15 bold").grid(row=0,column=3)

name = Label(root, text="NAME").grid(row=1,column=1)
phonenumber = Label(root, text="PHONE NUMBER").grid(row=2,column=1)
email = Label(root, text="EMAIL").grid(row=3,column=1)

nameentry = Entry(root, textvariable=StringVar()).grid(row=1,column=3)
phonenumberentry = Entry(root, textvariable=IntVar()).grid(row=2,column=3)
emailentry = Entry(root, textvariable=StringVar()).grid(row=3,column=3)

checkbtn = Checkbutton(text="Remember me?", variable=IntVar()).grid(row=4,column=3)

Button(text="Submit", command=getval).grid(row=5,column=3)

root.mainloop()