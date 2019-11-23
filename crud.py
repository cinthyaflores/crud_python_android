from tkinter import *

from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='scott', password='password',
                                 host='127.0.0.1',
                                 database='exmaple_crud')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
cursor = cnx.cursor()



def draw_edit_employee_window():
    root = Tk()
    root.config(width=500, height=700)
    new_name_label = Label(root, text="New employee name ", fg="black")
    new_name_label.place(x=50, y=30)
    new_name_entry = Entry(root)
    new_name_entry.place(x=50, y=50)

    new_salary_label = Label(root, text="New employee salary ", fg="black")
    new_salary_label.place(x=50, y=80)
    new_salary_entry = Entry(root)
    new_salary_entry.place(x=50, y=100)

    btn_add_employee = Button(root, text="Add employee", command="update_employee(new_name_entry, new_salary_entry)", bg="blue", fg="black")
    btn_add_employee.place(x=50, y=130)
    mainloop()


def draw_add_employee_window():
    root = Tk()
    root.config(width=500, height=700)
    name_label = Label(root, text="Employee name ", fg="black")
    name_label.place(x= 50, y= 30)
    name_entry = Entry(root)
    name_entry.place(x=50, y=50)

    salary_label = Label(root, text="Employee salary ", fg="black")
    salary_label.place(x= 50, y= 80)
    salary_entry = Entry(root)
    salary_entry.place(x=50, y=100)

    btn_add_employee = Button(root, text="Add employee", command="save_employee(name_entry, salary_entry)", bg="blue", fg="black")
    btn_add_employee.place(x=50, y=130)

    mainloop()


def draw_find_employee_window():
    root = Tk()
    root.config(width=500, height=700)
    id_label = Label(root, text="Employee id ", fg="black")
    id_label.place(x=50, y=30)
    id_entry = Entry(root)
    id_entry.place(x=50, y=50)
    btn_add_employee = Button(root, text="Find employee", command="find_employee(id_entry)", bg="blue", fg="black")
    btn_add_employee.place(x=50, y=130)
    mainloop()


def add_employee(employee_name, employee_salary):
    print(employee_salary)
    print(employee_name)
    insert_query = "INSERT INTO employees(name, salary) VALUES (" + str(employee_name) + ", " + str(employee_salary) + ");"
    cursors.execute(insert_query)
    conn.commit()


def find_employee(employee_id):
    root = Tk()
    select_query = "SELECT * FROM employees WHERE id = " + employee_id + ";"
    cursors.execute(select_query)
    conn.commit()
    if cursors.rowcount == 0:
        Label(root, text="Input the name:", font=("Helvetica", 20)).grid(row=1, column=1)
    mainloop()


def update_employee(employee_id, new_employee_name, new_employee_salary):
    update_query = "UPDATE employees SET name =" + new_employee_name + ", salary = " + new_employee_salary + "WHERE id = " + employee_id + ";"
    cursors.execute(update_query)
    conn.commit()


def draw_delete_employee_window():
    root = Tk()
    root.config(width=500, height=700)
    employee_id_label = Label(root, text="Employee id", fg="black")
    employee_id_label.place(x=50, y=30)
    employee_id_entry = Entry(root)
    employee_id_entry.place(x=50, y=50)
    btn_delete_employee = Button(root, text="Add employee", command="delete_employee(employee_id)", bg="blue", fg="black")
    btn_delete_employee.place(x=50, y=130)
    mainloop()


def delete_employee(employee_id):
    delete_query = "DELETE FROM employees WHERE id = " + employee_id + ";"
    cursors.execute(delete_query)
    conn.commit()


window = Tk()
window.title("Simple CRUD UI example")
window.geometry('800x400')
btn_add_employee = Button(window, text="Add employee", command=draw_add_employee_window, bg="blue", fg="#000")
btn_edit_employee = Button(window, text="Edit employee", command=draw_edit_employee_window, bg="blue", fg="black")
btn_delete_employee = Button(window, text="Delete employee", command=draw_delete_employee_window, bg="blue", fg="black")
btn_find_employee = Button(window, text="Find employee", command=draw_find_employee_window, bg="blue", fg="black")
btn_add_employee.grid(column=1, row=1)
btn_edit_employee.grid(column=1, row=2)
btn_delete_employee.grid(column=1, row=3)
btn_find_employee.grid(column=1, row=4)
mainloop()

