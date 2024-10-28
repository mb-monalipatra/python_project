# def sum(a,b):
#     c=a+b
#     return c

# def mul(a,b):
#     c=a*b
#     return c
# #import modules
# #print(modules.sum(10,20))
# #(or):===
# #from modules import sum
# #print(sum(10,20))
# ##(or):=====
# from modules import *
# print(sum(10,20))
# print(mul(10,20))

#1.)MATH MODULE:===================================================================================

#[math.ceil(),fabs(),factorial(),floor(),fsum(),sqrt():=======]

# import math
# x=10.5
# y=-10
# z=5
# p=30.6
# q=[10,20,30,40]
# r=16
#print(math.ceil(x))
#print(math.fabs(y))
#print(math.factorial(z))
#print(math.floor(p))
#print(math.fsum(q))
#print(math.sqrt(r))

#2.)RANDOM MODULE:=================================================================================

#[randint(),randrange(),choice(),random(),shuffle(),uniform()]

# import random
#l=["apple","orange","pineapple","carrot"]
#print(random.randint(5,10))
#print(random.randrange(3,9)) #3->included but 9-> not included
#print(random.choice(l))

#random():==
#r = random.random()
#print(r)

#shuffle():===

# i=[10,20,30,40]
# random.shuffle(i)
# print(i)

#uniform():==
# u=random.uniform(3,9)
# print(u)

#3.)DATETIME MODULE:=========================================================================

# import datetime
# x=datetime.datetime.now()
# y=x.strftime("%y")
# z=x.strftime("%B")
# print(z)


str="monali"
for i in enumerate(str):
    print(i)



    