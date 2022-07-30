def get_input():
    """Get input from user

    Return: 
        num = user inputed number"""

    num = str(input('What is the DEA or NPI number you are checking? '))

    return num


def check_num_len(num):
    """Checks the length of the number to see if it a possible DEA
    or NPI number. Prints statement if number is the wrong length.
    
    Return:
        num_type = the type of number that the user inputed."""

    if len(num) < 9:
        print('This number is not enough characters to be a DEA or NPI number')
        pass

    elif len(num) == 9:
        num_type = 'DEA'
        return num_type

    # 10-position NPI number
    elif len(num) == 10:
        num_type = 'NPI'
        return num_type

    # # 15-position NPI number
    elif len(num) == 15:
        num_type = 'NPI'
        return num_type

    else:
        print('This number is too many characters to be a DEA or NPI number')
        pass


def check_DEA_num(DEA_num):
    """Checks if the inputed number is a valid DEA number by verifying that 
    the first letter is an a, b, f, k, g, m, x based on type of provider.
    Then the first, third, and firth digits are added. The second, fourth, 
    and sixth digits are added. The sum of even numbers are doubled and added to the 
    sum of the odd numbers. The last digit of the resulting number is
    compared to the 7th digit checksum of the DEA number. 

    Return:
        num_is = True or False based on if number is valid"""

    ### set default
    num_is = False

    ### break string apart and convert numbers to int
    first_letter = (DEA_num [0])
    first = int(DEA_num [2])
    second = int(DEA_num [3])
    third = int(DEA_num [4])
    fourth = int(DEA_num [5])
    fifth = int(DEA_num [6])
    sixth = int(DEA_num [7])

    ## 7th digit is checksum
    check_sum = int(DEA_num [8])

    ## verify first letter is allowed value
    if (first_letter.lower()) in('a','b','f','k','g','m','x'):

        ## run digits through verifying calculations
        odd = first + third + fifth
        even = (second + fourth + sixth) * 2
        sum = odd + even
        string = f'{sum}'

        ## get last digit of resulting value
        last_digit = (string [1])

        ## check if last digit matches checksum
        if str(last_digit) == str(check_sum):
            num_is = True
        else:
            num_is = False
    else:
        num_is = False
    
    return num_is


def check_NPI_num(NPI_num):
    """Checks if the inputed number is a valid NPI number by verifying first 
    five digits (if 15-position NPI number) and then running last 10 digits through
    the Luhn algorithm to verify the checksum.

    Return:
        num_is = True or False based on if number is valid"""

    def double_and_sum_digits(num):
        """Doubles the given digit. If the returning number is 
        greater than 2 digits in length, then those digits are added together.
        
        Returns:
            num: the resulting number from doubling and possibly adding resulting digits"""

        num = num * 2

        if num > 9:
            num = str(num)
            num = int(num[0]) + int(num[1])

        return num

    ## set default
    num_is = False

    ## If NPI_num is 15-position, then need to check if first 5 digits 
    ## are 80840 and then pass on only the last 10 digits. If the
    ## first 5 digits are not 80840, then the number is not valid.
    if len(NPI_num) == 15:
        if NPI_num[0:5] == '80840':
            NPI_num = NPI_num[5:15]
        else:
            pass

    first = int(NPI_num [0])
    second = int(NPI_num [1])
    third = int(NPI_num [2])
    fourth = int(NPI_num [3])
    fifth = int(NPI_num [4])
    sixth = int(NPI_num [5])
    seventh = int(NPI_num [6])
    eighth = int(NPI_num [7])
    ninth = int(NPI_num [8])

    ## 10th digit is check digit
    check_sum = int(NPI_num [9])

    ## run odd digits through double and sum
    first = double_and_sum_digits(first)
    third = double_and_sum_digits(third)
    fifth = double_and_sum_digits(fifth)
    seventh = double_and_sum_digits(seventh)
    ninth = double_and_sum_digits(ninth)

    ## add all resulting digits together and add 24 (accounts for 15-position NPI by adding 24)
    digits_added = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + 24

    ## change into string to make iterable
    digits_added_str = str(digits_added)

    ## take last digit of the string and convert it to an int
    last_digit = int(digits_added_str[-1])

    ## take last digit of digits_added and subtract from 10
    check = 10 - last_digit

    ## verify checksum
    if check == check_sum:
        num_is = True
    else:
        num_is = False

    return num_is


def print_result(num_is, num_type):
    """Print results based on type of number and if number is found valid

    Return: 
        none"""

    print()
    if num_is:
        print(f'This number is a valid {num_type} number')
    else:
        print(f'This number is not a valid {num_type} number')


def main():

    ## get the input from the user
    num = get_input()

    ## check what type of number has been inputed
    num_type = check_num_len(num)

    ## check if num is valid
    if num_type == 'DEA':
        num_is = check_DEA_num(num)
        print_result(num_is, num_type)
    elif num_type == 'NPI':
        num_is = check_NPI_num(num)
        print_result(num_is, num_type)


# valid DEA number: BB1388568
# invalid DEA number: CC1258745

# valid 10-position NPI number: 1234567893
# invalid 10-position NPI number: 124567892

# valid 15-position NPI number: 808401234567893
# invalid 15-postion NPI number: 880001234567893

main()
