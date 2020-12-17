#import Reservation(BATSU) as r
from tkinter import *

class Reservation:
    def __init__(self, master):

       # self.sched = sched
        #self.reser = reser
        #self.s_reser = s_reser
        #self.avai = avai
        self.master = master
        master.title('Transportation System')
    #root.geometry('400x250')

        myHeight = 500 
        myWidth  = 500


        s_width = master.winfo_screenwidth()
        s_height = master.winfo_screenheight()

        x_coordinate = (s_width/2) - (myWidth/2)
        y_coordinate = (s_height/2) - (myHeight/2)

        master.geometry("%dx%d+%d+%d" % (myWidth, myHeight, x_coordinate, y_coordinate))
        master.resizable(width = False, height = False)
        centerFrame = Frame(master,height = myHeight/10, width = myWidth)
        centerFrame.grid(row = 0, column = 0,sticky='w'+'e'+'n'+'s')
        self.title = Label(centerFrame, text = "**********2C & M Transportation System **********")    
        
        self.title.grid(row = 0, column = 0)
        columnFrame = Frame(centerFrame, height = myHeight/5, width = myWidth)
        columnFrame.grid(row = 1, column= 0, sticky='w'+'e'+'n'+'s')

        self.sch = Button(columnFrame, text = "Schedule", command = self.shitEntry)
        self.reser = Button(columnFrame, text = "Reservation", command = self.resEntry)
        self.sReser = Button(columnFrame, text = "Show the Reservation", command = self.sReser)
        self.available = Button(columnFrame, text = "Available")
     
        self.sch.grid(row = 1, column = 0, padx = 15, sticky='w'+'e'+'n'+'s')
        self.reser.grid(row = 1, column =1,padx = 15, sticky='w'+'e'+'n'+'s')
        self.sReser.grid(row = 1, column = 2,padx = 15, sticky='w'+'e'+'n'+'s')
        self.available.grid(row = 1, column = 3,padx = 15, sticky='w'+'e'+'n'+'s')


        self.schedFrame = Frame(self.master, height = myHeight, width = myWidth)
        self.reserFrame = Frame(self.master, height = myHeight/5, width = myWidth , bg = 'grey')
        self.sReserFrame = Frame(self.master, height = myHeight/5, width = myWidth)
        self.availFrame = Frame(self.master, height = myHeight/5, width = myWidth)
        #self.schedFrame.grid(row = 3, column= 0, sticky='w'+'e'+'n'+'s')

    def shitEntry(self):
        
        
       
        self.schedFrame.grid(row = 3, column= 0)

        if(self.reserFrame.winfo_exists() == 1 and self.sReserFrame.winfo_exists()==1 and self.availFrame.winfo_exists()==1):
            self.reserFrame.grid_remove()
            self.sReserFrame.grid_remove()
            self.availFrame.grid_remove()


        self.busNum = Label(self.schedFrame, text = "Enter the bus number: ")
        self.butEnt = Entry(self.schedFrame, bd = 2)
        self.passName = Label(self.schedFrame, text = "Enter passenger's name:")
        self.passNameEntry = Entry(self.schedFrame, bd = 2)

        self.busNum.grid(row = 0, column = 0)
        self.butEnt.grid(row = 0, column = 1)

        self.passName.grid(row = 1, column = 0)

        self.passNameEntry.grid(row = 1, column = 1)

        schedTime = Frame(self.schedFrame, width = 500, height = 100, bg = 'grey')
        schedTime.grid(row = 4, column = 0,ipadx = 50, pady = 10)
        a = Button(schedTime, text = "7:00am - 9:00am") #in data save as 1
        b = Button(schedTime, text  = "10:00am - 12:00pm")
        c = Button(schedTime, text  = "1:00pm - 3:00pm")
        d = Button(schedTime, text  = "5:00pm - 7:00pm")
        e = Button(schedTime, text  = "8:00pm - 10:00pm")

        a.grid(row = 0, column = 0)
        b.grid(row = 0, column = 1)
        c.grid(row = 0, column = 2)
        d.grid(row = 1, column = 0)
        e.grid(row = 1, column = 1)
        


    
    def resEntry(self):
        self.reserFrame.grid(row = 3, column= 0, sticky='w'+'e'+'n'+'s')
        if(self.reserFrame.winfo_exists()==1):
            print("OKAY")
            print(self.reserFrame.grid_info())
        else:
            print("SHIT")
        #self.thirdFrame.destroy()
    def sReser(self):
        self.thirdFrame.grid_remove()



        

root = Tk()
b = Reservation(root)
root.mainloop()
