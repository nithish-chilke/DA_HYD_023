'''
Control Statements --> Flow of execution of the program
                    -->Conditional statments --> if,elif,else
                    -->Repetation statements --> for ,while ,(for with else)
                                                          (while with else)
                    -->Jumping statements -->break,continue,pass
'''
#Loops--> Loops are helpful for repetition (automative tasks)
#for keyword will helpfull to iterate over a sequence / range
#Syntax for (for Keyword):
'''
for <temp_var> in sequence / range
    statemwnt(s)....
    .....
'''

#range(start,stop,step)
'''
for i in range(10):
    print(i)
'''
#In above case we got 10 iterations
'''
for i in range(1,10):
    print(f'value of i is -->{i}')
'''
'''
for i in range(1,10):
    if i > 5:
        print(f'value of i is -->{i}')
'''
'''
for i in range(1,10):
    if i > 5 and i%2 == 0 :
        print(i)
'''
#range(start,stop,step)-->here step -->interval..
'''
for i in range(1,100,2):
    print(i)
    print("Done")
'''
#it returns counter in reverse order
'''
#printing -10 to -1
for i in range(-10,0,1):
    print(i)
'''
#[]--> we generally lists
'''
names = ['saketh','sai','akash']
print(len(names))#len denotes number of items in a object / container
for name in names:
    print(name)
    print(f'student name is {name}')
'''
'''
names = ['saketh','sai','akash']
print(len(names))
for name in names:
    if name == 'sai':
        print(f'student name is {name}')
'''

#calculate the sum of first 10 numbers
'''
result = 0
for i in range (11):
    result=result+i
    print(result)
'''    
#sum of first 10 evn numbers
'''
result = 0
for i in range (21):
    if i%2==0:
        result=result+i
        print(result)

'''
#counting longest work log streak

work_log=[0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1]
longest_streak=0
current_streak=0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(longest_streak)
















    
