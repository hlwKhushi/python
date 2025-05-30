# Dictionary in Python:-
# Dictionary are used to 'store data values in Key:Value pairs'.
# They are 'Unordered','Mutable'('Changeable') and'don't allow Duplicate'Key's.
'''
dict = {
    "Keys":"Value",
    "Name":"Khushi",
    "Age": 22,
    "Learning":"Coding",
    "Marks":[98,85,89,97,95,89,94],
    "Cgpa":9.78,
}

print(type(dict))
print(dict['Name'])
print(dict["Age"])
print(dict["Learning"])
print(dict["Marks"])
print(dict["Cgpa"])


# Null_Dict = {} :-
null_dict = {
    "Name":"Khushi",
    "College":"Dr. APJAK WIT Darbhanga",
    "Session":2022 -2026,
    "Semester":"5th",
    "Year":"3rd",
}
print(type(null_dict))
print(null_dict['Name'])


bio_data = {
    "Name":input("Enter Your Name:"),
    "Age":input("Enter Your Age:"),
    "College":input("Enter Your College Name:"),
    "Session":input("Enter in Which Session You are:"),
    "Year":input("Enter in Which Year You are:"),
    "Session":input("Enter Your Session:"),  
}
print(bio_data)

# Or BioData.....

bio_data = {
    "Name":input("Enter Your Name:"),
    "Age":input("Enter Your Age:"),
    "College":input("Enter Your College Name:"),
    "Semester":input("Enter in Which Semester You are:"),
    "Year":input("Enter in Which Year You are:"),
    "Session":input("Enter Your Session:"),  
}
print(bio_data['Name'])
print(bio_data['Age'])
print(bio_data['College'])
print(bio_data['Semester'])
print(bio_data['Year'])
print(bio_data['Session'])


# Nested_dict(one dict in one):-
Student = {
    'Name':input("Enter Your Name:"),
    "Score": {
        'Chem':input('Enter Chem Marks is:'),
        'Phy':input('Enter Phy Marks is:'),
        'Maths':input('Enter Maths Marks is:'),
        'Bio':input('Enter Bio Marks is:'),
    }
}
print(Student.keys())
print(Student['Score'])
print(Student['Score']['Chem'])
print(Student['Score']['Phy'])
print(Student['Score']['Maths'])
print(Student['Score']['Bio'])


# Dictionary Methods:-
# my dist.keys('Return all Keys'), 
# my dist.Values('Return all Values'), 
# my dist.items('Return all ['Key,Value]pairs as Tuples'), 
# my dist.get("key"['Return all the Keys according to the 'Value']), 
# my dist.update("new_dict"['inserts the specific items to the "dict"']),

Sellphone = {
    'Brand_name':input('Enter the Brand Name:'),
    'Details': {
        'Genration':input('Enter the Generation Name:'),
        'Material':input('Enter the Materials:'),
        'Model': input('Enter the Model Name:'),
        'Price': input('What is the Price:'),
        'Ram': input('Enter the ram:'),
        'Storage':input('How much Storage Capacity:'),
        'Battery':input('How much Battery Consumption:'),
        'Earphones':input('Is their Earphone along with Phone [YES/NO]:'),
        'Charger':input('Is their Charger along with Phone [YES/NO]:'),
        'Gurantee':input('Enter Phones Gurantee:'),
        'Discount':input('Enter how much discount:'),
    }
}
print(Sellphone.keys())
print(list(Sellphone.keys()))
print(len(Sellphone.keys()))
print(len(list(Sellphone.keys())))# It shows only Length, which is '2'.
print(Sellphone.values())
print(list(Sellphone.values()))
print(len(list(Sellphone.values())))
print(Sellphone.items())
print(list(Sellphone.items()))
print(len(Sellphone.items()))
print(len(list(Sellphone.items())))
print(Sellphone['Brand_name'])
print(Sellphone.get('Brand_name'))
# print(Sellphone.update{'Model':'Nokiya'})# Error 
print(Sellphone)


# Sets in Python:-
# Sets is the Collection of the Unorderd items.
# Each Element in the Sets must be 'Unique' and 'Immutable'['Can't Change the Value'].
# List & Dict ko 'Set' ke andar Store nhi kar sakte hai.

num = {1,3,2,5,4,7,8,9}
set1 = {1,6,8,9,6,7,2,6,5,4,6}# Repeated Elements Stored only Once so, it resolved to {1,2}.
null_set = set()# Empty Set syntax.

# Store these in Sets:-
# 1.Int, 2.Float, 3.String, 4.Boolean, 5.Tuple .
set1 = {1,6,8,9,6,7,2,6,5,4,6}
set2 = {12.5,35.2,658.51,36.2}
set3 = {'12','25','36','65'}
set4 = {'True','False'}
set5 = (12,12,15,446,86,35,78)

# Don't store in Sets:-
# 1.'Dict' and 'List'.
# 2.Duplicate items ignore.
# 3.Unordered items arranged.
# 4.'Length' mai bhi Duplicate Elements ko ignore karege.

# Code:-
Collection = {12,32,12,36,56,48,'khushi','kali','aayu','kissu','shivu'}
print(Collection)
print(type(Collection))
print(len(Collection))# Total Elements Counted, Duplicate items ignore.

# Empty Sets:-
Collect = set{}# Empty Set; Syntax.
print(type(Collect))


# Sets Methods:-
# set.add(). 
# set.remove().
# set.clear('Empty the Sets'). 
# set.pop('Remove a Random Value').

# NOTE:- ('Sets 'Mutable' hote hai, Sets ke Elements 'Immutable' hote hai').
# Sets ko Change kr sakte.
# Sets ke Elements ko Change nhi kr sakte.
# In this Case 'Tuple' ko pass kr sakte hai. 
# 'List' or 'Dict' ko pass nhi kr sakte.

Collect = set{}# Error
Collect.add(12),
Collect.add(15),
Collect.add(16),
Collect.add(18),
Collect.add(89),
Collect.add(54),
Collect.add(91)
print(Collect)

# set.add(). 
set1 = {12,54,'kali','kissu','khushi'}
set1.add(99)
print(set1)
print(type(set1))
print(len(set1))

# set.remove(). 
set2 = {12,54,'kali','kissu','khushi'}
set2.remove('khushi')
print(set2)
print(type(set2))
print(len(set2))

# set.clear('Empty the Sets').  
set3 = {12,54,'kali','kissu','khushi'}
set3.clear()
print(set3)
print(type(set3))
print(len(set3))

# set.pop('Remove a Random Value').
set4 = {12,54,'kali','kissu','khushi'}
set4.pop()
print(set4)
print(type(set4))
print(len(set4))

# set.pop('Remove a Random Value').
set4 = {12,54,'kali','kissu','khushi'}
set4.pop()
set4.pop()
print(set4)
print(type(set4))
print(len(set4))


# NOTE:-
# 'Hashing' ek yesi 'algorithm' hai, jiss mai 'Orignal Value' ko Change kr sakte hai,
#  wo 'new Value' mai Convert kr dega.
# 'Unhashable' jo Change ho jaye, 'Mutate' ho jaye, ['Dist','List' or 'Sets'].

# Sets Methods:-
# set.union(set1) 'Combines both Sets Eements and Return new'.
# set.intersection(set1) 'Combines Common Elements and Return new'.

# Code:-
Set1 = {1,2,5,4,1}
Set2 = {4,1,5,3,9,6,7}
print(Set1.union(Set2))# Duplicate items ignore.

Set1 = {1,2,5,4,1}
Set2 = {4,1,5,3,9,6,7}
print(Set1.intersection(Set2))# Only Common Elements return.


# Lets Practice Qus:-
# Qus1:- Stores following word meanings in a Python "Dictonary":-
# Table:'A piece of furniture', List of facts and figure'.
# Cat:'A small animal', ('"List" or "Tuple" ke form mai bhi print karwa sakte hai').

dict = {
    'Cat':'A small animal',
    'Table':'A piece of furniture',
}
print(dict)
print(type(dict))


# Qus2:- You are given a "list" of students. Assume one Classroom is required for 1 Sub. 
# How many Classroom are neede by all students :-
# Sub : 'Python','Java','JavaScript','C',Cpp','MongoDb'

sub = {
 'Python','Java','JavaScript','C','Cpp','MongoDb',
}
print(sub)
print(type(sub))
print(len(sub))


# Qus3:- Enter marks of '3 Sub', from the user ans store them in a 'dict',
# start with a empty, 'dict' and add ane by one,
# Use 'sub' name as 'key' and Marks as 'Value'. 

Marks = {}
sub1 = input('Enter Phy:-')
Marks.update({'Phy': sub1})
sub2 = input('Enter Chem:-')
Marks.update({'Chem': sub2})
sub3 = input('Enter Maths:-')
Marks.update({'Maths': sub3})
sub4 = input('Enter Bio:-')
Marks.update({'Bio': sub4})
sub5 = input('Enter Arts:-')
Marks.update({'Arts': sub4})

print(Marks)
print(len(Marks))
print(type(Marks))


#Integer Type:-
Marks = {}
sub1 = int(input('Enter Phy:-'))
Marks.update({'Phy': sub1})
sub2 = int(input('Enter Chem:-'))
Marks.update({'Chem': sub2})
sub3 = int(input('Enter Maths:-'))
Marks.update({'Maths': sub3})
sub4 = int(input('Enter Bio:-'))
Marks.update ({'Bio': sub4})

print(Marks)


# Qus4:- Figure out a way to store [9 to 9.0] as Seperate values in the set.
# ('You can take helps of 'built-in-data 'type').

Value = {9,9.0}# Both Value will 'Same'.
print(Value)
print(type(Value))

#Or,
Value = {9,'9.0'}# Both Value will 'Different'.
print(Value)
print(type(Value))

#Code........
Values = {
    ('float',9.0),
    ('int',9)
}
print(Values)
'''