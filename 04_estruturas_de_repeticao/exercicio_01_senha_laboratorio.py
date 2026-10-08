"""
EXERCÍCIO 01: Senha Fixa do Laboratório
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Repita a leitura da senha até que o usuário digite a senha correta (2002).
Para cada tentativa incorreta, imprima "Senha Invalida".
Ao acertar, imprima "Acesso Permitido" e finalize o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:

senha = 0

while senha != 2002:
    senha = int(input("Digite a senha: "))

    if senha != 2002:
        print("Senha Invalida")

print("Acesso Permitido")
         