from Tkinter import *
import csv
import time
import tkMessageBox

'''rating module'''

def rate():

    top = Tk()

    top.geometry("400x400" )

    title = Label(top, text = "\t\t\tRate Movies")
    title.pack(side = LEFT)
    title.place(x = "20", y = "20")

    movieName = Label(top, text = "Movie")
    movieName.pack(side = LEFT)
    movieName.place(x = "20", y = "80")

    m = Entry(top, bd =5)
    m.pack(side = LEFT)
    m.place(x = "80", y = "80")

    def select():

        flag = 0
        movie = m.get()
        timestamp = time.time()
        rating = var.get()
        fl = open("currentUserID.txt", "r")
        userID = int(fl.read())
        
        
        
        with open('movies.csv' , 'rb') as csvfile:
            dataReader = csv.reader(csvfile, delimiter = ',')
            for row in dataReader:
                if row[1] == movie:
                    movieID = row[0]
                    flag = 1

            if flag == 0:
                tkMessageBox.showinfo('Not Found', 'Movie not found. Please try again.')
         
            

            with open('rate.csv', 'ab') as csvfile:
                        dataWriter = csv.writer(csvfile, delimiter=',')     
                        dataWriter.writerow([userID] + [movieID] + [rating] + [timestamp])    

                
    var = IntVar()

    R1 = Radiobutton(top, text="1", variable=var, value=1)
    R1.pack( anchor = W )
    R1.place(x = "20", y = "120")

    R2 = Radiobutton(top, text="2", variable=var, value=2)
    R2.pack( anchor = W )
    R2.place(x = "80", y = "120")

    R3 = Radiobutton(top, text="3", variable=var, value=3)
    R3.pack( anchor = W)
    R3.place(x = "140", y = "120")

    R4 = Radiobutton(top, text="4", variable=var, value=4)
    R4.pack( anchor = W )
    R4.place(x = "200", y = "120")

    R5 = Radiobutton(top, text="5", variable=var, value=5)
    R5.pack( anchor = W )
    R5.place(x = "260", y = "120")

    save = Button(top, text = "Save", command = select)
    save.pack(side = BOTTOM)
    save.place(x = "150", y = "200")

    label = Label(top)
    label.pack()
    top.mainloop()


