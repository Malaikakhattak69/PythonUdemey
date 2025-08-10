num1=float(input("enter number 1"))
num2=float(input("enter number 2"))
operator=input("enter operator(+,-,*,/)")

if(operator=="+"):
    print("Result: ",num1+num2)
elif(operator=="-"):
    print("Result: " ,num1-num2)
elif(operator=="*"):
    print("Result: ",num1*num2)
elif(operator=="/"):
    if(num2==0):
        print("not divisible")
    else:
        print("Result: ",num1/num2)
else:
    print("invalid operator enter another")