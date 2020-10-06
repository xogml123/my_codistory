class Node:
    def __init__(self,value):
        self.value=value
        self.left,self.right=None,None
    
class Nodemk:
    def __init__(self,head):
        self.head=head
    def insert(self,node):
        self.current_node=self.head