#Grade Checker Program :
'''
marks=int(input("enter the marks :"))
if marks  < 0 or marks >100:
    print("Invalid marks entered")
elif marks >= 90 :
    print("grade:A")
    print("remark:Outstanding!")
elif marks >= 80 and marks<=89:
    print("grade:B")
    print("remark:Excellent!")
elif marks >= 70 and marks<=79:
    print("grade:C")
    print("remark:Good!")
elif marks >= 60 and marks<=69:
    print("grade:D")
    print("remark:fair,needs improvement")
elif marks >=50 and marks <=59:
    print("grade:E")
    print("remark:poor needs serious improvement")
elif marks <50:
    print("grade:F")
    print("remark:Fails ,needs to reappear")
'''
#Even-Odd Checker (with Twist)
'''
num=int(input("enter the number:"))
if num == 0:
    print("Zero is neither even nor odd")
elif num < 0 and num %2== 0:
    print("Negative Even number")
elif num < 0 and num % 2!= 0:
    print("Negative Odd Number")
elif num > 0 and num % 2==0:
    print("Even Number")
elif num > 0 and num %2 != 0:
    print("Odd Number")
'''
#Season Identifier
month=int(input("enter the month:"))
if month < 1 or month >12 :
           print("Invalid month enterd")
elif (month == 12 or month == 1 or month == 2):
    print("Winter")
elif (month == 3 or month == 4 or month == 5):
    print("Spring")
elif (month == 6 or month == 7 or month == 8):
    print("Summer")
else :
    print("Autumn")
    
