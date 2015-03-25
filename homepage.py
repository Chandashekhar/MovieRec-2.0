from Tkinter import *
import rate


def homepage():
	top = Tk()
	top.geometry("450x300")
	top.resizable(0,0)

	greeting = Label(top, text = "Welcome!")
	greeting.pack(side = BOTTOM)
	greeting.place(x = "190", y = "70")


	buttonRate = Button(top, text = "Rate Movies", command = rate.rate)
	buttonRate.pack(side = BOTTOM)
	buttonRate.place(x = "80", y = "130")

	buttonHistory = Button(top, text = "Rating History")
	buttonHistory.pack(side = BOTTOM)
	buttonHistory.place(x = "180", y = "130")

	buttonRecomm = Button(top, text = "Recommended")
	buttonRecomm.pack(side = BOTTOM)
	buttonRecomm.place(x = "290", y = "130")




  	top.mainloop()


homepage()