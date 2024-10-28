# print("Hello World")
# name = "monali"
# age = 24
# a=None
# print(name)
# print("my name is:",name)
# age2=age
# print(age2)
# print(type(name))
# print(type(age))
# print(type(a))

# print("this is statement 1",end="")
# print("this is statement 2")


#a = 2000
#b = 400
#sum = a+b
#print(sum)
#taking input from user and printing it.
# Name = input("name : ")
# age = int(input("age : "))
# print(Name)
# print(age)
# print("my name is",Name ,"and i am",age,"years old" )
# light = input("light color : ")
# if(light == "red"):
#     print("stop")
# elif(light == "orange"):
#     print("start")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")

# marks = int(input("marks : "))
# if(marks >= 90):
#     print("A")
# elif(marks >= 80 and marks<90):
#     print("B")
# elif(marks >= 70 and marks<80):
#     print("C")
# else:
#     print("D")

# A = int(input("A : "))
# B = input ("M/F : ")
# if(A ==1 or A ==2 and B =="M"):
#     print("fee is 100")
# elif(A ==3 or A==4 and B=="F"):
#     print("fee is 200")
# elif(A ==5 and B=="M"):
#     print("fee is 300")
# else:
#     print("no fee")

# food = input("food :")
# eat = "yes" if food == "ice cake" else "no"
# print(eat)

#food = input("food :")
#print(("sweet") if food == "cake" or food == "jalebi" else print("not sweet"))

#WAP to check if a number entered by the user is odd or even.
# num = int(input("enter a number"))
# if (num%2==0):
#     print("Even Number")
# else:
#     print("Odd Number")

#WAP to find the greatest of 3 number entered by the user.
# a=1000
# b=6000
# c=27000
# a = int(input("enter any value:"))
# b = int(input("enter any value:"))
# c = int(input("enter any value:"))
# if(a>b and a>c):
#     print("a value is greater")
# elif(b>c):
#     print("b value is greater")
# else:
#     print("c value is greater")

#WAP to check if a number is a multiple of 7 or not.
# num=int(input("enter any number"))
# if(num%7==0):
#     print("multiple of 7")
# else:
#     print("not multiple")


#simple intrest
# a = float(input("a :"))
# b = float(input("b :"))
# c = float(input("c :"))
# print(a*b*c/100)



#x ="hello world"
#print(len(x))

#type conversion
# a=2
# b=4.5
# sum=a+b
# print(sum)

#type casting
# a=int("2")
# b=4.5
# sum=a+b
# print(sum)

# name = input("enter name:")
# age= int(input(" enter age:"))
# marks=float(input(" enter marks:"))
# print("welcome:",name)
# print("my age is:",age)
# print("my total marks:",marks)

#write a program input 2 numbers and print their sum.
#num1=int(input("enter 1st number:"))
#num2=int(input("enter 2nd number:"))
#print("sum:",num1+num2)

#WAP to input side of a square and print its area.
#side = float(input("enter square side:"))
#print("area=",side*side)

#WAP to input 2 floating point numbers and their avg.
# num=float(input("enter number:"))
# num1=float(input("enter number:"))
# print("avg :",(num+num1)/2)

#WAP to input 2 int numbers a and b.print TRUE if a is greater than equal to b ,if not print FALSE.
# a=int(input("enter no. :"))
# b=int(input("enter no. :"))
# print(a>=b)

#WAP to input user's first name and prints its length.
#name = input("enter your name:")
#print("length of your name is",len(name))

#WAP to find occurence of '$' in a string.
#str="hi ,my name $is a $,and $$99.90"
#print(str.count("$"))

#join() function:===
# list=["one","two","three"]
# s=',' .join(list)
# print(s)

#split()  function:=====
# list=["four","five","six"]
# s=',' .join(list)
# newlist=s.split(',')
# print(newlist)

#string format=====
# first = "first"
# second = "second"
# s = "sunday is the {} day of the week,and monday is the {} day of the week".format("first","second")
# print(s)

#list:====(methods)
#examples= ["monday","tuesday","sunday","friday","saturday"]
#examples[1]="saturday"
#del examples[3]
#examples.append("saturday")
#print(examples)

