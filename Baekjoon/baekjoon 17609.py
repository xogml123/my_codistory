# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:16:53 2020

@author: Administrator
"""
#Time Over
n=int(input())
palins=[]
stk=[]

for i in range(n):
    palins.append(list(input()))
    
for palin in palins:
    palin_reverse=palin.reverse()
    if palin_reverse==palin:
        print(0)
    else:
        
        check=0
        #for 문 내부에서 len(palin)**2 됨
        for i in range(len(palin)):
            temp=palin
            del temp[i]
            if temp==temp.reverse():
                print(1)
                check=1
                break
        if check==0:
            print(2)
        
            
    
        
    