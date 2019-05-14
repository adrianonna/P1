'''
help(int)#mostra sobre int


nome=input('Qual seu nome?')
print(type(nome))
print('Olá', nome, '! Prazer em te conhecer!')
print('"Isso são duas "' + '"mensagens juntas"')



dianascimento = int(input('Qual o dia do seu nascimento'))
mesnascimento = input('Qual o mes do seu nascimento')
anonascimento = int(input('Qual o ano do seu nascimento'))
print('Você nasceu no dia', dianascimento, 'do mês de', mesnascimento, 'do ano', anonascimento)
print(dianascimento, mesnascimento, anonascimento, sep = '/')


n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
s=n1+n2
n1, n2 = n2, n1#troca os valores das variáveis repectivamente, n1 recebe n2 e n2 recebe n1
print('A soma é: {}'.format(n1+n2))
print('A soma entre', n1, 'e', n2, 'é:', n1+n2)
print('A soma entre {1} e {0} é {2}'.format(n1, n2, s))#posso ordenar com números dentro do {}
print('Isso é o endereço de memória {}'.format(id(n1)))#mostra endereço de memória
print('{}'.format(dir(nome)))#mostra métodos que podem ser usado com nome
#help()


n=input('Digite algo: ')
print(type(n))
print('Convertível?',n.isnumeric())#se o valor for número, verifica se é possível converter o valor str para int


n=input('Digite algo: ')
print(type(n))
print('É letra?',n.isalpha())#verifica se é letra, alfabético


n=input('Digite algo: ')
print(type(n))
print('É número?',n.isalnum())#verifica se é números, alfanumérico


n=input('Digite algo: ')
print('Todas maiúculas?',n.isupper())#verifica se todos estão com letra maiúscula


n=bool(input('Digite algo ou deixe vazio(verdadeiro ou falso): '))
print(n)#se vazio é falso


Ordem de precedência
1º ()
2º **(potencia)
3º *, /, //(divisão inteira), %(resto)
4º +, -
forçar raiz quadrada, cúbica ex. 81**(1/2), 127**(1/3)
a=5+3*2
b=3*5+4**2
a1 = str(a)#converte o valor int de "a" para string em "a1"
print(a,b)
print('Oi '*3)


nome=str(input('Digite seu nome: '))
print('Olá {:20}!'.format(nome))#Adiciona 20 espaços para nome


nome=str(input('Digite seu nome: '))
print('Olá {:>20}!'.format(nome))#Alinhado a direita


nome=str(input('Digite seu nome: '))
print('Olá {:^20}!'.format(nome))#Centralizado


nome=str(input('Digite seu nome: '))
print('Olá {:=^20}!'.format(nome))#preencher espaços com =


n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}, \no produto é {} \ne a divisão é {:.3f}'.format(s,m,d))#mostra apenas três casa decimais float)
print('A divisão inteira é {}'.format(di), end=' ')#junta os dois print em uma linha e adiciona o conteúdo
print('A potência é {}'.format(e))


#math: ceil(aredonda pra cima), floor(arredonda pra baixo), trunc(trunca, corta os decimais),
#pow(potência), sqrt(raiza quadrada), factorial(calculo fatorial)
#import math
#from math import sqrt, ceil


import math
num=float(input('Digite um número: '))
raiz=math.sqrt(num)#importando toda bbl math, precisa referenciar "math."sqrt(num)
print('A raiz de {} é {:.4f}, arrendodada é {}\n'.format(num, raiz, math.ceil(raiz)))#motra duas casa e arredonda pra cima


from math import sqrt, ceil
num1=float(input('Digite um número: '))
raiz=sqrt(num1)#importação expecífica da biblioteca, só basta o sqrt(num)
print('A raiz de {} é: {:.4f}\n'.format(num1, raiz))


import random
num2=random.random()#randon de 0 a 1
print('Núemero random de 0 a 1 é: {}'.format(num2))


num3=random.randint(1,10)#gera numero random de 1 a 10
print('Núemero random inteiro de 1 a 10 é: {}\n'.format(num3))


import emoji
print(emoji.emojize('Olá mundo :smirk: :sunglasses:', use_aliases=True))


from math import trunc
num=float(input('Digite um número real: '))
print('O número truncado é: {}'.format(trunc(num)))


from random import randint
alunos = ['Ana', 'Carlos', 'Pedro', 'Júlia']
e = randint(0, 3) #escolhe random uma posição de memória
print('\nO aluno(a) escolhido foi: {}!\n'.format(alunos[e])) #posição e


from random import choice, shuffle
nome1=input('Digite o 1º nome: ')
nome2=input('Digite o 2º nome: ')
nome3=input('Digite o 3º nome: ')
nome4=input('Digite o 4º nome: ')
lista=[nome1, nome2, nome3, nome4]#cria um array/lista com 4 variáveis
escolhido=choice(lista)#atribui um valor random da "lista" para "escolhido"
print('O aluno escolhi foi {}\n'.format(escolhido))
shuffle(lista)#embaralha a lista
print('A ordem de apresentação dos alunos é: {}'.format(lista))


lista = [1, 2, 3, 4, 5]
listanome = ["Adriano", "Ada", "Caio", "Cyro"]
for item in lista[0:3]:#variável item recebe os valores de 0 a 3 da lista
    print(item, end=' ')#coloca um espaço no final
for itemnome in listanome:
    if not itemnome == 'Ada':#Não mostra o nome Ada se existir na lista
        print(itemnome)
        print(listanome)
for numeros in range(5):#Conta e exibe a variável numero de 0 a 4
    print(numeros)


nome = str(input('Digite seu nome: '))
if nome in 'Maria Ana Paula Fernanda':#verifica se nome existe dentro da string
    print('Seu nome é feminino')


lista2 = ['abcdefghi']
for item2 in lista2 #ou 'abcdefghi'
    print(item2, end=' é uma ')
    if item2 == 'aei'
        print('vogal')
    else:
        print('consoante')


for i in range(2, 101, 2):
    print(i, end=' ')#coloca na mesma linha e adiciona um espaço entre os elementos


frase='Manipulação de string python'
print(frase[:11])#vazio subentende começa no índice 0
print(frase[12:])#começa no índice 12 vai até o final
print(frase[0:11:2])#começa no índice 0 ao 11 pulando de 2 em 2
print(frase[2::2])#começa no índice 2 até o final pulando de 2 em 2
print(len(frase))#comprimento da frase
print(frase.count('a'))#conta quantas letras "a" possui na frase
print(frase.count('i',0,11))#conta quantas letras "i" possui do índice 0 ao 11
print(frase.find('ula')+1)#Verifica se tem "ula" na string e mostra o primeiro índice, mostra -1 se não existir
print(frase.rfind('o')+1)#Verifica a partir do lado direito, +1 para começar igual a 1
print('strin' in frase)#mostra true se existir na frase
var = 'string' in frase #mostra true se existir na frase
print(var)
print(frase.replace('string','índices'))#troca "string" por "índices" na frase e adiciona os espaços necessários
print(frase.upper())#mostra tudo em letras maiúsculas, porém não altera de fato
print(frase.upper().count('A'))#coloca tudo em maiúsculo e conto quantos "A" tem na frase
print(frase.lower())#coloca tudo em minúsculas
print(frase.capitalize())#Coloca a primeira letra da string em maiúsculo, o resto minúsculo.
print(frase.title())#coloca todas as palavras com iniciais maiúsculas
print(frase.strip())#remove os espaços em branco dos lados
print(frase.rstrip())#remove os espaços em branco do lado direito
print(frase.lstrip())#remove os espaços em branco do lado esquerdo
frase = frase.split()#tira os espaços, cria um array pra cada palavra e outro array/lista para todas as palavras juntas
print(frase)
print(frase[0])#mostra o índice 0 dos array/lista de palavra
print(frase[0][3])#mostra o índice 3 dentro do array índice 0
frase = ' '.join(frase)#adiciona espaço entre os array/palavras
print(frase)
frase = len(frase.split())#conta quantos array a frase possui
print(frase)
print('Teste de um \033[7;30mexemplo de cor\033[m!!')#\033[m para colocar e parar cores
numeros = [2, 4, 5, 3, 6, 1]
print(numeros)
numeros.reverse()#coloca em ordem decrescente
print(numeros)
numeros.sort()#coloca em ordem crescente
print(numeros)
numeros.append(7)#acrescenta um numero
print(numeros)
numeros.remove(7)#remove o primeiro(se houver mais de um) valor 7 no caso
print(numeros)
del(numeros[0])#deleta a posição 0 da lista de numeros
print(numeros)
print(numeros, end='')


from datetime import datetime
now = datetime.now()
print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)


print(0.1 + 0.1 + 0.1 - 0.3)#bug
print('{}'.format(2 == 2))#retorna o valor true ou falso


cadastroCliente = ['pedra', 'papel', 'tesoura']
index = 0
for index in  range (len(cadastroCliente)):#index vai percorrer a quantidade de índices, no até caso 2
    print('{}'.format(cadastroCliente[index]))#cada índice é uma string
numero = cadastroCliente.index('pedra')#busca a string pedra na lista
print('{}'.format(numero))#mostra a posição de pedra
cadastroCliente.remove('tesoura')#deleta o nome tesoura da lista
print(cadastroCliente)
cadastroCliente.append('tesoura')
print(cadastroCliente)
del cadastroCliente[:2]#deleta as posições 0 a 1
print(cadastroCliente)



lista = []
for i in range(5):
    nome = str(input('Digite seu nome: '))
    lista.append(nome)#adiciona o valor da variável nome dentro da lista
    print(lista)
print('O primeiro índice/nome possue {} caracters'.format(len(lista[0])))



tam = int(input('Digite o tamanho da lista: '))
lista = [0]*tam
listainve = [0]*tam
impar = []
contimpar = 0
for i in range(tam):
    lista[i] = int(input('Digite o {} valor: '.format(i+1)))
    if lista[i] % 2 == 1:
        contimpar+=1
        impar.append(lista[i])
#aux = tam - 1
#for i in range(tam):
#    listainve[aux] = lista[i]
#    aux-=1
for i in range(tam)
    listainve[tam-1-i] = lista[i]
print('A lista invertida é {}'.format(listainve))
print('A lista é {}'.format(lista))
print('Tem {} números impares'.format(contimpar))
print('Os números impares são {}'.format(impar))



import time
for i in range(5):
        print(i)
        time.sleep(1)



import time
lista = list(range(5, 10000, 5))
num = int(input("Informe um valor: "))
qtde1 = 0
qtde2 = 0
qtde3 = 0
inicio = 0
fim = len(lista) - 1
repeticoes = 10000
# Busca sequencial simples
antes = time.time()
for i in range(repeticoes):
    for j in range(len(lista)):
        qtde1 += 1
        if (num == lista[j]):
            break
depois = time.time()
print("Tempo 1: ", (depois - antes))
if (j < len(lista) - 1):
    print("achei!!")
elif (lista[j] == num):
    print("achei")
else:
    print("nao achei")
print("Quantidade = ", qtde1)



# Busca sequencial - ordenada
antes = time.time()
for i in range(repeticoes):
    for j in range(len(lista)):
        qtde2 += 1
        if (num <= lista[j]):
            break
depois = time.time()
print("Tempo 2: ", (depois - antes))
if (num != lista[j]):
    print("nao achei")
else:
    print("achei")



#Busca binaria
lista = list(range(5, 10000, 5))
inicio = 0
fim = len(lista) - 1
repeticoes = 10000
num = int(input("Informe um valor: "))
antes = time.time()
for i in range(repeticoes):
    meio = int((fim + inicio)/2)
    while ((fim > inicio) and (lista[meio] != num)):
        qtde3 += 1
        if (lista[meio] < num):
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = int((fim + inicio)/2)
depois = time.time()
print("Tempo 3: ", (depois - antes))
if (lista[meio] == num):
    print("achei")
else:
    print("nao achei")


# analisando as três soluções
print(num)
print(qtde1)
print(qtde2)
print(qtde3)


#Algoritmo da bolha
l = [10, 20, 30, 90, 40, 80, 70]
tam_l = len(l)
cont = 0
for i in range(tam_l)
    cont += 1
    troca = False
    for j in range(1, tam_l - i)
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            troca = True
    if not troca:
        break
print(l)




n = list(range(10))
tam_n = len(n)
for i in range(tam_n):
    n[i] = int(input('Digite um número: '))
print(n)
for i in range(tam_n - 1):
    for j in range(i + 1, tam_n):
        if n[i] == n[j]:
            print('Os números {} e {} são iguais'.format(n[i], n[j]))



matriz = []
for i in range(3):
    linha = [0]*3
    for j in range(3):
        linha[i] = int(input('Digite um número: '))
    matriz.append(linha)
for i in range(len(matriz)):
    cont1 = 0
    for j in range(len(matriz)):
        if matriz[i][j] == 1:
            cont1 += 1
    if cont1 > 1:
        print('Não matriz de permitação')
    else:
        print('É matriz de permutação')
for i in range(len(matriz)):
    cont2 = 0
    for j in range(len(matriz)):
        if matriz[j][i] == 1:
            cont2 += 1
    if cont2 > 1:
        print('Não matriz de permitação')
    else:
        print('É matriz de permutação')



# altera valor da variável local na função para global
nome = "Adriano"
def test (var1):
  global nome
  nome = var1
  print(nome)
test("outro")
print(nome) #vai printar outro



#
def test2(a, b, *args, **kwargs):
  print(a, b, args, kwargs)

test2(1,2)
test2(a=30, b=40)
test2(1,2, 3, 4, 5, (6))




#Passa qualquer tipo de elemento
def test3(*elements):
  print(elements)
  return elements

test3(1,2,3,4,5)
test3([1,2,3,4])
test3(1)
test3(*[1,2])



#Cria dicionário com chave e valor
def test4(**elements):
    print(elements)
    return elements

test4(a=1, b=2, c=3, d=4)#
test4(var=[1,2,3,4])#chave var, valor lista
test4(var2=1)
test4(**{'x':1})





'''

