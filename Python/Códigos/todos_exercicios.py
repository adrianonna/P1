'''
n1 = float(input('Digite a 1ª nota de 0 a 10: '))
n2 = float(input('Digite a 2ª nota de 0 a 10: '))
n3 = float(input('Digite a 3ª nota de 0 a 10: '))
m = (n1 + n2 + n3)/3
print('Sua média foi {:.1f}'.format(m))
if m >= 7 and m <= 10:
    print('Aprovado')
else:
    if m >= 4 and m <= 6:
        print('Recuperação')
        r = float(input('Digite sua nota da recuperação: '))
        f = (r + m) / 2
        if f >= 5:
            print('Aprovado')
        else:
            print('Reprovado')
    if m <= 3:
        print('Reprovado')


import random#questão 28
n = random.randint(0,5)
u = 7
#u = int(input('Digite um número de 0 a 5: '))
#if u == n:
#    print('Parabéns você adivinhou.')
#else:
#    print('O número é {}'.format(n))
#    print('Tente novamente.')
while u != n:
    n = random.randint(0, 5)
    u = int(input('Digite um número de 0 a 5: '))
    if u == n:
        print('Parabéns você adivinhou.')
    else:
        print('O número é {}'.format(n))
        print('Tente novamente.')


v = int(input('Qual a velocidade do carro?'))#questão 29
if v > 80:
    k = v-80
    t = k*7
    print('Você foi multado em {} reais'.format(t))
else:
    print('Você está dentro da velocidade permitida')


n = int(input('Digite um número: '))#questão 30
r = (n % 2)
if r == 0:
    print('É par')
else:
    print('É impar')


d = float(input('Digite a distancia em km: '))#questão 31
if d <= 200:
    preco = d*0.5
    print('O valor do percurso é {:.2f}'.format(preco))
else:
    preco = d*0.45
    print('O valor do percurso é {:.2f}'.format(preco))
#preco = d*0.5 if d <= 200 else d2*0.45
#print('O valor do percurso é {:.2f}'.format(preco))


from datetime import date#ano bissexto
a = int(input('Digite qualquer ano ou 0 para ano atual: '))
if a == 0:
    a = date.today().year#pega o ano atual da máquina
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é Bissexto'.format(a))
else:
    print('O ano {} não é Bissexto'.format(a))


n1 = int(input('Digite o 1º número: '))#questão 33
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if n1 > n2 and n1 > n3:
    print('{} é maior'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é maior'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é maior'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é menor'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é menor'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é menor'.format(n3))
if n1 == n2 and n1 > n3:
    print('Os números {} {} são iguais e maiores que {}'.format(n1, n2, n3))
if n1 == n3 and n1 > n2:
    print('Os números {} {} são iguais e maiores que {}'.format(n1, n3, n2))
if n2 == n3 and n2 > n1:
    print('OS números {} {} são iguais e maiores que {}'.format(n2, n3, n1))
if n1 == n2 and n2 == n3:
    print('Os números são iguais')


s = float(input('Digite seu salário: '))#questão 34
if s > 1250:
    t = (s*10)/100
    t1 = s+t
    print('Seu novo salário é {:.2f}'.format(t1))
else:
    t = (s*15)/100
    t1 = s+t
    print('Seu novo salário é {:.2f}'.format(t1))


1009 URI
nome = str(input('Digite seu nome: '))
sal = float(input('Digite seu salário: '))
tven = float(input('Digite o total de vendas em reais do mês atual: '))
aumento = (tven * 15) / 100
tsal = aumento + sal
print('Seu salário vai ser de {:.2f} reais'.format(tsal))


1010 URI
cod1 = int(input('1 Cod da peça: '))
qtd1 = int(input('1 Quantidade de peças: '))
val1 = float(input('1 Valor da peça: '))
cod2 = int(input('2 Cod da peça: '))
qtd2 = int(input('2 Quantidade de peças: '))
val2 = float(input('2 Valor da peça: '))
if qtd1 > 1:
    val1 = qtd1 * val1
if qtd2 > 1:
    val2 = qtd2 * val2
val3 = val1 + val2
print('1 peça cod {} quantidade {} valor {:.2f}'.format(cod1, qtd1, val1))
print('2 peça cod {} quantidade {} valor {:.2f}'.format(cod2, qtd2, val2))
print('O total e de {:.2f}'.format(val3))


1013 URI
n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))
maior = n1
if n2 > maior and n2 > n3:
    print('{} eh o maior'.format(n2))
if n3 > maior and n3 > n2:
    print('{} eh o maior'.format(n3))
else:
    print('{} eh maior'.format(maior))


1014 URI
x = int(input(''))
y = float(input(''))
total = x / y
print('{:.3f} km/l'.format(total))


1015 URI
x1 = float(input(''))
y1 = float(input(''))
x2 = float(input(''))
y2 = float(input(''))
dist = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)
print('{:.4f}'.format(dist))


1016 URI
dist = int(input(''))
if dist > 0:
    tdis = dist * 2
print('{} minutos'.format(tdis))


1017 URI
t = int(input(''))
v = int(input(''))
km = v*t
l = km/12
print('{:.3f}'.format(l))


#transformar reais em dolares
din=float(input('Quantos reais você tem na carteira?'))
dol=3.27
res=din/dol
print('Você possue {:.2f} dolares'.format(res))


#Valor com % de desconto
val=float(input('Digite o valor do produto: '))
val1=val-((val*5)/100)
print('O desconto de 5% é de: {}'.format((val*5)/100))
print('O novo valor é de: {}'.format(val1))


#salario com % de aumento
sal=float(input('Digite seu salário: '))
sal1=sal+((sal*15)/100)
print('O salário com 15% de aumento é: {}'.format(sal1))


#Valor do metro em centímetros e milímitros
met=float(input('Digite um valor em metro: '))
print('{} metros tem {} centímetros e {} milímetros'.format(met, met*100, met*1000))


#retornar True se tiver o nome "silva", adicionar cada palavra em lista e verifica quantas palavras tem o nome,
#verifica o primeiro e último nome e a quantidade de letras no nome completo
nome=str(input('Digite seu nome completo: ')).upper()
print(nome)
print(nome.lower())
print('SILVA' in nome)
nome1 = nome.title().split()
print(nome1)
print('Possui {} índices'.format(len(nome1)))
print('o primeiro nome é {} e tem {} letras'.format(nome1[0], len(nome1[0])))
print('O ultimo nome é {}'.format(nome1[len(nome1)-1]))#mostra último índice de nome1(len diz total possições) -1
nome1 = ''.join(nome1)
print('o nome completo junto {} tem {} letras'.format(nome1, len(nome1)))


#Mostra os milhares, centenas, dezenas e unidades do número digitado
num=int(input('Digite um número de 0 a 9999: '))
print('O número digitado é {}'.format(num))
print('{}'.format(num//10))#Divide por 10 e mostra apenas os inteiro
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade é {}'.format(u))
print('Dezena é {}'.format(d))
print('Centena é {}'.format(c))
print('Milhar é {}'.format(m))


#Verifica se existe a palavra santo na primeira palavra
cid=input('Digite sua cidade: ')
cid = cid.upper().split()
#print(cid)
#print(cid[0])
cid1 = 'SANTO' in cid[0]
print(cid1)


#verifica quantos A aparecem na frase, verifica a primeira e última posição da letra A
frase=str(input('Digite uma frase: ')).upper()#coloca todas em maiúsculo para verificar
print('A letra A aparecem {} vezes'.format(frase.count('A')))
print('A primeira possição da letra A é {}'.format(frase.find('A')+1))
print('A ultima possição da letra A é {}'.format(frase.rfind('A')+1))


#mostra quanto tempo para pagar a casa
#prestação não pode passar de 30% do salário, dizer se pode pagar e qual o valor das parcelas
vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
tempo = int(input('Em quantos anos você quer pagar? '))
tempo *= 12 #multiplica por 12(quantidade de meses no ano) para saber quantos meses no total
mensalidade = vcasa / tempo #valor de cada mensalidade
sal = (salario*30) / 100 #sal recebe 30% do salário
print('30% do seu salário é {}'.format(sal))
if mensalidade > sal:
    print('A mensalidade {} é maior que 30% do salário! Você não pode comprar a casa!'.format(mensalidade))
else:
    print('A mensalidade vai ser de {}, você vai pagar em {} meses.'.format(mensalidade, tempo))


#converter o n para binário, octal ou hexadecimal
n = int(input('Digite um número '))
n2 = int(input('Digite a opção 1 para binário, 2 para octal e 3 para hexa '))
if n2 == 1:
    print(bin(n))
elif n2 == 2:
    print(oct(n))
elif n2 == 3:
    print(hex(n))
else:
    print('Opção inválida!')


#jogo pedra, papel e tesoura
from random import randint, choice
mao = str(input('Escolha e escreva: pedra, papel ou tesoura: '))
#pedra = 'pedra'
#tesoura = 'tesoura'
#papel = 'papel'
#lista=[pedra, tesoura, papel]
lista =['pedra', 'tesoura', 'papel']
escolhido2 = randint(0, 2)
#escolhido = choice(lista)
print('CPU escolheu {}, o índice é {}'.format(lista[escolhido2], escolhido2))
#print(escolhido)
if lista[escolhido2] != 'pedra' and lista[escolhido2] != 'tesoura': #CPU escolhe papel
#if escolhido != 'pedra' and escolhido != 'tesoura':
    if mao == 'tesoura':
        print('Você escolheu {} e ganhou de {}'.format(mao, lista[escolhido2]))
    if mao == 'pedra':
        print('Computador escolheu {} e ganhou de {}'.format(lista[escolhido2], mao))
    if mao == 'papel':
        print('São iguais, ninguem ganhou ou perdeu')
elif lista[escolhido2] != 'tesoura' and lista[escolhido2] != 'papel':
#elif escolhido != 'tesoura' and escolhido != 'papel': #CPU escolhe pedra
    if mao == 'papel':
        print('Você escolheu {} e ganhou de {}'.format(mao, lista[escolhido2]))
    if mao == 'tesoura':
        print('Computador escolheu {} e ganhou de {}'.format(lista[escolhido2], mao))
    if mao == 'pedra':
        print('São iguais, ninguem ganhou ou perdeu')
elif lista[escolhido2] != 'pedra' and lista[escolhido2] != 'papel':
#elif escolhido != 'pedra' and escolhido != 'papel': #CPU escolhe tesoura
    if mao == 'pedra':
        print('Você escolheu {} e ganhou de {}'.format(mao, lista[escolhido2]))
    if mao == 'papel':
        print('Computador escolheu {} e ganhou de {}'.format(lista[escolhido2], mao))
    if mao == 'tesoura':
        print('São iguais, ninguem ganhou ou perdeu')


#Verifica se já passou ou não do ano de alistamento, 18 anos
ano = int(input('Digite o ano de seu nascimento: '))
from datetime import datetime
now = datetime.now()
print ('Estamos no ano {}'.format(now.year))
idade = now.year - ano
print('Sua idade é {}'.format(idade))
if idade == 18:
    print('Está na hora de se alistar')
elif idade > 18:
    idade2 = idade - 18
    print('Já se passou {} anos do alistamento'.format(idade2))
elif idade < 18:
    idade2 = 18 - idade
    print('Faltam {} anos para o alistamento'.format(idade2))


#verifica quantos dias, meses e anos de nascimento
from datetime import datetime
dia = int(input('Qual o dia do seu nascimento: '))
mes = input('Qual o mês do seu nascimento: ')
ano = int(input('Qual o ano de seu nascimento: '))
now = datetime.now()
if mes.upper() == 'JANEIRO': #31 dias
    mes = 1
elif mes.upper() == 'FEVEREIRO':
    mes = 2
elif mes.upper() == 'MARÇO':#31 dias
    mes = 3
elif mes.upper() == 'ABRIL':
    mes = 4
elif mes.upper() == 'MAIO':#31 dias
    mes = 5
elif mes.upper() == 'JUNHO':
    mes = 6
elif mes.upper() == 'JULHO':#31 dias
    mes = 7
elif mes.upper() == 'AGOSTO':#31 dias
    mes = 8
elif mes.upper() == 'SETEMBRO':
    mes = 9
elif mes.upper() == 'OUTUBRO':#31 dias
    mes = 10
elif mes.upper() == 'NOVEMBRO':
    mes = 11
elif mes.upper() == 'DEZEMBRO':#31 dias
    mes = 12
#                   11/10/2017
#05/05/1990     20/05/1990  05/11/1990  20/11/1990
#27 anos        27 anos		26 anos		26 anos
#5 meses		4 meses		11 meses	10 meses
#6 dias         21 dias		6 dias		21 dias
idade_ano = now.year - ano
if int(mes) > now.month:
    idade_ano -= 1
    if dia < now.day: # 05 / 11 / 1990
        aux = 12 - int(mes)
        idade_mes = aux + now.month
    elif dia > now.day: # 20 / 11 / 1990
        aux = 12 - int(mes)
        idade_mes = (aux + now.month) - 1
elif int(mes) < now.month:
    if dia < now.day: # 05 / 05 / 1990
        idade_mes = now.month - int(mes)
    elif dia > now.day: # 20 / 05 / 1990
        idade_mes = (now.month - int(mes)) - 1
if dia > now.day:
    if int(mes) < now.month: # 20 / 05 / 1990
        aux = 30 - dia
        idade_dia = aux + now.day
    elif int(mes) > now.month: # 20 / 11 / 1990
        aux = 30 - dia
        idade_dia = aux + now.day
elif dia < now.day:
    if int(mes) < now.month: # 05 / 05 / 1990
        idade_dia = now.day - dia
    elif int(mes) > now.month: # 05 / 11 / 1990
        idade_dia = now.day - dia
if int(mes) == now.month:
    if dia == now.day:
        print('Você viveu exatos {} anos. Parabéns, hoje é seu aniversário!'.format(idade_ano))
else:
    print('Você tem {} anos, {} meses e {} dias'.format(idade_ano, idade_mes, idade_dia))



#Valor em nostas de 100, 50, 20, 10, 5, 2 e 1
valor = int(input(''))
cem = valor // 100
aux = valor - (cem * 100)
cinquenta = aux // 50
aux2 = aux - (cinquenta * 50)
vinte = aux2 // 20
aux = aux2 - (vinte * 20)
dez = aux // 10
aux2 = aux - (dez * 10)
cinco = aux2 // 5
aux = aux2 - (cinco * 5)
dois = aux // 2
aux2 = aux - (dois * 2)
um = aux2 // 1
print(valor)
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cinquenta))
print('{} nota(s) de R$ 20,00'.format(vinte))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinco))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(um))


#verifica maior e menor valor de 5 números digitados
n = int(input('Digite um número: '))
maior = n
menor = n
for i in range(5):
    n = int(input('Digite um número: '))
    if menor > n:
        menor = n
    if n > maior:
        maior = n
print(maior, menor)


#mostra maior e menor idade, total de idades digitadas e média entre elas
cont = 0
soma = 0
idade = int(input('Digite sua idade: '))
maior = idade
menor = idade
while(idade != 0):
    cont += 1
    soma += idade
    idade = int(input('Digite sua idade: '))
    if idade == 0:
        break
    if menor > idade:
        menor = idade
    if idade > maior:
        maior = idade
media = soma/cont
print('{:.2f}'.format(media))
print(cont)
print(maior)
print(menor)



for i in range(10):
    n = int(input('Digite um número: '))
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    if soma > 2:
        print('O número {} não é primo'.format(n))
    else:
        print('O número {} é primo'.format(n))


totalA = 0
totalD = 0
for i in range(2):
    nome = str(input('Nome: '))
    sal = float(input('Salário: '))
    if sal >= 0 and sal <= 1000:
        aux = (sal * 20) / 100
        salR = sal + aux
        print(nome, sal, salR)
    elif sal > 1000 and sal <= 5000:
        aux = (sal * 10) / 100
        salR = sal + aux
        print(nome, sal, salR)
    elif sal > 5000:
        print(nome, sal)
    totalA += sal
    totalD += salR
aux = totalD - totalA
total = float((aux * 100) / totalD)
print('{:.2f}{:.2f}{:.2f}'.format(totalA, totalD, total))


n1 = int(input('')); n2 = int(input('')); n3 = int(input(''))
for i in range(n2, n3+1):
    if i % n1 == 0:
        print('{}'.format(i))


frase=str(input('Digite uma frase:'))
fra=frase.strip()
i=0
for c in range(0,len(fra)):
    i=i+1
    lista = fra[::-1] #lista recebe a variavel fra invertida.
if lista[len(lista)-i]==fra[len(fra)-i]:
    print('Esta frase é palindromo')
else:
    print('Esta frase não é palindromo')


frase=str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Esta frase é palindromo')
else:
    print('Esta frase não é palindromo')


frase=str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Esta frase é palindromo')
else:
    print('Esta frase não é palindromo')


l = [10, 20, 30, 90, 40, 80, 70]
tam_l = len(l)
cont = 0
for i in range(tam_l):
    cont += 1
    troca = False
    for j in range(1, tam_l - i):
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            troca = True
    if not troca:
        break
print(l)


frase = "Eu AdOrO EstUDar python"
frase2 = frase.swapcase()
print(frase2)
print(ord(frase[0]))
if int(ord(frase[0])) >= 65 and int(ord(frase[0])) <= 90:
    print('Maiúscula')
else:
    print('Minúscula')
if frase[0].islower():#isupper - isdigit
    print('Maiúcula')
else:
    print('Minúscula')
frase1 = ''
for i in range(len(frase)):
    if frase[i].isupper():  # isupper - isdigit
        frase1 += frase[i].lower()
    elif frase[i].islower():
        frase1 += frase[i].upper()
    elif frase[i] == ' ':
        frase1 += ' '
print(frase1)


frase1 = []
qtde = 0
qtde1 =0
for i in range(6):
    frase = str(input('Digite uma frase: '))
    frase1.append(frase)
for i in range(len(frase1)):
    if 'ifpb' in frase1[i]:
        qtde += 1
    qtde1 += frase1[i].count('ifpb')
print(qtde, qtde1)


custos = []
cidades = []
soma = 0
maior = 0
for i in range(4):
    cidade = input('Informe a ' + str(i+1) + ' cidade: ')
    custo = int(input('Informe o valor gasto: '))
    cidades.append(cidade)
    custos.append(custo)
    soma += custo
    if custos[i] > maior:
        maior = custos[i]
for i in range(len(cidades)):
    if custos[i] == maior:
        print(cidades[i])
media = soma / 4
print(media)
for i in range(len(custos)):
    if custos[i] < media:
        print(custos[i], cidades[i])


#cria lista com 6 números distintos e gera sorteio com números distintos
import random
#função
def inserir(lista, num):
    "tentar inserir um número na lista"
    if num not in lista:
        lista.append(num)
        return True
    else:
        return False
def gerar_sorteio(lista):
    "gera 6 números aleatórios e distintos"
    while len(lista) < 6:
        inserir(lista, random.randint(1,60))
#programa principal
aposta = []
sorteio =[]
while len(aposta) < 6:
    #inserir(aposta, int(input("informe um número: ")))
    numero = int(input("informe um número: "))
    if inserir(aposta, numero) ==  False:
        print("Erro: Número Duplicado")
print(aposta)
gerar_sorteio(sorteio)
print(sorteio)


import funcao
import random
#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = []
for i in range(10):
    numeros.append(random.randint(1,100))
print(numeros)
print(funcao.maior_valor(numeros))
print(funcao.menor_valor(numeros))
print(funcao.media(numeros))
print(funcao.maior_menor(numeros))
print(funcao.maior_menor_2(numeros))


#inverter valores dentro da lista
def inverte(n):
    invertido = []
    for i in range(len(n)):
        invertido.append(n[len(n) - i - 1])
    return invertido
n = input('Digite um valor: ')
print(inverte(n))


#lista função
def inverti(n):
    n1 = str(n)
    n1 = n1[ ::-1]
    return n1
n = int(input('valor: '))
print(inverti(n))


#lista função
n = int(input('Digite um valor: '))
for i in range(n+1):
    print('*'*i)


#lista função
n = int(input('Digite os segundos: '))
hora = n//3600
resto_h = n%3600
minuto = resto_h//60
segundo = n%60
print('O(s) {} segundo(s) possui {} hora(s) {} minuto(s) e {} segundo(s)'.format(n, hora, minuto, segundo))
'''


