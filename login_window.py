import tkinter as tk
import MainWindow
import logged_page
import mysql.connector
from tkinter import messagebox

def verify_login(root, entry1, entry2):
    email = entry1.get()
    password = entry2.get()

    if(email=="" or password==""):
        messagebox.showinfo(title="Error", message="Please fill all the fields")
    else:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
        cursor = mycon.cursor()
        query = "SELECT Name FROM register WHERE Email = %s AND Password = %s"  # Using parameterized query to avoid SQL injection
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        if(user is None):
            messagebox.showinfo(title="Error", message="Email or Password is incorrect.")
        else:    
            name=user[0]
            # Fetching Phone number of user
            query = "SELECT Phone FROM register WHERE Email = %s AND Password = %s"  # Using parameterized query to avoid SQL injection
            cursor.execute(query, (email, password))
            num = cursor.fetchone()
            phone=num[0]
            mycon.close()
            
            root.destroy()  # Close the current window
            logged_page.create_window(name,phone)

def back_to_home(root):
    root.destroy()
    MainWindow.create_main_window()


def create_window():
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("380x300")
    root.title("Login Page")
    root.configure(bg="pink")

    label =tk.Label(root,text=" Login ",  bg="pink", font=("Arial", 19), borderwidth=2, relief="solid", height=2 )
    label.place(x=145,y=20)
    label1 = tk.Label(root, text=" Email ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=25,y=100)
    label2 = tk.Label(root, text=" Password ", bg="pink", font=("Arial", 14), height=2)
    label2.place(x=25,y=160)

    entry1 = tk.Entry(root,  font=("Arial", 14))
    entry1.place(x=140,y=105,width=190,height=40)
    entry2 = tk.Entry(root,  font=("Arial", 14), show="*")
    entry2.place(x=140,y=165,width=190,height=40)

    button = tk.Button(root, text="  Signin  ", command=lambda: verify_login(root, entry1, entry2), font=("Arial", 14), height=1, borderwidth=2, relief="solid")
    button.place(x=145,y=230)

    button1 = tk.Button(root, text="Back", command=lambda: back_to_home(root), font=("Arial", 10), height=1, borderwidth=2, relief="solid")
    button1.place(x=320,y=10)
    root.mainloop()

if __name__=="__main__":
    create_window()
