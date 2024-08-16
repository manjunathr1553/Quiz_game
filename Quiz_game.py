from tkinter import *

master = Tk()
master.minsize(width=300, height=300)
master.maxsize(width=301, height=301)
master.title("Quiz Game")
master.iconbitmap("qg (1).ico")
global score 
score=0
answered = False
global x
global y

def func(button):  
    global score, answered
    if not answered:
        button.config(bg="green")
        score += 1
        answered = True
    answered = False  

def funct(button, incorrect_button):
    global answered
    if not answered:
        button.config(bg="red")
        incorrect_button.config(bg="green")
        answered = True
    answered = False  
def disable_buttons(q_frame):
    for widget in q_frame.winfo_children():
        if isinstance(widget, Button):
            widget.config(state=DISABLED)

def qp1():
    global lb
    lb.config(text="")
    lb1 = Label(master, text="Question no. 1", fg="red")
    lb1.place(x=10,y=5)
  
    q_frame = Frame(master)  # Set desired width and height
    q1 = Label(q_frame, text="What does CPU stand for?", fg="olive",bg="white",width=40,height=3)
    q1.pack(pady=10)

    q11 = Button(q_frame, text="Central Processing Unit", bg="white", command=lambda: func(q11),width=40)
    q11.pack(pady=5)

    q12 = Button(q_frame, text="Control Processing Unit", bg="white", command=lambda: funct(q12, q11),width=40)
    q12.pack(pady=5)

    q13 = Button(q_frame, text="Central Primary Unit", bg="white", command=lambda: funct(q13, q11),width=40)
    q13.pack(pady=5)

    q14 = Button(q_frame, text="Control Primary Unit", bg="white", command=lambda: funct(q14, q11),width=40)
    q14.pack(pady=5)
    
    nextbut=Button(q_frame,text="Next question",fg="dark red",width=25,command=qp2)
    nextbut.pack(pady=5)

    q_frame.place(x=8, y=20)  # Keep the position adjustment
   
    

def qp2():
    lb1 = Label(master, text="Question no. 2", fg="red")
    lb1.place(x=10,y=5)
    q_frame = Frame(master)
    q2 = Label(q_frame, text="What does GPU stand for?", fg="olive",bg="white",width=40,height=3)
    q2.pack(pady=10)
    
    q21 = Button(q_frame, text="Graphics Processing Unit", bg="white", command=lambda: func(q21),width=40)
    q21.pack(pady=5)

    q22 = Button(q_frame, text="General Processing Unit", bg="white", command=lambda: funct(q22, q21),width=40)
    q22.pack(pady=5)

    q23 = Button(q_frame, text="Graphical User Interface", bg="white", command=lambda: funct(q23, q21),width=40)
    q23.pack(pady=5)

    q24 = Button(q_frame, text="Global Processing Unit", bg="white", command=lambda: funct(q24, q21),width=40)
    q24.pack(pady=5)
    
    nextbut=Button(q_frame,text="Next question",fg="dark red",width=25,command=qp3)
    nextbut.pack(pady=5)
    
    q_frame.place(x=8, y=20)

def qp3():
    lb1 = Label(master, text="Question no. 3", fg="red")
    lb1.place(x=10,y=5)
    q_frame = Frame(master)

    q3 = Label(q_frame, text="What does RAM stand for?",fg="olive",bg="white",width=40,height=3)
    q3.pack(pady=10)

    q32 = Button(q_frame, text="Read Access Memory", bg="white", command=lambda: funct(q32, q33),width=40)
    q32.pack(pady=5)

    q31 = Button(q_frame, text="Read Active Memory", bg="white", command=lambda: funct(q31, q33),width=40)
    q31.pack(pady=5)

    q33 = Button(q_frame, text="Random Access Memory", bg="white", command=lambda: func(q33),width=40)
    q33.pack(pady=5)

    q34 = Button(q_frame, text="Random Active Memory", bg="white", command=lambda: funct(q34, q33),width=40)
    q34.pack(pady=5)
    nextbut=Button(q_frame,text="Next question",fg="dark red",command=qp4,width=25)
    nextbut.pack(pady=5)
    

    q_frame.place(x=8, y=20)
