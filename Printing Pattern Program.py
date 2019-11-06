#exercise no 4
print("Printing Pattern...!")
print("Print Pattern...!")
n=int(input("Enter row no."))
var_bool=int(input("enter boolean value for 1=True and for 0= False"))
if var_bool==1:
    for i in range (0,n+1):
        print('*'*int(i))
elif var_bool==0:
    for i in range (n,0,-1):
        print("* "*int(i))


