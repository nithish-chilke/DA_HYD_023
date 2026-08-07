   #list=[4,6,1,11110,2,4,0,6]
#write a python program to calulate the innings of a bats man anad count boundarys,dot,amd total scores
'''
score=[4,6,1,0,2,4,0,6]
boundary=0
dot=0
total_score=0
for i in score:
    total_score +=i
    if i == 4 or i == 6:
        boundary +=1
    elif i == 0:
        dot += 1
print(boundary)
print(dot)
print(total_score)
'''
#pattern/password
'''
pin=1330
current=0
while current < 5:
    enter=int(input())
    if enter == pin :
        print("unlocked")
        current = 5
    else :
        current += 1
if enter  != pin:
    print("locked")
'''
#ATM pin
pin=2323
current=0
while current < 3:
    enter=int(input())
    if enter == pin :
        print("ATM pin is Correct ")
        current = 3
    else :
        current += 1
if enter  != pin:
    print("ATM pin is Wrong")
        
        
