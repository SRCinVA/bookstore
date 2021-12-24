from tkinter import *

window = Tk()

# need four labels for this build

l1=Label(window, text="Title")
l1.grid(row=0,column=0)

l2=Label(window, text="Author")
l2.grid(row=0,column=2)

l3=Label(window, text="Year")
l3.grid(row=1,column=0)

l4=Label(window, text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()  # need to initialize this object before creating the field
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar() 
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2) # 

window.mainloop()