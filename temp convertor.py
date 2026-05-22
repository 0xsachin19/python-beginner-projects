print("temp calculator")
print()
print("convert celsius into faherenheit cf")
print("convert celsius into kelvin ck")
print("convert faherenheit into celsius fc")
print("convert faherenheit into kelvin fk")
print("convert kelvin into celsius kc")
print("convert kelvin into faherenheit kf")
print()
a=input("enter what you want to convert: ")#getting input for what he going to convert
if a=="cf":
    c=float(input("enter the value: ")) #getting the value
    result=(c*9/5)+32
    print(result)
elif a=="ck":
    c=float(input("enter the value: ")) #getting the value
    result=c+273.15
    print(result)
elif a=="fc":
    f=float(input("enter the value: ")) #getting the value
    result=(f-32)*5/9
    print(result)
elif a=="fk":
    f=float(input("enter the value: ")) #getting the value
    result=(f-32)*5/9+273.15
    print(result)
elif a=="kc":
    k=float(input("enter the value: ")) #getting the value
    result=k-273.15
    print(result)
elif a=="kf":
    k=float(input("enter the value: ")) #getting the value
    result=(k-273.15)*9/5+32
    print(result)
else:
    print("you chose the wrong option")
    
