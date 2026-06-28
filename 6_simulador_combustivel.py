print('---⛽ Simulador de Combustivél 🚘 ---')

litros = float(input('Quantos litros possue seu veiculo? '))
viagem = float(input('Quantos km deseja viajar? '))

autonomia = litros * 10

if autonomia >= viagem:
    print('😊 Voce consegue viajar tranquilamente!')
else:
    print('😓 Infelizmente, voce não consegue viajar!')

print('-- Obrigado por utilizar o simulador! --')
