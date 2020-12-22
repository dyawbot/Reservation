#import Reservation(BATSU) as r
from tkinter import *
import tkinter
from db import database as db

class Reservation:
    def __init__(self, master):

       # self.sched = sched
        #self.reser = reser
        #self.s_reser = s_reser
        #self.avai = avai
        self.master = master
        master.title('Transportation System')
        #master.config(bg = "white")
        #root.geometry('400x250')
        #self.master = master

        myHeight = 550 
        myWidth  = 500


        s_width = master.winfo_screenwidth()
        s_height = master.winfo_screenheight()

        x_coordinate = (s_width/2) - (myWidth/2)
        y_coordinate = (s_height/2) - (myHeight/2)

        master.geometry("%dx%d+%d+%d" % (myWidth, myHeight, x_coordinate, y_coordinate))
        master.resizable(width = False, height = False)
        centerFrame = Frame(master,height = myHeight/10, width = myWidth)
        centerFrame.grid(row = 0, column = 0, padx = 80, pady = 20)
        
        self.title = Label(centerFrame, text = "2C & M Transportation System", font=("Arial", 12), fg = "dark blue")    
        
        self.title.grid(row = 0, column = 0)
        columnFrame = Frame(centerFrame, height = myHeight/5, width = myWidth)
        columnFrame.grid(row = 1, column= 0, sticky='w'+'e'+'n'+'s')

        self.sch = Button(columnFrame, text = "Schedule", command = self.shitEntry, fg = "blue")
        self.reser = Button(columnFrame, text = "Reservation", command = self.resEntry, fg = "blue")
        self.sReser = Button(columnFrame, text = "Show the Reservation", command = self.sReser, fg = "blue")
        self.available = Button(columnFrame, text = "Available")
     
        self.sch.grid(row = 1, column = 0, padx = 15, pady = 10, sticky='w'+'e'+'n'+'s')
        self.reser.grid(row = 1, column =1,padx = 15, pady = 10,sticky='w'+'e'+'n'+'s')
        self.sReser.grid(row = 1, column = 2,padx = 15,pady = 10, sticky='w'+'e'+'n'+'s')
        #self.available.grid(row = 1, column = 3,padx = 15, sticky='w'+'e'+'n'+'s')


        self.schedFrame = Frame(self.master, height = myHeight, width = myWidth)
        self.reserFrame = Frame(self.master, height = myHeight/5, width = myWidth )
        self.sReserFrame = Frame(self.master, height = myHeight/5, width = myWidth)
        self.availFrame = Frame(self.master, height = myHeight/5, width = myWidth)
        #self.schedFrame.grid(row = 3, column= 0, sticky='w'+'e'+'n'+'s')

        self.resFrame = Frame(self.master, width = 500, height = 100)
        self.schedTime = Frame(self.master, width = 500, height = 100)
        self.arrivalFrame = Frame(self.master, width = 500, height = 100)

        self.showAllFrame = Frame(self.master, width = 500, height = 100)
        self.btnFrame = Frame(self.master, width = 500, height = 100)
        self.saveBtnFrame = Frame(self.master, width = 500, height = 50)
        
        self.butSelected = False
        self.labeling = Label(self.master, width = 500, height =50)


        name = "reservation"

        
        


   
   
   
    def shitEntry(self):
        
        
       
        self.schedFrame.grid(row = 3, column= 0, pady = 50)

        if(self.reserFrame.winfo_exists() == 1 and self.sReserFrame.winfo_exists()==1 and self.availFrame.winfo_exists()==1 and self.resFrame.winfo_exists()==1):
            self.reserFrame.grid_remove()
            self.sReserFrame.grid_remove()
            self.availFrame.grid_remove()
            self.resFrame.grid_remove()
            self.showAllFrame.grid_remove()
            self.saveBtnFrame.grid_remove()
            self.btnFrame.grid_remove()
            self.labeling.grid_remove()


        self.busNum = Label(self.schedFrame, text = "Enter the bus number: ")
        self.butEnt = Entry(self.schedFrame, bd = 2)
        self.passName = Label(self.schedFrame, text = "Enter passenger's name:")
        self.passNameEntry = Entry(self.schedFrame, bd = 2)

        self.busNum.grid(row = 0, column = 0)
        self.butEnt.grid(row = 0, column = 1)

        self.passName.grid(row = 1, column = 0)

        self.passNameEntry.grid(row = 1, column = 1)

        name = "schedule"
        self.schedTime.grid(row = 4, column = 0,padx = 95, pady = 30)
        a = Button(self.schedTime, text = "7:00am - 9:00am", command =lambda: self.onclick(name, "7:00am - 9:00am")) #in data save as 1
        b = Button(self.schedTime, text  = "10:00am - 12:00pm",command =lambda: self.onclick(name, "10:00am - 12:00pm"))
        c = Button(self.schedTime, text  = "1:00pm - 3:00pm", command =lambda: self.onclick(name, "1:00pm - 3:00pm"))
        d = Button(self.schedTime, text  = "5:00pm - 7:00pm", command =lambda: self.onclick(name, "5:00pm - 7:00pm"))
        e = Button(self.schedTime, text  = "8:00pm - 10:00pm", command =lambda: self.onclick(name, "8:00pm - 10:00pm"))

        #self.timeSched = Label(self.schedTime, text = "You show: ")
        #self.timeSched.grid(row =1)

        a.grid(row = 0, column = 0)
        b.grid(row = 0, column = 1)
        c.grid(row = 0, column = 2)
        d.grid(row = 1, column = 0)
        e.grid(row = 1, column = 2)
        #self.timeSched.grid(row =2, column = 1)
        
        
        
        self.arrivalFrame.grid(row = 5, column = 0,padx = 95)

        self.cameFrom  = Label(self.arrivalFrame, text = "From: ")
        self.arriveTo = Label(self.arrivalFrame, text = "To: ")

        self.cameFromEntry = Entry(self.arrivalFrame, bd = 2)
        self.arriveToEntry = Entry(self.arrivalFrame, bd = 2)

        self.cameFrom.grid(row = 0, column = 0)
        self.cameFromEntry.grid(row = 0, column = 1)
        
        self.arriveTo.grid(row = 1, column = 0)
        self.arriveToEntry.grid(row = 1, column = 1)

        busNum = self.butEnt.get()
        #passengersName = self.passName.get()



        self.save = Button(self.arrivalFrame, text = "Save", command = lambda: self.saveBtn(name))
        self.save.grid(row = 2, column = 1, pady = 10, sticky = E)
    
    def onclick(self, name, textS):
        #print(textS)
       
        if name == "schedule":

       # myText = Button.cget('text')
            self.timeSched=Label(self.schedTime, text = textS)
            self.timeSched.grid(row=2, column = 1, pady = 10)
            print(textS)
        elif name == "reservation":
            self.butSelected = True
            self.timeSched=Label(self.saveBtnFrame, text = textS, fg = "red")
            self.sel = Label(self.saveBtnFrame, text = "You Seat Number is: ")
            self.sel.grid(row = 5, column =3)
            self.timeSched.grid(row=5, column = 4)
            

        elif name == "ShowAll":
            print(textS)
            busNumber = self.busEntry.get()
            saveToDb = db.showingReservation(self, busNumber)
            

    def saveBtn(self, name):

        if name == "schedule":
            #since schedule has no seat number 
            #we put the initial seatnumber as zero (0)
            seatNumber = "0"
            print("this is for schedule")
            bus_number = self.butEnt.get()
            passenger_name = self.passNameEntry.get()
            stime  = self.timeSched.cget('text')
            cameFroms = self.cameFromEntry.get()
            arriveTos = self.arriveToEntry.get()

            #print(str(bus_number)+" "+ str(passenger_name)+" " + str(stime)+ " "+ str(cameFroms)+" "+ str(arriveTos))
            saveToDb = db.BookSched(bus_number, passenger_name, stime,cameFroms, arriveTos, seatNumber)

            print(saveToDb)

        elif name == "reservation":
            self.master

            

            if self.butSelected ==True:
                print(self.butSelected)
                busNum = self.butEnt.get()
                passName = self.passNameEntry.get()
                seatNum = self.timeSched.cget('text')
                print("this is for reservation button")
                saveToDb = db.reserveSeat(str(busNum), str(passName), str(seatNum))
            else:
                tkinter.messagebox.showwarning(title="ERROR", message="NO SEAT SELECTED")



    
    def resEntry(self):
        ht = 2
        wh =3

        self.schedFrame.grid_remove()
        self.schedTime.grid_remove()
        self.arrivalFrame.grid_remove()
        self.btnFrame.grid_remove()
        self.showAllFrame.grid_remove()
        self.labeling.grid_remove()
        self.reserFrame.grid(row = 3, column= 0, pady = 50)
        
        self.busNum = Label(self.reserFrame, text = "Enter the bus number: ")
        self.butEnt = Entry(self.reserFrame, bd = 2)
        self.passName = Label(self.reserFrame, text = "Enter passenger's name:")
        self.passNameEntry = Entry(self.reserFrame, bd = 2)

        self.busNum.grid(row = 0, column = 0)
        self.butEnt.grid(row = 0, column = 1)

        self.passName.grid(row = 1, column = 0)

        self.passNameEntry.grid(row = 1, column = 1)


        
        name = "reservation"

        
        self.resFrame.grid(row = 4, column = 0,padx = 95, pady = 5)
        self.saveBtnFrame.grid(row = 5, column = 0,padx = 95, pady = 20)
        
        
        
       
        saveNa = Button(self.saveBtnFrame, text = "Save", height = 2, width = 10, bg = 'red', command =lambda: self.saveBtn(name))

        a = Button(self.resFrame, text = "1", height = ht, width = wh, command =lambda: self.onclick(name, "1")) #in data save as 1
        b = Button(self.resFrame, text = "2", height = ht, width = wh, command =lambda: self.onclick(name, "2"))
        c = Button(self.resFrame, text = "3", height = ht, width = wh,command =lambda: self.onclick(name, "3"))
        d = Button(self.resFrame, text = "4", height = ht, width = wh, command =lambda: self.onclick(name, "4"))
        e = Button(self.resFrame, text = "5", height = ht, width = wh,command =lambda: self.onclick(name, "5"))
        f = Button(self.resFrame, text = "6", height = ht, width = wh,command =lambda: self.onclick(name,"6"))
        g = Button(self.resFrame, text = "7", height = ht, width = wh, command =lambda: self.onclick(name,"7"))
        h = Button(self.resFrame, text = "8", height = ht, width = wh, command =lambda: self.onclick(name,"8"))
        i = Button(self.resFrame, text = "9", height = ht, width = wh, command =lambda: self.onclick(name,"9"))
        j = Button(self.resFrame, text = "10", height = ht, width = wh, command =lambda: self.onclick(name,"10"))
        k = Button(self.resFrame, text = "11", height = ht, width = wh, command =lambda: self.onclick(name,"11"))
        l = Button(self.resFrame, text = "12", height = ht, width = wh, command =lambda: self.onclick(name,"12"))
        m = Button(self.resFrame, text = "13", height = ht, width = wh, command =lambda: self.onclick(name,"13"))
        n = Button(self.resFrame, text = "14", height = ht, width = wh, command =lambda: self.onclick(name,"14"))
        o = Button(self.resFrame, text = "15", height = ht, width = wh, command =lambda: self.onclick(name,"15"))
        p = Button(self.resFrame, text = "16", height = ht, width = wh, command =lambda: self.onclick(name,"16"))
        q = Button(self.resFrame, text = "17", height = ht, width = wh, command =lambda: self.onclick(name,"17"))
        r = Button(self.resFrame, text = "18", height = ht, width = wh, command =lambda: self.onclick(name,"18"))
        s = Button(self.resFrame, text = "19", height = ht, width = wh, command =lambda: self.onclick(name,"19"))
        t = Button(self.resFrame, text = "20", height = ht, width = wh, command =lambda: self.onclick(name,"20"))
        u = Button(self.resFrame, text = "21", height = ht, width = wh, command =lambda: self.onclick(name,"21"))
        v = Button(self.resFrame, text = "22", height = ht, width = wh, command =lambda: self.onclick(name,"22"))
        w = Button(self.resFrame, text = "23", height = ht, width = wh, command =lambda: self.onclick(name,"23"))
        x = Button(self.resFrame, text = "24", height = ht, width = wh, command =lambda: self.onclick(name,"24"))
        y = Button(self.resFrame, text = "25", height = ht, width = wh, command =lambda: self.onclick(name,"25"))
        z = Button(self.resFrame, text = "26", height = ht, width = wh, command =lambda: self.onclick(name,"26"))
        aa = Button(self.resFrame, text = "27", height = ht, width = wh, command =lambda: self.onclick(name,"27"))
        ab = Button(self.resFrame, text = "28", height = ht, width = wh, command =lambda: self.onclick(name,"28"))
        ac = Button(self.resFrame, text = "29", height = ht, width = wh, command =lambda: self.onclick(name,"29"))
        ad = Button(self.resFrame, text = "30", height = ht, width = wh, command =lambda: self.onclick(name,"30"))
        ae = Button(self.resFrame, text = "31", height = ht, width = wh, command =lambda: self.onclick(name,"31"))
        af = Button(self.resFrame, text = "32", height = ht, width = wh, command =lambda: self.onclick(name,"32"))
        ag = Button(self.resFrame, text = "33", height = ht, width = wh, command =lambda: self.onclick(name,"33"))
        ah = Button(self.resFrame, text = "34", height = ht, width = wh, command =lambda: self.onclick(name,"34"))
        ai = Button(self.resFrame, text = "35", height = ht, width = wh, command =lambda: self.onclick(name,"35"))
        aj = Button(self.resFrame, text = "36", height = ht, width = wh, command =lambda: self.onclick(name,"36"))


        


      

        #self.timeSched = Label(self.schedTime, text = "You show: ")
        #self.timeSched.grid(row =1)

        a.grid(row = 0, column = 0)
        b.grid(row = 0, column = 1)
        c.grid(row = 0, column = 2)
        d.grid(row = 0, column = 3)
        e.grid(row = 0, column = 4)
        f.grid(row = 0, column = 5)
        g.grid(row = 0, column = 6)
        h.grid(row = 0, column = 7)
        i.grid(row = 0, column = 8)
        
        j.grid(row = 1, column = 0)
        k.grid(row = 1, column = 1)
        l.grid(row = 1, column = 2)
        m.grid(row = 1, column = 3)
        n.grid(row = 1, column = 4)
        o.grid(row = 1, column = 5)
        p.grid(row = 1, column = 6)
        q.grid(row = 1, column = 7)
        r.grid(row = 1, column = 8)
        
        s.grid(row = 2, column = 0)
        t.grid(row = 2, column = 1)
        u.grid(row = 2, column = 2)
        v.grid(row = 2, column = 3)
        w.grid(row = 2, column = 4)
        x.grid(row = 2, column = 5)
        y.grid(row = 2, column = 6)
        z.grid(row = 2, column = 7)
        aa.grid(row = 2, column = 8)
        
        ab.grid(row = 3, column = 0)
        ac.grid(row = 3, column = 1)
        ad.grid(row = 3, column = 2)
        ae.grid(row = 3, column = 3)
        af.grid(row = 3, column = 4)
        ag.grid(row = 3, column = 5)
        ah.grid(row = 3, column = 6)
        ai.grid(row = 3, column = 7)
        aj.grid(row = 3, column = 8)
        
        #c = self.timeSched.cget("text")
        #if self.butSelected == True:
        saveNa.grid(row = 6, column =4, pady = 10)
        #print(self.butSelected)
        
        #else:
            
            #

       
    
    def sReser(self):
        name = "ShowAll"
        self.schedFrame.grid_remove()
        self.schedFrame.grid_remove()
        self.schedTime.grid_remove()
        self.arrivalFrame.grid_remove()
        self.reserFrame.grid_remove()
        self.sReserFrame.grid_remove()
        self.availFrame.grid_remove()
        self.resFrame.grid_remove()
        self.saveBtnFrame.grid_remove()

        self.showAllFrame.grid(row = 3, column= 0, pady = 20)

        self.busLabel = Label(self.showAllFrame, text = "Enter the bus number: ")
        self.busEntry = Entry(self.showAllFrame, bd = 2)
        

        self.busLabel.grid(row = 0, column = 0)
        self.busEntry.grid(row = 0, column = 1)
        
        

        self.selectBtn = Button(self.showAllFrame, text = "Select", command = lambda: self.onclick(name, None))
        self.selectBtn.grid(row = 1, column = 1, pady = 10, sticky = E)
        self.labeling.grid(row =4, column = 0)
        indicator = Label(self.labeling, text = "LEGEND: ", font=("Arial", 9))
        redLabel = Label(self.labeling, text = "AVAILABLE: ", width = 15,font=("Arial", 8))
        redLabel1 = Label(self.labeling, text = "GREY", width = 15,font=("Arial", 8), bg = "#dff7df", fg ="#dff7df")

        
        greyLabel = Label(self.labeling, text = "UNAVAILABLE: ", width = 15, font=("Arial", 8))
        greyLabel1 = Label(self.labeling, text = "RED", width = 15,font=("Arial", 8), bg = "red", fg = "red")

        indicator.grid(row =0, column = 0, sticky = W)
        redLabel.grid(row= 1, column = 0,pady = 2, sticky = W)
        redLabel1.grid(row = 1, column = 1,pady = 2,sticky = W)
        
        greyLabel.grid(row = 2, column = 0,pady = 2, sticky = W)
        greyLabel1.grid(row = 2, column = 1, pady = 2,sticky = W)








        

root = Tk()
b = Reservation(root)
root.mainloop()
