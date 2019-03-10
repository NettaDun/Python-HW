def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    numbers_to_print = []
    for num in range(100000,1000000):
        num_str = str(num)  
        if (num_str[2] == num_str[5]) & (num_str[3] == num_str[4]):
            num_plus_1 = str(num + 1)
            if (num_plus_1[1] == num_plus_1[5]) & (num_plus_1[2] == num_plus_1[4]):
                num_plus_2 = str(num + 2)
                if (num_plus_2[1] == num_plus_2[4]) & (num_plus_2[2] == num_plus_2[3]):
                    num_plus_3 = str(num + 3)
                    if  (num_plus_3[0] == num_plus_3[5]) & (num_plus_3[1] == num_plus_3[4]) & (num_plus_3[2] == num_plus_3[3]):
                        numbers_to_print.append(num)
                        
    print(numbers_to_print)                          

check_palindrome()