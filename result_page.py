import tkinter as tk
import mysql.connector
import MainWindow
import logged_page
from tkinter import ttk

def fetch_results(name, phone):
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
    cursor = mycon.cursor()
    query = "SELECT test, marks FROM result WHERE name = %s AND phone = %s"
    cursor.execute(query, (name, phone))
    results = cursor.fetchall()
    mycon.close()
    return results

def try_again(root, name,phone):
    root.destroy()
    logged_page.create_window(name,phone)

def log_out(root):
    root.destroy()
    MainWindow.create_main_window()

def create_window(name,phone,test,marks):
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("500x650")
    root.title("Result Page")
    root.configure(bg="pink")

    mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
    cursor = mycon.cursor()
    query = "INSERT INTO result VALUES (%s, %s, %s, %s)"  # Using parameterized query to avoid SQL injection
    cursor.execute(query, (name, phone, test, marks))
    mycon.commit() # changes are reflected in database
    mycon.close()

    label = tk.Label(root, text=" Result ", bg="pink", font=("Arial", 20), borderwidth=2, relief="solid", height=2)
    label.place(x=180,y=20)
    label1 = tk.Label(root, text="You score", bg="pink", font=("Arial", 18), height=2)
    label1.place(x=120,y=130)
    txt=str(marks)+"/15"
    label2 = tk.Label(root, text=txt, font=("Arial", 18), height=2)
    label2.place(x=270,y=130)

    # Fetch results from the database
    results = fetch_results(name, phone)

    # Create a label for marks
    label3 = tk.Label(root, text="Your Previous Test Marks", bg="pink", font=("Arial", 16), height=2)
    label3.place(x=115,y=240)

    # Create a Treeview widget for displaying the results in a table
    tree = ttk.Treeview(root, columns=('Test', 'Marks'), show='headings')
    tree.heading('Test', text='Test')
    tree.heading('Marks', text='Marks')

    # Set the width of columns to center values
    tree.column('Test', width=150, anchor='center')
    tree.column('Marks', width=150, anchor='center')

    # Insert fetched results into the Treeview
    for result in results:
        tree.insert('', 'end', values=result)
   
    # Apply font to Treeview content
    style = ttk.Style()
    style.configure('Treeview', font=['Arial', 12,'normal'])
    style.configure('Treeview.Heading', font=['Arial', 14,'normal'])

    # Place the Treeview widget
    tree.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    button1 = tk.Button(root, text=" Try Again ", command=lambda: try_again(root,name,phone), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button1.place(x=120,y=580)
    button2 = tk.Button(root, text="  Log out  ", command=lambda: log_out(root), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button2.place(x=280,y=580)
    root.mainloop()


if __name__ == "__main__":
    create_window(None,None,None,None)
