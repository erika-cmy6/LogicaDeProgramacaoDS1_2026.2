"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota_um = float(input("digite sua nota um"))
nota_dois = float(input("digite sua nota dois"))
nota_tres = float(input("digite sua nota tres"))
valor_um = nota_um = 10.0
valor_dois = nota_dois = 8.0
valor_tres = nota_tres = 9.0
media=(nota_um+nota_dois+nota_tres) /3
print(f"media final={media}")