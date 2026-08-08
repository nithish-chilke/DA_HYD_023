#PHN PASSWRD
'''
pin='2323'
current=0
max_attempt=3
while current < max_attempt:
    enter=input("enter password:")
    if enter == pin :
        print(" pin is Correct ")
        break
    current+=1
    print("pin is Wrong")
        
else:
    print("wait for 30 sec...")

'''
#OTP
'''
otp='2323'
current=0
max_attempt=7
while current < max_attempt:
    enter=input("enter otp:")
    if enter == otp :
        print(" otp is Correct ")
        break
    current+=1
    print("pin is Wrong")
        
else:
    print("wait for 30 sec...")

'''
#Food Ordering
'''
food=input("enter the food :")
count=0
while food != "exist":
    count += 1
    food=input("enter the food:")
print("total no of orders",count)
'''
#football

score="20"
limit=0
attempts=3
while limit < attempts:
    goal=int(input("enter:"))
    if goal == score  :
        print("you won")
        break
    else:
        remaining=attempts-limit
        print(f"you need to score more")
        limit += 1
else:
    print("you loss")






















