#lists=[2,5,7,0,8]
#lists.sort()
#lists.reverse()
#lists.sort(reverse=True)
#lists.insert(0,10)
#lists.remove(0)
#lists.pop(1)
#print(lists)

#tuples====(methods)
#tup = (2,4,8,6,7,5,2,3,6)
#print(tup.index(4))   #4=>element
#print(tup.count(6))

#WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
# movies=[]
# mov1=input("enter 1st movie:")
# mov2=input("enter 2nd movie:")
# mov3=input("enter 3rd movie:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#(or)==>

# movies=[]
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2nd movie:"))
# movies.append(input("enter 3rd movie:"))
# print(movies)

#WAP to count the number of the students with the "A" grade in the following tuple.
    #["C","D","A","A","B","B","A"]
#grade=("C","D","A","A","B","B","A")
#print(grade.count("A"))

#store the above value in a list and sort them from "A" to "D".

# lists=["C","D","A","A","B","B","A"]
# lists.sort()
# print(lists)



#dictionary  and set:========
#store following word meaning in a python dictionary
# table:" a piece of furniture" , "list of facts and figures"
# cat: "a small animal"

# dictionary = {
#     "cat":"a small animal",
#     "table":[" a piece of furniture" , "list of facts and figures"]

# }
# print(dictionary)

# you are given a list of subjects for students.Assume one classroom required for one subject.
#How many classrooms are needed by all students.
#"python","java","C++","python","javascript","java","python","java","C++","C"

# subjects={
#     "python","java","C++","python","javascript","java","python","java","C++","C"
# }
# print(subjects)
# print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and add one by one.
#use subjects name as key and marks as value.
 
# marks={}
# x = int(input("Enter Physics:"))
# marks.update({"physics":x})
# y=int(input("Enter Chem:"))
# marks.update({"Chem":y})
# z=int(input("Enter Zoology:"))
# marks.update({"Zoology":z})
# print(marks)

#Figure out a way to store 9 and 9.0 as separate values in the set.
#values ={9,9.0}
#print(values)
#other method
#values={9.0,"9"}
#print(values)

# values={
#     ("float",9.0),
#     ("int",9)
   
# }
# print(values)
#=======================================================================================================================================
##While loop:========
# while True:
#     print("Hello")
# count = 1 #initialization
# while count <=5:
#     print("Hello")
#     count += 1

# print(count)

#print no. 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Loop Ended")

#Reverse method:====
# i = 5
# while i >= 1 :
#     print(i)
#     i -= 1
# print("Loop Ended")

## Q1..print number from 1 to 100.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print(i)

##Q2.. print number from 100 to 1.
# i = 100
# while i >=1:
#     print(i)
#     i -= 1

##Q3..  print the multiplication table of a number n.
# i = 1
# while i <= 10:
#     print(3 * i)
#     i += 1

# n = int(input("Enter any number:"))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

##Q4.. print the elements of the following list using a loop.
     #[1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
# i= 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

##Q5.. search for a number x in the tuple using loop.
       #(1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i]==x):
#         print("FOUND at index",i)
#     i += 1

##Q5..first 10 even numbers.
# num = 2
# while (num<=20):
#     print(num)
#     num+=2

##Q6..first 20 odd numbers.
# num = 1
# while(num<=40):
#     print(num)
#     num +=2

##Q7..20 natural numbers..
# num= 1
# while(num<=20):
#     print(num)
#     num += 1

##Q8.. 20 whole numbers..
# i = 0
# while i<20:
#     print(i)
#     i += 1

##Q9..print first 10 integer and their square..
# num = 1
# print("numbers\tsquares")
# while num<=10:
#     print(num,"\t",num**2)
#     num = num+1


##Q10..10,20,......300
# i = 10
# while i<=300:
#     print(i,end = ",")
#     i += 10


##Q11..105,98,91...7
# i = 105
# while i>=7:
#     print(i,end = ",")
#     i -= 7

##Q12.. 10 natural numbers in reverse process using while loop.
# i = 10
# while i>=1:
#     print(i)
#     i -=1

##Q13..sum of first 10 natural numbers.
# i = 10
# sum = 0
# while i>= 1:
#     sum =sum+i
#     i -= 1
# print(sum)

##Q14..sum of first 10 even numbers..
 
