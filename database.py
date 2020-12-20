import sqlite3
import tkinter
from tkinter import messagebox
from tkinter import *


def BookSched(bus_number, name, time, cameFrom, arrivalTo, seatNumber):
    print(" ITO NA DB TO HA" + bus_number + " "+ name+" " + time + " " +cameFrom+ " "+ arrivalTo)
    with sqlite3.connect("Reservation/db/Reservations.db") as db:
        cursor = db.cursor ()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY, 
    bus_number VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    time VARCHAR(50) NOT NULL,
    came_from VARCHAR(255) NOT NULL,
    arrival_to VARCHAR(255) NOT NULL,
    seat_number VARCHAR(255) NOT NULL);
    ''')
    
    shittyAss = [(bus_number, name, time, cameFrom,arrivalTo, seatNumber)]

    cursor.executemany("INSERT INTO user(bus_number,name,time, came_from, arrival_to, seat_number) VALUES(?,?,?,?,?,?)",shittyAss )
    db.commit ()

    cursor.execute ("SELECT * FROM user")
    print(cursor.fetchall())

def reserveSeat(busNumber, name, seatNumber):

    print("reservation")
    busNumber = str(busNumber)
    name = str(name)
    seatNumber = str(seatNumber)

    print(busNumber + " "+ name+ " "+ seatNumber)
    conn = sqlite3.connect('Reservation/db/Reservations.db')
    cursor = conn.cursor()
    try:    
        sql = "SELECT * FROM user WHERE bus_number= ?"
        cursor.execute(sql, [busNumber])
        rows = cursor.fetchall()

        sql2 = "SELECT * FROM user WHERE name= ?"
        cursor.execute(sql2, [name])
        rows2 = cursor.fetchall()
        i = 0
        if not rows or not rows2:
            print("there is no reservation")
            
            tkinter.messagebox.showwarning(title="ERROR", message="There is no reservation for this name or on this bus number")
       
        seatNumber = str(seatNumber)    
        
        for x in rows:
            
            i = i+1
            
            if x[1]==busNumber:
                
                print("Goods")
                if x[2] == name:
                    query = "UPDATE user SET seat_number = ? WHERE name = ?"
                    existence = "SELECT bus_number FROM user WHERE seat_number = ?"

                    #if cursor.execute(existence, [seatNumber]).fetchone():
                       # tkinter.messagebox.showwarning(title="ERROR", message="This seat was taken. PLease choose another one")
                       # return
                    else:
                        print("Proceed")
                    dataS = (seatNumber, name)
                    cursor.execute(query, dataS)
                    conn.commit()

                    messageKO = "Successfully reserve a seat, your schedule is: " + x[3]

                    tkinter.messagebox.showinfo(title="Congrats", message=messageKO)

                    print("Bus Number: ",x[1])
                    print("Name: ", x[2])
                    print("Time: ", x[3])
                    print("Came From: ", x[4])
                    print("Arrive to: ", x[5])
                    print("seat number: ", x[6])

                    print("*" * 50)
         
            
            

            
    except Exception as e:
        print(str(e))
        print("database error")
        
def showingReservation(self, busNumber):
    


    
    self.a = Button(self.btnFrame, text = "1") #in data save as 1
    self.b = Button(self.btnFrame, text = "2")
    self.c = Button(self.btnFrame, text = "3")
    self.d = Button(self.btnFrame, text = "4")
    self.e = Button(self.btnFrame, text = "5")
    self.f = Button(self.btnFrame, text = "6")
    self.g = Button(self.btnFrame, text = "7")
    self.h = Button(self.btnFrame, text = "8")
    self.i = Button(self.btnFrame, text = "9")
    self.j = Button(self.btnFrame, text = "10")
    self.k = Button(self.btnFrame, text = "11")
    self.l = Button(self.btnFrame, text = "12")
    self.m = Button(self.btnFrame, text = "13")
    self.n = Button(self.btnFrame, text = "14")
    self.o = Button(self.btnFrame, text = "15")
    self.p = Button(self.btnFrame, text = "16")
    self.q = Button(self.btnFrame, text = "17")
    self.r = Button(self.btnFrame, text = "18")
    self.s = Button(self.btnFrame, text = "19")
    self.t = Button(self.btnFrame, text = "20")
    self.u = Button(self.btnFrame, text = "21")
    self.v = Button(self.btnFrame, text = "22")
    self.w = Button(self.btnFrame, text = "23")
    self.x = Button(self.btnFrame, text = "24")
    self.y = Button(self.btnFrame, text = "25")
    self.z = Button(self.btnFrame, text = "26")
    self.aa = Button(self.btnFrame, text = "27")
    self.ab = Button(self.btnFrame, text = "28")
    self.ac = Button(self.btnFrame, text = "29")
    self.ad = Button(self.btnFrame, text = "30")
    self.ae = Button(self.btnFrame, text = "31")
    self.af = Button(self.btnFrame, text = "32")
    self.ag = Button(self.btnFrame, text = "33")
    self.ah = Button(self.btnFrame, text = "34")
    self.ai = Button(self.btnFrame, text = "35")
    self.aj = Button(self.btnFrame, text = "36")




    self.a.grid(row = 0, column = 0)
    self.b.grid(row = 0, column = 1)
    self.c.grid(row = 0, column = 2)
    self.d.grid(row = 0, column = 3)
    self.e.grid(row = 0, column = 4)
    self.f.grid(row = 0, column = 5)
    self.g.grid(row = 0, column = 6)
    self.h.grid(row = 0, column = 7)
    self.i.grid(row = 0, column = 8)        
    self.j.grid(row = 1, column = 0)
    self.k.grid(row = 1, column = 1)
    self.l.grid(row = 1, column = 2)
    self.m.grid(row = 1, column = 3)
    self.n.grid(row = 1, column = 4)
    self.o.grid(row = 1, column = 5)
    self.p.grid(row = 1, column = 6)
    self.q.grid(row = 1, column = 7)
    self.r.grid(row = 1, column = 8)        
    self.s.grid(row = 2, column = 0)
    self.t.grid(row = 2, column = 1)
    self.u.grid(row = 2, column = 2)
    self.v.grid(row = 2, column = 3)
    self.w.grid(row = 2, column = 4)
    self.x.grid(row = 2, column = 5)
    self.y.grid(row = 2, column = 6)
    self.z.grid(row = 2, column = 7)
    self.aa.grid(row = 2, column = 8)
        
    self.ab.grid(row = 3, column = 0)
    self.ac.grid(row = 3, column = 1)
    self.ad.grid(row = 3, column = 2)
    self.ae.grid(row = 3, column = 3)
    self.af.grid(row = 3, column = 4)
    self.ag.grid(row = 3, column = 5)
    self.ah.grid(row = 3, column = 6)
    self.ai.grid(row = 3, column = 7)
    self.aj.grid(row = 3, column = 8)
    
    
    #print("okie")
    busNumber = str(busNumber)
    
    conn = sqlite3.connect('Reservation/db/Reservations.db')
    cursor = conn.cursor()
    #print(busNumber)

    try:    
        sql = "SELECT * FROM user WHERE bus_number= ?"
        cursor.execute(sql, [busNumber])
        rows = cursor.fetchall()

        if not rows:
           # print("there is no reservation")
            #return "false"
            tkinter.messagebox.showwarning(title="ERROR", message="There is no reservation for this bus number")

        for xi in rows:
            #sql = "SELECT * FROM user WHERE bus_number= ?",(busNumber)
            #cursor.execute(sql)
            #rows = cursor.fetchall()
            
            
            if xi[1]==busNumber:
                

                
               
                self.btnFrame.grid(row =4, column = 0 )
                

                a = self.a.cget('text')
                b = self.b.cget('text')
                c = self.c.cget('text')
                d = self.d.cget('text')
                e = self.e.cget('text')
                f = self.f.cget('text')
                g = self.g.cget('text')
                h = self.h.cget('text')
                i = self.i.cget('text' )
                j  = self.j.cget('text')
                k  = self.k.cget('text')
                l  = self.l.cget('text')
                m  = self.m.cget('text')
                n  = self.n.cget('text')
                o  = self.o.cget('text')
                p = self.p.cget('text' )
                q  = self.q.cget('text')
                r = self.r.cget('text')
                s  = self.s.cget('text')
                t = self.t.cget('text')
                u = self.u.cget('text')
                v = self.v.cget('text')
                w = self.w.cget('text')
                x = self.x.cget('text')
                y = self.y.cget('text')
                z= self.z.cget('text')
                aa = self.aa.cget('text')
                ab = self.ab.cget('text')
                ac = self.ac.cget('text')
                ad = self.ad.cget('text')
                ae = self.ae.cget('text')
                af = self.af.cget('text')
                ag = self.ag.cget('text')
                ah = self.ah.cget('text')
                ai = self.ai.cget('text')
                aj = self.aj.cget('text')
                #print(type(aj))

                dam = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj]
                
                
                seatNum = xi[6]
                if seatNum == '0':
                    tkinter.messagebox.showwarning(title="ERROR", message="Some of the passenger has no reservation yet.")
                #print(type(dam))
                #print(seatNum)
                #print(dam[int(seatNum)])

                for ix in dam:
                    
                    if seatNum == ix:
                        ax = dam[int(seatNum)-1]
                        print(ax)
                        if ax =="1":
                            self.a.config(bg = "red")
                        elif ax == "2":
                            self.b.config(bg = "red")
                        elif ax == "3":
                            self.c.config(bg = "red")
                        elif ax == "4":
                            self.d.config(bg = "red")
                        elif ax == "5":
                            self.e.config(bg = "red")
                        elif ax == "6":
                            self.f.config(bg = "red")
                        elif ax == "7":
                            self.g.config(bg = "red")
                        elif ax == "8":
                            self.h.config(bg = "red")
                        elif ax == "9":
                            self.i.config(bg = "red")
                        elif ax == "10":
                            self.j.config(bg = "red")
                        elif ax == "11":
                            self.k.config(bg = "red")
                        elif ax == "12":
                            self.l.config(bg = "red")
                        elif ax == "13":
                            self.m.config(bg = "red")
                        elif ax == "14":
                            self.n.config(bg = "red")
                        elif ax == "15":
                            self.o.config(bg = "red")
                        elif ax == "16":
                            self.p.config(bg = "red")
                        elif ax == "17":
                            self.q.config(bg = "red")
                        elif ax == "18":
                            self.r.config(bg = "red")
                        elif ax == "19":
                            self.s.config(bg = "red")
                        elif ax == "20":
                            self.t.config(bg = "red")
                        elif ax == "21":
                            self.u.config(bg = "red")
                        elif ax == "22":
                            self.v.config(bg = "red")
                        elif ax == "23":
                            self.w.config(bg = "red")
                        elif ax == "24":
                            self.x.config(bg = "red")
                        elif ax == "25":
                            self.y.config(bg = "red")
                        elif ax == "26":
                            self.z.config(bg = "red")
                        elif ax == "27":
                            self.aa.config(bg = "red")
                        elif ax == "28":
                            self.ab.config(bg = "red")
                        elif ax == "29":
                            self.ac.config(bg = "red")
                        elif ax == "30":
                            self.ad.config(bg = "red")
                        elif ax == "31":
                            self.ae.config(bg = "red")
                        elif ax == "32":
                            self.af.config(bg = "red")
                        elif ax == "33":
                            self.ag.config(bg = "red")
                        elif ax == "34":
                            self.ah.config(bg = "red")
                        elif ax == "35":
                            self.ai.config(bg = "red")
                        elif ax == "36":
                            self.aj.config(bg = "red")
                        
                        

                    #if seatNum == ix:
                       # for xe in len(dam):

                


                #print("return bus number")   
        #return seatNum

    except Exception as e:
        print(str(e))
        print("database error")
    
#BookSched()