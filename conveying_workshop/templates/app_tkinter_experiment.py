import tkinter as tk
#app_tkinter_experiment
root1=tk.Tk()
root = tk.Tk()


v = tk.IntVar()

def jack_status_positive():
    tk.myLabel=tk.Label(root1,text="green jack available")
    tk.myLabel.pack()

def power_button():
    tk.myLabel=tk.Label(root,text="press the power button")
    tk.myLabel.pack()



myButton3=tk.Button(root1,text='Connect',padx=40,command=jack_status_positive)
myButton4=tk.Button(root,text='Connect',padx=40,command=power_button)
myButton3.pack()
myButton4.pack()

tk.Label(root, 
        text="""Choose a 
cup size:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root, 
              text="small",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="medium",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="large",
              padx = 20, 
              variable=v, 
              value=3).pack(anchor=tk.W)

root.mainloop()
root1.mainloop()