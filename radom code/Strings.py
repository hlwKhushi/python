# Strings are 'Immutable'(not change!)....
'''
num = int(input('Enter the value:'))
if(num < 0):
    print('Number is -ve')
elif(num == 0):
    print('Number is zero')
else:
    print('Number is +ve')
print('I am Done.') # Execute itself..

#Strings amd Conditional Statements.......
#Concatination...

a = 'hello' 
b = "khushi"
sum = 'hello'+'khushi'
print(sum)

a = 'hello' 
b = "khushi"
sum = 'hello  '+'khushi'
print(sum)

a = 'hello' 
b = "khushi"
sum = 'hello'+'  khushi'
print(sum)

a = 'hello' 
b = "khushi"
sum = 'hello'+' '+'khushi'
print(sum)

a = 'hello' 
b = "khushi"
sum = a +' '+ b
print(sum)

#Length of string....
str1 = "This is a string" #spaces will never ignore in len(str) 
print(str1)
print(len(str1))                                                                                                                                       

str2 = "   This is a string"
print(len(str2),str2)

str3 = "This is a string     "
print(len(str3),str3)

str4 = """This is a string"""
print(len(str4),str4)

#[\n] for next line....
var = "khushi \n" "shivani\n" 'kali\n'
print(var) 

s1 = '12\n' '54\n'
print(s1)
print(len(s1))

#[\t] for "spacing tab "
str1 ="khushi\t""kali\t""kissu\t" #space is also countable in length.
print(len(str1),str1)

#Indexing[]......
num = "Khushi Kumari"
print(num[10]) # it is like Array.

num = "Khushi Kumari"
print(len(num),num[10])

#Slicing[]......
str1 = "ApnaCollege"
print(str1[0:3]) #last index not be included.
print(str1[:5]) #[0:5] it's mean.
print(str1[4:]) #[4:] till last index.
print(str1[6:len(str1)]) #till last index.

#Slicing[] ('negative' index).....
val = 'KhushiKumari'
print(val [-8:-2])
print(val[-6:-3])
print(val[-2:])
print(val[:-10])
print(val[-2:len(val)])

#String Function......
code ='I am Khushi from W.I.T College Darbhanga, bihar'
print(code.endswith('ar'))#True.
print(code.endswith('op'))#False.
print(code.capitalize())#jitne bhi Capital words hai unn sabhi ko Small kar dega.
print(code.replace('h','o'))#jaha "h" hai wha "o" se change ho jayega.
print(code.find('bihar'))#Position bataega.
print(code.count('e'))#Count krega kitni baar "e" likha gya h.
print(len(code),code)#give Length.

#Let's Practice....
#input user's first name and print it's length.
name = input("Please enter your name:")
print("length of your name is:",len(name),name)

#find the occurance of '$' in aString.
str1 = "hello$ I$ am $Khushi My Symbol$ is$ $Dollor $10000000000 "
print(str1.count("$"))
print(type(str1))

#Conditional Statements.......
#if - elif - else [SYNTAX]

# if(Condition):
#     statement1
# elif(Condition):
#     statement2
# else:
#     statement....

#Trafic Light....
Light = input("Enter Only Small letters of Light:")

if(Light =='red'):
    print("STOP")
elif(Light =='yellow'):
    print('READY')
elif(Light =='green'):
    print("GO")
else:
    print('Other Colors not allowed.')
    print('NO SIGNAL!')

#Students Marks With Grade.....

#marks = input("enter your marks:")
marks = int(input("enter your marks:")) #both these are same.
if(marks >= 92):
    print("Grade: A")
elif(marks >= 85 and marks < 92):
    print("Grade: B")
elif(marks >= 70 and marks < 85):
    print("Grade: C")
elif(marks >= 60 and marks < 70):
    print("Grade: D")
else:
    print("Grade: F")

#NESTING......
#age = 78
age = 19
if(age >= 18):
    if(age >= 60):
        print("you can't drive")
    else:
        print("you can drive")
else:
    print("you can't drive")

#From users.....
age = input("Enter your age:")
age = int(age)
if(age >= 18):
    if(age >= 60):
        print("you can't drive")
    else:
        print("you can drive")
else:
    print("you can't drive")

# OR....
#From users.....
age = int(input("Enter your age:"))
if(age >= 18):
    if(age >= 60):
        print("you can't drive")
    else:
        print("you can drive")
else:
    print("you can't drive")

#Odd and Even......
num = input("Enter the num:")
num = int(num)
remainder = num % 2
if(remainder == 0):
    print("Even")
else:
    print("ODD")

# OR....
num = int(input("Enter the num:"))
if(num % 2 == 0):
    print("Even")
else:
    print("ODD")

#OR....
num = int(input("Enter the num:"))
remainder = num % 2
if(remainder == 0):
    print("Even")
else:
    print("ODD")

#Qus. Find the Greatest of Three numbers entered by the user.

a = int(input("Enter first num:"))
b = int(input("Enter sec num:"))
c = int(input("Enter third num:"))
if(a>=b and b>=c):
    print("First num is Largest",a)
elif(b>=c):
    print("Sec num is the Largest",b)
else:
    print("Third num is the Largest",c)

#Qus. To check if a number is a Multiple of 7 oe not.

num = int(input("Enter the number:"))
remainder = num % 7
if(remainder == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")

#OR....

num = int(input("Enter the number:"))
if(num % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")

'''


