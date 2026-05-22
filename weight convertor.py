print("kg into pounds & punds into kg")
print("if kg means enter K , and pounds means P")
a=input("what you want to conert: ")

if a=="k" or a=="K":
    weight=float(input("enter the weight in pounds: "))
    result=weight/2.2046
    print(f"your kg is : {result}")
elif a=="p" or a=="P":
    weight=float(input("enter the weight in kg: "))
    result=weight*2.2046
    print(f"your pounds is : {result}")
