while True:
    try:
        n=int(input("Enter a number"))
        b=1
        for a in range(n):
            b*=(a+1)
        print(f"It's {b}")
        break
    except:
        print("Try again!")