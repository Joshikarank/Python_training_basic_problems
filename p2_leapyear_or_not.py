years = 0

while True:
    years = input("enter the year: ")
    if len(years) == 4:
        break
    else:
        print("invalid year")
years = int(years)
if (years%4 == 0 and years%100 != 0):
    print("leap year")
elif years%400 == 0:
    print("Leap year")
else:
    print("not leapyear")
