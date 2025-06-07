#  we can use return in different ways in a function.
'''
#Code1
print("code-1")
def func1(a,b):
    return a+b

res=func1(5,10)
print("Value returned:",res)


#Code2:
print("------------------------------------")
print("code-2")
def func2():
    print("This code has nothing to return")
    return

func2()

#Code3:
print("------------------------------------")
print("code-3")
def func3():
    print("This code also has nothing to return and there is no return statement")

func3()

#Code 4:
print("------------------------------------")
print("code-4")
print("------------------------------------")
def func4(a,b):
    if(a>b):
        print("returns from if block")
        return a
    print("returns from outside if block")
    return b
print("1st invocation of code-4")
print("Value returned:",func4(10,5))
print("------------------------------------")
print("2nd invocation of code-4")
print("Value returned:",func4(2,3))


#  we can use values returned from a function.
#Code1
print("code-1")
def func6(a,b,c):
    res_avg=(a+b+c)/3
    return res_avg
print("1st invocation of code-1")
func6(6,8,10)
print("returned value is not assigned to any variable")

print("------------------------------------------------")
print("2nd invocation of code-1")
average=func6(10,15,20)
print("returned value assigned to a variable")
print("value of variable, average:", average)

print("------------------------------------------------")
print("3rd invocation of code-1")
print("returned value is directly printed")
print(func6(1,2,3))

#Code2
print("------------------------------------------------")
print("code-2")
print("------------------------------------------------")
def func7(a,b):
    if(a>b):
        return True
    return False
x=5
y=6

print("1st invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")


x=6
y=5
print("------------------------------------------------")
print("2nd invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")


# Qus2. During check-in process in an airport, the luggage weight of each 
# passenger is checked and in case of over-weight, they are asked 
# to pay for extra luggage. 

ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")


# Qus1. The program you have seen uses various decision control statements 
# for implementing the logic. Let’s explore it one by one using scenarios
# related to check-in process.
passenger_name="Chan"
passport_status="valid"
if(passport_status=="valid"):
     print("Airport security cleared")
else:
    print("Invalid passport")

# Qus3. The conditional statement in this program is known as the else if 
# ladder . The conditions are evaluated from top of the ladder downwards. 
# As soon as a true condition is encountered, the statement associated
#  with it is executed. The remaining condition checks in the ladder
#  will be skipped.
luggage_weight=30
weight_limit=30 #Weight limit for the airline
extra_luggage_charge=0
if(luggage_weight>0 and luggage_weight<=weight_limit):
    print("Check-in cleared")
elif(luggage_weight<=(weight_limit+10)):
    extra_luggage_charge=300*(luggage_weight-weight_limit)
else:
    extra_luggage_charge=500*(luggage_weight-weight_limit)
if(extra_luggage_charge>0):
    print("Extra luggage charge is Rs.", extra_luggage_charge)
print("Please make the payment to clear check-in")

# Code.......
luggage_weight=30
weight_limit=30 #Weight limit for the airline
extra_luggage_charge=0
if(luggage_weight>0 and luggage_weight<=weight_limit):
    print("Check-in cleared")
elif(luggage_weight<=(weight_limit+10)):
    extra_luggage_charge=300*(luggage_weight-weight_limit)
else:
    extra_luggage_charge=500*(luggage_weight-weight_limit)
if(extra_luggage_charge>0):
    print("Extra luggage charge is Rs.", extra_luggage_charge)
print("Please make the payment to clear check-in")

# Code.......
airline = "AirIndia"
if(airline == "AirIndia"):
    print("Proceed to Air India check-in counter")
elif(airline == "Emirates"):
    print("Proceed to Emirates check-in counter")
elif(airline == "British Airways"):
    print("Proceed to British Airways check-in counter")
else:
    print("Invalid airline")

    
# Qus4. The conditional statement written in this program is known as
#  nested if statement. In this case, an if statement is written within
#  another if statement. Similarly, any decision logic can also be written
#  within an else statement.
ticket_status="Confirmed"
luggage_weight=32
weight_limit=30#Weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared") 
    elif(luggage_weight<=(weight_limit+10)):
         extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
         extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")

    # Qus5.
# 1. Change the luggage_weight to 42, execute and observe the result.
# 2. Change the luggage_weight to 30, execute and observe the result.
# 3. For any extra luggage, passenger has to pay Rs. 500 per extra kg. 
# Make the necessary change in the code, execute and observe the result.

ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")

    # Qus6.
# Airport security cleared
# Extra luggage charge is Rs. 600
# Please make the payment to clear check-in
passport_status="valid"
ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(passport_status=="valid"):
    print("Airport security cleared")
    if(ticket_status=="Confirmed"):
        if(luggage_weight>0 and luggage_weight<=weight_limit):
            print("Check-in cleared")
        elif(luggage_weight<=(weight_limit+10)):
            extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
        if(extra_luggage_charge>0):
            print("Extra luggage charge is Rs.", extra_luggage_charge)
            print("Please make the payment to clear check-in")
        else:
            print("Sorry, ticket is not confirmed")
else:
    print("Invalid passport")

    
 # Qus7.
# What is the output of the below code snippet? 
num1=100
num2=200
num3=6
if(5>=num3):
    if(num1>100 or num2>150):
        print("1")
elif(num1>=100 and num2>150):
    print("2")
else:
    print("3")


 # Qus8.
a = -10
b = -200
c = 2000
d = 4000
if( a*b >=d):
    if(d>c):
        if(d%c!=0):
            print(11)
        else:
            print(22)
else:
    if(b/a >0):
        if(a<b or d%c!=0):
          print(33)
        else:
          print(44)

 # Qus9.
# If it is a multiple of three, display "Zip"
# If it is a multiple of five, display "Zap".
# If it is a multiple of both three and five, display "Zoom".
# If it does not satisfy any of the above given conditions,display "Invalid".
def display(num):
    message = ""
    if num % 3 == 0 and num % 5 == 0:
        message = "Zoom"
    elif num % 3 == 0:
        message = "Zip"
    elif num % 5 == 0:
        message = "Zap"
    else:
        message = "Invalid"
    return message

# Test the function
message = display(9)
print(message)  # Output: Zip

# Code.......
# Suppose a flight has landed with 5 passengers and immigration 
# check needs to be done for all of them. 
print("Flight has landed")
print("Proceed for immigration check")
passenger_count=1
print("Immigration check done for passenger,", passenger_count)
passenger_count+=1
print("Immigration check done for passenger,", passenger_count)
passenger_count+=1
print("Immigration check done for passenger,", passenger_count)
passenger_count+=1
print("Immigration check done for passenger,", passenger_count)
passenger_count+=1
print("Immigration check done for passenger,", passenger_count)

# Code.......
# When we want to execute some statements specific (known) number
# of times as in the case of immigration check, we can use a for loop as
# shown below:
print("Flight has landed")
print("Proceed for immigration check")
for passenger_count in 1,2,3,4,5:
    print("Immigration check done for passenger,", passenger_count)

#  Code.......
# Modify the below code to pick exactly 10 baggage per iteration instead of 
# accepting the input, execute and observe the result. 
# Note: 
# Execute the code only after making the necessary modifications.
# 'input' function works in eclipse IDE.
baggage_count=100
no_of_baggage_picked=0
while(baggage_count>0):
    no_of_baggage_picked = (int)(input ("Number of baggage:"))
    baggage_count = baggage_count - no_of_baggage_picked
    print("No. of baggage remaining:",baggage_count)

# Code.......
# What if we want the loop to run from 1 to 100?
# Should we modify the below code to create a sequence of values
# from 1 to 100?

# Code.......
for number in 1,2,3,4,5:
    print("The current number is ",number)
start=1
end=10
step=2
for number in range (start, end, step):
    print("The current number is ", number)
for number in range(1,5):
    print ("The current number is ",number)
print("---------------------------")
for number in range(1,7,2):
    print ("The current number is ",number)
print("---------------------------")
for number in range(5,0,-1):
    print ("The current number is ",number)
    

# Code.......
# Here, we need to use nested loop (loop inside another loop) as 
# we need to maintain the count of passengers and the count of baggage of
# each passenger.
# Assume that there are 5 passengers and each of them have 2 baggage.
# The below code will make sure that all baggage of each passenger have
# undergone the security check.

number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
         
        if(security_check==True):
           print("Security check of passenger:", passenger_count, 
                 "-- baggage:", baggage_count,"baggage cleared")
        else:
           print("Security check of passenger:", passenger_count,
                  "-- baggage:", baggage_count,"baggage not cleared")

# Code.......
# Go through the below code and guess the output. 
# Assume A – Adult passenger, C- Child, FC – Flight Captain, 
# FA – Flight Attendant, SP – Suspicious passenger. 
for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
     if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue
     if(passenger=="SP"):
         print("Declare emergency in the airport")
         break
     if(passenger=="A" or passenger=="C"):
         print("Proceed with normal security check")
         print("Check the person")
         print("Check for cabin baggage")


# Code.....
# In this code, we observe that loop condition will always evaluate to true.
# Hence the loop will never terminate.
# Such loops are known as infinite loops.
counter = 5
while (counter >= 5):
    print(counter)
    counter = counter + 1
 #  Don't run this the infinite loop...   

 counter = 1
while(counter <= 3):
    print(counter)
    counter += 1

# Code.....
# In case of for loops in Python, as initialization and change of value are automatically,
# taken care, while testing we just need to test it with an empty sequence a non-empty sequence.
num_list = [1,2]
for num in num_list:
    print(num, end = " ")
'''