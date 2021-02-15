from tkinter import *
import tkinter.messagebox
import pickle
# from requests.auth import HTTPBasicAuth
# import json
# import requests


root = Tk()
root.title("Project and Issues Finder")
root.geometry('1300x1000')


def Exit1():
    res = tkinter.messagebox.askquestion(message="Do you want to exit?")
    if res == "yes":
        root.destroy()


def ClearFrame():
    for widget in F2.winfo_children():
        widget.destroy()


def Clear():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    ClearFrame()


def ViewAll():
    for widget in F2.winfo_children():
        widget.destroy()
    try:
        with open("Results", 'rb') as fil:
            Label(F2, text="%s %s %s %s" % (
                " Domain Name ",
                " Product Key ",
                " Username/Email ",
                " Api Key "
            )).pack()
            Label(F2, text="%s" % "*"*60).pack()
            Rec = pickle.load(fil)
            c = len(Rec)
            for i in Rec:
                Label(F2, text="%s %s %s %s" %(
                    i["Domain Name"],
                    i["Product Key"],
                    i["Username/Email"],
                    i["Api Key"]
                )).pack()
    except:
        pass


def Enter():
    for widget in F2.winfo_children():
        widget.destroy()
    try:
        fil = open("Results",'ab+')
        if fil.tell() > 0:
            fil.seek(0)
            Rec1 = pickle.load(fil)
        else:
            Rec1 = []

        Rec = {}

        if len(E1.get()) <= 0:
            tkinter.messagebox.showerror(message="Name not entered")
        else:
                Rec["Domain Name"] = E1.get()

        if len(E2.get()) <= 0:
            tkinter.messagebox.showerror(message="Key not entered")
        else:
            Rec["Product Key"] = E2.get()

        if len(E3.get()) <= 0 or '@' not in E3.get():
            tkinter.messagebox.showerror(message="Enter a valid Username/Email")
        else:
                Rec["Username/Email"] = E3.get()

        if len(E4.get()) <= 0:
            tkinter.messagebox.showerror(message="Name not entered")
        else:
                Rec["Api Key"] = E4.get()

        fil.close()
    except:
        pass


Label(root, text="Your Projects and Issues", font=("Arial bold", 30), fg="blue").pack()
F1 = Frame(root, borderwidth=3, relief="solid")
F1.pack(side="left", expand=True, fill="both")
F2 = Frame(root, borderwidth=3, relief="solid")
F2.pack(side="right", expand=True, fill="both")
Label(F2, text="WELCOME TO THE JIRA INSTANCE", font=("trebuchet", 30)).grid(row=0, column=0)

Label(F1, text="Enter Domain Name").grid(row=0, column=0)
E1 = Entry(F1, bd=4)
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

Clr = Button(F1, text="CLEAR",command=Clear)
Clr.grid(row=20, column=1, sticky=NSEW, padx=13, pady=10)

Exit = Button(F1, text="EXIT", command=Exit1, padx=13, pady=10)
Exit.grid(row=20, column=2, sticky=NSEW, padx=13, pady=10)

root.mainloop()
