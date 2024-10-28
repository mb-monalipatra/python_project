##OOps Concept:=======

# class Student:
#     name ="monali"

# s1 = Student()
# print(s1.name)

##using constructor(__init__):===

# class Student:
#     def __init__(self,name):
#         self.name = name
#         print("adding some student data inside the database..")

# s1=Student("monali")
# print(s1.name)

##using methods:=====


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome students...",self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("monali",98)
# s1.welcome()
# print(s1.get_marks())

##Q.)create student class that takes name and marks of 3 subjects as arguments in constructor.Then craete a method to print the avg.

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks


#     def get_avg(self):
#         sum=0
#         for value in self.marks:
#             sum+=value
#         print("hi",self.name,"your avg score is:",sum/3)


# s1=Student("monali",[90,80,70])
# s1.get_avg()


#ex:=====
# base class
# class Animal:
#     def eat(self):
#         print( "I can eat!")
    
#     def sleep(self):
#         print("I can sleep!")

# derived class
# class Dog(Animal):
#     def bark(self):
#         print("I can bark! Woof woof!!")

# # Create object of the Dog class
# dog1 = Dog()

# # Calling members of the base class
# dog1.eat()
# dog1.sleep()

# # Calling member of the derived class
# dog1.bark()


##Ex:=====

# class Computer :
#     def __init__(self,maxprice):
#         self.maxprice=8000
#     def sell(self):
#         print("selling price:{}".format(self.maxprice))

#     def setMaxprice(self,price):
#         self.setMaxprice=price

# c1=Computer()
# print(c1.maxprice)
# c1.sell()
# c1.setMaxprice(20000)
# c1.sell()




##Q..w.a.p to create a Student class and creates an object to it. Call the method talk() to display student details..
# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def talk(self):
#         print("my name is :",self.name)
#         print("my rollno :",self.rollno)
#         print("my marks are :",self.marks)

# s1=Student("monali",24,[90,80,70])
# s1.talk()

# ##Ex:===
# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def display(self):
#         print("student name :{}\nrollno:{}\nmarks;{}".format(self.name,self.rollno,self.marks))

# s1=Student("monali",34,[90,68,89])
# s1.display()
# s2=Student("manisha",56,[80,78,50])
# s2.display()


##Ex:==(movies)

# class Movie:
#     def __init__(self,moviename,hero,rating):
#         self.moviename=moviename
#         self.hero=hero
#         self.rating=rating
#     def info(self):
#         print("movie name:",self.moviename)
#         print("hero name:",self.hero)
#         print("rating:",self.rating)

#m=Movie("bahubali","mahesh",9)
#m.info()


##using constructor:==]

# class Movie:
#     def __init__(self,moviename,hero,rating):
#         self.moviename=moviename
#         self.hero=hero
#         self.rating=rating
#     def info(self):
#         print("movie name:",self.moviename)
#         print("hero name:",self.hero)
#         print("rating:",self.rating)

# movies=[Movie('Spider','Mahesh',30),
#         Movie('Bahubali','Prabhas',30),
#         Movie('Geethagovindam','Vijay',90)]
# for movie in movies:
#     movie.info()


##Ex:====
# class College:
#     def __init__(self,name,rollno,section):
#         self.name = name
#         self.rollno = rollno
#         self.section =  section
#     def info(self):
#         print("name:",self.name)
#         print("rollno:",self.rollno)
#         print("section:",self.section)

# c=College("monali",34,"A")
# c.info()

#[INSTANCE VARIABLE:===============]

##1.)Inside constructor by using self variable:=============================================


# class Employee:
#     def __init__(self):
#         self.eno=100
#         self.ename="monali"

# e=Employee()
# print(e.__dict__)


##2.)inside instance method by using self variable:=========================================


# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20

#     def m1(self):
#         self.c=30
 
# t=Test()
# t.m1()
# print(t.__dict__)


##3.) Outside of the class by using object reference variable.

# class Test:
#     def __init__(self):
#         self.a=100
#         self.b=200
#     def m2(self):
#         self.c=300

# t=Test()
# t.m2()
# t.d=400
# print(t.__dict__)

##Q.)how to access????

# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20

#     def display(self):
#         print(self.a)
#         print(self.b)

# t=Test()
# t.display()
# print(t.a,t.b)


##Q.)how to delete??????

#i.) within class:===

# class Test:
#     def __init__(self):
#         self.a=100
#         self.b=200
#         self.c=300
#         self.d=400
#     def display(self):
#         del self.d

# t=Test()
# t.display()
# print(t.__dict__)

##ii.)from outside of class:====

