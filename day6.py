# Typecasting in Python
# "Explicit typecasting"

# eg.1
a = "1"
b = "2"
print(int(a)+int(b))

# eg.2
string = "22"
number = 8
string_number = int(string) #if the string is not a valid integer it will throw an error
sum= number + string_number
print("The sum of both the numbers is:",sum)

# "Implicit typecasting"

# eg.1
c= 2.1
d= 5
print(c+d)

# eg.2
a = 4  #python automatically convert a to int
print(type(a))  
b = 6.0  #python automatically convert b to float
print(type(b))  
c = a+b  #python automatically converts c to float as it is a float addition
print(c)
print(type(c))

