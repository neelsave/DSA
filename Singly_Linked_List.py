#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:29:57 2020

@author: neel
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after(self,prev_node,data):
        if prev_node is None:
            print("the given node is not in a linked list")
            return
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
        
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def delete_node(self,key):
        temp = self.head
        
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
                
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
                
        #if key was not present
        if temp==None:
            return
        
        #unlinking the node
        prev.next = temp.next
        
        temp = None
            
    def delete_node_position(self,position):
        
        #If linked list is empty
        if self.head == None:
            return
        
        #store head node
        temp = self.head
        
        #if the head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        #Find previous node of the node to be deleted
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
            
        #If position is more than a number of nodes
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        
        temp.next = None
        temp.next = next
        
    def delete_list(self):
        temp = self.head
        while temp:
            temp.data = None
            temp = temp.next
        self.head = None
    
    def count(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count
    
    def node_replacement(self,dat1,dat2):
        temp = self.head
        while temp:
            if temp.data == dat1:
                break
            temp = temp.next
        temp2 = self.head    
        while temp2:
            if temp2.data == dat2:
                break
            temp2 = temp2.next
            
        temp.data = dat2
        temp2.data = dat1
        return
    
    def sorting(self):
        temp = self.head
        while temp:
            break
        
        
        
 
if __name__ == "__main__":  
    llist = LL()
    llist.head = Node(1)
    second =  Node(2)
    third = Node(3)
    
    
    llist.head.next = second
    second.next = third
    #llist.printlist()
    
    #list.push(10)
    #llist.printlist()
    
    llist.insert_after(second,100)
    #list.printlist()
    
    llist.append(10100)
    #llist.delete_node(2)
    #llist.delete_node_position(0)
    llist.append(21)
    #llist.delete_list()    
    #llist.printlist()   
    #print(llist.count())
    llist.node_replacement(100,10100)
    print(" ")
    llist.printlist()

