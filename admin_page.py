import tkinter as tk
import MainWindow
import test_questions
import add_question
import registrations


def log_out(root):
    root.destroy()
    MainWindow.create_main_window()

def Test_Ques(root):
    root.destroy()
    test_questions.create_window()   

def Add_Ques(root):
    root.destroy()
    add_question.create_window()

def Registrations(root):
    root.destroy()
    registrations.create_window()            

def create_window():
    root = tk.Tk()
    root.resizable(False,False)
    root.geometry("500x350")
    root.title("Admin Page")
    root.configure(bg="pink")

    label = tk.Label(root, text=" Admin Page ", bg="pink", font=("Arial", 20), borderwidth=2, relief="solid", height=2)
    label.place(x=160,y=20)
    button1 = tk.Button(root, text=" Test  \nQuestions ", command=lambda: Test_Ques(root), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button1.place(x=30,y=180)
    button2 = tk.Button(root, text="  Add   \nQuestion  ", command=lambda: Add_Ques(root), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button2.place(x=175,y=180)
    button3 = tk.Button(root, text="  Registration \nDetails ", command=lambda: Registrations(root), font=("Arial", 14), height=2, borderwidth=2, relief="solid")
    button3.place(x=325,y=180)
    button4 = tk.Button(root, text="Log out", command=lambda: log_out(root), font=("Arial", 10), height=1, borderwidth=2, relief="solid")
    button4.place(x=420,y=10)


if __name__=="__main__":
    create_window()    
