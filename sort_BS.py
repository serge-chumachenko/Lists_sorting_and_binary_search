import sort_BSCL
odd_nums = []
even_nums = []
all_nums = []
print("Hello! I'm a program...")
while True:
    ask = input("Would you like to insert your numbers? Y or N?\n")
    if ask == "Y" or ask == "y":
        try:
            number = int(input("OK! Let's go! You can insert your number here: \n"))
        except ValueError:
            print("Attention! You can insert only integer numbers!") 
        else:
            if number %2 == 0:
                even_nums.append(number)
                sort_BSCL.general_list(number,all_nums)
                print("OK! Your number has been added!")
            else:
                odd_nums.append(number)
                sort_BSCL.general_list(number,all_nums)
                print("OK! Your number has been added!")
    elif ask == "N" or ask == "n":
        print("How would you like to sort your lists?\n")
        choose = input("Choose your method?\n1-ASC\n2-DESC\n1 or 2:\n")
        s1 = sort_BSCL.My_sorting(odd_nums)
        s2 = sort_BSCL.My_sorting(even_nums)
        if choose == "1":
            s1.asc()
            s2.asc()
            print("Thank you! Your lists are here:")
            break
        elif choose == "2":
            s1.desc()
            s2.desc()
            print("Thank you! Your lists are here:")
            break
    else:
        ask = input("Y or N? \n")
print("ODD NUMBERS LIST:\n{}".format(odd_nums))
print("EVEN NUMBERS LIST:\n{}".format(even_nums))
print("ALL NUMBERS LIST:\n{}".format(all_nums))