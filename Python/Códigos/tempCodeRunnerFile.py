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