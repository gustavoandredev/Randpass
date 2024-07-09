#   Gerador de Senhas(v1.0)

import random
import string
# etapas de criação
# a ideia principal é criar um criador de senha aleátorias para se usar como um comando bash, irei fazer o prototipo em python para depois converte-lo em sh

#Idealização
# 1. Criar uma lista para senhas criadas 
# 2. Criação de comandos para deixar o programa mais interativo para quem é acostumado com atalhos
# 3. Terá duas caixas interativas. Uma perguntando em até quantos caracteres será a senha a segunda, é para caso o usuário tenha alguma senha em mente e apenas queira 'criptogafa-lá'

def gerador_alfanumerico(tamanho=10, caracteres=string.ascii_letters + string.digits):
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# print(gerador_alfanumerico())

print('-'*50)
print('|', ' '*46, '|')
print('|', ' '*15, 'Randpass (v1.0 - 8/7/24)', ' '*14, '|')
print('|', ' '*46, '|')
print('-'*50)


print(' '*16, 'O que você deseja?')
print('-'*50)
print(' ')
print('1. Criar Nova senha')
print('2. Modificar uma Senha já criada')
print('')
print('-'*50)

opt = int(input('Qual Opção você escolhe?: '))
print('-'*50)
if opt == 1:
    while True:
        qtdpass = int(input('Quantos caracteres serão usados?: '))
        print(gerador_alfanumerico(qtdpass))

        conf = str(input('Você gostaria de criar Outra Senha? [Y/N]: ')).upper().strip()[0]
        if conf == 'N':
            break
        elif conf != 'Y' and 'N':
            print('[Erro] Tente novamente')
elif opt == 2:
    modpass = str(input('Digite a Sequûencia que você queira modificar: '))
    print(gerador_alfanumerico(modpass.lenght(), modpass))

print('-'*15,'fim de execução', '-'*15)
print('')
print('Criado por Gustavo André ')
#print(qtdpass)

#Depois, terá opções para usos dos caracteres

#Alfabético
#Numerico
#AlfaNumerico
#Alfanumerico com Caracteres especiais
#Caracteres Especiais

# Comentários

# Criar um script para diferentes Linguagens. Ex: Html/Css(site)
#mudei de ideia sobre uma coisa, vou criar um encriptador. no final. essa é a real função