# class Test:
#     def __init__(self):
#         self.a=1000
#         self.b=2000
#         self.c=3000
# t=Test()
# del t.a
# print(t.__dict__)


##[STATIC VARIABLE:=========================================]

# class Test:
#     x=100
#     def __init__(self):
#         self.y=200

# t1=Test()
# t2=Test()
# print("t1:",t1.x,t1.y)
# t2.x=900
# t2.y=600
# print("t2:",t2.x,t2.y)


##using @staticmethod:====
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

#     @staticmethod
#     def hello():
#         print("welcome students...")

#     def info(self):
#         print("my name is:",self.name)
#         print("my rollno:",self.rollno)

# s=Student("monali",67)
# s.hello()
# s.info()


##[LOCAL VARIABLES:==================================]

# ##EX:===
# class Test:
#     def m1(self):
#         a=1000
#         print(a)
#     def m2(self):
#          b=2000
#          print(b)

# t=Test()
# t.m1(),t.m2()


##[INSTANCE METHOD:=================]

# class Student:
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks= marks
#     def display(self):
#         print("hello ",self.name)
#         print("your marks are: ",self.marks)
#     def grade(self):
#         if self.marks >=60:
#             print("you got first grade...")
#         elif self.marks >=50:
#             print("you got second grade...")
#         elif self.marks >=35:
#             print("you got third grade...")
#         else:
#             print("you are fail...")

# n=int(input("enter no.:"))
# for i in range(n):
#     name=input("enter name: ")
#     marks=int(input("enter any marks: "))
#     s=Student(name,marks)
#     s.display()
#     s.grade()


##using getter and setter method:======

# class Bank:
#     def __init__(self,acc,bal):
#         self.acc=acc
#         self.bal=bal
#     def debit(self,amount):
#         self.bal-=amount
#         print("Rs." ,amount,"was debited....")
#         print("total balance= ",self.get_bal())

#     def credit(self,amount):
#         self.bal+=amount
#         print("Rs.",amount,"was credited...")
#         print("total balance= ",self.get_bal())

#     def get_bal(self):
#         return self.bal

# b1=Bank(1000,2000)
# b1.debit(500)
#b1.credit(200)

##[public attributes:======================]
# class Test:
#         x=10
#         def __init__(self):
#           self.y=20

# t1=Test()
# print(t1.x)
# print(t1.y)

##[protected attribute:===================]
# class Test:
#     _x=20
#     def __init__(self):
#         self._y=30

# t1=Test()
# print(t1._x)
# print(t1._y)



##[EX:(private attribute)======================]

# class Test: 
#        x=10 
#        _y=20 
#        __z=30 
#        def m1(self): 
#            print(Test.x) 
#            print(Test._y) 
#            print(Test.__z)

# t1=Test()
# t1.m1()
# print(Test.x) 
# print(Test._y) 
# print(Test.__z)


##EX:=====
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.acc_pass=acc_pass
#     def reset_pass(self):
#         print(self.__acc_no)



# acc1=Account("12345","abcdefg")
# print(acc1.acc_no)
# #print(acc1.acc_pass)
# print(acc1.reset_pass) 


##[INHERITANCE:=============================================]

##1.)Single inheritance:========
# class Car:
#     @staticmethod
#     def start():
#         print("car started....")
    
#     @staticmethod
#     def stop():
#         print("car stoped......")

# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name= name

# car1=Toyotacar("Fortuiner")
# car2=Toyotacar("Prius")
#print(car1.start())

##2.)multi-level inheriance:========
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped...")
# class Toyotacar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(Toyotacar):
#     def __init__(self,type):
#         self.type=type

# car1=Fortuner("diesel")
# car1.start()


##3.)Multiple inheritance:================
# class A:
#     varA="welcome to class A"
# class B:
#     varB="welcome to class B"
# class C(A,B):
#     varC="welcome to class C"

# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

##[super method():==============================]
# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("car started..........")
#     def stop():
#         print("car stopped.......")
    
# class Toyotacar(Car):
#     def __init__(self,name,type):
#         self.name=name
#         #self.type=type
#         super().__init__(type)
#         super().start()
# c1=Toyotacar("prius","electric")
# print(c1.name)
# print(c1.type)

##[@classmethod:===================================================================]


# class Person:
#     name="Anonumous"

#     def ChangeName(self,name):
#         self.name = name

# p1=Person()
# p1.ChangeName("Monali")
# print(p1.name)
# print(Person.name)

##(we want to change class attribute without using @classmethod):=======================================

# class Person:
#     name="Anonumous"

#     def ChangeName(self,name):
#         #Person.name=name
#         self.__init__.name=name


