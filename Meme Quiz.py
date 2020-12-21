import tkinter
from tkinter import *
import random
from PIL import Image,ImageTk

#list of questions to be asked

questions=[
    "The woman is yelling at which animal?",
    "What does the 2nd astronaut say?",
    "What is the phrase in this meme?",
    "What is the phrase in this meme?",
    "Which animal is in this meme?",
    "What is the phrase in this meme?",
    "Which famous personality is in this meme?",
    "Barak Obama is awarding the medal to whom",
    "What word is missing in the meme?",
    "What word is missing in the meme?",
    "What word is missing in the meme?",
    "What word is missing in the meme?",
    "What word is missing in the meme?",
    "What word is missing in the meme?",
    "What thing is hulk giving to ant-man?",
    "What word is missing in the meme?",
    "Which living thing is present in the meme?",
    "What is the missing word in the meme?",
    "What is the name of penguin which is asked to do analysis?",
    "What is the missing time period in the meme?"
]

#list of options

choices=[
    ["Dog","Snake","Cat","Monkey"],
    ["I will kill you","Always have been","You didn't know?","No, it is not"],
    ["Stocks","Power","Upgrade","Stonks"],
    ["I see this as an absolute win","Time heist!","My brain is this big","Come here my friend, hug me"],
    ["Penguin","Polar bear","Arctic fox","Sealion"],
    ["Au revoir","Sayonara","Adios","Hasta la vista"],
    ["Tom Hanks","Leonardo Dicaprio","Tom Cruise","George Clooney"],
    ["Captain america","Barak Obama","Donald Trump","Bill Gates"],
    ["The negotiator","The traitor","The general","The greatest"],
    ["Bored","Tired","Happy","Satisfied"],
    ["Heaven","Home","God","Angel"],
    ["Nazi party","Soviet Union","Communist party","Chinese government"],
    ["Pro gamer move","Hack","The greatest move","Rookie move"],
    ["Food","Drinks","Answers","Questions"],
    ["Infinity stones","Taco","Pym particles","His suit"],
    ["Shooting","Running","Firing","Blasting"],
    ["Pegion","Butterfly","Wasp","Sparrow"],
    ["Dragon Balls","Ancient people","Gods","My Guru"],
    ["Rico","Kowalski","Private","Skipper"],
    ["3 years","38 years","51 years","174 years"],
    
]

#creating a list of answers given by user with the help of radiobuttons

answer_selected=[]

#list of correct answers

answer_actual=[2,1,3,0,1,2,1,1,0,3,2,1,0,2,1,3,1,2,1,2]


#generating random numbers to randomize the questions
rand_int=[]
def generator():
    global rand_int
    while(len(rand_int)<20):
        x=random.randint(0,19)
        if x in rand_int:
            continue
        else:
            rand_int.append(x)

#defining a function to create the final look of the quiz, including the score and some text

def result(score):
    question.destroy()
    meme_image.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    result_text=Label(
        root,
        text="RESULTS",
        font=("algerian",50,"bold"),
        background="#B200FF",
    )
    result_text.pack(pady=20)
    result_text1=Label(
        root,
        text=(score,"/20"),
        font=("ariel",40,"bold"),
        background="#00FF41",
    )
    result_text1.pack(pady=30)
    
    #giving different text based on different scores

    b=""
    if score>17:
        b=b+"Excellent, You are a Meme Lord!!!"
    elif 11<score<=17:
        b=b+"Good, You have a decent knowledge about Memes"    
    elif 6<score<=11:
        b=b+"Not Bad, You see memes once in a while"
    elif score<=6:
        b=b+"What are you doing with your life?\nSee some memes and enjoy your life"        

    result_text2=Label(
        root,
        text=b,
        font=("bahnschrift",30),
        background="#ffff00"
    )
    result_text2.pack(pady=30)

#calculating the score

def score_calculator():
    global answer_selected,answer_actual,rand_int
    
    score=0
    y=0
    for i in rand_int:

        if answer_selected[y]==answer_actual[i]:
            score=score+1
        y=y+1    
    result(score)        


#making the window

root=tkinter.Tk()
root.title("Meme Quiz")
root.geometry("1000x600")
root.config(background="#ffff00")

#list of images

