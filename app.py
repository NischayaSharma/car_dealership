from tkinter import *
import sqlite3

root = Tk()
conn = sqlite3.connect("database.db")
cur = conn.cursor()
current_user=current_car=desc_eng = desc_tire = desc_body = ""



def dashboard():
    dash = Toplevel()
    Label(dash, text="Username: ").grid(row=0, column=0)
    uname = Entry(dash)
    uname.grid(row=0, column=1)
    Label(dash, text="Password: ").grid(row=1, column=0)
    paass = Entry(dash)
    paass.grid(row=1, column=1)
    btn = Button(dash, text="Login", command=oldNew)
    btn.grid(row=2)



def oldNew():
    oldNewWindow = Toplevel()
    oldBtn = Button(oldNewWindow, text="Old Customer", command=old)
    newBtn = Button(oldNewWindow, text="New Customer", command=new)
    oldBtn.grid(row=0, column=0)
    newBtn.grid(row=0, column=1)



def old():
    global current_user
    oldCust = Toplevel()
    Label(oldCust, text="Enter the phone number: ").grid(row=0, column=0)
    num = Entry(oldCust)
    phoneNum = int(num.get())
    # rows = cur.execute("SELECT * FROM customer c, car_dets cd, repair as r WHERE c.phone="+str(phoneNum)+" AND (cd.ownerId=c.id AND (cd.id=r.carId AND c.id=r.ownerId))")
    # print(rows)



def new():
    newCust = Toplevel()
   
    Label(newCust, text="Name: ").grid(row=0, column=0)
    Label(newCust, text="Phone Number: ").grid(row=1, column=0)
    Label(newCust, text="Email: ").grid(row=2, column=0)
    Label(newCust, text="License Number: ").grid(row=3, column=0)
   
    name = Entry(newCust)
    phNum = Entry(newCust)
    email = Entry(newCust)
    liceNum = Entry(newCust)
    name.grid(row=0,column=1)
    phNum.grid(row=1,column=1)
    email.grid(row=2,column=1)
    liceNum.grid(row=3,column=1)
   
    cmd = "CREATE TABLE IF NOT EXISTS 'customer' ( 'id' INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT, 'name' TEXT DEFAULT NULL, 'phone' NUMERIC DEFAULT NULL, 'email' TEXT DEFAULT NULL, 'licenseNum' TEXT DEFAULT NULL);"
    cmd1 = "CREATE TABLE IF NOT EXISTS 'car_det' ( 'id' INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT, 'ownerId' NUMERIC DEFAULT NULL REFERENCES 'customer' ('id'), 'type' TEXT DEFAULT NULL, 'name' TEXT DEFAULT NULL, 'kilometers' INTEGER DEFAULT NULL, 'insurance' TEXT DEFAULT NULL, 'engineNum' TEXT DEFAULT NULL, 'chassisNum' TEXT DEFAULT NULL);"
    cmd2 = "CREATE TABLE IF NOT EXISTS 'repair' ( 'id' INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT, 'ownerId' NUMERIC DEFAULT NULL REFERENCES 'customer' ('id'), 'carId' NUMERIC DEFAULT NULL REFERENCES 'car_det' ('id'), 'engine' INTEGER DEFAULT NULL, 'carWash' TEXT DEFAULT NULL, 'tireChange' INTEGER DEFAULT NULL, 'bodyReshaping' INTEGER DEFAULT NULL, 'desc_engine' TEXT DEFAULT NULL, 'desc_tire' TEXT DEFAULT NULL, 'desc_body' TEXT DEFAULT NULL);"
    cur.execute(cmd)
    cur.execute(cmd1)
    cur.execute(cmd2)
    conn.commit()
    def insertCust():
        global current_user
        cmd = "INSERT INTO customer(name, phone, email, licenseNum) VALUES (\""+name.get()+"\", "+str(phNum.get())+", \""+email.get()+"\", \""+liceNum.get()+"\")"
        cur.execute(cmd)
        conn.commit()
        cur.execute("SELECT id FROM customer")
        id = cur.fetchall()
        current_user = id[len(id)-1][0]
        print(current_user)
        carDetails()
    submitBtn = Button(newCust,text="Submit",command=insertCust)
    submitBtn.grid(row=4)



