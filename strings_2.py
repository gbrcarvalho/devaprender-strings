''' 
Aula do DevAprender Mini Curso de Strings
https://www.youtube.com/watch?v=kvHe2Yp-FTI&list=PLnNURxKyyLIKX73U7hISjIY7T5KiNNLu_&index=8
Aula do DevAprender Curso de Git e Github
https://www.youtube.com/watch?v=kB5e-gTAl_s
'''
print('Manipulação de Strings!')

# Caracteres de Escape
nome = "Gabriel"
diretorio = "C:\\Users\\User1\\Envs\\"
texto = "1. Olá!\n2. Bom dia!"

print('Nome: ' + nome)
print('Pasta: ' + diretorio)
print('Texto:\n' + texto)

# Formatando Strings
mensagem = f' Olá {nome}, seja bem vindo! Você tem {5 + 15} dias para completar o curso! '

print('mensagem: ' + mensagem)

# Metodos comuns
print('mensagem(maiuscula): ' + mensagem.upper())
print('mensagem(minuscula): ' + mensagem.lower())
print('mensagem(sem espaco esq): ' + mensagem.lstrip())
print('mensagem(sem espaco dir): ' + mensagem.rstrip())
print('mensagem(sem espaco): ' + mensagem.strip())
print('mensagem(indice(vindo)): ', mensagem.find('vindo'))
print('mensagem(troca(ola, oi)): ', mensagem.replace('Olá', 'Oi'))

# Acessando partes de uma string

palavra = 'Mouse'

print('primeira letra:', palavra[0])
print('ultima letra:', palavra[-1])
print('indice de u:', palavra.index('u'))

# Separando partes de uma string

link = 'https://github.com/gbrcarvalho/devaprender-strings/tree/master'

print(link[0:5])
print(link[56:])
print(link[-6:])
