Name=input("Enter your name :")   
iteration=len(Name)
for j in range (0,iteration):
    for h in range(0,iteration):
        if(j==h):
            print(Name[h],sep="",end="")                       
        else:
            print("*",sep="",end="")
          
    print()
    