from tkinter import *
import random


rt=Tk()
root = Tk()
root.title("GUI 1")
rt.title("GUI 2")
root.minsize(250, 200)
rt.minsize(250, 200)

def start():
    myLabel=Label(rt,text="started,jack status check, see result on GUI1")
    myLabel.pack()

def jack_status():
    myLabel=Label(root,text="jack status is okay, now click on GUI2 to check power status")
    myLabel.pack()

def power_status():
    myLabel=Label(rt,text="power is on now, now click on GUI1 to check tray status")
    myLabel.pack()

def tray_status():
    r=IntVar()
    myLabel=Label(root,text="tray status fine, choose from following, and then GUI2 for speed")
    myLabel.pack()
    Radiobutton(root, text="small", variable=r, value=1).pack()
    Radiobutton(root, text="medium", variable=r, value=2).pack()
    Radiobutton(root, text="large", variable=r, value=3).pack()

def speed_status():
    a=IntVar()
    myLabel=Label(rt,text="choose from following speed options")
    myLabel.pack()
    Radiobutton(rt, text="low", variable=a, value=4).pack()
    Radiobutton(rt, text="medium", variable=a, value=5).pack()
    Radiobutton(rt, text="high", variable=a, value=6).pack()

def error_status():
    myLabel1=Label(root,text="starting belt")
    myLabel2=Label(root,text="starting arm")
    myLabel3=Label(root,text="checking other errors")
    myLabel4=Label(root,text="checking air fault status")
    myLabel5=Label(root,text="air fault doesn't exist, all well")
    myLabel6=Label(root,text="checking axis controller fault")
    myLabel7=Label(root,text="checking critical conveyer motor fault")
    myLabel8=Label(root,text="checking critical fault emergency stop")
    myLabel9=Label(root,text="everything is fine, no errors found")
  
    myLabel1.pack()
    myLabel2.pack()
    myLabel3.pack()
    myLabel4.pack()
    myLabel5.pack()
    myLabel6.pack()
    myLabel7.pack()
    myLabel8.pack()
    myLabel9.pack()

def no_of_pots():
    a=IntVar()
    myLabel=Label(rt,text="choose the number of cups")
    myLabel.pack()
    Radiobutton(rt, text="number of cups is 1", variable=a, value=7).pack()
    Radiobutton(rt, text="number of cups is 2", variable=a, value=8).pack()
    Radiobutton(rt, text="number of cups is 3", variable=a, value=9).pack()
    Radiobutton(rt, text="number of cups is 4", variable=a, value=10).pack()
    Radiobutton(rt, text="number of cups is 5", variable=a, value=11).pack()
    Radiobutton(rt, text="number of cups is 6", variable=a, value=12).pack()
    Radiobutton(rt, text="number of cups is 7", variable=a, value=13).pack()
    Radiobutton(rt, text="number of cups is 8", variable=a, value=14).pack()
    Radiobutton(rt, text="number of cups is 9", variable=a, value=15).pack()
    Radiobutton(rt, text="number of cups is 10", variable=a, value=16).pack()

def start_process():
    myLabel1=Label(root,text="7 medium sized cup has been selected for high speed")
    myLabel2=Label(root,text="7 medium sized cup has arrived at the end of conveyer belt")
    myLabel1.pack()
    myLabel2.pack()


button11 = Button(rt,text="press START to start",command=start)
button1 = Button(root,text="jack status",command=jack_status)
button22 = Button(rt,text="power button status",command=power_status)
button2 = Button(root,text="tray status",command=tray_status)
button33 = Button(rt,text="speed status",command=speed_status)
button3 = Button(root,text="checking errors",command=error_status)
button44 = Button(rt,text="no of pots",command=no_of_pots)
button4=Button(root,text="start process",command=start_process)

button11.pack()
button22.pack()
button1.pack()
button2.pack()
button3.pack()
button33.pack()
button44.pack()
button4.pack()
root.mainloop()
rt.mainloop()
