#Python program to calculate taxi charges according to specific slab of kilometers.
#shreyanshrp (github.com/shreyanshrp)

#Ask for change in charges:
ask=input("Do you want to change the rates? (Y/N) : ")
if ask == "Y" or ask == "y" :
    frst_10 = float(input("Enter rate(Rs/Km) for first 10Km : "))
    nxt_90 = float(input("Enter rate(Rs/Km) for next 90Km : "))
    abv_100 = float(input("Enter rate(Rs/Km) for further : "))
elif ask == "N" or ask == "n" :
    print("Taking default values for Rate")
    #Charges Declaration:
    frst_10 = 15.00
    nxt_90 = 8.00
    abv_100 = 6.00
else:
    print("Invalid input, Enter only 'Y' or 'N' (without quotes).")
    exit()

#Kilometers input:
tkm = float(input("Enter TOTAL no. of kilometers travelled : "))

#fixed distance cost:
rs_10km=10*frst_10
rs_90km=90*nxt_90

#Cost calculation & Output:
if tkm <=10 :
    print("the toatal cost is:" , tkm*frst_10 , " Rupees")
elif tkm >10 and tkm <=100 :
    print("the toatal cost is:" , ((tkm-10)*nxt_90) + rs_10km  , " Rupees")
elif tkm > 100 :
    print("the toatal cost is:" , ((tkm-100)*abv_100) + rs_10km + rs_90km , " Rupees")
else:
    print("invalid Data input!")
