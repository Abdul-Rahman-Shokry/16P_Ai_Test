from tkinter import *

myframe = Tk()

#global edits
myframe.title('Personality Test')
myframe.geometry("1400x670")
myframe.resizable(False,False)
myframe.configure(bg="lightblue")

# define a grid
myframe.columnconfigure(0, weight=1)
myframe.columnconfigure(1, weight=1)
myframe.columnconfigure(2, weight=1)
myframe.columnconfigure(3, weight=1)
myframe.columnconfigure(4, weight=1)
myframe.rowconfigure(0, weight=1)
myframe.rowconfigure(1, weight=1)
myframe.rowconfigure(2, weight=1)
myframe.rowconfigure(3, weight=1)
myframe.rowconfigure(4, weight=1)
myframe.rowconfigure(5, weight=1)
myframe.rowconfigure(6, weight=1)
myframe.rowconfigure(7, weight=1)
myframe.rowconfigure(8, weight=1)
myframe.rowconfigure(9, weight=1)
# main label
mainLBL = Label(myframe, text="Welcome to 16 Personality Test",
                font="Tahoma 30 bold", fg="black")
mainLBL.grid(row=0, column=0, columnspan = 5 , sticky='ew' , padx = 50)

# --- q 1 ---
# lbl
lbl_q1 = Label(myframe, text = '1) Making new friends regularly',font="Tahoma 12")
lbl_q1.grid(row=1, column=0, sticky='w')
# txt
txt_q1 = Entry(myframe)
txt_q1.grid(row=2, column=0 , sticky='wn', padx=10)

# --- q 2 ---
# lbl
lbl_q2 = Label(myframe, text = '2) Exploring random topics in free time',font="Tahoma 12")
lbl_q2.grid(row=3, column=0, sticky='w')
# txt
txt_q2 = Entry(myframe)
txt_q2.grid(row=4, column=0 , sticky='wn', padx=10)

# --- q 3 ---
# lbl
lbl_q3 = Label(myframe, text = '3) Empathizing easily when others cry',font="Tahoma 12")
lbl_q3.grid(row=5, column=0, sticky='w')
# txt
txt_q3 = Entry(myframe)
txt_q3.grid(row=6, column=0 , sticky='wn', padx=10)

# --- q 4 ---
# lbl
lbl_q4 = Label(myframe, text = '4) Planning backups for backups',font="Tahoma 12")
lbl_q4.grid(row=7, column=0, sticky='w')
# txt
txt_q4 = Entry(myframe)
txt_q4.grid(row=8, column=0 , sticky='wn', padx=10)

# --- q 5 ---
# lbl
lbl_q5 = Label(myframe, text = '5) Staying calm under pressure',font="Tahoma 12")
lbl_q5.grid(row=1, column=2, sticky='w')
# txt
txt_q5 = Entry(myframe)
txt_q5.grid(row=2, column=2 , sticky='wn', padx=10)

# --- q 6 ---
# lbl
lbl_q6 = Label(myframe, text = '6) Rarely introducing yourself at social events',font="Tahoma 12")
lbl_q6.grid(row=3, column=2, sticky='w')
# txt
txt_q6 = Entry(myframe)
txt_q6.grid(row=4, column=2 , sticky='wn', padx=10)

# --- q 7 ---
# lbl
lbl_q7 = Label(myframe, text = '7) Finishes one project before starting another',font="Tahoma 12")
lbl_q7.grid(row=5, column=2, sticky='w')
# txt
txt_q7 = Entry(myframe)
txt_q7.grid(row=6, column=2 , sticky='wn', padx=10)

# --- q 8 ---
# lbl
lbl_q8 = Label(myframe, text = '8) Very sentimental',font="Tahoma 12")
lbl_q8.grid(row=7, column=2, sticky='w')
# txt
txt_q8 = Entry(myframe)
txt_q8.grid(row=8, column=2 , sticky='wn', padx=10)

# --- q 9 ---
# lbl
lbl_q9 = Label(myframe, text = '9) you Like using schedules and lists',font="Tahoma 12")
lbl_q9.grid(row=1, column=3, sticky='w')
# txt
txt_q9 = Entry(myframe)
txt_q9.grid(row=2, column=3 , sticky='wn', padx=10)

# --- q 10 ---
# lbl
lbl_q10 = Label(myframe, text = '10) Small mistakes make doubt abilities',font="Tahoma 12")
lbl_q10.grid(row=3, column=3, sticky='w')
# txt
txt_q10 = Entry(myframe)
txt_q10.grid(row=4, column=3 , sticky='wn', padx=10)

# --- q 11 ---
# lbl
lbl_q11 = Label(myframe, text = '11) Comfortable striking up conversations',font="Tahoma 12")
lbl_q11.grid(row=5, column=3, sticky='w')
# txt
txt_q11 = Entry(myframe)
txt_q11.grid(row=6, column=3 , sticky='wn', padx=10)

# --- q 12 ---
# lbl
lbl_q12 = Label(myframe, text = '12) Not interested in analyzing creative works',font="Tahoma 12")
lbl_q12.grid(row=7, column=3, sticky='w')
# txt
txt_q12 = Entry(myframe)
txt_q12.grid(row=8, column=3 , sticky='wn', padx=10)


# --- q 13 ---
# lbl
lbl_q13 = Label(myframe, text = '13) Following head rather than heart',font="Tahoma 12")
lbl_q13.grid(row=1, column=4, sticky='w')
# txt
txt_q13 = Entry(myframe)
txt_q13.grid(row=2, column=4 , sticky='wn', padx=10)

# --- q 14 ---
# lbl
lbl_q14 = Label(myframe, text = '14) Preferring spontaneity over routine',font="Tahoma 12")
lbl_q14.grid(row=3, column=4, sticky='w')
# txt
txt_q14 = Entry(myframe)
txt_q14.grid(row=4, column=4 , sticky='wn', padx=10)

# --- q 15 ---
# lbl
lbl_q15 = Label(myframe, text = '15) you rarely worry about impressions',font="Tahoma 12")
lbl_q15.grid(row=5, column=4, sticky='w')
# txt
txt_q15 = Entry(myframe)
txt_q15.grid(row=6, column=4 , sticky='wn', padx=10)

# --- q 16 ---
# lbl
lbl_q16 = Label(myframe, text = '16) you enjoy group activities',font="Tahoma 12")
lbl_q16.grid(row=7, column=4, sticky='w')
# txt
txt_q16 = Entry(myframe)
txt_q16.grid(row=8, column=4 , sticky='wn', padx=10)

# --- Button(submit) ---
btn_submit = Button(myframe, text="submit", bd = 2 , width = 10 , height = 2 , font = ("Arial",16))
btn_submit.grid(row = 9 , column=2 , columnspan =2 )


myframe.mainloop()