'''
peso = float(input('Qual o peso do peixe? '))
if peso > 50:
    excesso = peso-50
    multa = excesso*4
    if excesso == 1:
        print('O execesso foi de {} kilo e a multa é de {} reais'.format(excesso, multa))
    else:
        print('O execesso foi de {} kilos e a multa é de {} reais'.format(excesso, multa))
else:
    print('O excesso e a multa foram 0 reais')


ce = float(input('Quantos litros de cerveja foi consumido? '))
ca = float(input('Quantos litros de cana foi consumido'))
if ce <= 20:
    vtce = ce * 5
    dce = (vtce * 3) / 100
     vce= vtce - dce
    print('O valor a ser pago da cerveja é {} reais'.format(vce))
else:
    vtce = ce * 5
    dce = (vtce * 5) / 100
    vce = vtce - dce
    print('O valor a ser pago da cerveja é {} reais'.format(vce))
if ca <= 20:
    vtca = ca * 1.9
    dca = (vtca * 4) / 100
    vca = vtca - dca
    print('O valor a ser pago da cana é {} reais'.format(vca))
else:
    vtca = ca * 1.9
    dca = (vtca * 6) / 100
    vca = vtca - dca
    print('O valor a ser pago da cana é {} reais'.format(vca))


#calcular ICM, < 18.5 abaixo do peso, >= 18.5 < 25 peso ideal, >= 25 < 30 sobrepeso, >= 30 < 40 obesidade, >= 40 obesidade morbida
peso = float(input('Digite seu peso em kilogramas: '))
altura = float(input('Digite sua altura em metros: '))
imc = (peso / altura) ** 2
print('Seu IMC é {:.2f}'.format(imc))

while(alive):
    exp = str(input('Experiment the life: '))
    if exp != 'die':
        life += exp
    else:
        print('Good trip')


Lista 1.4
n1 = float(input('nota 1 '))
n2 = float(input('nota 2 '))
n1 *= 6
n2 *= 4
soma = (n1 + n2) / 10
print('{:.2f}'.format(soma))

n1 = int(input('Valor 1 '))
n2 = int(input('Valor 2 '))
res = n1 // n2
print('A divisão de {} por {} é igual a {}'. format(n1, n2, res))
'''


'''
import datetime

hoje=datetime.date.today()

anoAtual= hoje.strftime("%Y")

meses = { 'janeiro' : 1 , 'fevereiro' : 2 , 'marco' : 3 , 'abril' : 4 , 'maio' : 5 , 'junho' : 6 , 'julho' : 7 , 'agosto' : 8 , 'setembro' : 9 , 'outubro' : 10 , 'novembro' : 11 , 'dezembro' : 12 }
meses1 = {  1 : 'janeiro' , 2 : 'fevereiro' , 3 : 'marco', 4 : 'abril' , 5 : 'maio' , 6 : 'junho', 7 : 'julho', 8 : 'agosto' , 9 : 'setembro' , 10 : 'outubro' , 11 : 'novembro' , 12 : 'dezembro' }

bissexto = False

#dados forncecidos

coletandodados = True

while coletandodados == True:
    dia= input("Digite o dia do seu nascimento \nExemplo: 31 \n" )

    mes= input("\n Digite o mes do seu nascimento (numero ou por extenso entre aspas)\nExemplos: 12 , 'agosto', 'marco'")
    print (type(mes))
# #Testa se o mês existe
    if type(mes) is str:
        if meses.has_key(mes) == True:
            print (mes) in meses
            mes= meses[mes]
            print (mes)
        elif mes in meses == False:
            print ("nome de mes invalido. Tente novamente.")
            continue
# #Testa se o dia é compatível com o mês
    if type(mes) is int:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes ==12:
            if dia > 31:
                print ("Esse mes possui somente 31 dias.")
                continue
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 30:
                print ("Esse mes possui somente 30 dias.")
                continue
        if mes == 2:
            if dia == 29:
                bissexto = True
                print ("Sera verificado se o ano e bissexto")
            elif dia > 29:
                print ("Fevereiro tem no maximo 29 dias!")
                continue

    ano=input("\n Digite o ano do seu nascimento (a partir de 1583) \n Exemplo: 1990 \n ")
    if ano < 1583:
        print ("Nao e possivel calcular para antes de 1583, o calendario que usamos hoje nao existia.")
        continue

# #Verifica se o ano é bissexto
    if bissexto == True:
        if ano % 100 == 0:
            if ano % 400 != 0:
                print ("Esse ano nao e bissexto, portanto nao possui 29 de fevereiro.")
                continue
        elif ano % 100 != 0:
            if ano % 4 != 0:
                print ("Esse ano nao e bissexto, portanto nao possui 29 de fevereiro.")
                continue

        print ("Esse ano e bissexto.")

#Verifica se a pessoa "nasceu no futuro":
    if ano > anoAtual:
        print ("Voce nasceu no futuro?")
        continue

    print ("Sua data de nascimento e: ", dia, "de", meses1[mes], "de", ano,  "\n")
    confirma = raw_input("Confirma sua data de nascimento (s/n)? ")
    if confirma == 's':
        coletandodados = False

# Cálculos
# fica bem facil usando o modulo datetime

niver = datetime.date(ano, mes, dia)

idadeemdias = hoje - niver

print ("Sua idade em dias e ", idadeemdias.days, "dias.")


#digite um numero, enquanto diferente de 0 mostre os números de 1 ao numero digitado.

n = int(input('Digite um número: '))
soma = 0
for i in range(n+1):
    soma += i
print(soma)

n1 = float(input('Digite um número: '))
h = 1
for i in range(1, n1+1):
    h += 1/n
print(h)
'''

'''
a = 5000
b = 2000
ta = (1 * a) / 100
tb = (1.5 * b) / 100
while a > b:
'''

'''
for i in range(5):
    n = int(input('Digite um número: '))
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    if cont > 2:
        print('O número {} não é primo'.format(n))
    else:
        print('O número {} é primo'.format(n))
'''

'''
lista = []
for i in range(3):
    n = int(input('Digite o {} valor: '.format(i)))
    lista.append(n)
cont = 1
while (cont != 0):
    cont = 0
    for i in range(len(lista)):
        for j in range(i - 1):
            if lista[j + 1] < lista[i]:
                aux = lista[i]
                lista[i] = lista[j + 1]
                lista[j + 1] = aux
                cont += 1
            print(cont)
            print(lista)
print(lista)
'''


valor = int(input('Digite um valor: '))
cem = valor//100
print('qtde de cem', cem)
resto_cem = valor%100
print('sobrou', resto_cem)
cinque = resto_cem//50
print('qtde de cinquenta', cinque)
vinte = (resto_cem - 50)//20
print('qtde de vinte', vinte)
aux = (resto_cem - 50)%20
dez = aux//10
print('qtde de dez', dez)
cinco = aux//5
print('qtde de cinco', cinco)
dois = (aux - 5)//2
print('qtde de dois', dois)#2
um = (aux - 5)%2
print('qtde de um', um)#0
