#!/usr/bin/env python3
# -*- coding: utf-8 -*-
        
from pexpect import ExceptionPexpect


class Cell():
    """ Creates an instance of class Cell
    input   -- self : instance of class Cell
    """
    def __init__(self):
        self.value = object
        self.next = None
        
    def __str__(self):
        """ Returns a string representing Cell self
        input   -- self : instance of class Cell
        output  -- string
        """
        result = str(self.value) + ', next:'
        if self.next == None:
            result += 'None'
        else:
            result += str(self.next.value)
        return '{ ' + result + ' }'
        
class StackList:
           
    """
    The class StackList allows to represent a stack implemented by a linked list
    """
    def __init__(self, capacity=100):

        """ Creates an instance of StackList
        input    -- self
        output   -- self is an empty stack
        """
        self.mtop = None            # element at the top of the stack
        self.size = 0               # size of 
        self.capacity = capacity    # size MAX of the stack = 100 by default
        
    def __str__(self):
        """ Returns a string representing the StackList self
        input   -- self : instance of class StackList
        output  -- string
        """
        res=""
        count=0
        if not self.empty_stack():
            x=self.mtop
            while (count<self.size-1):
                res+=str(x.value)+", "
                x=x.next
                count+=1
            res+=str(x.value)
        return res

    def empty_stack(self):
        """ Returns True if the stack self is empty and False otherwise
        input   -- self : instance of class StackList
        output  -- bool
        """
        if self.size==0:
            return True
        return False

    def full_stack(self):
        """ Return True if the stack self is full and False otherwise
        In this version implemented by a list, we don't give the maximum size of the stack
        input   -- self : instance of class StackList
        output  -- bool
        """
        if self.size==self.capacity:
            return True
        return False
    
    def size_stack(self):
        """ Returns the size of the stack
        input   -- self : instance of class StackList
        output  -- size, the size of self
        """
        return self.size

    def push(self, v):
        """ Stacks an element at the top of StackList
        The stack is modified by adding the Cell of value v at the top of the stack
        input    -- self: instance of class StackList
                 -- v : object, value of the Cell to push
                    pre-cond: self is not full
        output   -- self which has been modified
                 post-cond: the size of the stack is incremented
        """
        c=Cell()
        c.value=v
        if not self.full_stack():
            if self.empty_stack():
                self.mtop=c
                self.size+=1
                return self
            c.next=self.mtop
            self.mtop=c
            self.size+=1
            return self
        else :
            raise Exception("Stack full you cant push")

    def top(self):
        """ Returns the element at the top of the stack self
        input   -- self : instance of class StackList
        output  -- t: Cell element 
        """
        if not self.empty_stack():
            return self.mtop
        else :
            raise Exception("Stack empty cant return the top value")
        
    def top_value(self):
        """ Returns the value of the element at the top of the stack self
        input   -- self : instance of class StackList
        output  -- s: object (type of value, attribute of class Cell) 
        """
        if not self.empty_stack():
            return self.mtop.value
        else :
            raise Exception("Stack empty cant return the top value")
    def pop(self):
        """ Unstacks the element at the top of the stack self
        input    -- self : instance of class PileList
                    pre-cond: self is not empty
        output   -- self in which the element at the top of the stack has been unstacked
                  post-cond: the size of the stack is decremented
        """
        if not self.empty_stack():
            self.mtop=self.mtop.next
            self.size-=1
            return self
        else :
            raise Exception("Stack empty you cant pop")


# EXERCICE 1

#Test pile representee par une liste
if __name__ == "__main__":
    print("Hello StackList !")

    

