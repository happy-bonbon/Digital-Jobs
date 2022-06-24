while True:
    try:
        year=int(input("Enter the year, \"-\"for BC"))
        if year%400==0 or (year%400!=0 and year%100!=0 and year%4==0):
            print("leap year")
            break
        else:
            print("not leap year")
            break
    except:
        print("Try again!")