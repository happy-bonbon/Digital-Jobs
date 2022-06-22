while True:
    try:
        #validate input
        a=int(input("Enter a number: "))
        i=1
        while i<=a:
            print(i*"*")
            i+=1
        break
    except:
        print("Invalid input. Please enter any number. ")