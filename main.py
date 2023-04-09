from random import choice

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm',
            'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

caracters = ['!', '@', '#', '$', '%', '&', '*', '_', '+', '-', '=', '~']

_list = alphabet + numbers + caracters
passwords_length = 15
password = ''

for i in range(passwords_length):
    password += choice(_list)

print(password)