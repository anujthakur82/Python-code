# String
name = "Alok" 
friend = "xyz"
print("Hello,"+ name)

#To make single line string
Listen = "He said,\"I want to play football"
#can't put double cot in another double cot; use '\' to make it string.
print(Listen)

# To make multiple line string;use triple double cot or triple single cot just after the first n last word
friend = '''He said
Hi Alok
How are you?
"I want to play football"'''
print(friend)

#Accesssing chracter of a string
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print(name[4]); this throws an error

#Looping through string
print("Let's use a for Loop\n")
for chracter in friend:
    print(chracter)