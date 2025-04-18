# Function Arguments and return statement

# 1.Default argument:
def average(a=6,b=4):
    print("The average is",(a+b)/2)
average()
average(a=2)
average(b=8)

# 2.Keyword argument:
average(b=9,a=6)

# 3.Required argument
def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)
#name("Alok","Singh");this does not match with requird argument
name("Alok","Singh","Srinet")

# 4.Variable-length argument:
def average(*numbers):
    print(type(numbers))
    sum =0
    for i in numbers:
        sum =sum + i
    print("Average is:",sum/len(numbers))
average(4,5,6,7,8)

def name(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(mname = "Singh",lname = "Srinet",fname = "Alok")

# Return statement:"iska mtlb finding value ko le k wps chle jana as a output"
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
c= average(1,2,3,4)
print(c)

def name(fname,mname,lname):
    return "Hello," + fname + " " + mname + " " + lname
print(name("Alok","Singh","Srinet"))