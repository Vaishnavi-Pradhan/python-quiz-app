import random
import mysql.connector
import tkinter as tk
from tkinter import *
import result_page

def create_window(name,phone):
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="password", database="project")  # write your mysql password
    cursor = mycon.cursor()
    
    query1 = "SELECT COUNT(id) FROM java_questions"
    cursor.execute(query1,())
    ID = cursor.fetchone()
    id=ID[0]
    #print(id)
    
    # Generate a list of 15 unique random numbers
    ran = random.sample(range(1, id), 15)
    
    #print(ran)

    root=tk.Tk()
    root.geometry("750x700")
    root.title("Java Test")
    root.resizable(False, False)

    selected_answers = []      #Address of each objects
    answers = []             #Values of selected radio buttons
    db_ans = []            #Answers stored in database in the form of values

    def check_answers():
        for ans in selected_answers:
            i = ans.get()                  #By get function we will get the actual selected value of radio buttons
            answers.append(i)

        print(answers)
        print(db_ans)

        points = 0
        for i in range(15):
            sel = answers[i]
            a_ans = db_ans[i]
            if(sel == a_ans):
                points += 1
    
        root.destroy()
        result_page.create_window(name,phone,"Java",points)

    f = Frame(root)
    f.pack(fill=BOTH, expand=True)

    # Create a canvas widget
    canvas = Canvas(f)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a frame to hold questions and options
    inner_frame = Frame(canvas)
    inner_frame.pack(fill=BOTH, expand=True)
    inner_frame.configure(bg="pink")
    
    label=tk.Label(inner_frame,text=" Java Test ",wraplength=300,bg="pink", font=("Arial", 22), borderwidth=2, relief="solid", height=2)
    label.pack(padx=250,pady=30, anchor="n")
    
    for i,v in enumerate(ran):
        query = "SELECT ques FROM java_questions WHERE id=%s"
        cursor.execute(query,(v,))
        ques=cursor.fetchone()
        q=ques[0]
        n=str(i+1)
        txt=n+") "+q
        label1=tk.Label(inner_frame,text=txt,wraplength=670,bg="pink",justify="left", font=("Arial", 16))
        label1.pack(padx=50,pady=50, anchor="w")

        query = "SELECT op1 FROM java_questions WHERE id=%s"
        cursor.execute(query,(v,))
        option=cursor.fetchone()
        op=option[0]

        ans_var = IntVar()
        selected_answers.append(ans_var)
    
        r1=tk.Radiobutton(inner_frame,text=op,wraplength=670,bg="pink",font=("Arial", 16),justify="left",value=1, variable=ans_var)
        r1.pack(padx=50,anchor="w")

        query = "SELECT op2 FROM java_questions WHERE id=%s"
        cursor.execute(query,(v,))
        option=cursor.fetchone()
        op=option[0]
        r1=tk.Radiobutton(inner_frame,text=op,wraplength=670,bg="pink",font=("Arial", 16),justify="left",value=2, variable=ans_var)
        r1.pack(padx=50,anchor="w")

        query = "SELECT op3 FROM java_questions WHERE id=%s"
        cursor.execute(query,(v,))
        option=cursor.fetchone()
        op=option[0]
        r1=tk.Radiobutton(inner_frame,text=op,wraplength=670,bg="pink",font=("Arial", 16),justify="left",value=3, variable=ans_var)
        r1.pack(padx=50,anchor="w")

        query = "SELECT op4 FROM java_questions WHERE id=%s"
        cursor.execute(query,(v,))
        option=cursor.fetchone()
        op=option[0]
        r1=tk.Radiobutton(inner_frame,text=op,wraplength=670,bg="pink",font=("Arial", 16),justify="left",value=4, variable=ans_var)
        r1.pack(padx=50,anchor="w")

        query = "SELECT ans FROM java_questions WHERE id=%s"
        cursor.execute(query,(v,))
        ans=cursor.fetchone()
        db_ans.append(ans[0])

    submit_button = Button(inner_frame, text="Submit",font=("Arial", 20), relief="solid", borderwidth=2, command=check_answers)
    submit_button.pack(padx=50,pady=50)

    mycon.close()    

    # Update canvas scroll region
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", update_scroll_region)

    # Create a scrollbar for the canvas
    scrollbar = Scrollbar(f, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.config(yscrollcommand=scrollbar.set)

    
    canvas.create_window((0,0), window=inner_frame, anchor="nw")


    root.mainloop()


if __name__=="__main__":
    create_window(None)

