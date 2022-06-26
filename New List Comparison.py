def common_str(alist, blist):

    # check for matches by count the new list
    common_list = {a for a in alist for b in blist if a == b}

    return len(common_list)


# to fix the duplicate items problem:
def cheat(alist, blist):
    return len(set(alist).intersection(blist))


a_list = input("Enter the first list:  ").split()
b_list = input("Enter the second list:  ").split()

# print(common_str(a_list,b_list))
print(cheat(a_list, b_list))
