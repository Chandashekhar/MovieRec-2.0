from Tkinter import *
import tkMessageBox
import time
import csv
import os
import operator
import recommender

def recom():
	root = Tk()
	root.geometry("500x500")
	root.resizable(0,0)

	L = Label(root, text = "\t\t\tRecommended Movies")
	L.pack(side = BOTTOM)
	L.place(x = "20", y = "20")

	T = Text(root, height= 25, width=50)
	T.pack()
	T.place(x = '45', y = '50')
	T.insert(END, "S.No\t\tMovie\n\t")

	recommender.collabf()
	i = 1
	

	with open('moviereco.csv' , 'rb') as csvfile:
		dataReader = csv.reader(csvfile, delimiter = ',')
			
			
		for row in dataReader:
				
					
			s = str(i) + "\t"
					
			T.insert(END, "\n\n")
			T.insert(END, s)
			T.insert(END, row[0])

			i = i + 1





	os.remove('moviereco.csv')
	mainloop()




