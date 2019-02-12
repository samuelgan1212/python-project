#input

EmployeeID=input("1 of 6-Enter Employee ID(i.e. AF101):")
EmployeeLn=input("2 of 6-Enter Employee Last Name:")
EmployeeFn=input("3 of 6-Enter Employee First Name:")

Hours=float(input("4 of 6-Enter Weekly Hours(Maximun of 60 Hours per Week):"))

while Hours>60 or Hours<0:
    if Hours>0:
        print(Hours,"Weekly Hours is ABOVE the 60 maximum")
        Hours=float(input("4 of 6-Enter Weekly Hours(Maximun of 60 Hours per Week):"))
    else:
        print("You entered a NEGATIVE Weekly Hours. Please enter a POSITIVE Weekly Hours.")
        Hours=float(input("4 of 6-Enter Weekly Hours(Maximun of 60 Hours per Week):"))
        
Pay=float(input("5 of 6-Enter Hourly Pay Rate(Minimun of $10.50 To a Maximum of $100.00 per Hours):"))

while Pay<10.5 or Pay>100:
    if Pay<10.5 and Pay>0:
        print ("You entered a Pay Rate of $",Pay,"LESS than the Minimunm of $10.50" )
        Pay=float(input("5 of 6-Enter Hourly Pay Rate(Minimun of $10.50 To a Maximum of $100.00 per Hours):"))
    elif Pay<0:
        print("You entered a NEGATIVE Pay rate. Please enter a POSITIVE Pay Rate.")
        Pay=float(input("5 of 6-Enter Hourly Pay Rate(Minimun of $10.50 To a Maximum of $100.00 per Hours):"))
    else:
        print("You entered a Pay Rate of $",Pay,"MORE than the Maximunm of $100")
        Pay=float(input("5 of 6-Enter Hourly Pay Rate(Minimun of $10.50 To a Maximum of $100.00 per Hours):"))

Tax=float(input("6 of 6-Enter Income tax Rate(Minimum of 0 to a Maximum of 40%(0.4)):"))

while Tax<0 or Tax>0.4:
    if Tax<0:
        print("You entered a NEGATIVE Tax Rate. Please enter a POSITIVE Tax Rate.")
        Tax=float(input("6 of 6-Enter Income tax Rate(Minimum of 0 to a Maximum of 40%(0.4)):" ))
       
    else:
        print("You enetered a taxrate of",Tax,"which is above the Maximum of 0.4")
        Tax=float(input("6 of 6-Enter Income tax Rate(Minimum of 0 to a Maximum of 40%(0.4)):" ))


#Calculation

Grosspay=Hours*Pay
TaxWithheld=Grosspay*Tax
Netpay=Grosspay-TaxWithheld
Taxrate=100*Tax

#Output

print( "\n\nWeekly Pay Check for",EmployeeID,"\t",EmployeeFn,EmployeeLn )
print( Hours,"Hours Worked@ $",Pay )
print( "\nGross pay for \t\t$",format(Grosspay, "2.2f"))
print( "Tax Withheld@",Taxrate,"%\t$",format(TaxWithheld, "2.2f") )
print( "Netpay\t\t\t$",format(Netpay, "2.2f"))


print("\n\nHit any key to continue")

