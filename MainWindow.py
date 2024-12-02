import tkinter as tk
import login_window
import admin_login
import register_window

def open_login_window(root):
    root.destroy()  # Close the current window
    login_window.create_window()

def open_adminLogin_window(root):
    root.destroy()  # Close the current window
    admin_login.create_window()

def open_register_window(root):
    root.destroy()  # Close the current window
    register_window.create_window()    

def create_main_window():
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("450x400")
    root.title("Home Page")
    root.configure(bg="pink")

    label1 = tk.Label(root,text=" Computer Languages Test ",font=("Arial", 20), height=2, borderwidth=2, relief="solid", bg="pink")
    label1.place(x=50,y=20)

    para = "Whether you are a beginner or an\nexperienced programmer, our platform \nis here to help you to enhance your skills\nand knowledge of computer languages."
    label2 = tk.Label(root,text=para,font=("Arial", 16), height=5, bg="pink")
    label2.place(x=35,y=130)
    
    button1 = tk.Button(root, text="Register", command=lambda: open_register_window(root), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button1.place(x=50,y=290)
    
    button2 = tk.Button(root, text="  Login  ", command=lambda: open_login_window(root), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button2.place(x=160,y=290)

    button3 = tk.Button(root, text=" Admin Login  ", command=lambda: open_adminLogin_window(root), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button3.place(x=270,y=290)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
