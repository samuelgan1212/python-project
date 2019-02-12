#input

CustID= raw_input("1 of 6- Enter Cumstomer ID:")
Whizbangsqty=abs(int(input("2 of 6- Enter the Number of Whizbangs@$5.00:")))
Gizmosqty=abs(int(input("3 of 6- Enter the Number of Gizmos@$10.15:")))
Widgetsqty=abs(int(input("4 of 6- Enter the Number of Widgets@$5.99:")))
Wabbitsqty=abs(int(input("5 of 6- Enter the Number of Wabbits@$7.75:")))
Elmersqty=abs(int(input("6 of 6- Enter the Number of Elmers@$9.50:")))

#Calculation

Whizbangstotal=Whizbangsqty*5.00
Gizmostotal=Gizmosqty*10.15
Widgetstotal=Widgetsqty*5.99
Wabbitstotal=Wabbitsqty*7.75
Elmerstotal=Elmersqty*9.50
Subtotal=Whizbangstotal+Gizmostotal+Widgetstotal+Wabbitstotal+Elmerstotal
Saletax=Subtotal*0.095
Shipping=Subtotal*0.1
Grandtotal=Saletax+Shipping+Subtotal

#Output

print"\nInvoice for Customer",CustID,":"
print"\t",Whizbangsqty,"Whizbangs @$5.00 \t $" ,'{0:.2f}'.format(Whizbangstotal)
print"\t",Gizmosqty,"Gizmos @$10.15 \t $" ,'{0:.2f}'.format(Gizmostotal)
print"\t",Widgetsqty,"Widgets @$5.99 \t $" ,'{0:.2f}'.format(Widgetstotal)
print"\t",Wabbitsqty,"Widgets @$7.75 \t $" ,'{0:.2f}'.format(Wabbitstotal)
print"\t",Elmersqty,"Elmers @$7.75 \t $" ,'{0:.2f}'.format(Elmerstotal)
print"\nSubtotal:\t $",'{0:.2f}'.format(Subtotal)
print"Salestax @9.5% \t $",'{0:.2f}'.format(Saletax)
print"Shipping@10.0% \t $" ,'{0:.2f}'.format(Shipping)
print"\nGrand Total \t $",'{0:.2f}'.format(Grandtotal)

print"\nHit Any Key to Continue..."


