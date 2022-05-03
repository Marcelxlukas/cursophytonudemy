nome = (input('Qual o seu nome?'))
idade = 18
peso = 58.0
alt = 1.70
imc = (peso / (alt**2))
anoatual = 2022
nascimento = (anoatual - idade)

print (f'{nome} tem {alt} de altura e pesa {peso}kg, e tem {idade} anos')
print(f'{nome},o seu imc é: {imc:.2f}')
print(f'{nome} você nasceu em:{nascimento}')