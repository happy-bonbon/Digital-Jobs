def frecheck(fre):
    return 88.0 <= fre <= 108.0


while True:
    try:
        my_fre = input("Enter the frequency with only One decimal place: ")

        # check decimal place
        if len(my_fre.split(".")[1]) == 1:
            
            # Check frequency
            if frecheck(float(my_fre)):
                print("Valid frequency!!")
                break
            else:
                print("Invalid frequency!!")
                break
        else:
            raise Exception("Bad input.")
    except:
        print("Bad input.")