def qp4():  
    
    
    lb1 = Label(master, text="Question no. 4", fg="red")
    lb1.place(x=10,y=5)
    q_frame = Frame(master)

    q4 = Label(q_frame, text="What does PSU stand for?", fg="olive",bg="white",width=40,height=3)
    q4.pack(pady=10)

    q42 = Button(q_frame, text="Peripheral Supply Unit", bg="white", command=lambda: funct(q42, q43),width=40)
    q42.pack(pady=5)

    q41 = Button(q_frame, text="Power Supply Unit", bg="white", command=lambda: func(q41),width=40)  
    q41.pack(pady=5)

    q43 = Button(q_frame, text="Primary Storage Unit", bg="white", command=lambda: funct(q43, q41),width=40)
    q43.pack(pady=5)

    q44 = Button(q_frame, text="Processor Supply Unit", bg="white", command=lambda: funct(q44, q41),width=40)
    q44.pack(pady=5)
    nextbut=Button(q_frame,text="Submit",command=final,fg="dark red",width=25)
    nextbut.pack(pady=5)

    q_frame.place(x=8, y=20)

def quiz_game():
    
    enter = Label(master, text="",width=40,height=30)
    enter.place(x=0,y=0)
    enter_name = Label(master, text="Enter Your Name:", fg="Maroon")
    enter_name .place(x=10,y=50)
    enter_mail = Label(master, text="Enter Your Mail ID:", fg="Maroon")
    enter_mail.place(x=10,y=80)
    global lb
    lb = Label(master, text="Welcome to my computer quiz!", fg="Cyan",font=(1))
    lb.place(x=10,y=10)
    varr=StringVar()
    name=Entry(master,textvariable=varr,fg="red")
    name.place(x=120,y=50)
    mailid=StringVar()
    name=Entry(master,textvariable=mailid,fg="red")
    name.place(x=120,y=80)
    def submit():
        global x
        global y
        x = varr.get().capitalize()
        y=mailid.get().lower()
        lb1.config(text=x,bg="white",width=20,fg="Coral")
        lb1.place(x=120,y=50)
        lb2.config(text=y,bg="white",width=20,fg="Coral")
        lb2.place(x=120,y=80)
        enter_name.config(text="Name:") 
        enter_name .place(x=70,y=50)
        enter_mail.config(text="Mail ID:")
        enter_mail .place(x=70,y=80)
        quiz=Button(master,text="Click here to Start Quiz",bg="cyan",command=qp1,fg="Navy blue")
        quiz.place(x=150,y=120)
      
    submitt=Button(master,text="Submitt",bg="cyan",command=submit,fg="Navy blue")
    submitt.place(x=150,y=120)
    lb1 = Label(master, text="", fg="red")
    lb2=Label(master,text="",fg="red")

def final():
    global x
    global y
    global score
    empty=Label(master,text="",width=45,height=37)
    empty.place(x=0,y=1)
    score_label = Label(master, text=f"  Quiz is over !!👍👍👍\n{x} Your Score is : {score}/ 4  \n ", font=("Ariel", 10, "bold"),fg="Turquoise")
    score_label.place(x=40,y=50)
    score_label = Label(master, text="if you want to restar click the bellow button", font=("Ariel", 10, "bold"),fg="teal")
    score_label.place(x=10,y=130)
    score=0
    quiz=Button(master,text="Restart Quiz...♻️",bg="white",command=quiz_game,height=1,fg="#FFCC00")
    quiz.place(x=10,y=155)
    quiz=Button(master,text="Click here to close...",bg="white",command=close,font=("Ariel", 12, "bold"))
    quiz.place(x=70,y=225)
def close():
    master.destroy()


quiz_game()
master.mainloop()
