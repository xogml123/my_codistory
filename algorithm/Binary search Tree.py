class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.head=Node(None)

    def search(self,item):
        if self.head.val==None:
            return False
        else:
            return self.__search_node(self.head,item)
    def __search_node(self,cur,item):
        if item==cur.val:
            return True
        elif item<cur.val:
            if cur.left==None:
                return False

            else:
                return self.__search_node(cur.left,item)
        elif item>cur.val:
            if cur.right==None:
                return False
            else:
                return self.__search_node(cur.right,item)


    def add(self,item):
        if self.head.val==None:
            self.head.val=item
        else:
            self.__add_node(self.head,item)
    def __add_node(self,cur,item):
        if cur.val >= item:
            if cur.left !=None:
                self.__add_node(cur.left,item)
            else:
                cur.left=Node(item)
        else:
            if cur.right !=None:
                self.__add_node(cur.right,item)
            else:
                cur.right=Node(item)

