#function
def Add(x,y):
    return x+y;
def Subtract(x,y):
    return x-y;
def Mult(x,y):
    return x*y;
def Divide(x,y):
    return x/y; 
def power(x,y):
    return x**y;
def All(x,y):
        result=x+y
        result2=x-y;
        result3=x*y;
        result4=x/y;
        result5=x**y;
        print(num1,"+",num2,"=",format(result, "2.2f"))
        print(num1,"-",num2,"=",format(result2, "2.2f"))
        print(num1,"*",num2,"=",format(result3, "2.2f"))
        print(num1,"/",num2,"=",format(result4, "2.2f"))
        print(num1,"^",num2,"=",format(result5, "2.2f"))


def Nodivide(x,y):
        result=x+y
        result2=x-y;
        result3=x*y;
        result5=x**y;
        print(num1,"+",num2,"=",format(result, "2.2f"))
        print(num1,"-",num2,"=",format(result2, "2.2f"))
        print(num1,"*",num2,"=",format(result3, "2.2f"))
        print(num1,"^",num2,"=",format(result5, "2.2f"))    


    
#Main routine
again = "y"
while again == "y":

    print("Option#1-Add Two Numbers")
    print("Option#2-Subtract Two Numbers")
    print("Option#3-Multiply Two Numbers")
    print("Option#4-Divide two Numbers")
    print("Option#5-Raise One Number to the Power of a Second Number")
    print("Option#6-ALL Calcutions")
    print("Option#7-Quit")
    Option= input("Enter Option:1,2,3,4,5,6 or 7:")


    if Option=="1":
        num1=float(input("\nEnter First Number:"))
        num2=float(input("\nEnter Second Number:"))
        result=Add(num1,num2)
        print(num1,"+",num2,"=",format(result, "2.2f"))

    elif Option=="2":
        num1=float(input("\nEnter First Number:"))
        num2=float(input("\nEnter Second Number:"))
        result=Subtract(num1,num2)
        print(num1,"-",num2,"=",format(result, "2.2f"))
        
    elif Option=="3":
        num1=float(input("\nEnter First Number:"))
        num2=float(input("\nEnter Second Number:"))
        result=Mult(num1,num2)
        print(num1,"*",num2,"=",format(result, "2.2f"))
        
    elif Option=="4":
        num1=float(input("\nEnter First Number:"))
        num2=float(input("\nEnter Second Number:"))
        if num2!=0:
            result=Divide(num1,num2)
            print(num1,"/",num2,"=",format(result, "2.2f"))
        else:
            print("0 can not be denominator, Please try again")

    elif Option=="5":
        num1=float(input("\nEnter First Number:"))
        num2=float(input("\nEnter Second Number:"))
        power(num1,num2)
        print(num1,"^",num2,"=",format(power(num1,num2), "2.2f"))
        
    elif Option=="6":
        num1=float(input("\nEnter First Number:"))
        num2=float(input("\nEnter Second Number:"))
        if num2!=0:
            All(num1,num2)
        else:
            Nodivide(num1,num2)
            print("0 can not be denominator, Please try again")

    elif Option=="7":
        exit()

    else:
        print("You enter an Invaild Number")


    again = input("\nRun this Again (Y or N): ")
    again = again.lower()
exit()
