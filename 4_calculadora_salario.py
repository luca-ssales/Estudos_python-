print('--- ➕ Calculadora de Hora Extra ➖ ---')   

salario = int(input('💵 Qual seu salario: '))
horas = int(input('⏰ Quantas horas trabalhadas: '))
valor = int(input('💰 Valor da hora: '))

print('-----------------------------')

preco = horas * valor
completo = preco + salario

print('💵 Seu salario bruto:', salario)
print('⏰ Horas extras(h):',preco)
print('💰 Salario completo:', completo)

print('-----------------------------')