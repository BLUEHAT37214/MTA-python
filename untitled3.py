# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:16:41 2021

@author: harry
"""

from random import randint
x=randint(1,10)
n=0
while n<5:
    a=int(input("猜數字:"))
    if(a>x):
        print("太大")
    elif(a<x):
        print("太小")
    else:
        print("答對了")
        break
    n=n+1
    print("你猜了",n,"次")
print(x)
    
        
    
    

        