# i = 2
# sum =0
# while i <=20:
#     sum = sum + i
#     i += 2
# print(sum)

##Q15.. print a table of a number entered from the  user.
# i = 1
# num = int(input("enter number:"))
# while i <= 10:
#     print(num,"*",i,"=",num*i)
#     i +=1

##16..print all  even number that between two numbers entered by user..

# num1 = int(input("enter number:"))
# num2 = int(input("enter number:"))
# if num1>num2:
#    while num1>num2:
#       if num2 %2 == 0:
#        print(num2)
#       num2+=2
# else:
#    while num1<num2:
#       if num1 %2 == 0:
#        print(num1)
#       num1+=2

##Q17..to print factorial of a number accepted from user..

# num = int(input("enter number:"))
# i=1
# f=1
# while (i<=num):
#     f=f*i
#     i=i+1
# print("factorial of number is:",f)


##Q18..print first 10 numbers using for loop..
#for i in range(1,11):
#    print(i)

#using while loop:==
#i = 1
#while i<=10:
 #   print(i)
  #  i+=1

##Q19..caluculate sum of numbers..(given range=10)
# sum=0
# for i in range(1,10+1):
#     sum = sum+i
# print(sum)


##using while loop:===
# i=10
# sum=0
# while i>=1:
#     sum=sum+i
#     i-=1

# print(sum)

##Q20..calculate sum of odd numbers (given range 10)...
# sum=0
# for i in range(10):
#     if i%2!=0:
#      sum +=i
# print(sum)

#using while loop:===

# i=1
# sum=0
# while i<=10:
#    if i %2!=0:
#     sum+=i
#     i+=2
# print(sum)

##Q21..multiplication table (no.=5)
#for i in range(11):
#    print(5,"*",i,"=",5*i)

#using while loop:===
# i = 1
# while i <=10:
#     print(5,"*",i,"=",5*i)
#     i+=1

##Q22..using list[1,2,4,6,88,125]

# list=[1,2,4,6,88,125]
# for i in (list):
#     print(i)

##Q23..count the total number of digits in a number..
#(num=1234567)
# num ="1234567"
# count=0
# for i in (num):
#     count+=1
# print(count)

# ##Q24..reverse method==> given name  

# str="monali"
# rev_str=""
# for i in (str):
#     rev_str=i+rev_str
# print(rev_str)


##Q25..to count the even and odd num from a series of number.
#list=[1,2,3,4,,5,6,7,8,9,77,66,99,33,44,213,456,738,5433]

# list=[1,2,3,4,5,6,7,8,9,77,66,99,33,44,213,456,738,5433]
# for i in (list):
#     if i%2==0:
#         print(i,"is a even number")
#     else:
#         print(i,"is a odd number")

##Q26..a string and calculates the number of digits and letters..
#user_str="monali123"

# user_str = "monali123"
# digits = 0
# letters = 0
# for i in user_str:
#     if i.isdigit():
#         digits = digits+1
#     elif i.isalpha():
#         letters=letters+1
# print("the input string",user_str,"has",letters,"letters and",digits,"digits.")


##Q27..print even numbers 1 to 10 using for loop
#num=2
#for num in range(2,11,2):
#    print(num)

##using while loop:==
# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i +=1

##Q28..reverse number 10 to 1..
# for i in range(10,0,-1):
#     print(i)
##using while loop:==
# i=10
# while i>=1:
#     print(i)
#     i-=1

##Q29..prints char of a string using a for loop..

# str="monalipatra"

# for char in str:
#     print(char)
# print(len(str))

##Q30.. find the largest num in a list..
#list=[2,9,7,5,99,88,0]

# list=[2,9,7,5,99,88,0]
# largest_num=list[0]
# for num in list:
#     if num>largest_num:
#         largest_num=num
# print(largest_num)

##Q31..find the average number in a list
#list=[2,4,7,9,1]

# list=[2,4,7,9,1]
# average = 0
# for num in list:
#     average +=num
# average= average/len(list)
# print(average)

##Q32..print all uppercase letter in a string using for loop..
# str="MonAli PatRa"
# for i in str:
#     if i.isupper():
#        print(i)

