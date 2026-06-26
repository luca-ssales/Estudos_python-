print('--- 👟 Loja de Calçados ---')
compra = float(input('Qual o valor da compra? '))

if compra > 200.0:
    desconto = compra * 0.20
    total = compra - desconto
    print('😯 Voce ganhou 20% de desconto:',total)

elif compra > 100.0:
    desconto = compra * 0.10
    total = compra - desconto
    print('😯 Voce ganhou 10% de desconto:',total)

else: 
    print('😓 Não há desconto para compras abaixo de R$100,00')

print('--- Obrigado pela compra! ---')