#Python program to award bonus marks according to marks scored in different type(theory/lab) of subject.
#It accept the marks, class type ‘T’ for theory or ‘L’ for lab and displays final marks after adding bonus marks as output.

#criteria:
#for marks>=80 , 8% bonus in theory subject and 6% bonus in lab subjects
#for marks>=60 and <80 , 6% bonus in theory subject and 4% bonus in lab subjects
#for marks>=40 and <60 , 4% bonus in theory subject and 2% bonus in lab subjects
#for marks<40 , 0% bonus in theory subject and 0% bonus in lab subjects

#shreyanshrp (github.com/shreyanshrp)

#marks and type input:
marks=float(input("Enter your marks: "))
type=input("Enter your class type , Theory(T) / Lab(L) : ")

#main:
if marks >= 80 :
    if type=='T' or type=='t':
        print("You will get 8% Bonus!")
        print("Your final marks are: " , marks*1.08)
    elif type=='L' or type=='l':
        print("You will get 6% Bonus!")
        print("Your final marks are: " , marks*1.06)
    else:
        print("enter valid class type! , either T or L")
elif marks >= 60 and marks<80 :
    if type=='T' or type=='t':
        print("You will get 6% Bonus!")
        print("Your final marks are: " , marks*1.06)
    elif type=='L' or type=='l':
        print("You will get 4% Bonus!")
        print("Your final marks are: " , marks*1.04)
    else:
        print("enter valid class type! , either T or L")
elif marks >= 40 and marks < 60 :
    if type=='T' or type=='t':
        print("You will get 4% Bonus!")
        print("Your final marks are: " , marks*1.04)
    elif type=='L' or type=='l':
        print("You will get 2% Bonus!")
        print("Your final marks are: " , marks*1.02)
    else:
        print("enter valid class type! , either T or L")
elif marks > 40 :
    if type=='T' or type=='t':
        print("You will get 0% Bonus!")
        print("Your final marks are: " , marks*1.00)
    elif type=='L' or type=='l':
        print("You will get 0% Bonus!")
        print("Your final marks are: " , marks*1.00)
    else:
        print("enter valid class type! , either T or L")
else:
    print("Please enter valid marks!")