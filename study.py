while True:
    try:
<<<<<<< HEAD
        n=int(input("Enter a number "))
        print(f"{len(str(n))} digits.")
        break
    except:
        print("Try again!")
=======
        #validate input
        a=int(input("Enter a number: "))
        i=1
        while i<=a:
            print(i*"*")
            i+=1
        break
    except:
        print("Invalid input. Please enter any number. ")
>>>>>>> aae8f558fd94e984dbfd083e59e6bbe5f636dd49
