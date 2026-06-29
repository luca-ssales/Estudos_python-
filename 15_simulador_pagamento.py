print('Simulador de folha de Pagamento')

nome = input('Qual seu nome? ')
cargo = input('Qual seu cargo? ')
salario = float(input('Qual seu salario? '))

if salario <= 2000:
    inss = salario * 0.80
    liquido = salario - inss
    print(liquido)

# elif salario <=2000 and <=5000:
#     desconto = salario - 0.10
#     print(desconto)
#     
# elif salario >5000:
#     print(desconto)
#     