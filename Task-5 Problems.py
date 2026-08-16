#Question 1: Student Marks Manager
'''
marks = []
for i in range(3):
    mark=int(input("enter the marks:"))
    marks.append(mark)
print("initialmarks:",marks)
marks.insert(0,90)
marks.extend([75,85])
print("marks:",marks)
if 75 in marks:
    marks.remove(75)
    print("marks:",marks)
remove=marks.pop()
print("marks removed",remove)
print("Final marks:",marks)
print("length of marks:",len(marks))
'''    
    
#Question 2: Number List Analyser
'''
numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()
print("Ascending order:", numbers)
numbers.reverse()
print("Descending order:", numbers)

a = int(input("Enter a number: "))
if a in numbers:
    print("Number exists")

    count = numbers.count(a)
    print("Count of number:", count)

    i = numbers.index(a)
    print("Index of number:", i)

else:
    print("Number does not exist")
smallest_value = min(numbers)
print("Smallest value:", smallest_value)
largest_value = max(numbers)
print("Largest value:", largest_value)
total_numbers = sum(numbers)
print("Total:", total_numbers)

'''
#Question 3: Even and Odd Number Separator
'''
numbers = [10, 15, 20, 25, 30, 35]
even=[]
odd=[]
for i in numbers:
    if i % 2 == 0:
        even.append(i)
        print("even:",even)
    elif i % 2 == 1:
        odd.append(i)
        print("odd:",odd)
print(numbers[0:3])
print(numbers[3:])
backup=numbers.copy()
print(backup)
numbers.clear()
print(numbers)
print(backup)
'''

#Question 4: Unique Name Manager 
'''
names = ["Asha", "Rahul", "Asha", "John", "Rahul"] 
name=set(names)
print(name)
new="Meera"
name.add(new)
print(name)
name.update(("Arun","Priya"))
print(name)
if "John" in name:
    name.remove("John")
    print(name)
name.discard("David")
print(name)
for i in name:
    print(i)
'''

#Question 5: Course Student Comparison

'''
python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

print("Union of students:", python_students.union(da_students))
print("Intersection of both course:", python_students.intersection(da_students))
print("Only Python:", python_students.difference(da_students))
print("Only one course:", python_students.symmetric_difference(da_students))

print("subset:", da_students.issubset(python_students))
print("superset:", python_students.issuperset(da_students))
print("Both are disjoint:", python_students.isdisjoint(da_students))
print("Union students:")
for i in python_students.union(da_students):
    print(i)
print("Common students:")
for i in python_students.intersection(da_students):
    print(i)
'''



























