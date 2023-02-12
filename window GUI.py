from tkinter import  *
# object creating tkinter class
tab=Tk()
# creating size width,height
tab.geometry("700x500")
#minimume size creat width ,height

tab.minsize(500,500)
     #maximume size creat width ,height

tab.maxsize(1200,1200)
tab.title("my first GUI")
tab["bg"]="pink"
word=Label(text="Wellcome my first text in GUI").place(x=140,y=60)

""" if place use then not need pack() method"""
# word.pack()

tab.mainloop()

