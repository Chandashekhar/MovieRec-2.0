from Tkinter import *
import tkMessageBox
import csv

'''register'''

def callRegister():
    '''
    prompts new user to register

    asks username, age, sex, occupation and passcode from user 
    
    '''

    top = Tk()

    top.geometry("300x300")

    L1 = Label(top, text = "Username")
    L1.pack(side = LEFT)
    L1.place(x = "20", y = "20")
    username = Entry(top, bd =5)
    username.pack(side = RIGHT)
    username.place(x = "150", y = "20")

    L2 = Label(top, text = "Age")
    L2.pack(side = LEFT)
    L2.place(x = "20", y = "60")
    age = Entry(top, bd =5)
    age.pack(side = RIGHT)
    age.place(x = "150", y = "60")

    L3 = Label(top, text = "Sex")
    L3.pack(side = LEFT)
    L3.place(x = "20", y = "100")
    sex = Entry(top, bd =5)
    sex.pack(side = RIGHT)
    sex.place(x = "150", y = "100")

    L4 = Label(top, text = "Occupation")
    L4.pack(side = LEFT)
    L4.place(x = "20", y = "140")
    job = Entry(top, bd =5)
    job.pack(side = RIGHT)
    job.place(x = "150", y = "140")

    L5 = Label(top, text = "Passcode")
    L5.pack(side = LEFT)
    L5.place(x = "20", y = "180")
    passcode = Entry(top, bd =5, show = "*")
    passcode.pack(side = RIGHT)
    passcode.place(x = "150", y = "180")

    L6 = Label(top, text = "Confirm Passcode")
    L6.pack(side = LEFT)
    L6.place(x = "20", y = "220")
    confirmPasscode = Entry(top, bd =5, show = "*")
    confirmPasscode.pack(side = RIGHT)
    confirmPasscode.place(x = "150", y = "220")

    def getData():
        '''
        reads username, age, sex, occupation and passcode from user 
        reads userID from UserID.txt
        writes userID + 1 into UserID.txt
        writes userID, username, age, sex, occupation and passcode into registration.csv
        
        '''
        gUsername = username.get()
        gAge = age.get()
        gSex = sex.get()
        gJob = job.get()
        gPasscode = passcode.get()
        gConfirmPasscode = confirmPasscode.get()
        if gPasscode == gConfirmPasscode:

            f = open("UserID.txt", "r")
            gUserID = int(f.read())
            gUserID = gUserID + 1
            f = open("UserID.txt", "w")
            f.write(str(gUserID))

            with open('registration.csv', 'ab') as csvfile:
                    dataWriter = csv.writer(csvfile, delimiter=',')     
                    dataWriter.writerow([gUserID] + [gUsername] + [gAge] + [gSex] + [gJob] + [gPasscode])
            top.destroy()
            
        else:
            tkMessageBox.showinfo("Error!", "Passwords don't match!")


    register = Button(top, text = "Register", command = getData)
    register.pack(side = BOTTOM)
    register.place(x = "145", y = "260")

    top.mainloop()


