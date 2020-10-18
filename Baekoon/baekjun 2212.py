# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:26:42 2020

@author: Administrator
"""

n=int(input())
k=int(input())
sensors=list(map(int,input().split()))
sensors=set(sensors)
sensors=list(sensors)
sensors.sort()
diff=[]
for i in range(len(sensors)-1):
    diff.append(abs(sensors[i]-sensors[i+1]))
diff.sort(reverse=True)

print(sum(diff[k-1:]))
    