def carDetails():
    carDet = Toplevel()
    Label(carDet, text="Car Type: ").grid(row=0, column=0)
    Label(carDet, text="Name(Eg. Hyundai Santro Zls): ").grid(row=1, column=0)
    Label(carDet, text="Kilometers: ").grid(row=2, column=0)
    Label(carDet, text="Engine Number: ").grid(row=3, column=0)
    Label(carDet, text="Chassis Number: ").grid(row=4, column=0)
    Label(carDet, text="Insurance Number: ").grid(row=5, column=0)

    carType = StringVar()
    suv = Radiobutton(carDet, text="SUV", variable=carType, value="suv")
    hatch = Radiobutton(carDet, text="Hatchback", variable=carType, value="hatchback")
    sedan = Radiobutton(carDet, text="Sedan", variable=carType, value="sedan")
    suv.grid(row=0,column=1)
    hatch.grid(row=0,column=2)
    sedan.grid(row=0,column=3)

    carName = Entry(carDet)
    carName.grid(row=1,column=1)
    km = Entry(carDet)
    km.grid(row=2,column=1)
    engNum = Entry(carDet)
    engNum.grid(row=3,column=1)
    chasNum = Entry(carDet)
    chasNum.grid(row=4,column=1)
    insNum = Entry(carDet)
    insNum.grid(row=5,column=1)
    
    def insertCar():
        global current_car
        cmd = "INSERT INTO car_det(ownerId, type, name, kilometers, insurance, engineNum, chassisNum) VALUES ("+str(current_user)+", \""+carType.get()+"\", \""+carName.get()+"\", "+str(km.get())+", \""+insNum.get()+"\", \""+str(engNum.get())+"\", \""+chasNum.get()+"\")"
        cur.execute(cmd)
        conn.commit()
        cur.execute("SELECT id FROM car_det")
        id = cur.fetchall()
        current_car = id[len(id)-1][0]
        print(current_car)
        repair()

    submitBtn = Button(carDet,text="Submit",command=insertCar)
    submitBtn.grid(row=6)


def repair():
    repair=Toplevel()
    Label(repair, text="Engine Repair").grid(row=0,column=0)
    Label(repair, text="Car Wash").grid(row=1,column=0)
    Label(repair, text="Tires Change").grid(row=2,column=0)
    Label(repair, text="Body Reshaping").grid(row=3,column=0)

    engRep = IntVar()
    yes = Radiobutton(repair, text="Yes", variable=engRep, value=1)
    no = Radiobutton(repair, text="No", variable=engRep, value=0)
    desc_eng = Entry(repair)
    desc_eng.grid(row=0,column=3)
    yes.grid(row=0,column=1)
    no.grid(row=0,column=2)

    carWash = StringVar()
    dry = Radiobutton(repair, text="Dry Wash", variable=carWash, value="dry")
    wet = Radiobutton(repair, text="Wet Wash", variable=carWash, value="wet")
    dlx = Radiobutton(repair, text="Deluxe Wash", variable=carWash, value="deluxe")
    none = Radiobutton(repair, text="None", variable=carWash, value="none")
    none.grid(row=1,column=4)
    dry.grid(row=1,column=1)
    wet.grid(row=1,column=2)
    dlx.grid(row=1,column=3)

    tire = IntVar()
    yes = Radiobutton(repair, text="Yes", variable=tire, value=1)
    no = Radiobutton(repair, text="No", variable=tire, value=0)
    desc_tire = Entry(repair)
    desc_tire.grid(row=2,column=3)
    yes.grid(row=2,column=1)
    no.grid(row=2,column=2)

    body = IntVar()
    yes = Radiobutton(repair, text="Yes", variable=body, value=1)
    no = Radiobutton(repair, text="No", variable=body, value=0)
    desc_body = Entry(repair)
    desc_body.grid(row=3,column=3)
    yes.grid(row=3,column=1)
    no.grid(row=3,column=2)

    def submit():
        global current_car
        global current_user
        cmd = "INSERT INTO repair(ownerId,carId,engine,carWash,tireChange,bodyReshaping,desc_engine,desc_tire,desc_body) VALUES ("+str(current_user)+", "+str(current_car)+", "+str(engRep.get())+", \""+carWash.get()+"\", "+str(tire.get())+", "+str(body.get())+", \""+desc_eng.get()+"\", \""+desc_tire.get()+"\", \""+desc_body.get()+"\")"
        print(cmd)
        cur.execute(cmd)
        conn.commit()
        billboard()
    submitBtn = Button(repair,text="Submit",command=submit)
    submitBtn.grid(row=4)



