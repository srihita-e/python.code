#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:23:26 2021

@author: raghuetukuru
"""

from tkinter import *
root = Tk()
root.title("fibonacci")
root.geometry("400x400")

enter_number = Entry(root)
label = Label(root,text="fibonacci series: ")
label2 = Label(root,text="fibonacci sum: ")

def fibonacci():
    input_no=int(enter_number.get())
    first_no=0
    second_no=1
    sum=0
    sum2=0
    counter=1
    
    while(counter<=input_no):
        label["text"] += str(sum) + " "
        label2["text"] = "fibonacci sum: "+ str(sum2)
        counter=counter+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
        sum2=sum2+sum
        
enter_no.pack()
btn=Button(root,text="Show Fibonacci Series",command=Fibonacci, fg="white", bg="dark blue")
btn.pack()
label.pack()
label2.pack()
root.mainloop()