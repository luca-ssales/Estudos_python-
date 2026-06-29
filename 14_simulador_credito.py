print('--- 💳 Simulador de aprovação de credito ---')

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
salario = float(input('Qual seu salário? '))

print('1-Sim')
print('2-Não')
estatus = input('Voce possue nome sem restrição? ')

if idade >=18 and estatus == '1':
    aprovacao = salario * 10
    limite = aprovacao
    print('Parabéns, seu limite é de:',limite)
    
else:
    print('Infelizmente seu cartão de credito não está disponivel no momento')

print('------------------------------------------')
    