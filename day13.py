x = int(input("Enter the value of x: "))
#x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
        #case with if-condition
    case 5:
        print("case is 5")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)