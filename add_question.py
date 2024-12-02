import tkinter as tk
import admin_page
import mysql.connector
from tkinter import messagebox
from tkinter import *

def clear_all(entry1, entry2, entry3, entry4, entry5):
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)
    entry4.delete(0,tk.END)
    entry5.delete(0,tk.END)

def add_question(root, entry1, entry2, entry3, entry4, entry5, radio1, radio2):
    ques = entry1.get()
    op1 = entry2.get()
    op2 = entry3.get()
    op3 = entry4.get()
    op4 = entry5.get()
    test = radio1.get()
    ans = radio2.get()

    if(ques=="" or op1=="" or op2=="" or op3=="" or op4==""):
        messagebox.showinfo(title="Error", message="Please fill all the fields")
    else:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
        cursor = mycon.cursor()
        id=0
        if(test==1):           #C/C++
            query1 = "SELECT COUNT(id) FROM c_questions"
            cursor.execute(query1,())
            ID = cursor.fetchone()
            id=ID[0]+1

            query2 = "INSERT INTO c_questions VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query2,(id,ques,op1,op2,op3,op4,ans))
            mycon.commit() # changes are reflected in database
            mycon.close()

            messagebox.showinfo(title="Successfull", message="Question added successfully!..")
            root.destroy()
            admin_page.create_window()
        elif(test==2):            #Python
            query1 = "SELECT COUNT(id) FROM py_questions"
            cursor.execute(query1,())
            ID = cursor.fetchone()
            id=ID[0]+1

            query2 = "INSERT INTO py_questions VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query2,(id,ques,op1,op2,op3,op4,ans))
            mycon.commit() # changes are reflected in database
            mycon.close()

            messagebox.showinfo(title="Successfull", message="Question added successfully!..")
            root.destroy()
            admin_page.create_window()
        else:                #Java
            query1 = "SELECT COUNT(id) FROM java_questions"
            cursor.execute(query1,())
            ID = cursor.fetchone()
            id=ID[0]+1

            query2 = "INSERT INTO java_questions VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query2,(id,ques,op1,op2,op3,op4,ans))
            mycon.commit() # changes are reflected in database
            mycon.close()

            messagebox.showinfo(title="Successfull", message="Question added successfully!..")
            root.destroy()
            admin_page.create_window()


def back_to_home(root):
    root.destroy()
    admin_page.create_window()

def create_window():
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("700x720")
    root.title("Add Question")
    root.configure(bg="pink")

    radio1 = tk.IntVar()
    radio2 = tk.IntVar()
    radio1.set(1)
    radio2.set(1)

    label = tk.Label(root, text=" Add Question ", bg="pink", font=("Arial", 20), borderwidth=2, relief="solid", height=2)
    label.place(x=250,y=20)
    label1 = tk.Label(root, text=" Select Test ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=150)
    label1 = tk.Label(root, text=" Enter Question ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=220)
    label1 = tk.Label(root, text=" Enter 1st option ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=290)
    label1 = tk.Label(root, text=" Enter 2nd option ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=360)
    label1 = tk.Label(root, text=" Enter 3rd option ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=430)
    label1 = tk.Label(root, text=" Enter 4th option ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=500)
    label1 = tk.Label(root, text=" Enter answer number ", bg="pink", font=("Arial", 14), height=2)
    label1.place(x=50,y=570)

    R1 = tk.Radiobutton(root, text="C/C++", variable=radio1,font=("Arial", 14), bg="pink" , value=1)  
    R1.place(x=250, y=155)
    R2 = tk.Radiobutton(root, text="Python", variable=radio1,font=("Arial", 14), bg="pink" , value=2)  
    R2.place(x=380, y=155)
    R3 = tk.Radiobutton(root, text="Java", variable=radio1,font=("Arial", 14), bg="pink" , value=3)  
    R3.place(x=510, y=155)
    entry1 = tk.Entry(root,  font=("Arial", 14))
    entry1.place(x=250,y=220,width=400,height=45)
    entry2 = tk.Entry(root,  font=("Arial", 14))
    entry2.place(x=250,y=290,width=400,height=45)
    entry3 = tk.Entry(root,  font=("Arial", 14))
    entry3.place(x=250,y=360,width=400,height=45)
    entry4 = tk.Entry(root,  font=("Arial", 14))
    entry4.place(x=250,y=430,width=400,height=45)
    entry5 = tk.Entry(root,  font=("Arial", 14))
    entry5.place(x=250,y=500,width=400,height=45)
    r1 = tk.Radiobutton(root, text="1", variable=radio2,font=("Arial", 14), bg="pink" , value=1)  
    r1.place(x=300, y=580)
    r2 = tk.Radiobutton(root, text="2", variable=radio2,font=("Arial", 14), bg="pink" , value=2)  
    r2.place(x=380, y=580)
    r3 = tk.Radiobutton(root, text="3", variable=radio2,font=("Arial", 14), bg="pink" , value=3)  
    r3.place(x=460, y=580)
    r4 = tk.Radiobutton(root, text="4", variable=radio2,font=("Arial", 14), bg="pink" , value=4)  
    r4.place(x=520, y=580)

    button1 = tk.Button(root, text=" Clear all ", command=lambda: clear_all(entry1, entry2, entry3, entry4, entry5), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button1.place(x=200,y=650)
    button2 = tk.Button(root, text=" Add question ", command=lambda: add_question(root, entry1, entry2, entry3, entry4, entry5, radio1, radio2), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button2.place(x=380,y=650)
    button3 = tk.Button(root, text="Back", command=lambda: back_to_home(root), font=("Arial", 12), height=1, borderwidth=2, relief="solid")
    button3.place(x=600,y=10)

if __name__ == "__main__":
    create_window()
