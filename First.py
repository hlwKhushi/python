# 1st in Python:
# Variables and Data Types:.........
# Variables,Which Value is Varry [Change ho sakta hai.]
'''
print("Hello Khushi")
print("Python's Extensions [.py]")
print("[#] or [ctrl+/] for Commenting")
print('Print is a Function')
print("[\n] for New Line")
print("Khushi, Age = 21") # In same line.
print("Khushi,\n Age = 21")# \n Break the line. 
print("These quots['',""] is used for only Strings.")
 
# Variable:
# Code:-

name = 'Khushi'
age = 21
brand = 'khushjit'
print(name)
print(age)
print(brand)

print('My name is:', name)
print('My age is:',age)
print('My brand name is:',brand)

print(type(name))
print(type(age))
print(type(brand))



# Data Types : 
# 1. 'Integer' (+,-,0)
# 2. 'String' ("khushi",'Kali','shivani','kissu','aayu')
# 3. 'Float' (2.36,56.1,325.2)
# 4. 'Boolean' (True, False)
# 5. 'None' (Not Store any Value)

# Note: "Python is case Sensetive".


# Types Of Operator :
# 1. Arithmetic Operators :-- [+,-,*,/,%,**]
# 2. Relational Operators :-- [==,!=,>,<,>=,<=]
# 3. Assignment Operators :-- [=,+=,-=,*=,/=,%=,**=]
# 4. Logical Operators :--
# i) 'not' {'True' Value ko 'False' kar dega},
# ii) 'and' {Both Value have to same},
# iii) 'or' {Two Value ke liye use hoga}

# 1. Arithmetic Operators :-- [+,-,*,/,%,**]
# Code:

a = 12
b = 55

sumAdd = a + b
sumSub = a - b
sumMulti = a * b
sumDivide = a / b
sumModulo = a % b
sumExpo = a ** b # [a^b] a Power b

print(sumAdd)
print(sumSub)
print(sumMulti)
print(sumDivide)
print(sumModulo)
print(sumExpo)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b) # [a^b] a Power b

print(12 + 55)
print(12 - 55)
print(12 * 55)
print(12 / 55)
print(12 % 55)
print(12 ** 55)

# 2. Relational Operators :-- [==,!=,>,<,>=,<=]
# Code:
a = 11
b = 45
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)
print(a > b)
print(a < b)


# 3. Assignment Operators :-- [=,+=,-=,*=,/=,%=,**=]
# Code:
num = 12
num = num + 12
num += 12
print("num:",num)

num = 12
num = num - 12
num -= 12
print("num:",num)

num = 12
num = num * 12
num *= 12
print("num:",num)

num = 12
num = num / 12
num /= 12
print("num:",num)

num = 12
num = num % 12
num %= 12
print("num:",num)

num = 12
num = num ** 12
num ** 12
print("num:",num)


# 4. Logical Operators :-- i) 'not' {}'True' Value ko 'False' kar dega}, 
#  ii) 'and' {Both Value have to same} , iii) 'or' {Two Value ke liye use hoga}
#  code:
a = 45
b = 96
# i) not ('True' Value ko 'False' kar dega)
# print(not False)
print('not Operator:',not (a > b))

a = 45
b = 96
# i) not ('True' Value ko 'False' kar dega)
# print(not False)
print('not Operator:',not (a >= b))

a = 45
b = 96
# i) not ('True' Value ko 'False' kar dega)
# print(not False)
print('not Operator:',not (a < b))

a = 45
b = 96
# i) not ('True' Value ko 'False' kar dega)
# print(not False)
print('not Operator:',not (a <= b))


#  ii) 'and' {Both Value have to same}
#  code:
value1 = False
value2 = True
# and (Ek bhi value 'False' hoga then 'False' print karega)
print ('and Operator:', value1 and value2)

value1 = False
value2 = False
# and (Ek bhi value 'False' hoga then 'False' print karega)
print ('and Operator:', value1 and value2)

value1 = True
value2 = True
# and (Ek bhi value 'False' hoga then 'False' print karega)
print ('and Operator:', value1 and value2)


#  iii) 'or' {Two Value ke liye use hoga}
#  code:
a = 10
b = 44
# any one value have to True or False.
print('or Operator:',(a > b) or (a >= b))

a = 10
b = 44
# any one value have to True or False.
print('or Operator:',(a < b) or (a <= b))


#1.Type Conversion...[Automatically Type convert kr deta hai.]
# code:
a,b = 51 , 9.2  # 'Int' and 'Float' ko combine kr sakte hai.
sum = a + b     # 'Float' 'Int' se superior hota hai, Value goes to change into 'Float'.
print(sum)
# print(a + b)

# throw ERROR!
a,b = 51 , '9'  # {Type Error} 'String' and 'Int' ko combine nhi kar sakte.
sum = a + b 
print(sum)
# print(a + b)

# throw ERROR!
a,b = 5.1 , '9'  # {Type Error} 'String' and 'Float' ko combine nhi kar sakte.
sum = a + b 
print(sum)
# print(a + b)

a,b = '51' , '9'  #'String' and 'String' ko combine kar sakte.
sum = a + b 
print(sum)
# print(a + b)

a,b = 5.1 , 0.9  #'Float' and 'Float' ko combine kar sakte.
sum = a + b 
print(sum)
# print(a + b)

a,b = 51 , 23  #'Int' and 'Int' ko combine nhi kar sakte.
sum = a + b 
print(sum)
# print(a + b)

#2.Type Casting...[Manually karte hai.]
#  Code:
a,b = 12,'23'
c = int (b)
sum = a + c
print(sum)

a,b = 12,'23'
c = float (b)
sum = a + c
print(sum)

a,b = 12, 23
c = float (a)
sum = a + c
print(sum)

# throw ERROR!
a,b = '12','23'
c = int (b)
sum = a + c
print(sum)

# Code:--
a = float('2')
b = 12.0
print(type (a))
print(a + b)

a = int('2')
b = 12.0
print(type (a))
print(a + b)

a = float(2)
b = 12.0
print(type (a))
print(a + b)

a = int(2.0)
b = 12.0
print(type (a))
print(a + b)

a = str(2.0)
b = 12.0
print(type (a))
print(a + b)

a = str(2)
b = 12.0
print(type (a))
print(a + b)

# Code:--
a = 25
a = str(a)
print(type (a))

a = 2.05
a = str(a)
print(type (a))

a = '25'
a = int(a)
print(type (a))

a = 25
a = float(a)
print(type (a))

a = '25'
a = float(a)
print(type (a))


# Input in Python :
# input (used to accept the values using keyboard from user.)
# input (Result from input() is always a string.) 

# Code:--
name = input('Enter Your Name:')

print('Welcom',name)
print('Welcom',name, 'in Our Python Course.')

value = input('Enter Some Value:')

print(type (value))

# Code:--
name = input('Enter Your Name:')
age = input('Enter Your Age:')
marks = input('Enter Your Marks:')

print('Welcome',name,'in Our First Coding Prongram.')
print('Your are in Your',age,'Years Congratulations! You are in Your Growing age.')
print('Your Obtaion',marks,'woohoo!')

# Other Way:--
name = int(input('Enter Your Name:'))
age = int(input('Enter Your Age:'))

print(name)
# print(age)
'''

#Qus 1.Write a program to input two numbers and print their sum.
first = int(input('Enter Your First Item:'))
second = int(input('Enter Your Second Item:'))
print('Sum = ',first + second)