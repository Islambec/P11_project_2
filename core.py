num = (int(input('Введите первое число: ')))
con = input('Выберите значение (+,-,/,*): ')
num_2 = (int(input('Введите второе число: ')))
while True:
    if con == '+':
        print(f'{num} + {num_2} = {num + num_2}')
        break
    elif con == '-':
        print(f'{num} - {num_2} = {num - num_2}')
        break
    elif con == '/':
        print(f'{num} / {num_2} = {num / num_2}')
        break
    elif con == '*':
        print(f'{num} * {num_2} = {num * num_2}')
        break
    else:
        print('Ведите правилно')
        break
