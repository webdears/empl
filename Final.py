import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymongo


# Connect to MongoDB Atlas
try:
    client = pymongo.MongoClient("mongodb+srv://muskan-1234:muskan-1234@cluster0.uk5zslw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    print("Connection to MongoDB Atlas successful")
except pymongo.errors.ConnectionFailure:
    print("Could not connect to MongoDB Atlas")


# db
db = client["employee_management"]

# Accessing the collection
collection = db["employees"]

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("EMPLOYEE MANAGEMENT DATABASE")


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
Search_val = tk.StringVar()

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


search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)
search_lbl = tk.Label(search_frame, text="Search ", bg="lightgrey", font=("Arial", 10))
search_lbl.grid(row=0, column=0, padx=7, pady=7)




def on_combobox_select(event):
    if search_in.get() != "Search":
        search_entry.config(state='normal')
        search_entry.grid(row=0, column=2, padx=12, pady=2)
        search_entry.delete(0, tk.END)
    else:
        search_entry.grid_forget()


search_in = ttk.Combobox(search_frame, text="Search", font=("Arial", 14), state="readonly")
search_in["values"] = ("Search", "EMP ID", "NAME", "PHONE NUMBER", "EMAIL")
search_in.grid(row=0, column=1, padx=2, pady=2)
search_in.bind("<<ComboboxSelected>>", on_combobox_select)



def search():
    map={
        "EMP ID":"emp_id", "NAME":"name", "PHONE NUMBER":"phone_number", "EMAIL":"email"

    }
    search_option = search_in.get()
    search_text = search_entry.get()

    if search_text!="":
        dropdown = map[search_option]

        regex_pattern = f"^{search_text}$"
        employee=collection.find_one({dropdown:  {"$regex": regex_pattern, "$options": "i"}})
        print(employee)
        if( employee!=None):
            EMPLOYEE_TABLE.delete(*EMPLOYEE_TABLE.get_children())
            EMPLOYEE_TABLE.insert('', 'end', values=(
                employee["emp_id"], employee["name"], employee["DOB"], employee["phone_number"], employee["email"],
                employee["dept"], employee["position"], employee["gender"]))
        else:

            show_message_dialog("Employee Details Not Found")
        # Perform the search operation based on the selected option and search text
        print("Searching for:", dropdown, search_text)
    else:
        show_message_dialog("Please Select DropDown and Enter Search Value")


search_entry = tk.Entry(search_frame, font=("Arial", 14),textvariable="Search_val")
search_entry.grid(row=0, column=2, padx=2, pady=2)
search_entry.config(state='disabled')
search_entry.grid_forget()
search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=2, width=8, bg="lightgrey", command=search)
search_btn.grid(row=0, column=3, padx=2, pady=2)


# for that five buttons
btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=40, y=355, width=382, height=130)

def reset():
    clear()
    search_entry.delete(0, tk.END)
    search_in.set("Search")
    search_entry.grid_forget()
    list_employees()

reset = tk.Button(btn_frame, text="Reset Search", font=("arial", 13), width=18, height=1, bg="lightgrey",command=reset)
reset.grid(row=2, column=0,columnspan=2, padx=2, pady=2)




def list_employees():
    EMPLOYEE_TABLE.delete(*EMPLOYEE_TABLE.get_children())
    employees = collection.find()
    clear()
    EMPID_ent.config(state='normal')
    print(employees)
    for employee in employees:
        EMPLOYEE_TABLE.insert('', 'end', values=(
        employee["emp_id"], employee["name"], employee["DOB"], employee["phone_number"], employee["email"],
        employee["dept"], employee["position"], employee["gender"]))

list_btn = tk.Button(btn_frame, bg="lightgrey", text="List All", font=("arial", 13), width=18, height=1, command=list_employees)
list_btn.grid(row=1, column=1, padx=2, pady=2)



