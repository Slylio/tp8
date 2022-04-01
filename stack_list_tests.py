#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import stack_list as stl

#%% Test des méthodes __str__, empty_stack, push, size_stack, full_stack
p1 = stl.StackList(100)
print("p1.empty_stack()", p1.empty_stack())
p1.push(1)
p1.push(2)
p1.push(3)
p1.push(4)
p1.push(5)
print("p1:", p1)
print("p1.size_stack() : ", p1.size_stack())


# %% Tests des méthodes top_value, top
p1 = stl.StackList(100)
p1.push(1)
p1.push(2)
p1.push(3)
p1.push(4)
p1.push(5)
print("p1.top_value():", p1.top_value())
print("p1.top():", p1.top())

# %% Tests de la méthode pop
p1 = stl.StackList(100)
p1.push(1)
p1.push(2)
p1.push(3)
p1.push(4)
p1.push(5)
print("p1:", p1)
p1.pop()
print("p1.pop()", p1)