#List in Python........
'''
marks = [15.2,56.02,365.0,48,125,158] # List is mutable(change).
student = ["aayu","kashish","kissu","shivani","khushi"] 
print(len(marks))
print(len(student))
print("marks:-",marks)
print("student:-",student)
print(type(marks))
print(type(student))
print(marks[0])
print(student[2])
print(student[0],"karishma")#Change allowed in Python. 



#List Slicing......('Similar to the String Slicing').
            #List Method:- 
#(list.append('Add from the End'))
#(list.sort('Arrange in Ascending'))
#(list.sort(reverse = True),'Decending Order')
#(list.reverse())
#(list.insert('insert element at Index')).
#(list.insert('insert element at Index')).
#(list.insert('insert element at Index')).
#(list.pop()'Remove element at indx').

#(list.append('Add from the End')).          
list = [12,52,25,"kali","kissu","aayu"]
print(list)
list.append("kashish")#ad from the End.
print(list)
print(type(list))


#(list.sort('Arrange in Ascending')).
num = [12,52,25]
print(num)
num.sort()#Arrange in Ascending order.
print(num)

num = ["kali","shivu","aayu","kissu","kali"]
print(num)
num.sort()#Arrange in Ascending order.
print(num)

#(list.sort(reverse = True),'Decending Order').
value = [45,15,85,65,95,97]
print(value)
value.sort(reverse = True)#Arrange in Decending order.
print(value)

value = ["kali","shivu","aayu","kissu","kali"]
print(value)
value.sort(reverse = True)#Arrange in Decending order.
print(value)


#(list.reverse())
words = ['a','s','d','f','g','h','j','k','l']
print(words)
words.reverse()
print(words)

#(list.insert('insert element at Index')).
int = [14,25,84,79,86]
print(int)
int.insert(36,152)#add from the End.
print(int)


#(list.pop()'Remove the first Occurance of Element').
num = [12,25,68,74]
print(num)
num.pop()#remove from the End.
print(num)

num = [12,25,68,74]
print(num)
num.pop(2)#remove from the End.
print(num)
'''
