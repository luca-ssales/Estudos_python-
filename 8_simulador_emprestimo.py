print('--- 💸 Simulador de emprestimo 🏦 ---')

salario = float(input('Digite o seu salário: '))
valor_emprestimo = float(input('Digite o valor do emprestimo solicitado: '))

if valor_emprestimo > salario * 10:
    print('Empréstimo reprovado ❌')
else:
    print('Empréstimo aprovado ✅')
