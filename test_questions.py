import tkinter as tk
import mysql.connector
import admin_page
from tkinter import ttk

def Ques(root,a):
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
    cursor = mycon.cursor()
    if(a==1):                      #Python questions
        query = "SELECT id,ques,op1,op2,op3,op4,ans FROM py_questions"
        cursor.execute(query, ())
        results = cursor.fetchall()
        label = tk.Label(root, text=" Python Questions ", bg="pink", font=("Arial", 16), height=2)
        label.place(x=680,y=170)
    elif(a==2):                    #Java questions
        query = "SELECT id,ques,op1,op2,op3,op4,ans FROM java_questions"
        cursor.execute(query, ())
        results = cursor.fetchall()
        label = tk.Label(root, text=" Java  Questions ", bg="pink", font=("Arial", 18), height=2)
        label.place(x=680,y=170)
    else:                          #C/C++ questions
        query = "SELECT id,ques,op1,op2,op3,op4,ans FROM c_questions"
        cursor.execute(query, ())
        results = cursor.fetchall()
        label = tk.Label(root, text=" C/C++ Questions ", bg="pink", font=("Arial", 16), height=2)
        label.place(x=680,y=170) 

    # Create a Treeview widget for displaying the results in a table
    tree = ttk.Treeview(root, columns=('No.', 'Questions','Option1','Option2','Option3','Option4', 'Ans'), show='headings')
    tree.heading('No.', text='No.')
    tree.heading('Questions', text='Questions')
    tree.heading('Option1', text='Option1')
    tree.heading('Option2', text='Option2')
    tree.heading('Option3', text='Option3')
    tree.heading('Option4', text='Option4')
    tree.heading('Ans', text='Ans')

    # Set the width of columns to center values
    tree.column('No.', width=50, anchor='center')
    tree.column('Questions', width=600, anchor='center')
    tree.column('Option1', width=180, anchor='center')
    tree.column('Option2', width=180, anchor='center')
    tree.column('Option3', width=180, anchor='center')
    tree.column('Option4', width=180, anchor='center')
    tree.column('Ans', width=80, anchor='center')

    # Insert fetched results into the Treeview
    for result in results:
        tree.insert('', 'end', values=result)
   
    # Apply font to Treeview content
    style = ttk.Style()
    style.configure('Treeview', font=['Arial', 16,'normal'])
    style.configure('Treeview.Heading', font=['Arial', 14,'normal'])

    # Adjust row height
    style.configure('Treeview', rowheight=40)  


    # Place the Treeview widget
    tree.place(relx=0.5, rely=0.65, anchor=tk.CENTER)   
    
    mycon.close()

def back_to_home(root):
    root.destroy()
    admin_page.create_window()

def create_window():
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("1500x750")
    root.title("Questions")
    root.configure(bg="pink")

    label = tk.Label(root, text=" Questions ", bg="pink", font=("Arial", 18), borderwidth=2, relief="solid", height=2)
    label.place(x=710,y=15)
    button1=tk.Button(root, text=" Python ", command=lambda: Ques(root,1), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button1.place(x=550,y=110,width=80,height=40)
    button2=tk.Button(root, text=" Java ", command=lambda: Ques(root,2), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button2.place(x=750,y=110,width=80,height=40)
    button3=tk.Button(root, text=" C/C++ ", command=lambda: Ques(root,3), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button3.place(x=950,y=110,width=80,height=40)
    button = tk.Button(root, text="Back", command=lambda: back_to_home(root), font=("Arial", 10), height=1, borderwidth=2, relief="solid")
    button.place(x=1420,y=10)
    label = tk.Label(root, text=" Python  Questions ", bg="pink", font=("Arial", 16), height=2)
    label.place(x=680,y=170)

    Ques(root,1)

    root.mainloop()


if __name__=="__main__":
    create_window()