##Q33..count the numbers of vowels in a string using a for loop..
# str="rteiosNHFJKPOUYC"
# vowels="AEIOUaeiou"
# count=0
# for char in str:
#     if char in vowels:
#         count+=1
# print(count)

##Q34..a pattern of star s using nested for loops..
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
# print()

##Q35.. To print sum of numbers prestent inside list
# list = eval(input("enter list:"))
# sum = 0
# for i in list:
#     sum= sum+i
# print("the sum",sum)


#break method:===
# i = 1
# while  i <= 5:
#     print(i)
#     if(i == 4):
#         break
#     i += 1
# print("End of loop")

#continue method:====
# i= 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

## print odd number...
# i = 0
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

##for loop:=====

# list=[1,2,3,4,5,6,7,8]
# for num in list:
#     print(num)

##using else statement:

# str ="monalipatra"
# for char in str:
#     if (char == 'o'):
#         print("o found")
#         break
#     print(char)
# else:
#     print("END")

##Q1.. print the elements of the following list using a loop.
     #[1,4,9,16,25,36,49,64,81,100]

# list = [1,4,9,16,25,36,49,64,81,100]
# for num in list:
#     print(num)

##Q2.. search for a number x in the tuple using loop.
       #(1,4,9,16,25,36,49,64,81,100)

# tup = (1,4,9,16,25,36,49,64,81,100,36)
# x = 36
# index = 0
# for el in tup:
#     if(el== x):
#         print("num found at index",index)
#     index += 1

##range:====
#seq = range(10)
# for i in range(10):
#     print(i)

# for i in range(2,10,2):
#     print(i)

##Q1..print number 1 to 100.

# for i in range(101):
#     print(i)

##Q2..print number 100 to 1.

# for i in range(100,0,-1):
#     print(i)

##Q3..print a multiplication table of a number n.

# n = int(input("Enter any number:"))
# for i in range(1,11):
#     print(n * i)

##Q4..WAP to find the sum of first n number.
# n = 5
# sum = 0
# for i in range(n+1):
#     sum += i 

# print("total sum",sum)
#using whilw loops:==
# n= 5
# sum = 0
# i = 0
# while i <= n:
#     sum *= i
#     i += 1

# print("total sum =",sum)

##Q5..WAP to find the factorial of first n numbers.

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("total factorial:",fact)
## using for loop:

# n=5
# fact=1
# for i in range(1,n+1):
#     fact *= i
# print("factorial=",fact)


#Functions:=======================

#function defination
#def calc_sum(a,b):#a,b are parameters
#    return a + b

#sum = calc_sum(2,3)# function call and 2 ,3 are arguments stored inside parameters
#print(sum)

##print HELLO:====

# def print_hello():
#     print("HELLO")

# print_hello()


# def print_hello():
#     print("HELLO")

# output = print_hello()
# print(output)#None


###print 3 average value.

# def calc_avg(a ,b ,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg 
# calc_avg(1,2,3)

## two numbers multiplication..(default parameters)

# def calc_mul(a,b=3):
#     mul = a * b
#     print(mul)
#     return mul

# calc_mul(2)


###Q1.)WAF to print the length of the list.(list is the parameter)

# numbers = [1,2,3,4,5,6,7,8]
# cities = ["odisha","delhi","mumbai","pune","hyd"]

# def print_len(list):
#     print(len(list))

# print_len(numbers)
# print_len(cities)
    

###Q1.)WAF to print the elements of the list in the single line.(list is the parameter)

# cities = ["odisha","delhi","mumbai","pune","hyd"]

# def print_list(list):
#     print(list)
# print(cities[0], end=" ")
# print(cities[1], end=" ")

##add two numbers..
# def add_num(num1,num2):
#     sum = num1 + num2
#     print("sum: ",sum)
    
# add_num(10,20)


##(using return statement):
#Q.calculate square..
# def squ_num(num):
#     result = num*num
#     return result

# output=squ_num(5)
# print("square:",output)

##Q.check odd and even number..
# def evenodd(num):
#     if (num %2==0):
#         print("even")
#     else:
#         print("odd")

# evenodd(23)
# evenodd(18)

##Q.print x and y value..
# def myfun(x,y=34):
#     print("x :",x)
#     print("y :",y)
# myfun(12,45)

##Q.print name..

