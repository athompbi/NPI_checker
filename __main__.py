

def get_input():
    """Get input from user

    Return: 
        num = user inputed number"""

    num = str(input('What is the DEA or NPI number you are checking? '))

    return num


def check_num_type(num):
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
    elif len(num) == 10:
        num_type = 'NPI'
        return num_type
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

    ### break DEA number into single digits
    first = int(DEA_num [2])
    second = int(DEA_num [3])
    third = int(DEA_num [4])
    fourth = int(DEA_num [5])
    fifth = int(DEA_num [6])
    sixth = int(DEA_num [7])
    seventh = int(DEA_num [8])

    if (DEA_num.lower()[0]) in('a','b','f','k','g','m','x'):
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

def check_NPI_num(number):
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
    num_type = check_num_type(num)

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
