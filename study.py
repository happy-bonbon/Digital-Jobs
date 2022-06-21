# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:32:20 2022

@author: BonBon
"""
while True:
    try:
        #validate input
        a=int(input("Enter the month (1-12): "))
        if 0<a<13:
            if 0<a<3:
                print("It's summer. Have fun in the sun! ")
                break
            elif 3<a<6:
                print("It's autumn. Enjoy the beautiful sunsets! ")
                break
            elif 6<a<9:
                print("It's winter. Go skiing! ")
                break
            else:
                print("It's spring. Check out the spring racing carnival! ")
                break
        else:
            raise Exception("Invalid input. Please enter any number between 1 and 12. ")
    except:
        print("Invalid input. Please enter any number. ")