# def student(firstname,lastname):
#     print("fristname:",firstname)
#     print("lastname:",lastname)

# student("monali","patra")

##Q.find factorial..
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))

##Q..return square value..
# def square(num):
#     return(num**2)
# print(square(2))
# print(square(-4))

##Q..print index value  in given list..
# list=[1,2,3,4,5,6,7]
# def myfun(x):
#     if x[0]==1:
#         return 1
#     else:
#         return 0
# print(myfun(list))

#(or):===
# def myfun(x):
#     x[3]==99

# list=[40,30,90,78]
# myfun(list)
# print(list)

##Q.. write a functions to accept 2 no. as input and return sum..
# def add(x,y):
#     return x+y

# result=add(20,30)
# print("sum is:", result)
# print("sum is :",add(20,30))

##Q:write a function to check whether the given number is even or odd?
# def even_odd(num):
#     if num%2==0:
#         print(num,"no. is even")
#     elif num%2!=0:
#         print(num,"no. is odd")
#     else:
#         print("none")

# even_odd(20)
# even_odd(13)
# even_odd(0)

##variable length argument:====

# def sum(*n):
#     total = 0
#     for i in n:
#         total= total+i
#     print("sum is:",total)
# sum=0
# sum(10,60)

#=========================================================================================================

#using for loop:==

# cities = ["odisha","delhi","mumbai","pune","hyd"]
# def print_list(cities):
#     for item in list(cities):
#         print(item, end=" ")
# print_list(cities)

###WAP to find the factorial of n.(n is the parameter)
#using for loop:==

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

#using function:

# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# calc_fact(5)


###Q4.)WAP to convert USD to INR.

# def convertor(usd_val):
#     inr_val= usd_val* 83
#     print(usd_val,"USD =",inr_val,"INR")

# convertor(1)
 

#a=lambda x,y:x*y
#print(a(7,3))

# a = 5
# b = 2
# print(a // b)

# def func(a, b=5, c=10):
#     print(a, b, c)

# func(1, 2)

# [x**2 for x in range(5)]




# def checkpaleindrom(str="madam"):
#     return str == str[::-1]








# def isPalindrome(str):
#     if(str==str[::-1]):
#         return("yes")
#     else:
#         return("no")
# str=input("enter str:")
# print(isPalindrome(str))

# s=["hello"]
# s=s*3
# print(s)

# ex=["hello","hii","heyyyyyy"]
# # del ex[2]
# # print(ex)
# ex.pop()
# print(ex)

# list=[1,2,3,4,5]
# list.insert(2,6)
# print(list)





###local,global,nonlocal variables:=========================================================================================

# global_var="i am a local variable"

# def global_variable_name():
#     global global_var
#     global_var="i have been modified"

# print(global_var)

# global_variable_name() 
# print(global_var) 



# def out_var_function():
#     out_var_function="i am a out variable function"

#     def inner_var():
#         nonlocal out_var_function
#         out_var_function="i have been modified by inner variable functions"
#         print(out_var_function)

#     inner_var()
#     print(out_var_function)
# out_var_function()


# global_var="i am a global variable"

# def outer_var():
#     outer_var="i am a outer variable"

#     def inner_var():
#         nonlocal outer_var
#         outer_var="i have been modified by inner variable"
        
#         local_var="i am a local variable"
#         print(local_var)

#         global global_var
#         global_var="i have been modified by inner variable"


#     inner_var()
#     print(outer_var)

# outer_var()
# print(global_var)


##note:===
# 1.Local Variable: local_var is only accessible within inner_function.
# 2.Global Variable: global_var is accessible and modifiable throughout the script using the global keyword.
# 3.Nonlocal Variable: outer_var is modified within inner_function using the nonlocal keyword, reflecting the change in outer_function.

##if-else conditions problems:====================================================================

##Q.)Write a Python program that checks if a number is positive, negative, or zero and prints an appropriate message.

# num=float(input("Enter any number :"))
# if num > 0:
#     print("this is positive number")
# elif num < 0:
#     print("this  is negative number")
# else:
#     print("the number is zero")

##Q.)Write a Python program that takes an age as input and prints whether the person is a child,
#  a teenager, an adult, or a senior. Use the following criteria:

