import rate
import register
from Tkinter import *
import tkMessageBox
import csv

'''login'''

top = Tk()

top.geometry("250x250")

def validate():
	'''
	searches for the username and if found, validates username passcode.

	updates currentUserID.txt with current userID. 
	'''
	currentUsername = loginUsername.get()
	currentPasscode = loginPasscode.get()
	with open('registration.csv' , 'rb') as csvfile:
		dataReader = csv.reader(csvfile, delimiter = ',')
		for row in dataReader:
			if row[1] == currentUsername:

				currentUserID = row[0]
				f = open("currentUserID.txt", "w")
				f.write(str(currentUserID))
				f.close()


				if row[5] != currentPasscode:
					tkMessageBox.showinfo("Error!", "Username and Passcode don't match!")
                else:
 
                    top.destroy()
                    rate.rate()
                    

L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
L1.place(x=20,y=20)

L2 = Label(top, text = "Passcode")
L2.pack( side = LEFT)
L2.place(x=20,y=60)

loginUsername = Entry(top, bd =5)
loginUsername.pack(side = RIGHT)
loginUsername.place(x=100,y=20)

loginPasscode = Entry(top, show = "*", bd=5)
loginPasscode.pack(side = RIGHT)
loginPasscode.place(x=100,y=60)

sign_in = Button(top, text = "Sign In", command = validate)
sign_in.pack(side = BOTTOM)
sign_in.place(x=65,y=140)

regis = Button(top, text = "Register", command = register.callRegister)
regis.pack(side = BOTTOM)
regis.place(x=145,y=140)

top.mainloop()
