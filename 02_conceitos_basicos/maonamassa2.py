TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string
valor_conta = float(input("o valor da conta e"))
numero_pessoas = int(input("qual numero de pessoas?"))
valor_pessoa = valor_conta/numero_pessoas
print(f"o valor total para cada pessoa e{valor_pessoa: .2f}") 
