from tkinter import *
import sqlite3

root = Tk()
conn = sqlite3.connect("database.db")
cur = conn.cursor()


def dashboard():
    dash = Toplevel()
    Label(dash,text="Username: ").grid(row=0,column=0)
    uname = Entry(dash)
    uname.grid(row=0,column=1)
    Label(dash,text="Password: ").grid(row=1,column=0)
    paass = Entry(dash)
    uname.grid(row=1,column=1)
    btn = Button(dash, text="Login", command=oldNew)
    btn.grid(row=2)

def oldNew():
    oldNewWindow = Toplevel()
    oldBtn = Button(oldNewWindow, text="Old Customer", command=old)
    newBtn = Button(oldNewWindow, text="New Customer", command=new)
    oldBtn.grid(row=0,column=0)
    newBtn.grid(row=0,column=1)

def old():
    oldCust = Toplevel()
    Label(oldCust, text="Enter the phone number: ").grid(row=0,column=0)
    num = Entry(oldCust)
    phoneNum = int(num.get())
    rows = cur.execute("SELECT * FROM customer AS c, car_dets AS cd WHERE c.phone="+str(phoneNum)+" AND cd.ownerId=c.id")



root.mainloop()