#
# class Aluno():
#     def __int__(self, nome, matricula, sexo, idade):
#         self.nome = nome
#         self.matricula = matricula
#         self.sexo = sexo
#         self.idade = idade
#
#
#     def VerificaSerie(self, matricula):
#         if self.idade <= 5:
#             print("Maternal")
#         elif self.idade <= 10:
#             print("Ensino fundamental")
#         elif self.idade <= 17:
#             print("Ensino medio")
#         elif self.idade > 17:
#             print("Ensino superior")
#
# a = Aluno("Adriano", 20162, "M", 28)
# b = Aluno("Pedro", 20183, "M", 10)
# c = Aluno("Paulo", 20172, "M", 16)






class Pessoa(object):
    def __init__(self, nome, ano_nascimento):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento

    def idade(self, ano):
        return ano - self.__ano_nascimento

    def getNome(self):
        return self.__nome

    def __str__(self):
        return "Nome: {}\nAno de nascimento: {}".format(self.__nome, self.__ano_nascimento)



class Aluno(Pessoa):
    def __init__(self, matricula, escolaridade, ano_nascimento, nome):
        super(Aluno, self).__init__(nome, ano_nascimento)
        self.__matricula = matricula
        self.__escolaridade = escolaridade
        self.__ano_nascimento = ano_nascimento

    def get_matricula(self):
        return self.__matricula

    def __str__(self):
        return "Matricula: {}\nEscolaridade: {}\nAno de nascimento: {}".format(self.__matricula, self.__escolaridade, self.__ano_nascimento)

b = Pessoa("Pedro", 1990)
a = Aluno(1234, "Medio completo", 1990, "Pedro")
print(a.idade(2016))
print(b)
