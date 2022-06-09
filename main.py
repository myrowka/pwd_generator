import random
import string

symbols = []
numbers = []
letters = []
symbols[:0] = string.punctuation
letters[:0] = string.ascii_lowercase + string.ascii_uppercase
numbers = list(map(lambda x: str(x), list(range(0, 10))))


def define_num(question=''):
    num = None
    while num is None:
        try:
            num = int(input(question))
        except ValueError:
            print('Invalid input. Int is requiered.')

    return num


def get_num_char(char_list, num):
    for i in range(0, num):
        pwd_list.append(random.choice(char_list))


num_letters = define_num('How many letters you want in your password: ')
num_numbers = define_num('How many numbers you want in your password: ')
num_symbols = define_num('How many symbols you want in your password: ')

pwd_list = []
get_num_char(letters, num_letters)
get_num_char(numbers, num_numbers)
get_num_char(symbols, num_symbols)

password = ""
if pwd_list:
    random.shuffle(pwd_list)
    for char in pwd_list:
        password += char
    print(f'Your generated password is: {password}\nThe length is: {len(password)}')
else:
    print("There is nothing to generate.")
