from tkinter import *
import backend

def view_command(): # we need to insert each of the 5 items in the tuple into the list
    # to ensure that the list box on the left is empty (not sure what this achieves; supposed to clear it out but it looks the same each time)
    list1.delete(0,END)
    # iterate over the tuples (items)
    for row in backend.view():
        list1.insert(END,row)  # 'END' ensures that every item is added to the end of the list

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):  # need the .get() method because these are all StringVar objects
        list1.insert(END, row)  # we want to insert new values (a row) at the end of list1.

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.insert(0, END)  # this strange line again ... to "clear the list" ...
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    # (for above) at the END of the list, insert those 4 posssible values as a tuple

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
list1.grid(row=2,column=0,rowspan=6,columnspan=2) # unclear how height/with and the spans interact.

#need to create the scrollbar method
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# the configure method combines the listbox and the scrollbar
list1.configure(yscrollcommand=sb1.set) # on the y axis
sb1.configure(command=list1.yview) # telling it to position on the y axis

b1=Button(window,text="View All", width=12,command=view_command)  # no brackets here
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update", width=12)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12)
b6.grid(row=7,column=3)

window.mainloop()