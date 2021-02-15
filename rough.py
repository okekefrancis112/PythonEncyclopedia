for widget in F2.winfo_children():
        widget.destroy()
    try:
        fil=open("Results",'ab+')
        if fil.tell()>0:
            fil.seek(0)
            Rec1=pickle.load(fil)
        else:
            Rec1=[]

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

        fil.close()