from Tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)

L2 = Label(top, text = "Passcode")
L2.pack( side = LEFT)

E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

E2 = Entry(top, show = "*", bd=5)
E2.pack(side = RIGHT)

sign_in = Button(top, text = "Sign In")
sign_in.pack(side = BOTTOM)

top.mainloop()