def add_employee():
    insert=True
    if(EMPID.get()=="" or Name.get()=="" or BIRTHDATE.get()=="" or PHONENUMBER.get()=="" or EMAIL.get()=="" or DEPT.get()==""
    or JOB_POSITION.get()=="" or GENDER.get()==""):
        insert=False
    if(insert):

        employee_data = {
            "emp_id":EMPID.get(),
            "name": Name.get(),
            "DOB": BIRTHDATE.get(),
            "phone_number": PHONENUMBER.get(),
            "email": EMAIL.get(),
            "dept": DEPT.get(),
            "position": JOB_POSITION.get(),
            "gender": GENDER.get()
        }
        state = EMPID_ent['state']
        if state == 'disabled':
            show_message_dialog("Employee Id Already Registered")

        else:

            collection.insert_one(employee_data)
            list_employees()
            show_message_dialog("Employee Registered Successfully")
        print("Data inserted successfully")
    else:
        show_message_dialog("Please Enter All the details")

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", font=("arial", 13), width=18, height=1, command=add_employee)
add_btn.grid(row=0, column=0, padx=2, pady=2)



def update_employee():
    if (EMPID.get()!=""):
        filter_query = {"emp_id": EMPID.get()}
        update_query = {"$set": {
            "name": Name.get(),
            "DOB": BIRTHDATE.get(),
            "phone_number": PHONENUMBER.get(),
            "email": EMAIL.get(),
            "dept": DEPT.get(),
            "position": JOB_POSITION.get(),
            "gender": GENDER.get()
        }}
        show_message_dialog("Employee Updated Successfully")
        collection.update_one(filter_query, update_query)
        clear()
        list_employees()
        print("Data updated successfully")
    else:
        show_message_dialog("Please Select Employee To update")

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", font=("arial", 13), width=18, height=1, command=update_employee)
update_btn.grid(row=0, column=1, padx=2, pady=2)



def delete_employee():
    if (EMPID.get()!=""):
        filter_query = {"emp_id": EMPID.get()}
        result = messagebox.showinfo("Message", "Confirm Delete Employee ?", detail="Press Ok to Delete Employee " + Name.get())
        if result == "ok":
            collection.delete_one(filter_query)
            list_employees()
            clear()
            show_message_dialog("Employee Deleted Successfully")
        else:
            print("Close button clicked")
    else:
        show_message_dialog("Please Select Employee To Delete")


    print("Data deleted successfully")

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", font=("arial", 13), width=18, height=1, command=delete_employee)
delete_btn.grid(row=1, column=0, padx=2, pady=2)




def show_message_dialog(message):
    # Create a messagebox with "OK" and "Close" buttons
    result = messagebox.showinfo("Message", message)




def clear():
    EMPID.set('')
    Name.set('')
    BIRTHDATE.set('')
    PHONENUMBER.set('')
    EMAIL.set('')
    DEPT.set('')
    JOB_POSITION.set('')
    GENDER.set('')


def on_select(event):
    selected_item = EMPLOYEE_TABLE.selection()[0]
    values = EMPLOYEE_TABLE.item(selected_item, 'values')
    EMPID_ent.config(state='disabled')
    EMPID.set(values[0])
    Name.set(values[1])
    BIRTHDATE.set(values[2])
    PHONENUMBER.set(values[3])
    EMAIL.set(values[4])
    DEPT.set(values[5])
    JOB_POSITION.set(values[6])
    GENDER.set(values[7])

# table
main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)
''' EMP ID,NAME,GENDER,BIRTH DAY,PHONE NUMBER EMAIL,DEPT,JOB_POSITION,GENDER'''

EMPLOYEE_TABLE = ttk.Treeview(main_frame,columns=("EMP ID","NAME","BIRTHDATE","PHONE NUMBER","EMAIL","DEPT","JOB_POSITION","GENDER"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

# Add this line to center align text in cells
style = ttk.Style()
style.configure("Treeview.Heading", justify="center")
style.configure("Treeview", font=('Arial', 12), rowheight=25, bd=10, background="lightgrey", fieldbackground="lightgrey", justify="center")


style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

y_scroll.config(command=EMPLOYEE_TABLE.yview)
x_scroll.config(command=EMPLOYEE_TABLE.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

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
EMPLOYEE_TABLE.bind('<<TreeviewSelect>>', on_select)

win.mainloop()
