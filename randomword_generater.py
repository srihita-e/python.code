#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:20:24 2021

@author: raghuetukuru
"""

from tkinter import *
import random
root = Tk()
root.title("Random words")
root.geometry("500x500")
root.configure(background='yellow')

label1=Label(root)

def generate_randomword():
    list=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num1=random.randint(1,26)
    num2=random.randint(1,26)
    num3=random.randint(1,26)
    num4=random.randint(1,26)
    num5=random.randint(1,26)
    
    alpha1=list[num1]
    alpha2=list[num2]
    alpha3=list[num3]
    alpha4=list[num4]
    alpha5=list[num5]
    
    label1["text"]=alpha1+alpha2+alpha3+alpha4+alpha5
    
btn=Button(root,text="Generate a random word",command=generate_randomword,bg="royal blue")
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()