img_1=ImageTk.PhotoImage(Image .open("cat.jpg"))
img_2=ImageTk.PhotoImage(Image .open("astronaut.jpg"))
img_3=ImageTk.PhotoImage(Image .open("stonks.jpg"))
img_4=ImageTk.PhotoImage(Image .open("win.jpg"))
img_5=ImageTk.PhotoImage(Image .open("bonjour.jpg"))
img_6=ImageTk.PhotoImage(Image .open("adios.jpg"))
img_7=ImageTk.PhotoImage(Image .open("leo.jpg"))
img_8=ImageTk.PhotoImage(Image .open("obama.jpg"))
img_9=ImageTk.PhotoImage(Image .open("negotiator.jpg"))
img_10=ImageTk.PhotoImage(Image .open("satisfied.jpg"))
img_11=ImageTk.PhotoImage(Image .open("everyday.jpg"))
img_12=ImageTk.PhotoImage(Image .open("soviet union.jpg"))
img_13=ImageTk.PhotoImage(Image .open("pro gamer mave.jpg"))
img_14=ImageTk.PhotoImage(Image .open("nosleep.jpg"))
img_15=ImageTk.PhotoImage(Image .open("taco.jpg"))
img_16=ImageTk.PhotoImage(Image .open("blasting.jpg"))
img_17=ImageTk.PhotoImage(Image .open("pegion.jpg"))
img_18=ImageTk.PhotoImage(Image .open("westrayfurther.jpg"))
img_19=ImageTk.PhotoImage(Image .open("analysis.jpg"))
img_20=ImageTk.PhotoImage(Image .open("51 years.jpg"))

#collecting the images in one list for ease of use
images=[img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10,img_11,img_12,img_13,img_14,img_15,img_16,img_17,img_18,img_19,img_20]

#selecting an option

a=1
def select():
    global answer_selected,variable,r1,r2,r3,r4,question,a
    x=variable.get()
    answer_selected.append(x)
    variable.set(-1)
    if a<20:
        question.config(text=questions[rand_int[a]])
        meme_image.config(image=images[rand_int[a]])
        r1['text']=choices[rand_int[a]][0]
        r2['text']=choices[rand_int[a]][1]
        r3['text']=choices[rand_int[a]][2]
        r4['text']=choices[rand_int[a]][3]
        a=a+1
    else: 
        score_calculator()   

#defining a function to simulate the pressing the start button

def start_press():
    text_areyouready.destroy()
    instructions.destroy()
    start_button.destroy()
    title_meme_quiz.destroy()
    generator()
    start_quiz()
    
#creating questions and options after the quiz is started

def start_quiz():
    global meme_image,question,r1,r2,r3,r4
    
    #adding meme image

    meme_image=Label(
        root,
        image=images[rand_int[0]]
    )
    meme_image.pack()
    
    #the question

    question=Label(
        root,
        text=questions[rand_int[0]],
        font=("BankGothic Md BT",25,"bold"),
        width=600,
        justify="center",
        wraplength=500,
        background="#AE00FF",
        foreground="#ffff00"
    )
    question.pack(pady=20)
    
    #creating buttons
    
    global variable
    variable=IntVar()
    variable.set(-1)

    r1=Radiobutton(
        root,
        text=choices[rand_int[0]][0],
        font=("Bahnschrift",20),
        value=0,
        variable=variable,
        background="#00F2FF",
        command=select

    )
    r1.pack(pady=5)

    r2=Radiobutton(
        root,
        text=choices[rand_int[0]][1],
        font=("Bahnschrift",20),
        value=1,
        variable=variable,
        background="#00F2FF",
        command=select

    )
    r2.pack(pady=5)

    r3=Radiobutton(
        root,
        text=choices[rand_int[0]][2],
        font=("Bahnschrift",20),
        value=2,
        variable=variable,
        background="#00F2FF",
        command=select
    )
    r3.pack(pady=5)

    r4=Radiobutton(
        root,
        text=choices[rand_int[0]][3],
        font=("Bahnschrift",20),
        value=3,
        variable=variable,
        background="#00F2FF",
        command=select

    )
    r4.pack(pady=5)


# creating the starting page 

title_meme_quiz=Label(
    root,
    text="Meme Quiz",
    font=("Jokerman",40,"bold"),
    background="#ffff00"
)
title_meme_quiz.pack()

text_areyouready=Label(
    root,
    text="Are you ready to test your Meme knowledge?",
    font=("BankGothic Lt BT",25),
    background="#FF60D1"
)
text_areyouready.pack(pady=40)

instructions=Label(
    root,
    text="Instructions:\nThis quiz contains 20 questions\nOnce you select an option, you can't change your answer,\nso select carefully\nIf you are ready to begin, Press Start",
    font=("BankGothic Lt BT",20),
    background="#00F2FF"
)
instructions.pack(pady=30)

#adding start button

start_image=PhotoImage(file="start.png")
start_button=Button(
    root,
    image=start_image,
    background="#ff0000",
    command=start_press
)
start_button.pack()


root.mainloop()