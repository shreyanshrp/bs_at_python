# A python program to accept the monthly income of an employee and display the income tax to be paid at the end of the year according to a specific criteria.
# shreyanshrp

print("""Tax slab is as follows:
nil tax for annual income <=500k
2% tax for annual income in range (500k 1M]
4% tax for annual income >1M""")

slab_change = input("Do you want to change? (y/n)")

#slab settings:
if slab_change == "y" :
    #new slab
    a=float(input("enter % tax for =<500k : "))
    b=float(input("enter % tax for (500k  1M] : "))
    c=float(input("enter % tax for >1M : "))
    
elif slab_change == "n" :
    #default slab
    a=0
    b=2
    c=4
else:
    print("Invalid input, write only 'y' or 'n' (without quotes)")
    exit()

#income input:
incm_m= float(input("enter your monthly income:"))
incm= incm_m * 12

#Tax Calculation:
if incm > 1000000 :
    print("Your annual  income is: ", incm , " So,applicable tax % =" , c , "%")
    print("Tax to be paid= " , (c/100)*incm , "yearly")
elif incm > 500000 and incm <= 1000000 :
    print("Your annual  income is: ", incm , " So,applicable tax % =", b , "%")
    print("Tax to be paid= " , (b/100)*incm , "yearly")
elif incm <= 500000 :
    print("Your annual  income is: ", incm , " So,applicable tax % =" , a , "%")
    print("Tax to be paid= " , (a/100)*incm , "yearly")
else :
    print("Invalid Input , Make sure you don't add comma in that!")