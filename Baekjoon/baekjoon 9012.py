# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:26:47 2020

@author: Administrator
"""

n=int(input())
case=[]

for i in range(n):
    case.append(list(input()))



for parens in case:
    stk=[]
    pre_no=0
    for paren in parens:
        if paren=='(':
            stk.append('(')
        else:
            if len(stk)!=0:
                stk.pop()
            elif len(stk)==0:
                print('NO')
                pre_no+=1
                break
            
    if len(stk)==0 and pre_no==0:
        print('YES')
    elif len(stk)!=0:
        print('NO')
                
            
        
