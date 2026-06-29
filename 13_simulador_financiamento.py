print('--- 🚘 Simulador de Financiamento de veiculo 🚧 ---')

salario = float(input('Insira o valor do seu salario: '))
carro = float(input('Insira o valor do carro: '))
entrada = float(input('Insira o valor de entrada: '))
parcelas = float(input('Quantidades de parcelas: '))

financiado = carro - entrada

parcela = financiado / parcelas

limite = salario * 0.30

if parcela <= limite:
    print('Parabéns! financiamento aprovado.')
    valor = carro / parcelas
    print('O valor da sua parcela ficou:',valor)
    print('1-Sim')
    print('2-Não')
    resul = input('Fica bom para voce? ')
    
    if resul == '1':
        print('Financiamento em processo...')
    
    elif resul == '2':
        print('Poxa que pena! Vamos tentar outro modelo?')
    
else:
    print('Infelizmente, seu financiamento foi negado!')
    
print('------------------------------------------')
