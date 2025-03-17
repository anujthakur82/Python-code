#String slicing and Operations on string
#length of a string
names = "Alok,Abhinav"
print(names[0:4]) # this gives output from 0 to n-1
print(len(names)) #len() function is used to find the lenght of the string

fruits = "Mango"
len1 = len(fruits)
print("Mango is a", len1,"letter word.")
print(len1)
print(fruits[0:4])
print(fruits[:4]) #slicing from start
print(fruits[1:4]) #slicing in btwn 
print(fruits[:5])
print(fruits[-1:len(fruits)-3]) # will not give any output
print(fruits[-3:-1]) #slicing using negative index

#Quick Quiz:
nm = "Alok"
print(nm[-3:-2])


