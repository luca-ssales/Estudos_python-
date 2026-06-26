#Pergunte a idade, menor que 18 anos, informe que não pode tirar a CNH, 
# maior ou igual a 18 anos, informe que já pode tirar a CNH.

print('Verificador de CNH🚘')
nome = input('👀 Qual é seu nome? ')
idade = float(input('🤐 Qual sua idade? '))

if idade >=18:
    print(nome,', voce já pode tirar sua CNH!😀')

else:
    print(nome,', poxa que pena! voce ainda na pode tirar sua CNH 😓')           

