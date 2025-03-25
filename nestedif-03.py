num = 108
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num <= 100):
        print("Number is between 1-100")
    elif(num > 100 and num <= 199):
        print("Number is between 101-199")
    else:
        print("Number is greater than 199")
else:
    print("Number is Zero")