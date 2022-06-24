while True:
    try:
        a=float(input("Enter the 1st Number "))
        b=float(input("Enter the 2nd Number "))
        c=input("Enter an operator")

        #validate operators, But forgot div by 0        
        if len(c)==1:
            if c=="+":
                d=a+b
            elif c=="-":
                d=a-b
            elif c=="/":
                d=a/b
            elif c=="*":
                d=a*b
            else:
                raise Exception("Try again!")
            #print result
            print(f"{a}{c}{b} is equal to {d}.")
            break
        else:
            raise Exception("Try again!")
    except:
        print("Try again!")