from program.scripting.parse_string_to_int import parse_string_to_int


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
        print('This number is not enough characters long to be a DEA or NPI number')
        pass

    elif len(num) == 9:
        num_type = 'DEA'
        return num_type

    # 10-position NPI number
    elif len(num) == 10:
        num_type = 'NPI'
        return num_type

    # # 15-position NPI number
    # elif len(num) == 15:
    #     num_type = 'NPI'
    #     return num_type

    else:
        print('This number is too many characters to be a DEA or NPI number')
        pass


def check_DEA_num(DEA_num):
    """Checks if the inputed number is a valid DEA number by verifying.....
    (add how it verifies here)
    
    Return:
        num_is = True or False based on if number is valid"""

    ### set default
    num_is = False

    # ### break number into list and change type if character is an int
    # dea_list = parse_string_to_int(DEA_num)

    # ### break list for calculations
    # first_letter = dea_list [0]
    # first = dea_list [2]
    # second = dea_list [3]
    # third = dea_list [4]
    # fourth = dea_list [5]
    # fifth = dea_list [6]
    # sixth = dea_list [7]
    # seventh = dea_list [8]

    first_letter = (DEA_num [0])
    first = int(DEA_num [2])
    second = int(DEA_num [3])
    third = int(DEA_num [4])
    fourth = int(DEA_num [5])
    fifth = int(DEA_num [6])
    sixth = int(DEA_num [7])
    seventh = int(DEA_num [8])

    if (first_letter.lower()) in('a','b','f','k','g','m','x'):
        odd = first + third + fifth
        even = (second + fourth + sixth) * 2
        sum = odd + even
        string = f'{sum}'
        last_digit = (string [1])
        if str(last_digit) == str(seventh):
            num_is = True
        else:
            num_is = False
    else:
        num_is = False
    
    return num_is

def check_NPI_num(NPI_num):
    num_is = False

    # if NPI_num is 15-position, then need to check if first 5 digits are 80840 and 
    # then pass on only the last 10 digits

    # Valid test NPI number: 1234567893

    first = int(NPI_num [0])
    second = int(NPI_num [1])
    third = int(NPI_num [2])
    fourth = int(NPI_num [3])
    fifth = int(NPI_num [4])
    sixth = int(NPI_num [5])
    seventh = int(NPI_num [6])
    eighth = int(NPI_num [7])
    ninth = int(NPI_num [8])

    ### check digit
    tenth = int(NPI_num [9])


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


    first = double_and_sum_digits(first)
    third = double_and_sum_digits(third)
    fifth = double_and_sum_digits(fifth)
    seventh = double_and_sum_digits(seventh)
    ninth = double_and_sum_digits(ninth)

    ### add all resulting digits together and add 24 (accounts for 15-position NPI)
    digits_added = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + 24

    ### change into string to make iterable
    digits_added_str = str(digits_added)

    ### take last digit of the string and convert it to an int
    last_digit = int(digits_added_str[-1])

    ### take last digit of digits_added and subtract from 10
    ### could also subtract total from next multiple of 10 (70 - 67 = 3)
    check_sum = 10 - last_digit

    if tenth == check_sum:
        num_is = True
    else:
        num_is = False

    return num_is


def print_result(num_is, num_type):

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

main()
