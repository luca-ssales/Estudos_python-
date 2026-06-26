#Obejtivo: Peça o saldo da conta e o valor do pix, se tiver saldo suficiente, 
#faça o pix, se não, informe que não tem saldo suficiente.

print('----💸 Simulador de Pix ----')
saldo = float(input('Digite o saldo da conta: '))
valor_pix = float(input('Digite o valor do pix: '))
print()

conta = saldo - valor_pix

if conta >= 0:
    print('Pix realizado com sucesso✅')
    print('Saldo atual da conta:R$',conta)

else:
    print('Saldo insuficiente❌')
    print('Saldo atual da conta:R$',saldo)

print('----------------------------')