# 0-12 years: Child
# 13-19 years: Teenager
# 20-59 years: Adult
# 60 years and above: Senior
        
# age=int(input("Enter any number :"))
# if age < 0:
#     print("Age cannot be negative...")
# elif age <= 12:
#     print("You are a child...")
# elif age <= 19:
#     print("You are a teenages..")
# elif age <= 59:
#     print("you are a adult...")
# else:
#     print("you are a senior...")

##Q.)Write a Python program that checks if a given year is a leap year or not. 
# A year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.

# year=int(input("Enter any numbers :"))
# if (year % 4==0 or year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year...")
# else:
#     print(f"{year} is not a leap year...")

##Q.)Write a Python program that checks if a number is even or odd.

# num=int(input("Enter any number :"))
# if(num %2==0):
#     print("number is even...")
# else:
#     print("number is odd number...")

##Q.)Write a Python program that takes a score as input (0-100) and prints the corresponding grade based on the following criteria:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F

# score = int(input("Enter your score(0-100):"))
# if score < 0 or score > 100:
#     print("Invalid score. Please enter a score between 0 and 100.")
# elif score >= 90:
#     print("your grade is A...")
# elif score >= 80:
#     print("you grade is B...")
# elif score >= 70:
#     print("your grade is C...")
# elif score >= 60:
#     print("your grade is D...")
# else:
#     print("your grade is F")

##Q.)Write a Python program that checks if a character is a vowel or a consonant.

# char = input("Enter a character: ")

# if char in 'aeiou':
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is a consonant.")



#Q.)write a python function first _non_repeating_char that takes a string as input and returns the first
#  non-repeating character.
# if all characters are repeating or the string is empty,return None.

# def first_non_repeating_char (string):
#     if not string:
#         return
#     helper=''
#     for index,i in enumerate(string):
#         if i not  in string[index+1:] and i not in helper:
#             return i
#         helper+=i
#     else:
#         return
# print(first_non_repeating_char('string'))
# print(first_non_repeating_char('abcdf'))
# print(first_non_repeating_char('hjkoi'))
# print(first_non_repeating_char('aabbcc'))
# print(first_non_repeating_char('abcabcdef'))

#Q.)Longest Balanced Substring
#Write a Python function longest_balanced_substring(s: str) -> str that takes a string containing only 
# parentheses ( and ) and returns the longest balanced substring.
#A balanced substring contains an equal number of opening and closing parentheses in the correct order.



# def find_longest_balanced_substring(string: str):
#     max_len = 0
#     start = 0
#     stack = [-1]
#     for i, char in enumerate(string):
#         if char == '(':
#             stack.append(i)
#         else:
#             stack.pop()
#             if not stack:
#                 stack.append(i)
#             else:
#                 length = i - stack[-1]
#                 if length > max_len:
#                     max_len = length
#                     start = stack[-1] + 1
   
#     return string[start:start + max_len]
 
# print(find_longest_balanced_substring("()(((()))))))))))"))

# print(find_longest_balanced_substring("()(()))))"))  
# print(find_longest_balanced_substring("()(()))))(())"))  
# print(find_longest_balanced_substring(""))  
# print(find_longest_balanced_substring("(()"))  
# print(find_longest_balanced_substring(")()())"))  

#Q.)Find Missing Ranges
#Write a Python function find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[str] 
#that takes a sorted list of unique integers nums within the 
#range [lower, upper] and returns the list of missing ranges in the format "lower->upper".

# from typing import List
# def find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[str]:
#     '''find missing ranges'''
#     def format_range(low, high):
#         if low == high:
#             return str(low)
#         else:
#             return f"{low}->{high}"
#     missing_ranges = []
#     prev = lower - 1
#     for i in range(len(nums) + 1):
#         curr = nums[i] if i < len(nums) else upper + 1
#         if prev < lower - 1:
#             prev = lower - 1
#         if curr > upper + 1:
#             curr = upper + 1
#         if prev + 1 <= curr - 1:
#             missing_ranges.append(format_range(max(prev + 1, lower), min(curr - 1, upper)))
#         prev = curr
#     return missing_ranges
 
# nums = [23,54,66,75]
# lower = 10
# upper = 75
# print(find_missing_ranges(nums, lower, upper))




