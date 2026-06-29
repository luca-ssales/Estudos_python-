print('--- 🪪  Validador de Login ---')

login = input('👤 Login: ')
senha = input('🔐 Senha: ')

if login == 'admin' and senha == '123':
    print('Bem vindo, Admin')
else:
    print('Login e senha incorretos')