'''
sequences --> strings,lists,Tuples,Sets
Mapping --> Dictionary
'''

#Lists --> Collection of heterogenous elements (items)
#List --> Indexed,Ordered,Mutable,Heterogenous,we use [] to store the data
'''
marks=[12,35,26,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
'''
#Operations:Indexing,Slicing,Striding,Merging,Repetation

#Nested lists --> a list in another list
'''
names=['codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names)

print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4])
print(names[0][4:])

#print get the op as Cdga
print(names[0][::2])
names[0] = names[0][::-1]
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])
'''
#Indexing,slicing --> mutable
'''
names[2]='python'
print(names)
'''
#by indexing if we change the elements , length of collection will remain same
'''
names[4]=['codegnan','PFS','JFS']
print(names)
print(len(names))
print(names[4][0][4:])

names[2:4]='Abhi','than','nitg','bhav'
print(names)
print(len(names))
'''
#In slicing whatever elements u pass as per the logic length keeps on increasing

#O/p as followa:
'''
names[3:6:2]=['puthon','java']
print(names)
'''
#TASK:
#create a mested list with strings,lists and work on indexing,slicing,striding,
#added advantage if u could add strings functions also to it
#Lists functions--> append(),inseert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()

names =['codegnan','saketh']
#append()-->inserts single element to the end of the list
names.append('data')
print(names)
#names.append('analysis','agents')#TypeError
names.append(['analysis','agents'])
print(names)
#append() will always increment the length of lists by 1
#print(names[3])
#print(names[3].append('chatgpt'))#it returns none
#print(names[3])

#extend() --> inser6ts multiple element to the end of list
'''
names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45)# typeError
#print(names)
'''
#insert(index,object) -->inserts given object before index
'''
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b'])#syntax error
#print(names)
names.insert(-1,'AAA')
print(names)

'''
#pop(),remove(),clear()
#pop() by default last,else given index
names.pop()
print(names)
names.pop(2)
print(names)

#remove() --> we can remove a specific value
names.extend([23,14,15])
print(names)

names.remove(14)
print(names)
del names[1:3]#del keyword will apply pemanent changes
print(names)
names.clear()#clear all data from list and gives empty list
print(names)






























































































