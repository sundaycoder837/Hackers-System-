from tkinter import*
root = Tk()

root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading

Label(root,text="Hacker Competion form", font="arial 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="name")
phone = Label(root, text="phone")
gender= Label(root, text="Gender")
emergency= Label(root, text="Emergency")
paymentmood= Label(root, text="Payment Mood")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variable for storing data

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar

checkvalue = IntVar

#Creating entry fields
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)
emergencyentry = Entry(root, textvariable =emergencyvalue)

#Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#Submitt Button 
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
