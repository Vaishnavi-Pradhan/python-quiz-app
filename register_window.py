import tkinter as tk
import re
import login_window
import MainWindow
import mysql.connector
from tkinter import messagebox

def open_login_window(root, entry1, entry2, entry3, entry4):
    name = entry1.get()
    phone = entry2.get()
    email = entry3.get()
    password = entry4.get()

    name_regex = r"^[A-Za-z\s]+$"
    phone_regex = r"^[1-9][0-9]{9}$"
    email_regex = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$"
    password_regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if(name=="" or phone=="" or email=="" or password==""):
        messagebox.showinfo(title="Error", message="Please fill all the fields")
    elif(not(bool(re.match(name_regex, name)))):
        messagebox.showinfo(title="Error", message="Please enter appropriate Name")
    elif(not(bool(re.match(phone_regex, phone)))):
        messagebox.showinfo(title="Error", message="Please enter appropriate Number")
    elif(not(bool(re.match(email_regex, email)))):
        messagebox.showinfo(title="Error", message="Please enter appropriate email ex.(yahoo@gmail.com)")
    elif(not(bool(re.match(password_regex, password)))):
        messagebox.showinfo(title="Error", message="Password must be of 8 characters which contain 1 Captial letter, 1 Small letter, 1 Digit and 1 Special character.")
    else:    
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
        cursor = mycon.cursor()
        query = "INSERT INTO register VALUES (%s, %s, %s, %s)"  # Using parameterized query to avoid SQL injection
        cursor.execute(query, (name, phone, email, password))
        mycon.commit() # changes are reflected in database
        mycon.close()
        messagebox.showinfo(title="Signup Successfull", message="You are successfully registered!..")
        
        root.destroy()  # Close the current window
        login_window.create_window()

def clear_all(entry1, entry2, entry3, entry4):
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)
    entry4.delete(0,tk.END)

def back_to_home(root):
    root.destroy()
    MainWindow.create_main_window()

def create_window():
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("500x500")
    root.title("Register Page")
    root.configure(bg="pink")

    label = tk.Label(root, text=" Register ", bg="pink", font=("Arial", 20), borderwidth=2, relief="solid", height=2)
    label.place(x=180,y=20)
    label1 = tk.Label(root, text=" Name ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=120)
    label1 = tk.Label(root, text=" Phone No. ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=190)
    label1 = tk.Label(root, text=" Email ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=260)
    label1 = tk.Label(root, text=" Password", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=330)

    entry1 = tk.Entry(root,  font=("Arial", 14))
    entry1.place(x=180,y=125,width=230,height=40)
    entry2 = tk.Entry(root,  font=("Arial", 14))
    entry2.place(x=180,y=195,width=230,height=40)
    entry3 = tk.Entry(root,  font=("Arial", 14))
    entry3.place(x=180,y=265,width=230,height=40)
    entry4 = tk.Entry(root,  font=("Arial", 14), show="*")
    entry4.place(x=180,y=335,width=230,height=40)


    button1 = tk.Button(root, text=" Clear all ", command=lambda: clear_all(entry1, entry2, entry3, entry4), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button1.place(x=120,y=410)
    button2 = tk.Button(root, text="  Signup  ", command=lambda: open_login_window(root, entry1, entry2, entry3, entry4), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button2.place(x=280,y=410)
    button3 = tk.Button(root, text="Back", command=lambda: back_to_home(root), font=("Arial", 10), height=1, borderwidth=2, relief="solid")
    button3.place(x=420,y=10)
    root.mainloop()

if __name__ == "__main__":
    create_window()
