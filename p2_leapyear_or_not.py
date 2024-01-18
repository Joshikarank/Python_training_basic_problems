years = input("enter the year: ")

if len(years) != 4:
    print("Invalid Year")
else:
    years = int(years)
    if years%4 == 0:
        print("leap year")
    else:
        print("not leap")
