import tkinter as tk
import py_test
import java_test
import c_test
import MainWindow

def Python_test(root,name,phone):
    root.destroy()
    py_test.create_window(name,phone)

def Java_test(root,name,phone):
    root.destroy()
    java_test.create_window(name,phone)

def C_test(root,name,phone):
    root.destroy()
    c_test.create_window(name,phone)

def back_to_home(root):
    root.destroy()
    MainWindow.create_main_window()

def create_window(name,phone):
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("500x300")
    root.title("Your Page")
    root.configure(bg="pink")

    txt = "Hello, "+name+"...!"
    label1 = tk.Label(root, text=txt, bg="pink", font=("Arial", 22), height=2)
    label1.place(x=125,y=25)
    label2 = tk.Label(root, text="Let's start test", bg="pink", font=("Arial", 16), height=1)
    label2.place(x=180,y=80)
    label2 = tk.Label(root, text="SELECT LANGUAGE", bg="pink", font=("Arial", 18), height=1)
    label2.place(x=125,y=160)

    button1=tk.Button(root, text=" Python ", command=lambda: Python_test(root,name,phone), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button1.place(x=60,y=210,width=80,height=40)
    button2=tk.Button(root, text=" Java ", command=lambda: Java_test(root,name,phone), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button2.place(x=210,y=210,width=80,height=40)
    button3=tk.Button(root, text=" C/C++ ", command=lambda: C_test(root,name,phone), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button3.place(x=350,y=210,width=80,height=40)
    button = tk.Button(root, text="Log out", command=lambda: back_to_home(root), font=("Arial", 10), height=1, borderwidth=2, relief="solid")
    button.place(x=420,y=10)
    root.mainloop()

if __name__=="__main__":
    create_window('Vaishnavi',9877678548)
