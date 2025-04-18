#Function in python

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def name(fname,lname):
    print("Namaste,", fname,"and",lname)

name("Ram","Shyam")    

def isLesser(a,b):
    pass   #(pass means ki isko user bd me perform krega abbi kevl funtn likh k chodd rkha h)

x = 4
y = 8
isGreater(x,y)
calculateGmean(x,y)
#gmean1 = (a*b)/(a+b)
#print(gmean1)

p = 5
q = 10
isGreater(p,q)
calculateGmean(p,q)
#gmean2 =(c*d)/(c+d)
#print(gmean2)