# p1=Person()
# p1.ChangeName("Monali")
# print(p1.name)
# print(Person.name)

##[property method:==================================]

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

#     #def CalcPercentage(self):
#       #  self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"

# stu1=Student(98,97,99)
# #print(stu1.percentage)
# stu1.phy=89
# #print(stu1.phy)
# #stu1.CalcPercentage()
# print(stu1.percentage)

##[polymorphism:=================================================================================]

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showvalue(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,c3):
#         newReal=self.real+c3.real
#         newimg=self.img+c3.img
#         return Complex(newReal,newimg)

# c1=Complex(1,2)
# c1.showvalue()

# c2=Complex(3,8)
# c2.showvalue()

# c3=c1+c2
# #c3=c1.add(c2)
# c3.showvalue()


# Examples:===============================================================================================================

##Q.)Define a class named Book with attributes title, author, and year. Create an object of this class and print the attributes.

# class Book:
#     def __init__(self,title,author,year):
#         self.title=title
#         self.author=author
#         self.year=year

# my_book=Book("human","mohan das",2002)
#print(my_book.title,my_book.author,my_book.year)

# print(f"Title:{my_book.title}")
# print(f"Author:{my_book.author}")
# print(f"Year:{my_book.year}")


##Q.)Define a class named Person with attributes name and age. Create two objects of this class and print their attributes.

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=Person("monali",24)
# print("Name:",p1.name)
# print("Age:",p1.age)

# print(f"Name:{p1.name}")
# print(f"Age:{p1.age}")

##Q.) Define a class Rectangle with attributes width and height, and a method area that returns the area of the rectangle. 
# Create an object of the class and print the area.

# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height

#     def Area(self):
#         return self.width * self.height
    
# r1=Rectangle(4,6)
# print(f"Area of the rectangle:{r1.Area()}")


##Q.)Define a class Employee with a class variable total_employees that keeps track of the number of employees. 
# Increment this variable each time a new employee is created. Print the total number of employees.


# class Employee:
#     total_emp=0

#     def __init__(self,name):
#         self.name=name
#         Employee.total_emp += 1

# emp1=Employee("monali")
# emp1=Employee("ruoali")
# print(f"total employee:{Employee.total_emp}")

               

##Q.) Define a class Circle with an attribute radius, and a method circumference that returns the circumference of the circle. 
# Use a class method from_diameter to create a Circle object using its diameter.

# class Circle:
#     def  __init__(self,radius):
#         self.radius=radius
#     def circumference(self):
#         return 2 * 3.14 * self.radius
    
#     @classmethod
#     def from_diameter(cls,diameter):
#         radius=diameter/2
#         return cls(radius)
    
# c=Circle.from_diameter(10)

# print(f"circumference of the circle:{c.circumference()}")


##Q.)Define a class MathOperations with a static method add that takes two numbers and returns their sum.
#  Call this static method without creating an object of the class.


# class Mathoperations:
#     @staticmethod
#     def add (a,b):
#         return a+b
    
# result=Mathoperations.add(4,5)
# print(f"total result:{result}")


##Q.)Define a class Address with attributes street and city. 
# Define a class Person with attributes name and an address object of the Address class. Print the address of a person.

# class Address:
#     def __init__(self,street,city):
#         self.street=street
#         self.city=city

# class Person:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address

# result=Address("202-ABC","odisha")
# result1=Person("monali","purushottampur")
# print(f"name:{result1.name,result1.address}")
# print(f"address:{result.street,result.city}")



#####operator overloading:=================================================================================
##Q.) Define a class Vector with attributes x and y. Overload the + operator to add two vectors.
# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __add__(self,add):
#         return Vector(self.x+add.x ,self.y+add.y)
#     def __str__(self):
#         return f"Vector({self.x},{self.y})"
# v1=Vector(3,4)
# v2=Vector(4,0)
# result= v1 + v2
# print(result)

##Ex:========
# class Car:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model

#     def display_info(self):
#         print(f"Name:{self.name},Model:{self.model}")
    
# c1=Car("monali","Thor")
# c1.display_info()

###Ex:========
# class Animal:
#     def __init__(self,name):
#         self.name= name

#     #def sound(self):
#      #   pass
# class Dog(Animal):
#         def sound(self):
#             return "bruk"
        
# dog=Dog("bunny")
# print(dog.name)
# print(dog.sound())


##Ex:=========
# class Animal:
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return "brew"
    
# class Cat(Animal):
#     def sound(self):
#         return "mewo"

# animals=[Dog(),Cat()]
# for animal in animals:
#        print(animal.sound())

