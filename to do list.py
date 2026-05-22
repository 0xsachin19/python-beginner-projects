print("To do list")
print()
to_do=["home work","study"]
print(" enetr 1 to add ")
print(" enetr 2 to show ")
print(" enetr 3 to delete ")
print()
def result():
    for i in range(len(to_do)):
        print(i+1,to_do[i])
            
a=int(input("enter what you want to do: "))
            
if a==1:
    times=int(input("enter how many to add: "))
    for i in range(times):
        answer=input("enter what you want to add: ")
        to_do.append(answer)
    result()
    
elif a==2:
     if to_do==[]:
         print("the to do list is empty")
     else:
         result()
elif a==3:
    d=input("enetr what youn wnat to del: ")
    to_do.remove(d)
    print(f"your {d} is removed")
    result()
else:
    print("you chose the wrong option")


    
