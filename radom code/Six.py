
# Break:- It is used to 'Terminate' the loop, when 'Encountered'.
# Continue:- 'Terminals' execution in the current 'iteration' and
# continues 'execution' of the loop with next 'iteration'.

'''
# Break Code:- ['Break Keywords']
i = 1
while i <= 5:
    print(i)
    if(i == 5):
        break
    i += 1
    print('End of the Loop')

    
# Continue Code:-
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue # 'Act aaws Skip'
    print(i)
    i += 1


i = 1
while i <= 10:
    if (i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1


i = 1
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1


# Loops in Python:
# Loops are used for 'Sequential Traversal', for traversing List , String , Tuples.


# Code:-
list = [12,23,31,33]
for elem in list:
    print(elem)


# Code:-
list = (44,85,11,63)
for elem in list:
    print(elem)

    
# Code:-
str = 'Khushi'
for char in str:
    print(char)

# Code:-
tup = ['patato', 'Onion','Pea']
for num in tup:
    print(num)


                            # Syntax :-[For Loop with 'else']
                            # for elem in list:
                                # Some Work
                            # else: 
                                # work when Loops ENDs.


# Lets Practice:-[Using for Loop]


# Qus 1:- Print the Element of the following list using a Loop:
num = [12,51,54,1,5,7,8,9,5]
for elem in num:
    print(elem)


# Qus 2:- Search for a number (x) in this Tuple using Loop:
num = [1,2,5,8,9,7,5,5,5,5,5,5,5]
x = 5
idx = 0
for elem in num:
    if(elem == x):
        print('Number Found at idx', x)
    #break
    idx == 1


# Range ():- 'Range' function returns a 'Sequence of Numbers', Starting from [0] by default,
# and inc. by [1] (by default), and stops before a specified number.
# These are the Three 'Range':- 1)Start = 0 {'Optional'}
#                                2)Stop/End = 0 
#                                3)Step = 0 {'Optional'}


# Code:-
seq = range(10) # [0] is also included.
for i in seq:
    print(i) # [10] isn't included.

    
# OR,
for i in range(10): # Range (Stop)
    print(i)

    
# Code:-
for i in range(2,12): # Range (Start,Stop)
    print(i) # [0,1] is not included till [11]

    
# Code:-
     # Start, Stop, Step
for i in range(2,10,2):
   print(i)


# Print 'Even' Numbers:-
     # Start, Stop, Step
for i in range(2,100,2):
    print(i)

    
# Print 'ODD' Numbers:-
     # Start, Stop, Step
for i in range(1,100,2):
    print(i)

    
# Lets Practice:-[Using for & Range()]
# Qus 1. Print Number from 1 to 100.
for i in range (1,101):
    print(i)

    
# Qus 2. Print Number from 100 to 1.
for i in range (100,0,-1):
    print(i)

    
# Qus 3. Print the multiplication Table of a number(n).
n = int(input("Enter any Number:-"))
for i in range (1,11): # 1 to 10
   print(n*i)


# Qus 4. Print the multiplication Table of a number(n).
n = int(input("Enter any Number:-"))
for i in range (10,0,-1):
   print(n*i)

   
# Pass Statement:"Pass is a 'null' statement that does 'nothing'.
# It is used as a Placeholder for future code".
# Code:
for elem in range (0):
    pass # Null state Nothing.
print('Hlw Khushi')


# Qus 1. Find the Sum of the first (n) Naturals numbers.
n =  int(input("Enter the Number:"))
sum = 0
for i in range(1, 1+n):
    sum += i
    print('Total Sum =', sum)


# Qus 2. Find the Factorial of the first (n) Naturals numbers.['Using For Loop']
n = int(input('Enter the Number:'))
fact = 1
for i in range(1,n+1):
    fact *= i
    print("fact:", fact)


# Qus 3. Find the Sum of the first (n) Naturals numbers.['Using While Loop']
n = int(input('Enter the Number:'))
sum = 1
i = 1
while i <= n:
    sum += i
    i += 1
    print("Total Sum =", sum)

'''

# *-------------------------*****------------------------------

# Functions in Python:- 'Block of the Statements that Perform a Specific Task.'
# Syntax:-
'''
def fun_name(a1,a2,.....):
    # Some Work..
    return Value
fun_name(arg1,arg2....) # Fun. Call


# Code:-
def calc_sum(a,b): # Fun. Defination
    sum = a+b # Parameters
    print (sum)
    return sum
'''

# Code:-
# def print():
#    print('hello')
#    output = print-hello()
#    print(output) # NONE
