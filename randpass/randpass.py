#   Randpass (v1.0)

import random
import string
# etapas de criação
# a ideia principal é criar um criador de senha aleátorias para se usar como um comando bash, irei fazer o prototipo em python para depois converte-lo em sh

#Idealização
# 1. Criar uma lista para senhas criadas 
# 2. Criação de comandos para deixar o programa mais interativo para quem é acostumado com atalhos
# 3. Terá duas caixas interativas. Uma perguntando em até quantos caracteres será a senha e a segunda, é para caso o usuário tenha alguma senha em mente e apenas queira modifica-lá ou criptografar a senha


def gerador_alfanumerico(tamanho=10, caracteres=string.ascii_letters + string.digits + string.printable):
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def gerador_alfanumerico_pass(modpass, tamanho=10, caracteres=string.ascii_letters + string.digits + string.printable):
    return modpass.join(random.choice(caracteres) for _ in range(tamanho))

listpass = []

print('-'*50)
print('|', ' '*46, '|')
print('|', ' '*11, 'Randpass (v1.0 - 8/7/24)', ' '*9, '|')
print('|', ' '*46, '|')
print('-'*50)
print('')

print(' '*11, 'O que você deseja fazer?')
print('')
print('-'*50)
print(' ')
print('1. Criar Nova senha')
print('2. Modificar uma Senha já criada')
print('0. Sair')
print('')
print('-'*50)

opt = int(input('Qual Opção você escolhe?: '))
print('-'*50)
if opt == 1:
    while True:
        qtdpass = int(input('Quantos caracteres serão usados?: '))

        pasw = str(gerador_alfanumerico(qtdpass))
        print(pasw)
        print('')

        conf = str(input('Você gostaria de criar Outra Senha? [Y/N]: ')).upper().strip()[0]
        if conf == 'N':
            break
        elif conf != 'Y' and 'N':
            res = ''
            while conf != 'Y' and 'N':
                print('[Erro] Tente novamente')
                conf = str(input('Você gostaria de criar Outra Senha? [Y/N]: ')).upper().strip()[0]
                print('')
                if conf == 'N':
                    res += conf
                    break
            if res == 'N':
                break
            
        
    save = str(input('Você deseja Salvar a Senha? [Y/N]: ')).upper().strip()[0]
    if save == 'Y':
        listpass.append(pasw)
        print(f'Sua Senha: ', listpass[0])
    print('-'*50)
# parei aqui


elif opt == 2:
    modpass = str(input('Digite a Sequûencia que você queira modificar: '))
    print(gerador_alfanumerico_pass(modpass, len(modpass)))

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