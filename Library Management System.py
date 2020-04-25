import sys
import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import pandas as pd

win = tk.Tk()         
win.title('PYTHON PROJECT')
win.configure(background='#757575',bd=20)

title= ttk.Label(text='LIBRARY MANAGEMENT SYSTEM',font='Times 20 bold')
title.configure(background='#757575',foreground='white')
title.grid(row=0,column=2)

hint_label = ttk.Label(win, text = '* one marked with astrisk are mandatory',font = 'Times 14 bold italic')
hint_label.configure(background='#757575',foreground='red')
hint_label.grid(row=2,column=0, sticky=tk.W)

id_label = ttk.Label(win, text='Enter your ID number/Reference no :*', font='Times 14 bold')
id_label.configure(background='#757575',foreground='white')
id_label.grid(row=3,column=0, sticky=tk.W)
id_var = tk.StringVar()
id_entrybox = ttk.Entry(win, width=40, textvariable=id_var)
id_entrybox.grid(row=3,column=1)
id_entrybox.focus()

type_label = ttk.Label(win, text='Enter membertype :*', font='Times 14 bold')
type_label.configure(background='#757575',foreground='white')
type_label.grid(row=4,column=0, sticky=tk.W)
type_var = tk.StringVar()
type_combobox= ttk.Combobox(win, width=37, textvariable=type_var,state='readonly')
type_combobox['values'] = ("  ","Lecturer","Student","Staff" )
type_combobox.grid(row=4,column=1)

issue_label = ttk.Label(win, text='Enter book you want to issue :*', font='Times 14 bold')
issue_label.configure(background='#757575',foreground='white')
issue_label.grid(row=5,column=0, sticky=tk.W)
issue_var = tk.StringVar()
issue_combobox= ttk.Combobox(win, width=37, textvariable=issue_var,state='readonly')
issue_combobox['values'] = ("     ","Core Python Programming by Dr.R.Nageswara Rao","Digital Communication by Simon Haykin","Microprocessor 8085 by Ramesh Gaonkar",
                            "Engineering Mathematics by Kumbhojkar","Numerical Techniques by J.S.Chitode","Integrated circuits by Ramakant Gaykwad",
                            "Microcontroller 8051 by Mazidi" )
issue_combobox.grid(row=5,column=1)

bid_label = ttk.Label(win, text='Book ID :*', font='Times 14 bold')
bid_label.configure(background='#757575',foreground='white')
bid_label.grid(row=6,column=0, sticky=tk.W)
bid_var = tk.StringVar()
bid_entrybox = ttk.Entry(win, width=40, textvariable=bid_var) 
bid_entrybox.grid(row=6,column=1)

edit_label = ttk.Label(win, text='Edition :*', font='Times 14 bold')
edit_label.configure(background='#757575',foreground='white')
edit_label.grid(row=7,column=0, sticky=tk.W)
edit_var = tk.StringVar()
edit_combobox= ttk.Combobox(win, width=37, textvariable=edit_var,state='readonly')
edit_combobox['values'] = ("  ","First","Second","Third","Fourth","Fifth","Sixth","Seventh")
edit_combobox.grid(row=7,column=1)

idate_label = ttk.Label(win, text='Date of issue :', font='Times 14 bold')
idate_label.configure(background='#757575',foreground='white')
idate_label.grid(row=8,column=0, sticky=tk.W)
idate_var = tk.StringVar()
idate_entrybox = ttk.Entry(win, width=40, textvariable=idate_var)
idate_entrybox.grid(row=8,column=1)
        
rdate_label = ttk.Label(win, text='Date of return :', font='Times 14 bold')
rdate_label.configure(background='#757575',foreground='white')
rdate_label.grid(row=9,column=0, sticky=tk.W)
rdate_var = tk.StringVar()
rdate_entrybox = ttk.Entry(win, width=40, textvariable=rdate_var)
rdate_entrybox.grid(row=9,column=1)

return_label = ttk.Label(win, text='Enter book you want to return :*', font='Times 14 bold')
return_label.configure(background='#757575',foreground='white')
return_label.grid(row=10,column=0, sticky=tk.W)
return_var = tk.StringVar()
return_entrybox = ttk.Entry(win, width=40, textvariable=return_var)
return_entrybox.grid(row=10,column=1)

