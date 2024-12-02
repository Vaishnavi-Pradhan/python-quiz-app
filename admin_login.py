import tkinter as tk
import MainWindow
import admin_page
from tkinter import messagebox

def verify_adminLogin(root, entry1, entry2):
    admin = entry1.get()
    password = entry2.get()

    if(admin=="Admin" and password=="Admin"):
        root.destroy()
        admin_page.create_window()
    else:
        messagebox.showinfo(title="Error", message="Name or Password is incorrect.")


def back_to_home(root):
    root.destroy()
    MainWindow.create_main_window()

def create_window():
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("380x300")
    root.title("Admin Login")
    root.configure(bg="pink")

    label =tk.Label(root,text=" Admin Login ",  bg="pink", font=("Arial", 19), borderwidth=2, relief="solid", height=2 )
    label.place(x=120,y=20)
    label1 = tk.Label(root, text=" Admin Name ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=20,y=100)
    label2 = tk.Label(root, text=" Password ", bg="pink", font=("Arial", 14), height=2)
    label2.place(x=25,y=160)

    entry1 = tk.Entry(root,  font=("Arial", 14))
    entry1.place(x=140,y=105,width=190,height=40)
    entry2 = tk.Entry(root,  font=("Arial", 14), show="*")
    entry2.place(x=140,y=165,width=190,height=40)

    button = tk.Button(root, text="  Signin  ", command=lambda: verify_adminLogin(root, entry1, entry2), font=("Arial", 14), height=1, borderwidth=2, relief="solid")
    button.place(x=145,y=230)

    button1 = tk.Button(root, text="Back", command=lambda: back_to_home(root), font=("Arial", 10), height=1, borderwidth=2, relief="solid")
    button1.place(x=320,y=10)
    root.mainloop()

if __name__=="__main__":
    create_window()
