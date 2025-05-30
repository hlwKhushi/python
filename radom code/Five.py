'''
# LOOPS.........
# Loops are used to 'Repeat' instructions.
# Tow Types of Loops:-
# 1. For Loops,
# 2. While Loops,
# 'Revolving around the Loops is called Iteration'.
# Iterator(i) is a variable.


# Code:-
count = 0
while count <= 5:
    print('Khushi Kumari')
    count += 1
    print(count)

    
# Never Run this Infinite Loop:-
# Count = 0
# while Count <= 4:
   # Count += 0
   # print(count)

   
i = 0
while i <= 99:
    print('Khushi')#('Khushi',i) Also use this.
    i += 1 # [1 to till 100]
    print(i)


# Prints Numbers from (1 to 10):-
i = 1
while i <= 10:
    print(i)
    i += 1
   # print('Loop Ended')

   
# Prints Numbers from (1 to 10) in 'Reverse Order':-
i = 10
while i >= 1:
    print(i)
    i -= 1


# Let's Practice Qus:-
# 1. Print Numbers from (1 to 100):-
i = 1
while i <= 100:
    print(i)
    i += 1


# 2. Print Numbers from (1 to 100) in 'Reverse order':-
i = 100
while i >= 1:
    print(i)
    i -= 1


# 3. Print Numbers from (1 to 100) in 'Reverse order':-
i = int(input('Enter the Number:'))
while i >= 1:
    print(i)
    i -= 1

    
# 4. Print the Multiply-Table of a Number (n):-
n = 12
i = 1
while i <= 10:
    print(n*i)
    i = i+1


# 5. Print the 'Multiply-Table' of a Number (n):-
n = int(input('Enter the Number:'))
i = 1
while i <= 10:
    print(n*i)
    i = i+1


# 6. Print the 'Multiply-Table' of a Number (n):-
n = int(input('Enter the Number:'))
i = 1
while i >= 50:
    print(n*i)
    i = i-1# ERROR
    print(i)
   # i*= 10


# 7. Print Elements of the Following 'List' using a Loop.
num = [1,2,3,5,2,4,58,94,75]
idx = 0
while idx < len(num):
    print(num[idx])
    #print(num[0])
    #print(num[3])
    idx += 1


# 8. Print Elements of the Following 'List' using a Loop (Reverse).
num = [1,2,3,5,2,4,58,94,75]
idx = 0
while idx < len(num):
    print(num[idx])
    #print(num[0])
    #print(num[3])
    idx -= 1


# 9. Search for a number(X) in tuple using loop.
nums = (1,2,3,21,24,25,56,51,23)
X = 3
i = 0
while i < len(nums):#ERROR
    if (nums(i) == X):
        print('Found at idx',i)
    else: 
        print('Finding.....')
        i += 1
'''

# *-----------------------******--------------------*
#Tuples in Python.......(Very Important Topics)
#Tuple is Immutable (not Changeble)
'''
tup = ("khushi","kali","shivu","aayu","kissu")
print(type(tup))
print(tup[0])
print(tup[3])

tup = (12,54,87,95,62,34)
print(tup[1:2])
print(tup[1:3])
print(tup[1:4])


#Note:-'Tuple is allmost work like List'.
           #List Method:- 
#(tup.index('Return Index from First Occurance')).
#(tup.count('count all the Occurance')).


tup = (41,25,65,84,82)
print(tup)
print(tup.index(41))#'Return Index from First Occurance'.


tup = (41,25,25,82,45,95,45,25,65,84,82)
print(tup)
print(tup.count(25))#'count all the Occurance'.


#Qus:- Ask the user to enter the names of their favourate Movies and Store in a List.
Movies = []
mov1 = input("enter 1st Movie:")
mov2 = input("enter 2nd Movie:")
mov3 = input("enter 3rd Movie:")
mov4 = input("enter 4th Movie:")

Movies.append(mov1)
Movies.append(mov2)
Movies.append(mov3)
Movies.append(mov4)

print(Movies)


# Self-Biodata:-
Biodata = []
info1 = input("enter Your Name:")
info2 = input("enter Your Father's Name:")
info3 = input("enter Your Mother's Name:")
info4 = input("enter Your Date of Birth:")

Biodata.append(info1)
Biodata.append(info2)
Biodata.append(info3)
Biodata.append(info4)

print(Biodata)


#Short Trick to solve this Qus:-
Biodata = []
Biodata.append (input("enter Your Name:")) 
Biodata.append (input("enter Your Father's Name:"))
Biodata.append (input("enter Your Mother's Name:"))
Biodata.append (input("enter Your Date of Birth:"))

print(Biodata)


#Palindrome:-['which is the form of Similar Fornt or Back'].
#Hint: Use this Method: copy('Return a Shadow copy of this List').
tup1 = ("M","a","a","M")
print(tup1)
copi = tup1.copy()               #ERROR
copi.reverse()              
if (copi == tup1):                  
    print("This is Palindrome")
else:
    print("This isn't palindrome")
    
    
#Qus:- Count the Numbers of Students with the 'A' Grade in the Tuple.
Grade = ('C','A','S','A','B','A','A','A')
print(Grade)
print(Grade.count('A')


#Qus:-Store the above value in a 'List []' and Sort them from 'A' to 'E'.
grade = ['C','A','A','B','A','A','D','A','E']
print(grade)
grade.sort()
print(grade)
'''
