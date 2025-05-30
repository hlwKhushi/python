# 25 else statement interview questions and solutions
# else_interview_qs_solutions 
"""
1. What is the purpose of the else clause in Python if-else?
Answer: Executes a block when the if condition is False.

2. Can you use else with loops in Python?
Answer: Yes, else runs after the loop finishes normally without a break.

3. Demonstrate else in a for loop.
for i in range(3):
    print(i)
else:
    print("Done")

4. What happens if an exception occurs in the try block?
Answer: The except block runs, else is skipped.

5. Use else to handle division safely.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Result:", result)

6. Difference between else with if vs else with loop?
Answer: With if - runs when if fails. With loop - runs if no break occurs.

7. Use else to identify non-prime numbers.
n = 7
for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

8. Can we use else without if?
Answer: No, it must follow if, for, while, or try.

9. Check if a file exists or not using else.
import os
filename = "test.txt"
if os.path.exists(filename):
    print("File found")
else:
    print("File not found")

10. What happens if both if and else are false?
Answer: Only one runs; else runs if if is false.

11. Use else to determine number type.
num = -2
if num > 0:
    print("Positive")
else:
    print("Zero or Negative")

12. Explain how else works with while loop.
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Completed")

13. Use else to find a target in list.
nums = [1, 2, 3]
for n in nums:
    if n == 4:
        print("Found")
        break
else:
    print("Not found")

14. Can else execute after break?
Answer: No, else block is skipped if break occurs.

15. What if else is not provided in if condition?
Answer: Nothing happens if the if fails.

16. Show nested if-else with final else.
score = 75
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C")

17. Use else in input validation.
age = 20
if age < 0:
    print("Invalid")
else:
    print("Valid age")

18. Can else be used with pass?
num = 5
if num < 0:
    pass
else:
    print("Non-negative")

19. Use else to classify numbers.
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

20. Use else for string check.
text = "hello"
if text.isupper():
    print("Upper")
else:
    print("Not upper")

21. Check student result with if-else.
marks = 35
if marks >= 40:
    print("Pass")
else:
    print("Fail")

22. Use else in even/odd checker.
n = 12
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

23. Can you use multiple else blocks?
Answer: No, only one else is allowed per if or loop.

24. Use else in ternary operation.
age = 17
print("Adult" if age >= 18 else "Minor")

25. Explain else priority in compound conditions.
a, b = 5, 10
if a > b:
    print("a > b")
else:
    print("a <= b")
"""

