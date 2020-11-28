# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:00:08 2020

@author: Administrator
"""

def quicksort(x):
    if len(x)<=1:
        return x
    else:
        pivot=len(x)//2
        less=[]
        equal=[]
        more=[]
        
        for num in x:
            if num <x[pivot]:
                less.append(num)
            elif num==x[pivot]:
                equal.append(num)
            else:
                more.append(num)
    return quicksort(less)+equal+quicksort(more)
                
    