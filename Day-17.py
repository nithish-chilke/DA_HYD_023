'''
Mapping-->Dictionary-->Collection of key_value pairs used to store
related data -->JSON,APIs,Database records

dict() --> data ={} ,
Dictionary is a mutable ,Indexed through keys,Ordered,heterogenous,
Keys must be unique (int,strings,float values...)
'''

details ={}
print(type(details))

details={'Id' : 'CGH4022',
         'Name' : 'Manasa',
         'Gender':'Female',
         'Age':20,
         'Batch':'DA23',
         'Place ': 'HYD'}
print(details)
print(len(details))
'''
#Acessing the data from dictionary
#index[0]#KeyError

print(details.keys())#it returns keys from the dictionary
print(details['Id'],details['Name'])
#if key name is not matching /invalid
#print(details['marks'])#KeyError as marks is no present
details['marks']=[]
print(details)
print(type(details['marks']))

details['marks'].append(20)
print(details)
details['marks'].extend([30,40,25,45])
print(details)

#create a key-value pair of practice Session
details['practice_session']=('Tuesday','Thursday','saturday')
print(details)
print(details.keys())

#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day of practice Session
print(details['practice_session'][1])

details['MI']=('Monday','Wednesday','friday')
#operations -->Mutabble,indexing through keys,membership

print('Wednesday' in details)
print('MI' in details)#returns true as we have MI as Key

for i in details:
    print(i)#it retrns Keys one by one

for i in details.keys():
    print(f'key={i}')
    print(f'value={details[i]}')
'''
#keys()-->returns keys from dictionary
'''
for i in details.values(): #returns values from dictionary
    print(i)
for i in details.items():#returns a key value pair in tuple
    print(i)


for key,value in details.items():
    print(f'key is {key}')
    print(f'valueis {value}')

'''
#update()-->updating the dictionar with key value pairs
'''
details.update({'marks':[],'PS':('Tuesday','Thursday','Saturday')})
print(details)
details['marks'].extend([25,30,35])
print(details)
marks=list(map(int,input("enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)
'''
print(details.keys())
print(details.get('Name'))
print(details.get('Branch'))#it returns None as we dont have Branch as Key
print(details.keys())

details.setdefault('Branch')#if key is not present it inserts into dict
print(details)
details['Branch']='CSE'
print(details)

print(details.setdefault('Name'))
print(details.keys())

print(details.pop('Branch'))
print(details.keys())

print(details.popitem())#removes and return a key,value pair as 2-tuple
print(details.popitem())

del details['Id']
print(details)

details.clear()#removes all elemnts from D
print(details)


#fromkeys()
data = ['saketh','sai','data']
b=dict.fromkeys(data)#creates a dict but value set to none
print(b)
b['saketh']=31
print(b)
c=dict.fromkeys(['CGH1234','CGH3212'],
                ['code','gnan'])
print(c)


























