from tkinter import *
import database as backend
import time

#functions
def get_selected_row(event):
    global selected_record
    try:
        index=list1.curselection()[0]
        selected_record=list1.get(index)
        E1.delete(0, END)
        E1.insert(END, selected_record[1])
        return selected_record[0]
    except:
        pass
#block functions
#this function writes into pathfile all of the blocked sites from sqlite DB
def block_sites():
    host_path= r"C:\Windows\System32\drivers\etc\hosts"
    redirect="127.0.0.1"
    sites=backend.view()
    with open(host_path, 'r+') as file:
            content=file.read()
            for website in sites:
                if website[1] in content:
                    pass
                else:
                    file.write(redirect+" "+website[1]+"\n")

#unblocks all sites in db
def un_block_sites():
    sites=backend.view()
    host_path= r"C:\Windows\System32\drivers\etc\hosts"

    with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website[1] in line for website in sites):
                    file.write(line)
                file.truncate()



#DB FUNCTIONS
def delete_command():
    backend.delete(selected_record[0])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(URL_text.get()):
        list1.insert(END, row)

def insert_command():
    list1.delete(0, END)
    backend.insert(URL_text.get())

def update_command():
    backend.update(selected_record[0], URL_text.get())



#front end
root = Tk()

backend.connect()

L1 = Label(root, text="Title")
L1.grid(row=0, column=0)

URL_text=StringVar()
E1=Entry(root, textvariable=URL_text)
E1.grid(row=0, column=1)


list1 = Listbox(root, height=8, width=50)
list1.grid(row=2, column=0, rowspan=8, columnspan=5)

list1.bind('<<ListboxSelect>>', get_selected_row)

#Buttons
b1=Button(root, text="View all", width=12, command=view_command)
b1.grid(row=2, column=6)

b2=Button(root, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=6)

b3=Button(root, text="Add Entry", width=12, command=insert_command)
b3.grid(row=4, column=6)

b4=Button(root, text="Update select", width=12, command=update_command)
b4.grid(row=5, column=6)

b5=Button(root, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=6)


block_button =  Button(root, text="Block Sites", width=12, command=block_sites)
block_button.grid(row=12, column=0, pady=10, padx=5)

un_block_button =  Button(root, text="Unblock Sites", width=12, command=un_block_sites)
un_block_button.grid(row=12, column=1, pady=10, padx=5)

quit_button =  Button(root, text="Close", width=12, command=root.destroy)
quit_button.grid(row=12, column=3, pady=10, padx=5)

root.title("Web Blocker")



root.mainloop()