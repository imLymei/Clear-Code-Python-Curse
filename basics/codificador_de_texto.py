import random

def codification(key,letters,text):
    letters_length = len(letters)
    new_text = list(text)
    new_text_length = len(new_text)
    final_text = ''

    for letter_index in range(0,new_text_length):
        found = False
        alphabet_index = 0

        while found == False and alphabet_index < letters_length:
            if letters[alphabet_index] == new_text[letter_index]:
                final_text += letters[(alphabet_index+key)%letters_length]
                found = True
            alphabet_index += 1
        
        if found == False:
            final_text += new_text[letter_index]

    return final_text

def decoding(key,letters,text):
    letters_length = len(letters)
    new_text = list(text)
    new_text_length = len(new_text)
    final_text = ''

    for letter_index in range(0,new_text_length):
        found = False
        alphabet_index = 0

        while found == False and alphabet_index < letters_length:
            if letters[alphabet_index] == new_text[letter_index]:
                final_text += letters[(alphabet_index-key)%letters_length]
                found = True
            alphabet_index += 1
        
        if found == False:
            final_text += new_text[letter_index]

    return final_text

def code_main(letters):
    text = input('\nDigite uma frase: ')

    key = random.randrange(10000)

    print(f'O código de decodificação é {key}')

    coded = codification(key, letters, text)

    print(f'\nSua mensagem codificada é [{coded}]\n')

def decode_main(letters):
    text = input('\nDigite uma frase: ')

    key = int(input('Digite o código de decodificação: '))

    decoded = decoding(key, letters, text)

    print(f'\nSua mensagem decodificada é [{decoded}]\n')

def menu():
    response = 0

    while response != '1' and response != '2' and response != '3':
        print('Pressione 1(um) para codificar.')
        print('Pressione 2(dois) para decodificar.')
        print('Pressione 3(três) para sair.\n')
        response = input()

    return response

def main():

    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ','!','?','@','*','%','&','/','.',',','<','>',')','(',']','[','~','^','`',]

    response = 0
    while response != '3':
        response = menu()
        if response == '1':
            code_main(letters)
        elif response == '2':
            decode_main(letters)

if __name__ == '__main__':
    main()