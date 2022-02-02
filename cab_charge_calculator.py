#Python program to calculate taxi charges according to specific slab of kilometers.
#shreyanshrp (github.com/shreyanshrp)

#Kilometers input:
tkm = float(input("Enter TOTAL no. of kilometers travelled : "))

#Charges Declaration:
frst_10 = 15
nxt_90 = 8
abv_100 = 6

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
