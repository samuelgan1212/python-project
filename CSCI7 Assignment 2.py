#input

CustID=input("1 of 5- Enter Cumstomer ID:")
MilkChoqty=abs(int(input("2 of 5- Enter the Numbers of pounds of Milk Chocolate@$8.50 :")))
DEChoqty=abs(int(input("3 of 5- Enter the Numbers of pounds of Dark European Chocolate@$9.75 :")))
WhiteChoqty=abs(int(input("4 of 5- Enter the Numbers of pounds of White Chocolate@$10.50 :")))
EuroChoqty=abs(int(input("5 of 5- Enter the Numbers of pounds of Eurpoean Truffles@$12.50 :")))

#Calculation

MilkChototal=MilkChoqty*8.50
DEChototal=DEChoqty*9.75
WhiteChototal=WhiteChoqty*10.50
EuroChototal=EuroChoqty*12.50
Subtotal=MilkChototal+DEChototal+WhiteChototal+EuroChototal

#Output

print("\nInvoice for Customer",CustID,":") 
print("\t",MilkChoqty,"lbs of Milk Chocolate@$8.50     \t $" , format(MilkChoqty, "2.3f"))
print("\t",DEChoqty,"lbs of Dark European Chocolate@$9.75 \t $" , format(DEChoqty, "2.3f"))
print("\t",WhiteChoqty,"lbs of White Chocolate@$10.50 \t $" , format(WhiteChoqty, "2.3f"))
print("\t",EuroChoqty,"lbs ofEurpoean Truffles@$12.50\t $" , format(EuroChoqty, "2.3f"))
print("\nSubtotal:\t\t$", format(Subtotal, "2.3f"))

if Subtotal>=80.00:
    Discount=Subtotal*0.25
    print("Less Discount of 25%\t$", format(Discount, "2.3f"))
    NetSubtotal=Subtotal-Discount
    print("\nNet Subtotal:\t $", format(NetSubtotal, "2.3f"))
elif Subtotal>=60.00 and Subtotal<=79.99:
    Discount=Subtotal*0.2
    print("Less Discount of 20%\t$", format(Discount, "2.3f"))
    NetSubtotal=Subtotal-Discount
    print("\nNet Subtotal:\t $", format(NetSubtotal, "2.3f"))
elif Subtotal>=40.00 and Subtotal<=59.99:
    Discount=Subtotal*0.15
    print("Less Discount of 15%\t$", format(Discount, "2.3f"))
    NetSubtotal=Subtotal-Discount
    print("\nNet Subtotal:\t $", format(NetSubtotal, "2.3f"))
elif Subtotal>=20.00 and Subtotal<=39.99:
    Discount=Subtotal*0.1
    print("Less Discount of 10%\t$", format(Discount, "2.3f"))
    NetSubtotal=Subtotal-Discount
    print("\nNet Subtotal:\t $", format(NetSubtotal, "2.3f"))
else:
    print ("No Discount")
    NetSubtotal=Subtotal
    print("\nNet Subtotal:\t $", format(NetSubtotal, "2.3f"))
 
Shipping=NetSubtotal
Grandtotal=Shipping+NetSubtotal
    

print("Shipping@10.0% \t $" , format(Shipping, "2.3f"))
print("\nGrand Total \t $", format(Grandtotal, "2.3f"))

print("\nHit Any Key to Continue")