##Ex:=======
# class Bank:
#     def __init__(self,initial__balance):
#         self.__balance=initial__balance
#     def deposite(self,amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("invalid")

#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("invalid")
    
#     def check_balance(self):
#         return self.__balance
    
# account=Bank(5000)
# account.deposite(500)
# print(account.check_balance())
# account.withdraw(300)
# print(account.check_balance())


##Ex:=====

##(mathod overloading:=====)

# class Math:
#     def add(self,a,b,c=9):
#         return a+b+c
    
# math=Math()
# print(math.add(1,2))

##Ex:====
##(mathod overriding:=====)

# class Parent:
#     def show(self):
#         print("parent class method")
# class Child(Parent):
#     def show(self):
#         print("child class method")

# parent=Parent()
# child=Child()
# parent.show()
# child.show()



##Ex:======
##(using constructor:=====)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# person=Person("monali",24)
# print(f"Name:{person.name},Age:{person.age}")
        
 ##Q.) Define a class Student with attributes name, age, and grade. 
 # Include methods to display the student's details and to update the student's grade.

# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
    
#     def display_info(self):
#         print(f"Name:{self.name} , Age:{self.age} , grade:{self.grade}")
    
#     def update_grade(self,new_grade):
#         self.grade = new_grade

# s1=Student("monali",23,"A")
# s1.display_info()
# s1.update_grade("A++")
# s1.display_info()


##Q.) Create a class BankAccount with private attributes account_number and balance.
#  Provide public methods to deposit and withdraw money, and to check the balance.

# class Bankaccount:
#     def __init__(self,account__no,initial__balance):
#         self.account__no=account__no
#         self.__balance=initial__balance

#     def deposite(self,amount):
#         if amount >0:
#             self.__balance += amount
#             print(f"Deposite:{amount}")
#         else:
#             print("invalid")

#     def withdraw(self,amount):
#         if 0 < amount < self.__balance:
#             self.__balance -= amount
#             print(f"withdraw:{amount}")
#         else:
#             print("invalid")

#     def check_balance(self):
#         return self.__balance

# account=Bankaccount(12345,1000)
# account.deposite(500)
# account.withdraw(100)
# account.check_balance()


##Q.)Define a class MathOperations with a static method add that takes two numbers and returns their sum.
#  Call this static method without creating an object of the class.

# class Mathoperations:
#     @staticmethod
#     def add(a,b):
#         return a + b
    
# math=Mathoperations.add(3,4)
# print(f"Result : {math}")
 

##Q.)declear a simple function:=====
def greet(name):
    print(f"Name:{name}")

greet("monali")

##Q.) Write a function named add that takes two numbers as arguments and returns their sum.

def add(a,b):
    return a+b
result=add(2,1)
print(result)

##Q.) Write a function named power that takes two arguments, base and exponent, and returns base raised to the power of exponent.
#  If the exponent is not provided, it should default to 2.
 
def power(base,exponent=2):
    return base**exponent
print(power(2))
print(power(2,3))


##Q.) Write a function named sum_all that takes a variable number of arguments and returns their sum.

def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3))

##Q.)Write two functions: square that returns the square of a number, 
# and sum_of_squares that takes two numbers and returns the sum of their squares.

def square(x):
    return x*x
def sum_of_square(a,b):
    return square(a)+ square(b)

print(sum_of_square(2,3))


##Q.)Write a function named increment that increases the value of a global variable
#  counter by 1 each time it is called.

counter=0
def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)

##Q.)Write a function named outer that contains a nested function named inner. 
# The inner function should print "Hello from inner", and the outer function should call the inner function.

def outer():
    def inner():
        print("hello from inner function")
    inner()

outer()

##Q.)Write a lambda function that takes two arguments and returns their product.
#  Assign it to a variable named multiply and use it to multiply two numbers.

multiply=lambda x,y:x*y
print(multiply(2,3))

##Q.)Write a function named divide that takes two numbers and returns their division. 
# Include a docstring that describes what the function does.

def divide(a,b):
    return a/b

print(divide(100,10))

##Q.)Write a recursive function named factorial that returns the factorial of a given number.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

##Q.) Write a function named display_info that takes a person's name and age as keyword arguments and prints them.

def display_info(name,age):
    print(f"Name:{name} , Age:{age}")
display_info("Monali",23)

##Q.)Write a function named apply_function that takes a function and a value as arguments,
# applies the function to the value, and returns the result.

# def apply_function(fun,value):
#     return fun(value)
# def double(x):
#     return x * 2
# result=apply_function(double,5)
# print(result)

##(or)============================================
 
def apply_function(n):
    return n * 2
print(apply_function(5))