def billboard():
    prices = {"eng_rep":{1:8000, 0:0}, "car_wash":{"dry":400, "wet":800, "deluxe":1200, "none":0}, "tire":{1:4000, 0:0}, "body_reshp":{1:18000, 0:0}}
    total=0
    bill = Toplevel()
    info=cur.execute("SELECT * FROM customer c, car_det cd, repair r WHERE c.id=cd.ownerId AND c.id=r.ownerId AND cd.id=r.carId AND c.id="+str(current_user)+" AND cd.id="+str(current_car))
    rows=info.fetchall()
    print(rows)
    Label(bill,text="Name:", justify=LEFT, anchor="w").grid(sticky=W, row=0,column=0)
    Label(bill,text=rows[len(rows)-1][1], justify=LEFT, anchor="w").grid(sticky=W, row=0,column=1)

    Label(bill,text="Phone Number:", justify=LEFT, anchor="w").grid(sticky=W, row=1,column=0)
    Label(bill,text=rows[len(rows)-1][2], justify=LEFT, anchor="w").grid(sticky=W, row=1,column=1)
    
    Label(bill,text="E-Mail:", justify=LEFT, anchor="w").grid(sticky=W, row=2,column=0)
    Label(bill,text=rows[len(rows)-1][3], justify=LEFT, anchor="w").grid(sticky=W, row=2,column=1)

    Label(bill,text="License Number:", justify=LEFT, anchor="w").grid(sticky=W, row=3,column=0)
    Label(bill,text=rows[len(rows)-1][4], justify=LEFT, anchor="w").grid(sticky=W, row=3,column=1)

    for i in range(4):
        Label(bill,text="|").grid(row=i,column=2)

    Label(bill,text="Car Type:", justify=LEFT, anchor="w").grid(sticky=W, row=0,column=3)
    Label(bill,text=rows[len(rows)-1][7], justify=LEFT, anchor="w").grid(sticky=W, row=0,column=4)

    Label(bill,text="Car Name:", justify=LEFT, anchor="w").grid(sticky=W, row=1,column=3)
    Label(bill,text=rows[len(rows)-1][8], justify=LEFT, anchor="w").grid(sticky=W, row=1,column=4)

    Label(bill,text="Kilometers Driven:", justify=LEFT, anchor="w").grid(sticky=W, row=2,column=3)
    Label(bill,text=rows[len(rows)-1][9], justify=LEFT, anchor="w").grid(sticky=W, row=2,column=4)

    Label(bill, text="Insurance Number:", justify=LEFT, anchor="w").grid(sticky=W, row=3, column=3)
    Label(bill,text=rows[len(rows)-1][10], justify=LEFT, anchor="w").grid(sticky=W, row=3,column=4)

    total = prices["eng_rep"][rows[len(rows)-1][16]]+prices["tire"][rows[len(rows)-1][18]]+prices["body_reshp"][rows[len(rows)-1][19]]+prices["car_wash"][rows[len(rows)-1][17]]

    if rows[len(rows)-1][16]==1:
        Label(bill, text="Engine Repair:", justify=LEFT, anchor="w").grid(sticky=W, row=4, column=0)
        Label(bill, text=prices["eng_rep"][rows[len(rows)-1][16]]).grid(row=4,column=2)
        if rows[len(rows)-1][20]!="":
            Label(bill, text=rows[len(rows)-1][20], justify=LEFT, anchor="w").grid(sticky=W, row=5, column=1)

    if rows[len(rows)-1][18]==1:
        Label(bill, text="Tire Change:", justify=LEFT, anchor="w").grid(sticky=W, row=6, column=0)
        Label(bill, text=prices["tire"][rows[len(rows)-1][18]]).grid(row=6,column=2)
        if rows[len(rows)-1][21]!="":
            Label(bill, text=rows[len(rows)-1][21], justify=LEFT, anchor="w").grid(sticky=W, row=7, column=1)

    if rows[len(rows)-1][19]==1:
        Label(bill, text="Body Reshaping:", justify=LEFT, anchor="w").grid(sticky=W, row=8, column=0)
        Label(bill, text=prices["body_reshp"][rows[len(rows)-1][19]]).grid(row=8,column=2)
        if rows[len(rows)-1][22]!="":
            Label(bill, text=rows[len(rows)-1][22], justify=LEFT, anchor="w").grid(sticky=W, row=9, column=1)

    if rows[len(rows)-1][17]!="none":
        Label(bill, text="Car Washing:", justify=LEFT, anchor="w").grid(sticky=W, row=10, column=0)
        Label(bill, text=prices["car_wash"][rows[len(rows)-1][17]]).grid( row=10,column=2)
        Label(bill, text=rows[len(rows)-1][17]+" wash", justify=LEFT, anchor="w").grid(sticky=W, row=11, column=1)
    Label(bill, text="Total:", justify=LEFT, anchor="w").grid(sticky=W, row=12, column=0)
    Label(bill, text=total, justify=LEFT, anchor="w").grid(sticky=W, row=12, column=2)

    Button(bill,text="Okay",command=oldNew).grid(row=13,column=2)

dashboard()
root.mainloop()