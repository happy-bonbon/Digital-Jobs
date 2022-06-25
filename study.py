while True:
    try:
        n=int(input("Enter a number "))
        print(f"{len(str(n))} digits.")
        break
    except:
        print("Try again!")
