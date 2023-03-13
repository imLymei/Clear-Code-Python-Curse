# Programa para verificar se um número é primo e descobrir o próximo e o anterior dele

def is_prime(number):  # Função para verificar se um número é primo 
    '''Verifica se um número é primo''' 
    prime = True
    divider = 2

    if number <= 1:  # Verifica se o número é menor ou igual a 1
        
        return False
    else:
        
        while prime == True and divider <= number/2:  # Verifica se o número é divisível por algum número menor ou igual a metade dele
            
            if number%divider == 0:
                
                prime = False
            else:
                
                divider += 1

        return prime


def next_prime(number, tick):  # Função para descobrir o próximo número primo 
    '''Encontra o proximo número primo'''
    if not is_prime(number+tick):  # Verifica se o número é primo
        
        return next_prime(number, tick+1)
    else:
        
        return number+tick


def previous_prime(number, tick):  # Função para descobri o número primo anterior 
    '''Encontra o número primo anterior'''
    if not is_prime(number-tick):
        
        return previous_prime(number, tick+1)
    else:
        
        return number-tick


def main():  # Rotina principal 
    my_number = int(input('Digite um número:\n'))

    if is_prime(my_number):
        
        print(f'{my_number} é um número primo.\n')
    else:
        
        print(f'{my_number} não é um número primo.\n')

    if my_number > 1:
        
        previous_number = previous_prime(my_number, 1)
        print(f'O primo anterior é: {previous_number}({previous_number-my_number}).')

    next_number = next_prime(my_number, 1)
    print(f'O proximo primo é : {next_number}(+{next_number-my_number}).')


if __name__ == '__main__':  # Prevenir ser executado com import 
    
    main()
