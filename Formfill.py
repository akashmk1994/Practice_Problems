from tkinter import *

import backend_formfill


def get_sel_row(event):
    global sel_tuple
    index = listbox.curselection()[0]
    sel_tuple = listbox.get(index)
    entry1.delete(0, END)
    entry1.insert(END, sel_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, sel_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, sel_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, sel_tuple[4])
    entry5.delete(0, END)
    entry5.insert(END, sel_tuple[5])


def view_command():
    listbox.delete(0, END)
    for row in backend_formfill.view_ent():
        listbox.insert(END, row)


def add_command():
    backend_formfill.add_ent(name_text.get(), age_text.get(), add_text.get(), room_text.get(), rent_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (name_text.get(), age_text.get(), add_text.get(), room_text.get(), rent_text.get()))


def delete_command():
    backend_formfill.delete_ent(sel_tuple[0])


def update_command():
    backend_formfill.update_ent(sel_tuple[0], name_text.get(), age_text.get(), add_text.get(), room_text.get(), rent_text.get())


window = Tk()

window.title("Welcome to my Hotel Green view!")

window.geometry('650x400')

l1 = Label(window, text="Name")
l1.grid(row=0, column=1)
l2 = Label(window, text="Age")
l2.grid(row=1, column=1)
l3 = Label(window, text="Address")
l3.grid(row=2, column=1)
l4 = Label(window, text="Room Type")
l4.grid(row=3, column=1)
l5 = Label(window, text="Rent[Auto calculated]")
l5.grid(row=4, column=1)

name_text = StringVar()
entry1 = Entry(window, textvariable=name_text)
entry1.grid(row=0, column=2)

age_text = StringVar()
entry2 = Entry(window, textvariable=age_text)
entry2.grid(row=1, column=2)

add_text = StringVar()
entry3 = Entry(window, textvariable=add_text)
entry3.grid(row=2, column=2)

room_text = StringVar()
entry4 = Entry(window, textvariable=room_text)
entry4.grid(row=3, column=2)

rent_text = StringVar()
entry5 = Entry(window, textvariable=rent_text)
entry5.grid(row=4, column=2)

listbox = Listbox(window, height=20, width=59)
listbox.grid(row=0, column=4, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=0, column=3, sticky='ns', rowspan=6, columnspan=1)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_sel_row)

button1 = Button(window, text='View All', command=view_command)
button1.grid(row=6, column=1, sticky="NSEW")
button2 = Button(window, text='Add Entry', command=add_command)
button2.grid(row=7, column=1, sticky="NSEW")
button3 = Button(window, text='Delete Entry', command=delete_command)
button3.grid(row=6, column=2, sticky="NSEW")
button4 = Button(window, text='Update Entry', command=update_command)
button4.grid(row=7, column=2, sticky="NSEW")

window.mainloop()
