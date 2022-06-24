while True:
    try:
        n=int(input("Enter a number "))
        #a is the fwd number, b is the aft number
        a,b=0,1  
        #hardcode 0,1st,2nd number
        if n==1:
            print("The 1st Fibonacci number is 0")
            break
        elif n==0:
            print("That Fibonacci number is 0")
            break
        elif n==2:
            print("The 2nd Fibonacci number is 1")
            break
        else:
            for _ in range(n-2):
                #calculate and swap
                a,b=b,a+b
            print(f"The {n}th Fibonacci number is {b}")
            break
    except:
        print("Try again!")
