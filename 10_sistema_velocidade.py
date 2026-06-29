print('🕰️  Bem-vindo ao Sistema de Velocidade')
print('- Velocidade maxima: 80km/h -')

speed = float(input('Insira sua velocidade em km/h: ')) 

if speed <=80:
    print('Voce esta dentro do limite de velocidade! ✅')
elif speed >80:
    print('Voce esta multado por execer o limite de velocidade! ⚠️') 

print('📤 Final do sistema-')