def done():

    import datetime
    d1=datetime.date.today()
    d2=datetime.timedelta(days=7)
    d3=(d1 + d2)
    idate_var.set(d1)
    rdate_var.set(d3)
    
    userid = id_var.get()
    if userid.isdigit():
        ui = True
    else:
        ui = False
    
    memtype = type_var.get()
    if memtype.isalpha():
        mt = True
    else:
        mt = False
            
    bookissued = issue_var.get()
    if type(bookissued) == str:
        bi = True
    else:
        bi = False
          
    bookid = bid_var.get()
    if type(bookid) == str:
        bd = True
    else:
        bd = False
    
    
    edition = edit_var.get()
    if edition.isalpha():
        ed = True
    else:
        ed = False
    
    bookreturned = return_var.get()
    if type(bookreturned) == str:
        br = True
    else:
        br = False
            
    dateofissue = idate_var.get()
    dateofreturn = rdate_var.get()
 
    if ui == True and mt == True and bi == True and bd == True and ed == True and br == True : 
        print(f'USERID = {userid}\nMEMBER TYPE = {memtype}\nBOOK ISSUED = {bookissued}\nBOOK ID = {bookid}\nEDITION = {edition}\nDATE OF ISSUE = {dateofissue}\nDATE OF RETURN = {dateofreturn}\nBOOK RETURNED = {bookreturned}\n')
        df1=pd.read_excel("C:/Users/AMRUTA/Desktop/PY Project/Book1.xlsx")
        SeriesA=df1['USERID']
        SeriesB=df1['MEMBERTYPE']
        SeriesC=df1['BOOK ISSUED']
        SeriesD=df1['BOOK ID']
        SeriesE=df1['EDITION']
        SeriesF=df1['DATE OF ISSUE']
        SeriesG=df1['DATE OF RETURN']
        SeriesH=df1['BOOK RETURNED']
        
        A=pd.Series(userid)
        B=pd.Series(memtype)
        C=pd.Series(bookissued)
        D=pd.Series(bookid)
        E=pd.Series(edition)
        F=pd.Series(dateofissue)
        G=pd.Series(dateofreturn)
        H=pd.Series(bookreturned)
        
        SeriesA=SeriesA.append(A)
        SeriesB=SeriesB.append(B)
        SeriesC=SeriesC.append(C)
        SeriesD=SeriesD.append(D)
        SeriesE=SeriesE.append(E)
        SeriesF=SeriesF.append(F)
        SeriesG=SeriesG.append(G)
        SeriesH=SeriesH.append(H)
        
        df2=pd.DataFrame({"USERID":SeriesA,"MEMBERTYPE":SeriesB,"BOOK ISSUED":SeriesC,"BOOK ID":SeriesD,"EDITION":SeriesE,"DATE OF ISSUE":SeriesF,"DATE OF RETURN":SeriesG,"BOOK RETURNED":SeriesH})
        df2.to_excel("C:/Users/AMRUTA/Desktop/PY Project/Book1.xlsx",index=False)

        id_entrybox.delete(0,tk.END)
        return_entrybox.delete(0,tk.END)
        rdate_entrybox.delete(0,tk.END)
        idate_entrybox.delete(0,tk.END)
        bid_entrybox.delete(0,tk.END)
        edit_combobox.current(0)
        issue_combobox.current(0)
        type_combobox.current(0)
    
    else:
        done = tk.messagebox.askyesno("Library Management System","You have not enter the mandatory information")
                
submit_btn = tk.Button(win,text = 'SUBMIT',font='Times 14 bold',command=done)
submit_btn.grid(row=11,column=0)
submit_btn.configure(background='#eeeeee')

def close():
    close = tk.messagebox.askyesno("Library Management System","Confirm if you want to exit")
    if close > 0:
        win.destroy()
        return

exit_btn = tk.Button(win,text = 'EXIT',font='Times 14 bold',command=close)
exit_btn.grid(row=11,column=1)
exit_btn.configure(background='#eeeeee')

def reset():
    userid = id_var.set("")
    memtype = type_var.set("")
    bookissued = issue_var.set("")
    bookreturned = return_var.set("")
    dateofissue = idate_var.set("")
    dateofreturn = rdate_var.set("")
    bookid = bid_var.set("")
    edition = edit_var.set("") 
    
reset_btn = tk.Button(win,text = 'RESET',font='Times 14 bold',command=reset)
reset_btn.grid(row=11,column=2)
reset_btn.configure(background='#eeeeee')
win.mainloop()
