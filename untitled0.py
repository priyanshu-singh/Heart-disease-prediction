from tkinter import*
from tkinter import messagebox
def open_window():
    top=Toplevel()
    top.title("app 1st ui")
    top.geometry("300x300+120+120")
    button1=Button(top, text="close",command=top.destroy)
    button1.pack()
    button2=Button(top, text="health",command=open_window2)
    button2.pack()
def open_window2():
    top=Toplevel()
    top.title("choose")
    top.geometry("300x300+120+120")
    button1=Button(top, text="tips on health",command=open_window3)
    button1.pack()
    button2=Button(top,text="disease prediction",command=top.destroy)
    button2.pack()
def open_window3():
    top=Toplevel()
    top.title("list of common diseases")
    top.geometry("300x300+120+120")
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    button2=Button(top,text="How to start fire",command=drug)
    button1.pack()
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    button1=Button(top,text="Drug-Overdose",command=drug)
    button1.pack()
    
def drug():
    answer=messagebox.askquestion("info")
    if(answer):
        root.quit

root=Tk()
button=Button(root,text="open app", command=open_window)
button.pack()



root.geometry("900x600+120+120")
root.mainloop()
