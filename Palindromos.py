def eh_palindromo(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace(" ", "")
    return palavra == palavra[::-1]


palavra_usuario = input("Digite uma palavra para verificar se é um palíndromo: ")


resultado = eh_palindromo(palavra_usuario)

if resultado:
    print(f'True')
else:
    print(f'False')