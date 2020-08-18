from tkinter import*
root = Tk()
text=Text(root,width=20,height=10,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
text.pack()
text.insert(INSERT,"hello world")
root.geometry("900x600+120+120")
root.mainloop() 
