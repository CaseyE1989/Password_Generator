import random
letters = ['a', 'b' , 'c' ,'d' , 'e' , 'f' , 'g', 'h', 'i', 'j', 'k' , 'l', 'm', 'n', 'o', 'p', 'q', 'r' ,'s','t','u','v','w','x','y','z',
           'A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','^','&','*','+']

print('Welcome to PyPassword Generator!')
password_letter_amount = int(input('How many letters would you like in your password? '))
password_symbol_amount = int(input('How many symbols would you like? '))
password_number_amount = int(input('How many numbers would you like? '))

password = ''

for letter in range(1, password_letter_amount + 1):
    random_char = random.choice(letters)
    password += random_char


for symbol in range(1, password_symbol_amount + 1):
    random_char = random.choice(symbols)
    password += random_char


for number in range(1, password_number_amount + 1):
    random_char = random.choice(numbers)
    password += random_char

shuffle_password = list(password)
random.shuffle(shuffle_password)
random_password = ''.join(shuffle_password)


print(f'Here is your password {random_password}')

input()


