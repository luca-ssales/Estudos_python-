print('-Sistema de E-commerce-')

valor = float(input('Insira o valor da compra: '))

print('-Formas de pagamento-')
print('1- Pix')
print('2- Cartão de Debito')
print('3- Cartão de Credito')

pag = input('Qual forma de pagamento? ')

if pag == '1':
    desconto = valor * 0.10
    final = valor - desconto
    print('Voce tem desconto de 10%, no valor de:', desconto)
    print('--------------------------------------------')
    print('Valor a ser pago:', final)
    
elif pag == '2':
    desconto = valor * 0.05
    final = valor - desconto
    print('Voce tem desconto de 5%, no valor de:', desconto)
    print('--------------------------------------------')
    print('Valor a ser pago:', final)

else:
    print('No credito não há desconto!')
    
print('Final do sistema ---------------------------')



