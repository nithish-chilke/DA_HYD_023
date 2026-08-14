'''
Sequences --> strings,lists,Tuples,Set,frozenset
Mapping --> dictionary
'''
#sets --> A set is a unique collection of objects,unordered,mutable,Hashing,UnIndexed,
#heterogenous
#set(),{}
#a={}--> its an empty dictionary
'''
a=set()
print(type(a))
stud_ids={123,243,354,243,126}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2]) #typeerror

print(234 in stud_ids)
#print(stud_ids * 2)#set cant be repeated
#print(stud_id+stud_ids)#Two sets cannot be merged
'''
'''
data={12,3,4,5,[12,3,4],'saketh'}
print(data)#No lists inside a set (hashing technique) lists are mutable
'''
'''
data={12,3,4,5,(12,3,4),'saketh'}
print(data)
print(len(data))
for i in data:
    print(i)
'''
'''
#Methods on sets --> add(),update(),remove(),discard(),pop()
names={'sai','saketh','kiran','codegnan'}
print(len(names))
#add() will insert an element intyo the set(it can be anywhere but only unique)
names.add('python')
print(names)
#names.add('saketh','poll')
#print(names)
names.add(("poll","polo"))
print(names)
da_names={'mani','akash','sai','sonu'}
#update() we can update multiple element (set)
names.update(da_names)
print(names)
print(len(names))
print(da_names)

da_names.update(names)
print(len(names))
print(len(da_names))

#remove(),discard(),pop(),clear()
da_names.remove('sai')
print(da_names)
#da_names.remove('Sai')#Keyerror is raised

#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')
'''
'''
da_names={'mani','akash','sai','sonu'}
print(da_names)
print(da_names.pop())#removes and returns an arbritary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add(("sairam","nithish"))
print(da_names)
'''

#copy()#creates a shallow copy of set(independent of each other)
'''
da_names={'mani','akash','sai','sonu'}
print(da_names)
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''

#mathematical operations --> union(),intersection(),difference(),symmetric_id
#issubset(),#issuperset(),isdisjoint()

da_23={12,23,34,45,23,36}
da_24={34,46,47,23}
'''
da_25={23,4,1}
event=da_23.union(da_24,da_25)
print(event)
print(len(event))
common =da_23.intersection(da_24)
print(common)
print(len(common))
'''
'''
common=da_23.intersection_update(da_24)
print(common)#it returns none
print(da_23)#common elements are finally stored
'''
'''
print(da_23)
print(da_24)

#diff() removes common elements and prints rmng elementsfrom first 

diff = da_23.difference(da_24)
print(diff)
f=da_23 - da_24
print(f)
#symmetric diff()--)removes common elements and print all amng
#elements from two sets
symm = da_23.symmetric_difference(da_24)
#print(symm)
h=da_23^da_24
#print(h)

#issubset() --> checks all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issubset(da_24))

#isdisjoint() returns false for sets havimg common elements
print(da_23.isdisjoint(da_24))
'''

#Length of unique student ids in a class ,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids

n=int(input())
student_ids=input().split()
result=set(student_ids)
print(len(result))












































































































