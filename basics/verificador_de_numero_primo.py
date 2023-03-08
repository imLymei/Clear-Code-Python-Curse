
#? Função para verificar se um numero é primo  ?#
def is_prime(number):
    prime = True
    divider = 2

    if number <= 1:
        return False
    else:
        while prime == True and divider <= number/2:
            if number%divider == 0:
                prime = False
            else:
                divider += 1

        return prime

#? Função para descobrir o próximo numero primo ?#
def next_prime(number, tick):
    if is_prime(number+tick) == False:
        return next_prime(number, tick+1)
    else:
        return number+tick

#? Função para descobri o numero primo anterior ?#
def previous_prime(number, tick):
    if is_prime(number-tick) == False:
        return previous_prime(number, tick+1)
    else:
        return number-tick

#? Rotina principal ?#
def main():
    my_number = int(input('Digite um número: '))
    print('')

    if is_prime(my_number):
        print(f'{my_number} é um número primo.')
    else:
        print(f'{my_number} não é um número primo.')

    previous_number = previous_prime(my_number, 1)
    next_number = next_prime(my_number, 1)

    print(f'O primo anterior é: {previous_number}({previous_number-my_number}).')
    print(f'O proximo primo é : {next_number}(+{next_number-my_number}).')

#? Prevenir ser executado com import ?#
if __name__ == '__main__':
    main()
