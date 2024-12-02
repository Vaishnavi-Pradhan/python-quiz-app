import tkinter as tk
import admin_page
import mysql.connector
from tkinter import ttk

def back_to_home(root):
    root.destroy()
    admin_page.create_window()

def create_window():
    root=tk.Tk()
    root.resizable(False,False)
    root.geometry("500x400")
    root.title("Registrations")
    root.configure(bg="pink")

    label = tk.Label(root, text=" Registrations ", bg="pink", font=("Arial", 20), borderwidth=2, relief="solid", height=2)
    label.place(x=150,y=20)
    button = tk.Button(root, text="Back", command=lambda: back_to_home(root), font=("Arial", 10), height=1, borderwidth=2, relief="solid")
    button.place(x=420,y=10)

    mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
    cursor = mycon.cursor()
    query="SELECT * FROM register"
    cursor.execute(query, ())
    results=cursor.fetchall()

    tree = ttk.Treeview(root, columns=('Name', 'Phone no.','Email'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Phone no.', text='Phone no.')
    tree.heading('Email', text='Email')

    tree.column('Name', width=150, anchor='center')
    tree.column('Phone no.', width=130, anchor='center')
    tree.column('Email', width=180, anchor='center')

    for result in results:
        tree.insert('', 'end', values=result)
   
    style = ttk.Style()
    style.configure('Treeview', font=['Arial', 12,'normal'])
    style.configure('Treeview.Heading', font=['Arial', 14,'normal'])
    style.configure('Treeview', rowheight=30)
    
    tree.place(x=20, y=120, width=460, height=200)

    root.mainloop()

if __name__=="__main__":
    create_window()


