#break and continue in python
for i in range(12):
    if (i==10):
        break
    print("5 X", i+1, "=", 5*(i+1))
print("Loop ko chorkar nikl gya")

for i in range(1,101,1):
    print(i, end=" ")
    if(i==10):
        break
    else:
        print("Kshatriya")
print("Thank you")
        
            
#continue
for i in range(15):
    if (i==10):
        print("skip the iteration")
        continue
    print("5 X", i,"=",5*i)

for i in[2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)