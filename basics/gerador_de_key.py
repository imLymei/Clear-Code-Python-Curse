import random

def key_default_check(key):
    if len(key) == 13:  # Verifica se a key tem 13 caracteres

        if key[3] == '-':  # Verifica se o 4º caractere é um hífen

            if key[:3].isnumeric() and key[4:].isnumeric():  # Verifica se os 3 primeiros e os 9 últimos caracteres são numéricos

                return True
    
    return False


def key_splitter(key):
    key = key.split('-')  # Separa a key em 2 partes, a primeira com 3 caracteres e a segunda com 9 caracteres

    divider = 0
    real_key = 0

    for number in key[0]:  # Converte os caracteres em números e os soma
        
        divider += int(number)

    for number in key[1]:  # Converte os caracteres em números e os soma
        
        real_key += int(number)

    return [divider, real_key]


def key_validation(key):
    if key_default_check(key):
        
        key = key_splitter(key)

        divider = key[0]
        real_key = key[1]

        if divider == 0:  # Verifica se o divisor é 0
            
            return False
        elif real_key == 0:  # Verifica se a key é 0
            
            return False
        else:
            
            if real_key % divider == 0:  # Verifica se a key é divisível pelo divisor
                
                return True

    return False


def key_generator():
    key = ''

    for i in range(0, 3):  # Gera os 3 primeiros caracteres

        key += str(random.randrange(10))

    key += '-'  # Adiciona o hífen

    for i in range(0, 9):  # Gera os 9 últimos caracteres

        key += str(random.randrange(10))

    if not key_validation(key):  # Verifica se a key gerada é válida

        key = key_generator()

    return key


def main():
    key = input('Digite a key (Ex: 123-123456789):\n')

    if key_validation(key):
        
        print(f'A key {key} é válida.')
    else:
        
        print(f'A key {key} não é válida.')

    print(f'\nA key gerada é: {key_generator()}')


if __name__ == '__main__':
    main()
