import tkinter as tk
from tkinter import ttk
import pymongo

# Connect to MongoDB Atlas
client = pymongo.MongoClient("your_connection_string")

# Accessing the database
db = client["employee_management"]

# Accessing the collection
collection = db["employees"]

win = tk.Tk()  # Creating a master variable
win.geometry("1350x700+0+0")
win.title("EMPLOYEE MANAGEMENT DATABASE")
# =============================================================#

title_label = tk.Label(win, text="EMPLOYEE MANAGEMENT DATABASE", font=("Arial", 35, "bold"), border=12,
                       relief=tk.GROOVE, bg="white", foreground="blue")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="ENTER DETAILS", font=("Arial", 20), bg="lightgrey", fg="blue", bd=12,
                             relief=tk.GROOVE)
detail_frame.place(x=30, y=90, width=460, height=575)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=500, y=90, width=700, height=575)

EMPID = tk.StringVar()
Name = tk.StringVar()
BIRTHDATE = tk.StringVar()
PHONENUMBER = tk.StringVar()
EMAIL = tk.StringVar()
DEPT = tk.StringVar()
JOB_POSITION = tk.StringVar()
GENDER = tk.StringVar()

Search_by = tk.StringVar()

EMPID_lbl = tk.Label(detail_frame, text="EMP ID", font=('Arial', 15), bg="lightgrey")
EMPID_lbl.grid(row=0, column=0, padx=2, pady=2)

EMPID_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=EMPID)
EMPID_ent.grid(row=0, column=1, padx=2, pady=2)

NAME_lbl = tk.Label(detail_frame, text="NAME", font=('Arial', 15), bg="lightgrey")
NAME_lbl.grid(row=1, column=0, padx=2, pady=2)

NAME_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=Name)
NAME_ent.grid(row=1, column=1, padx=2, pady=2)

BIRTHDATE_lbl = tk.Label(detail_frame, text="BIRTHDATE", font=('Arial', 15), bg="lightgrey")
BIRTHDATE_lbl.grid(row=2, column=0, padx=2, pady=2)

BIRTHDATE_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=BIRTHDATE)
BIRTHDATE_ent.grid(row=2, column=1, padx=2, pady=2)

PHONENUMBER_lbl = tk.Label(detail_frame, text="PHONE NUMBER", font=('Arial', 15), bg="lightgrey")
PHONENUMBER_lbl.grid(row=3, column=0, padx=2, pady=2)

PHONENUMBER_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=PHONENUMBER)
PHONENUMBER_ent.grid(row=3, column=1, padx=2, pady=2)

EMAIL_lbl = tk.Label(detail_frame, text="EMAIL", font=('Arial', 15), bg="lightgrey")
EMAIL_lbl.grid(row=4, column=0, padx=2, pady=2)

EMAIL_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=EMAIL)
EMAIL_ent.grid(row=4, column=1, padx=2, pady=2)

DEPT_lbl = tk.Label(detail_frame, text="DEPT", font=('Arial', 15), bg="lightgrey")
DEPT_lbl.grid(row=5, column=0, padx=2, pady=2)

DEPT_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=DEPT)
DEPT_ent.grid(row=5, column=1, padx=2, pady=2)

JOB_lbl = tk.Label(detail_frame, text="JOB_POSITION", font=('Arial', 15), bg="lightgrey")
JOB_lbl.grid(row=6, column=0, padx=2, pady=2)

JOB_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=JOB_POSITION)
JOB_ent.grid(row=6, column=1, padx=2, pady=2)

GENDER_lbl = tk.Label(detail_frame, text="GENDER", font=('Arial', 15), bg="lightgrey")
GENDER_lbl.grid(row=7, column=0, padx=2, pady=2)

GENDER_ent = ttk.Combobox(detail_frame, font=("Arial", 15), state="readonly", textvariable=GENDER)
GENDER_ent['values'] = ("Male", "Female", "Others")
GENDER_ent.grid(row=7, column=1, padx=2, pady=2)
# ============================================#
# =================button frame ================#

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=40, y=355, width=382, height=130)

def add_employee():
    employee_data = {
        "name": Name.get(),
        "birthdate": BIRTHDATE.get(),
        "phone_number": PHONENUMBER.get(),
        "email": EMAIL.get(),
        "dept": DEPT.get(),
        "job_position": JOB_POSITION.get(),
        "gender": GENDER.get()
    }

    collection.insert_one(employee_data)
    print("Data inserted successfully")

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", font=("arial", 13), width=18, height=2, command=add_employee)
add_btn.grid(row=0, column=0, padx=2, pady=2)

def update_employee():
    filter_query = {"_id": EMPID.get()}
    update_query = {"$set": {
        "name": Name.get(),
        "birthdate": BIRTHDATE.get(),
        "phone_number": PHONENUMBER.get(),
        "email": EMAIL.get(),
        "dept": DEPT.get(),
        "job_position": JOB_POSITION.get(),
        "gender": GENDER.get()
    }}

    collection.update_one(filter_query, update_query)
    print("Data updated successfully")

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", font=("arial", 13), width=18, height=2, command=update_employee)
update_btn.grid(row=0, column=1, padx=2, pady=2)

def delete_employee():
    filter_query = {"_id": EMPID.get()}

    collection.delete_one(filter_query)
    print("Data deleted successfully")

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", font=("arial", 13), width=18, height=2, command=delete_employee)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

# Similarly, define functions for clear, search, and showall buttons...

# ====================================================================================#
win.mainloop()



mongodb+srv://muskan-1234:muskan-1234@cluster0.uk5zslw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
