# A python program to accept the monthly income of an employee and display the income tax to be paid at the end of the year according to a specific criteria.
# shreyanshrp
incm_m= float(input("enter your monthly income:"))
incm= incm_m * 12
if incm > 1000000 :
    print("Your annual  income is: ", incm , " So,applicable tax % = 4%")
    print("Tax to be paid= " , 0.04*incm)
elif incm > 500000 and incm <= 1000000 :
    print("Your annual  income is: ", incm , " So,applicable tax % = 2%")
    print("Tax to be paid= " , 0.02*incm)
elif incm <= 500000 :
    print("Your annual  income is: ", incm , " So,applicable tax % = 0%")
    print("Tax to be paid= " , 0.00*incm)
else :
    print("Invalid Input , Make sure you don't add comma in that!")