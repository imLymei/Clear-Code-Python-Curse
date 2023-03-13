import random
import string


def password_generator(min_length: int, number=True, special=True) -> str:
    '''Gera uma senha com um tamanho minimo, e a presença de números e caracteres especiais caso nescessário'''
    letters = string.ascii_letters  # Pega as letras do alfabeto
    numbers = string.digits  # Pega todos os números
    specials = string.punctuation  # Pega os caracteres especiais

    all_letters = letters

    if number:  # Verifica se a senha precisa de números
        all_letters += numbers

    if special:  # Verifica se a senha precisa de caracteres especiais
        all_letters += specials

    has_number = False
    has_special = False
    is_valid = False

    password = ''

    while not is_valid or len(password) < min_length:  # Adiciona uma letra, numero ou caractere aleatorio até a senha ser do tamanho ideal e ser válida
        new_letter = str(random.choice(all_letters))
        password += new_letter

        if new_letter.isnumeric():
            has_number = True

        if not new_letter.isalnum():
            has_special = True

        if number:
            if has_number:
                is_valid = True

        if special:
            if has_special:
                is_valid = is_valid and has_special

    return password


def main():
    password_length = int(input('Digite o tamanho mínimo para a senha:\n'))
    has_number = bool(input('\nA senha precisa de números?\n1(sim) / 0(não)\n'))
    has_special = bool(input('\nA senha precisa de caracteres especiais?\n1(sim) / 0(não)\n'))
    print(f'Sua senha é: {password_generator(password_length, has_number, has_special)}')


if __name__ == '__main__':
    main()
