from tkinter import *

ws = Tk()
ws.title('Email System')
ws.geometry('940x500')
ws.config(bg='#f7ef38')

variable = StringVar()
gender = ('Male', 'Female', 'Other')
variable.set(gender[0])

# widgets

right_frame = Frame(ws, bd=2, relief=SOLID, padx=10, pady=10)

Label(right_frame, text="Enter Name", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
Label(right_frame, text="Enter Email", font=('Times', 14)).grid(row=1, column=0, sticky=W, pady=10)
Label(right_frame, text="Enter Mobile", font=('Times', 14)).grid(row=2, column=0, sticky=W, pady=10)
Label(right_frame, text="Enter Age", font=('Times', 14)).grid(row=3, column=0, sticky=W, pady=10)
Label(right_frame, text="Select Gender", font=('Times', 14)).grid(row=4, column=0, sticky=W, pady=10)
Label(right_frame, text="Enter Password", font=('Times', 14)).grid(row=5, column=0, sticky=W, pady=10)
Label(right_frame, text="Re-Enter Password", font=('Times', 14)).grid(row=6, column=0, sticky=W, pady=10)


reg_na = Entry(right_frame, font=('Times', 14))
reg_em = Entry(right_frame, font=('Times', 14))
reg_mo = Entry(right_frame, font=('Times', 14))
reg_ag = Entry(right_frame, font=('Times', 14))
reg_ge = OptionMenu(right_frame, variable, *gender)
reg_ge.config(width=10, font=('Times', 14))
reg_pw = Entry(right_frame, font=('Times', 14))
re_pw = Entry(right_frame, font=('Times', 14))

reg_btn = Button(right_frame, width=15, text='Register', font=('Times', 14), command=None)

# widgets placement



reg_na.grid(row=0, column=1, pady=10, padx=20)
reg_em.grid(row=1, column=1, pady=10, padx=20) 
reg_mo.grid(row=2, column=1, pady=10, padx=20)
reg_ag.grid(row=3, column=1, pady=10, padx=20)
reg_ge.grid(row=4, column=1, pady=10, padx=20)
reg_pw.grid(row=5, column=1, pady=10, padx=20)
re_pw.grid(row=6, column=1, pady=10, padx=20)
reg_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)

# infinite loop
ws.mainloop()