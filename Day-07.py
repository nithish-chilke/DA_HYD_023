'''
Usage of elsewith for -->the else keyword will only


'''
'''
#forwith else
work_log=[0,1,1,1,0,1,0]
longest_streak=0
current_streak=0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
    else:
        current_streak = 0
else:
    print(f'Longest streak is {longest_streak}')
'''
#in this case when the entire loop execution is done we get result of
    #else block
    #with break
'''
work_log=[0,1,1,1,0,1,0]
longest_streak=0
current_streak=0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            break
    else:
        current_streak = 0
else:
    print(f'Longest streak is {longest_streak}')
'''
''''
#For - else with notifications scenario
notifications=[0,0,0,0]
for notification in notifications :
    if notification == 1:
        print('unread Notification')
        break
else:
    print('all caught up')

'''
#try to take notifications from use --> list of integers
'''
notifications=list(map(int,input("enter the values --> 0 or 1:").split(',')))
print(notifications)
for notification in notifications :
    if notification == 1:
        print('unread Notification')
        break
else:
    print('all caught up')
'''

#while --> it relies on condition,it will be completely executed until the condition satisfied

'''
Syntax while:

while <condition>:
      statement(s).....
      .......
      ......
'''
'''
while True:
    print("yes")
'''

#It runs an infinite loop we need to press ctrl+c(keyboard interrupt)
'''
i = 0
while i<=10:
    print(i)
    i=i+1
'''
'''
i=10
while i>=1:
    print(i)
    i=i-1
'''
#banking scenario -->PIN authentication if more than 3 attempts
#account Locked..

pin='2616'
max_attempts=3
current_attempt=0
while current_attempt < max_attempts:
    enter_pin=input("enter the pin:")
    if enter_pin == pin:
        print("login successful")
        break
    else :
        print("enterd pin is wrong")
        current_attempt +=1
else:
    print("account locked,try after 24 hours...")
        
    








































