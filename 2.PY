import tkinter as tk
from tkinter import ttk
win = tk.Tk() #creating a master variable
win.geometry("1350x700+0+0")
win.title("EMPLOYEE MANAGEMENT DATABSE")
#=============================================================#

title_label=tk.Label(win,text="EMLOYEE MANAGEMENT DATABASE",font=("Arial",35,"bold"),border=12,relief=tk.GROOVE,bg="white",foreground="blue")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame= tk.LabelFrame(win,text="ENTER DETAILS",font=("Arial",20),bg="lightgrey",fg="blue",bd=12,relief=tk.GROOVE)
detail_frame.place(x=30,y=90,width=460,height=575)

data_frame=tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=500,y=90,width=700,height=575)

EMPID = tk.StringVar()
Name=tk.StringVar()
BIRTHDATE=tk.StringVar()
PHONENUMBER=tk.StringVar()
EMAIL=tk.StringVar()
DEPT=tk.StringVar()
JOB_POSITION=tk.StringVar()
GENDER=tk.StringVar()

Search_by=tk.StringVar()

EMPID_lbl = tk.Label(detail_frame,text="EMP ID",font=('Arial',15),bg="lightgrey")
EMPID_lbl.grid(row=0,column=0,padx=2,pady=2)

EMPID_ent=tk.Entry(detail_frame,bd=7,font=("arial",15),textvariable=EMPID)
EMPID_ent.grid(row=0,column=1,padx=2,pady=2)

NAME_lbl = tk.Label(detail_frame,text="NAME",font=('Arial',15),bg="lightgrey")
NAME_lbl.grid(row=1,column=0,padx=2,pady=2)

NAME_ent=tk.Entry(detail_frame,bd=7,font=("arial",15))
NAME_ent.grid(row=1,column=1,padx=2,pady=2)



BIRTHDATE_lbl = tk.Label(detail_frame,text="BIRTHDATE",font=('Arial',15),bg="lightgrey")
BIRTHDATE_lbl.grid(row=2,column=0,padx=2,pady=2)

BIRTHDATE_ent=tk.Entry(detail_frame,bd=7,font=("arial",15))
BIRTHDATE_ent.grid(row=2,column=1,padx=2,pady=2)

PHONENUMBER_lbl = tk.Label(detail_frame,text="PHONE NUMBER",font=('Arial',15),bg="lightgrey")
PHONENUMBER_lbl.grid(row=3,column=0,padx=2,pady=2)

PHONENUMBER_ent=tk.Entry(detail_frame,bd=7,font=("arial",15))
PHONENUMBER_ent.grid(row=3,column=1,padx=2,pady=2)

EMAIL_lbl = tk.Label(detail_frame,text="EMAIL",font=('Arial',15),bg="lightgrey")
EMAIL_lbl.grid(row=4,column=0,padx=2,pady=2)

EMAIL_ent=tk.Entry(detail_frame,bd=7,font=("arial",15))
EMAIL_ent.grid(row=4,column=1,padx=2,pady=2)

DEPT_lbl = tk.Label(detail_frame,text="DEPT",font=('Arial',15),bg="lightgrey")
DEPT_lbl.grid(row=5,column=0,padx=2,pady=2)

DEPT_ent=tk.Entry(detail_frame,bd=7,font=("arial",15))
DEPT_ent.grid(row=5,column=1,padx=2,pady=2)

JOB_lbl = tk.Label(detail_frame,text="JOB_POSITION",font=('Arial',15),bg="lightgrey")
JOB_lbl.grid(row=6,column=0,padx=2,pady=2)

JOB_ent=tk.Entry(detail_frame,bd=7,font=("arial",15))
JOB_ent.grid(row=6,column=1,padx=2,pady=2)

GENDER_lbl = tk.Label(detail_frame,text="GENDER",font=('Arial',15),bg="lightgrey")
GENDER_lbl.grid(row=7,column=0,padx=2,pady=2)

GENDER_ent = ttk.Combobox(detail_frame,font=("Arial",15),state="readonly")
GENDER_ent['values'] = ("Male","Female","Others")
GENDER_ent.grid(row=7,column=1,padx=2,pady=2)
#============================================#
#================button frame ================#

btn_frame = tk.Frame(detail_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=40,y=355,width=382,height=130)

add_btn = tk.Button(btn_frame,bg="lightgrey",text="Add",font=("arial",13),width=18,height=2)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="lightgrey",text="update",font=("arial",13),width=18,height=2)
update_btn.grid(row=0,column=1,padx=2,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgrey",text="Delete",font=("arial",13),width=18,height=2)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="lightgrey",text="Clear",font=("arial",13),width=18,height=2)
clear_btn.grid(row=1,column=1,padx=2,pady=2)

search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in = ttk.Combobox(search_frame,text="Search",font=("Arial",14),state="readonly")
search_in["values"] = ("EMP ID","NAME","PHONE NUMBER","EMAIL")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn=tk.Button(search_frame,text="search",font=("Arial",13),bd=9,width=12,bg="lightgrey")
search_btn.grid(row=0,column=2,padx=2,pady=2)

showall_btn=tk.Button(search_frame,text="showall",font=("Arial",13),bd=9,width=12,bg="lightgrey")
showall_btn.grid(row=0,column=3,padx=10,pady=2)

#====================================================================================#
main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)
''' EMP ID,NAME,GENDER,BIRTH DAY,PHONE NUMBER EMAIL,DEPT,JOB_POSITION,GENDER'''

EMPLOYEE_TABLE = ttk.Treeview(main_frame,columns=("EMP ID","NAME","BIRTHDATE","PHONE NUMBER","EMAIL","DEPT","JOB_POSITION","GENDER"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=EMPLOYEE_TABLE.yview)
x_scroll.config(command=EMPLOYEE_TABLE.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

EMPLOYEE_TABLE.heading("EMP ID",text="EMP ID")
EMPLOYEE_TABLE.heading("NAME",text="NAME")
EMPLOYEE_TABLE.heading("BIRTHDATE",text="BIRTHDATE")
EMPLOYEE_TABLE.heading("PHONE NUMBER",text="PHONE NUMBER")
EMPLOYEE_TABLE.heading("EMAIL",text="EMAIL")
EMPLOYEE_TABLE.heading("DEPT",text="DEPT")
EMPLOYEE_TABLE.heading("JOB_POSITION",text="JOB_POSITION")
EMPLOYEE_TABLE.heading("GENDER",text="GENDER")

EMPLOYEE_TABLE['show'] = " headings "

EMPLOYEE_TABLE.column("EMP ID",width=100)
EMPLOYEE_TABLE.column("NAME",width=100)
EMPLOYEE_TABLE.column("BIRTHDATE",width=100)
EMPLOYEE_TABLE.column("PHONE NUMBER",width=100)
EMPLOYEE_TABLE.column("EMAIL",width=100)
EMPLOYEE_TABLE.column("DEPT",width=100)
EMPLOYEE_TABLE.column("JOB_POSITION",width=100)
EMPLOYEE_TABLE.column("GENDER",width=100)






EMPLOYEE_TABLE.pack(fill=tk.BOTH,expand=True)




win.mainloop()
