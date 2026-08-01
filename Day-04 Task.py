marks = int(input("Enter the marks: "))

if marks < 0 or marks > 100:
    print("Invalid values")
else:
    if marks >= 90:
        print("Grade A")
    else:
        if marks >= 80:
            print("Grade B")
        else:
            if marks >= 70:
                print("Grade C")
            else:
                if marks >= 60:
                    print("Grade D")
                else:
                    print("Fail")
          
