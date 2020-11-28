# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:39:09 2020

@author: Administrator
"""
n=int(input())
dice=list(map(int,input().split()))
if n==1:
    print(sum(dice)-max(dice))
else:
    two_surf=[]
    for i in range(6):
        for j in range(6):
            if i!=j and i+j!=5:
                two_surf.append(dice[i]+dice[j])
    two_min=min(two_surf)
    
    three_surf=[]
    a=[0,5]
    b=[1,4]
    c=[2,3]
    for i in a:
        for j in b:
            for k in c:
                three_surf.append(dice[i]+dice[j]+dice[k])
    three_min=min(three_surf)
    
    
    
    
    
    
    one_surf=(n-1)*(n-2)*4*min(dice)+(n-2)*(n-2)*min(dice)+three_min*4+two_min*((n-1)*4+(n-2)*4)
    
    print(one_surf)
