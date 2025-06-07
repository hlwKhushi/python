'''

print("Let's see some examples.\n\nDid you notice the empty lines?")
print("Do you notice\t the tab space?\nDid you see that I have moved to next line?")
print("Do you want a \" in your text?")
print("Are you going to store more info about escape sequence in Z:\\\\user\\escape_sequence.txt??")
#Every print starts with a new line, end can change that behavior by specifying your own character
print("Did you see I start here", end=" ")
print("and I end in the same line although from a different print?")
print("As observed escape sequences help you to format your output.")

print("______________________________________________________________________")
print("BREAD BASKET")
print("Looking for a healthy breakfast, this is the place for you!!")
print("________________________________________________________________________")
print("Raisin Toast$2.50")
print("French Toast$2.80")
print("Mushroom Toast$3.00")
print("Pancake$4.00")
print("Pancake with Ice-cream$7.50")
print("Chef's speciality$10.00")
print("__________________________________________________________________________")

# Qus1. input Year
Year = int(input('Enter year:'))
if(Year % 4 == 0 and Year % 100 != 0):
    print("It is a leap year")
elif(Year % 400 == 0):
    print("It is a leap year")
else:
    print( "It is not a leap year")
    
# Qus2. infinet loop::::::
input Number
Temp = Number
Reverse = 0
while (Number != 0) do
Remainder = Number % 10
Reverse = Reverse * 10 + Remainder
Number = Number / 10
end-while
if (Temp == Reverse) then
display "Palindrome"
else
display "Not a Palindrome"
end-if

# Qus3. Write a pseudo-code to find the sum of numbers divisible by 4.
# The pseudo-code must allow the user to accept a number and add it to the sum if 
# it is divisible by 4. It should continue accepting numbers as long as
# the user wants to provide an input and should display the final sum.

sum=0
choice = 'Yes'

while(choice=='Yes')do
input number
if(number%4==0)
sum=sum + number
end-if
display "Do you want to continue?(enter yes or no)"
input choice
end-while

display sum


# Qus4. A three digit number is said to be an “Armstrong number” if the sum of 
# the third power of its individual digits is equal to the number itself.
 371 is an Armstrong number as 371 = 3 3 + 7 3 + 1 3  407 is an Armstrong 
 number as 407 = 4 3 + 0 3 + 7 3

 input number
temp=number
sum=0
while(number!=0)do
remainder=number%10

sum=sum+remainder*remainder*remainder
number=number/10

end while
if(temp==sum)then
display"this is armstrong number"
else
display"this is not armstrong number"
end if

# Qus5. Write a pseudo-code to recreate the figure given in the
#  expected canvas for the scenario.
display Daylight
for(Counter=1, Counter<=4, Counter=Counter+1 )
add Mountain
end-for

for(Counter=1, Counter<=3, Counter=Counter+1)
add Sheep
end-for


# Qus5. Write a pseudo-code to recreate the figure given in the expected canvas the scenario.
display Nightsky
display Moon
display Snow
for(Counter=1, Counter<=3, Counter=Counter+1)

add Tree
end-for

add Sheep
add Mountain

def calculate_sum(data1, data2):
    #All the statements in the block of code must have the same level of indentation
    result_sum=data1+data2
    return result_sum

result=calculate_sum(10,20)
print(result)

# Qus5. Write a Python program that converts temperature in Celsius to Fahrenheit and vice versa.
#  Implement the requirements using functions.Hint: 0C= (0F-32)*(5/9)
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Main program
def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f:.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F is equal to {c:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")
'''

