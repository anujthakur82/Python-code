#strings are immutable
a = "!!!Alok!!! !!!!! !!Alok!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #to remove trailing chracter
print(a.replace("Alok","John"))
print(a.split(" ")) #to seperate string as a list items
heading = "introduction to python"
print(heading.capitalize())#make first chrcter upper case n also other chrcter to lower case 
str1 = "Welcome to python"
print(str1.center(50)) 
print(len(str1))
print(len(str1.center(50)))
print(a.count("Alok"))

str2 = "Welcome to hood!!!"
print(str2.endswith("!!!"))
print(str2.endswith("to",4,10))#to check wheather the given word exits btwn the given points

str3 = "He's name is Alok. He is an honest man"
print(str3.find("is"))#will find the given word of it very first position and give its index nmbr.
print(str3.find("ishh"))#find will return -1 if the given word is not found
print(str3.index("is"))#will show the index nmbr of given word

str4 = "WelcomeToTheConsole"
print(str4.isalnum())#alpha numeric[A-Z,a-z,0-9];

str5 = "welcome"
print(str5.isalpha())#if only alphabet gives true either false
print(str5.islower())#to check all the chrcter is in lower case ,gives true either false 

str6 = "Jai Shree Ram"
str7 = "Jai Shree Ram\n"
print(str6.isprintable())#if printable gives true either return false
print(str7.isprintable())#\n is not printable; return false

str1 = "     "  #using spacebar
print(str1.isspace())#return true
str2 = "        " #using tab
print(str2.isspace())#return true

str8 = "World Health Organization"
print(str8.istitle())#return true if first chracter of all word is in upper case either return false
str9 = "TO kill a Mocking bird"
print(str9.istitle()) 

str1 ="Python is a Intrepreted Language"
print(str1.startswith("Python"))
print(str1.swapcase())#it chng upper case to lower case n vise versa

str1 = "His name is Alok. He is an honest man."
print(str1.title())#first chctr of all words switch to upper case
