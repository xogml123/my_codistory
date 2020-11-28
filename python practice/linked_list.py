# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:11:56 2020

@author: Administrator
"""

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    

node1=Node(1)
node2=Node(2)
node1.next=node2

print(node1.next)

def add