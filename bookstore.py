from tkinter import *
from backend import Database  # with OOP, you're now importing a specific object

database=Database()  
# 'Database' is the blueprint from the backend.
# 'database' is the instance of that object here for our use.

def get_selected_row(event):  # (did not understand his explanation for this)
    try:
        global selected_tuple  # need to make this variable available outside thsi local function
        index=list1.curselection()[0] # to find the index of the row you want to delete. We grad item 0 of the resulting tuple.
        selected_tuple=list1.get(index) # this says "grab the entire tuple (or row) at [index] in teh list selected by your cursor."
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError: 
        pass

# Ardit's exact explanation for the bug (clicking on the list field and causing an index error):
# "If there is an IndexError, none of the lines under try  will be executed; the line under except  
# will be executed, which is pass. The pass statement means "do nothing". Therefore, the function 
# will do nothing when there's an empty listbox." (Doing nothing is exactly what we would like to 
# see happen.)



def view_command(): # we need to insert each of the 5 items in the tuple into the list
    # to ensure that the list box on the left is empty (not sure what this achieves; supposed to clear it out but it looks the same each time)
    list1.delete(0,END)
    # iterate over the tuples (items)
    for row in Database.view():
        list1.insert(END,row)  # 'END' ensures that every item is added to the end of the list

def search_command():
    list1.delete(0,END)
    for row in Database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):  # need the .get() method because these are all StringVar objects
        list1.insert(END, row)  # we want to insert new values (a row) at the end of list1.

def add_command():
    Database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.insert(0, END)  # this strange line again ... to "clear the list" ...
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    # (for above) at the END of the list, insert those 4 posssible values as a tuple

def delete_command():
    Database.delete(selected_tuple[0])  # needed to make selected_tuple globally available, pulling out the id (the 0 index item)

def update_command():
    Database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) # we have to get what's already there, not what the user may input

window = Tk()

# a title for the window:
window.wm_title("Book Store") # notice that wm_title is a built-in method for the window object

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

list1.bind('<<ListboxSelect>>', get_selected_row) # we're binding an event to the list--when we select that row to delete, and provide the parameters it should include

b1=Button(window,text="View All", width=12,command=view_command)  # no brackets here
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12, command=window.destroy) # there will be no toher need for a front end function; we can accomplish this from here
b6.grid(row=7,column=3)

window.mainloop()