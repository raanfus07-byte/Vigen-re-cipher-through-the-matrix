def start(arr, arr2, key, mes, a):
    mes2 = []
    key2 = []
    for i in range(len(mes)):
        mes2.append(arr2.index(mes[i]))

    for i in range(len(key)):
        key2.append(arr2.index(key[i]))

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

arr2 = 'абвгдежзийклмнопрстуфхцчшщыьэюя 1234567890!?,.(){}[]:;№#$-_+=*&^%@"№/|`~<>'
N = len(arr2)
arr = [[(x + y) % N for x in range(N)] for y in range(N)]

print('---'*10)
print('Внимание! шифровка специфична, и не может взаимодействовать с онлайн шифровщиками Виженера, '
      '\nона сделана настолько криво что сообщения могут быть расшифрованы только подобным кодом'
      '\nв отличии от иных шифровщиков виженера, тут шифруются все, что вы вводите, от пробелов и обычных букв до спецсимволов и чисел'
      f'\nдоступный ряд символов: {arr2}')
print('---'*10)

while True:
    a = input('\nВведите опцию \n[1] зашифровать \n[2] расшифровать \n[0] выход \n:')

    if a == '1':
        key = input('введите ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно зашифровать: \n').lower().replace('ё', 'е').replace('ъ', 'ь')
        start(arr, arr2, key, mes, a)
    elif a == '2':
        key = input('введите ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно расшифровать: \n').lower().replace('ё', 'е').replace('ъ', 'ь')
        start(arr, arr2, key, mes, a)
    elif a == '0':
        print('выход из программы')
        break
    else:
        print('неверная команда')
