from tkinter import *
import tkinter.messagebox
import pickle
from requests.auth import HTTPBasicAuth 
import json
import requests
from proandissuesc import get_project, get_issue


root = Tk()
root.title("Project and Issues Finder")
root.geometry('1300x1000')

def Exit1():
    res=tkinter.messagebox.askquestion(message="Do you want to exit?")
    if res == "yes":
        root.destroy()


def ClearFrame():
    TKScrollTXT.configure(state='normal')
    TKScrollTXT.delete(0.0, "end")

def Clear():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    ClearFrame()

from contextlib import redirect_stdout
def redirector(inputStr):
        TKScrollTXT.insert("end", inputStr)
        TKScrollTXT.see("end")
import sys
sys.stdout.write = redirector

def Enter():
    try:
        Rec={}

        if len(E1.get())<=0:
            tkinter.messagebox.showerror(message="Name not entered")
        else:
                Rec["Name"]=E1.get()

        if len(E2.get())<=0:
            tkinter.messagebox.showerror(message="Key not entered")
        else:
                Rec["Name"]=E2.get()

        if len(E3.get())<=0 or '@' not in E3.get():
            tkinter.messagebox.showerror(message="Enter a valid Username/Email")
        else:
                Rec["Name"]=E3.get()

        if len(E4.get())<=0:
            tkinter.messagebox.showerror(message="Name not entered")
        else:
                Rec["Name"]=E4.get()
    except Exception:
        pass

    domain_name = E1.get()
    project_key = E2.get().upper()
    Username = E3.get()
    Api_key = E4.get()

    auth = HTTPBasicAuth(f"{Username}", f"{Api_key}")
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    get_project(domain_name,auth, headers, project_key)
    print('===================+++++++++++++++++++++====================')
    print('===================+++++++++++++++++++++====================')
    get_issue(domain_name, auth, headers, project_key)




Label(root, text="Your Projects and Issues", font=("Arial bold", 30), fg="blue").pack()
F1=Frame(root, borderwidth = 3, relief="solid")
F1.pack(side="left", expand=True, fill="both")
F3=Frame(root, borderwidth=3, relief="solid")
F3.pack(fill="both")
TKScrollTXT = Text(F3, wrap="none")
hbar = Scrollbar(F3, orient="horizontal", command=TKScrollTXT.xview)
TKScrollTXT.configure(xscrollcommand = hbar.set)
hbar.pack(side="bottom", fill="x")
vbar = Scrollbar(F3, orient="vertical", command=TKScrollTXT.yview)
TKScrollTXT.configure(yscrollcommand = vbar.set)
vbar.pack(side="right", fill="y")
TKScrollTXT.pack(fill='both', side='left')


Label(F1, text="Enter Domain Name").grid(row=0, column=0)
E1=Entry(F1, bd=4)
E1.grid(row=0, column=1, padx=13, pady=10)

Label(F1, text="Enter Product Key").grid(row=1, column=0)
E2 = Entry(F1, bd=4)
E2.grid(row=1, column=1, padx=13, pady=10)

Label(F1, text="Enter Username/Email").grid(row=2, column=0)
E3 = Entry(F1, bd=4)
E3.grid(row=2, column=1, padx=13, pady=10)

Label(F1, text="Enter API Key").grid(row=3, column=0)
E4 = Entry(F1, bd=4)
E4.grid(row=3, column=1, padx=13, pady=10)

Enter = Button(F1, text="ENTER", command=Enter, padx=13, pady=10)
Enter.grid(row=20, column=0, sticky=NSEW, padx=13, pady=10)

Clr = Button(F1, text="CLEAR",command = Clear)
Clr.grid(row=20, column=1, sticky = NSEW, padx=13, pady=10)

Exit = Button(F1, text="EXIT", command = Exit1, padx=13, pady=10)
Exit.grid(row=20, column=2, sticky = NSEW, padx=13, pady=10)

root.mainloop()