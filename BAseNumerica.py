num = int(input('Digite um numero Inteiro: '))
print("-----------------------------------------")
print('''Escola uma das bases para converção: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
print("-----------------------------------------")

opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para \033[1;31mBINARIO\033[m é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para \033[1;31mOCTAL \033[mé igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida!!')