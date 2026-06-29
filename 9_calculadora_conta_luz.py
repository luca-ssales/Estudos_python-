print('-Calculadora de conta de luz-')

consumo = float(input('Digite o consumo em kWh: '))

if consumo <= 100:
    valor = consumo * 0.50
    print('O valor da sua conta de luz é:', round(valor, 2))
elif consumo <= 300:
    valor = consumo * 0.70
    print('O valor da sua conta de luz é:', round(valor, 2) )
else:
    valor = consumo * 1.00
    print('O valor da sua conta de luz é:', round(valor, 2))

print('Obrigado por utilizar a calculadora de conta de luz!')
          