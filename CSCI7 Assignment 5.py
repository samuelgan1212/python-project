import random

again = "y"
while again == "y":

    tosses=input("How many times do you want to toss?")
    tosses=int(tosses)

    Sides=input("Which side of a coin will come up?(Head or Tail):")
    Sides=str(Sides)

    head=tail=0
    win=lost=0

    for n in range (1,tosses+1):
        Randomside=random.randint(1,2)
        if Randomside==1: 
                test="Head"
        elif Randomside==2:
                test="Tail"

        print("Result#",n," the coin comes up",test)
        if test=="Head":
                head+=1
        elif test=="Tail":
                tail+=1
        if test==Sides:
                win+=1
        elif test!=Sides:
                lost+=1


    print("\n\nThe result is out.Your guess is",Sides,".")
    print("It comes out total",tosses,"times")
    print("It have",head,"times head and have",tail,"times tail")
    print("You get",win,"times correct and you get",lost,"times incorrect")
    winpercent=win/tosses*100
    lostpercent=lost/tosses*100
    print("Your win percentages are",format(winpercent, "2.2f"),"%")
    print("Your lost percentages are",format(lostpercent, "2.2f"),"%")
       

    again = input("\nRun this Again (Y or N): ")
    again = again.lower()
exit()
