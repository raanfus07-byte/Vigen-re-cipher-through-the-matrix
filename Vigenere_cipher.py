import time

def start(arr, arr2, key, mes, a):
    mes2 = []
    key2 = []
    for i in range(len(mes)):
        if mes[i] in arr2:
            mes2.append(arr2.index(mes[i]))
        else:
            print(f'символа {mes[i]} нет, он заменен на пробел, раздел 0')
            mes2.append(32)

    for i in range(len(key)):
        if key[i] in arr2:
            key2.append(arr2.index(key[i]))
        else:
            print(f'символа {key[i]} нет, он заменен на пробел, раздел 1')
            key2.append(32)

    while True:
        if len(mes2) > len(key2):
            key2 += key2
        elif len(mes) < len(key2):
            key2.pop(-1)
        else:
            break

    print(f'key2: {key2}')
    print(f'mes2: {mes2}')

    if a == '1':
        pass
        code(arr, arr2, key2, mes2)
    elif a == '2':
        encode(arr, arr2, key2, mes2)
    elif a == '3':
        math_code(key2, mes2)
    elif a == '4':
        math_encode(key2, mes2)
    else:
        print('Error:start:if-else-block:1') # защита от неверных команд
        return

def code(arr, arr2, key, mes):
    mes2 =[]
    mes3 = ''
    for x in range(len(key)):
        mes2.append(arr[key[x]][mes[x]])
    print(f'mes2: {mes2}')

    for x in range(len(mes2)):
        mes3 += arr2[mes2[x]]
    print(mes3)

def encode(arr, arr2, key, mes):
    mes2 = []
    for i in range(len(mes)):
        row_index = key[i % len(key)]
        for y in range(len(arr[row_index])):
            if arr[row_index][y] == mes[i]:
                mes2.append(y)
                break

    print(f'mes2 {mes2}')

    mes3 = ''
    for x in range(len(mes2)):
        mes3 += arr2[mes2[x]]
    print(mes3)

def math_code(key, mes):
    global N

    mes2 = []

    for i in range(len(mes)):
        mis = (key[i] + mes[i]) % N
        mes2.append(mis)

    print(f'math_code mes2: {mes2}')

    mes3 = ''
    for x in range(len(mes2)):
        mes3 += arr2[mes2[x]]
    print(mes3)

def math_encode(key, mes):
    global N
    mes2 = []

    for i in range(len(mes)):
        mis = (mes[i] - key[i]) % N
        mes2.append(mis)

    print(f'math_encode mes2: {mes2}')
    mes3 = ''
    for x in range(len(mes2)):
        mes3 += arr2[mes2[x]]
    print(mes3)

arr2 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя 1234567890!?,.(){}[]:;№#$-—_+=*&^%@"№/|`~<>«»'
N = len(arr2)
arr = [[(x + y) % N for x in range(N)] for y in range(N)]

print('---'*10)
print('Внимание! шифровка специфична, и не может взаимодействовать с онлайн шифровщиками Виженера, '
      '\nшифруется любые символы что доступны в ряде ниже, все что не указанно в ряде то заменяется на пробел автоматически'
      f'\nдоступный ряд символов: {arr2}')
print('---'*10)

while True:
    a = input('\nВведите опцию \n[1] зашифровать \n[2] расшифровать \n[3] зашифровать математическим методом \n[4] расшифровать математическим методом \n[0] выход \n:')

    if a == '1':
        key = input('введите ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно зашифровать: \n').lower().replace('ё', 'е').replace('ъ', 'ь')
        start(arr, arr2, key, mes, a)
    elif a == '2':
        key = input('введите ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно расшифровать: \n').lower().replace('ё', 'е').replace('ъ', 'ь')
        start(arr, arr2, key, mes, a)
    elif a == '3':
        key = input('введите ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно зашифровать: \n').lower().replace('ё', 'е').replace('ъ', 'ь')
        start(arr, arr2, key, mes, a)
    elif a == '4':
        key = input('введите ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно расшифровать: \n').lower().replace('ё', 'е').replace('ъ', 'ь')
        start(arr, arr2, key, mes, a)
    elif a == '0':
        print('выход из программы')
        break
    else:
        print('неверная команда')
        time.sleep(1.5)
