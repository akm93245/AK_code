a=int(input("Enter num 1 :" ))
c=input("Enter the arthemetic operator : ")
b=int(input("Enter num 2 : "))


if (c=='+'):
    print("Addition of " , a , "and " , b , "= ", a + b )
    
elif (c=='-'):
    print("Subtraction of " , b, " from " , a , "= ", a - b )

elif(c=='*'):
    print("Multipliction of " , a , "and " , b , "= ", a * b )

elif (c=='/'):
    print("Division of " , a , "and " , b , "= ", a / b )
    
elif (c=='%'):
    print("Reminder  of " , a , "and " , b , "= ", a % b )
    
    
else : print("Invalid data ")