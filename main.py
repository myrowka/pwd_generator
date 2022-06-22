import random
import string

symbols, numbers, letters = [], [], []
symbols[:0] = string.punctuation
letters[:0] = string.ascii_lowercase + string.ascii_uppercase
numbers = [str(x) for x in range(10)]


def define_num(question=''):
    num = None
    while num is None:
        try:
            num = int(input(question))
        except ValueError:
            print('Invalid input. Int is required.')

    return num


def get_num_char(char_list, num):
    for i in range(0, num):
        pwd_list.append(random.choice(char_list))


num_letters = define_num('How many letters do you want in your password: ')
num_numbers = define_num('How many numbers do you want in your password: ')
num_symbols = define_num('How many punctuation symbols do you want in your password: ')

pwd_list = []
get_num_char(letters, num_letters)
get_num_char(numbers, num_numbers)
get_num_char(symbols, num_symbols)

if pwd_list:
    random.shuffle(pwd_list)
    password = ''.join(pwd_list)
    print(f'Your generated password is: {password}\nwith length is: {len(password)}')
else:
    print("There is nothing to generate.")
