# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:06:28 2019

@author: dhruv
"""

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
def search(node,key):
        if node is None or node.key == key:
            return node
        elif key<node.key:
            return search(node.left,key)
        elif key>node.key:
            return search(node.right,key)
    
def insert_node(root,node):
        if root is None:
            root = node
        else:
            if root.key < node.key:
                if root.right is None:
                    root.right = node
                else:
                    insert_node(root.right,node)
            else:
                 if root.left is None:
                    root.left = node
                 else:
                    insert_node(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
        
def preorder(root):
    if root:
        print(root.key)
        preorder(root.left)
        preorder(root.right)

            
def postorder(root):
    if root:
        postorder(root.right)
        print(root.key)
        postorder(root.left)

r = Node(50) 
insert_node(r,Node(10))
insert_node(r,Node(20)) 
insert_node(r,Node(40)) 
insert_node(r,Node(70)) 
insert_node(r,Node(60)) 
insert_node(r,Node(80)) 


inorder(r)
preorder(r)
postorder(r)


