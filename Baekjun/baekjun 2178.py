# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:42:43 2020

@author: Administrator
"""

import sys

inp=sys.stdin.readlines()
maze=[]
for i in range(len(inp)):
    if i==0:
        n,m=map(int,inp[i].split)
    else:
        maze.append(list(map(int,list(inp[i]))))
        

    