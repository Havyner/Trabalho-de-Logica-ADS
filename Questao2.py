# Print de Boas-vindas
print('Bem-vindo a Sorveteria do Havyner Siqueira')

# Cardápio
print('-' * 16, 'CARDÁPIO', '-' * 16)
print('-' * 42)
print('---| TAMANHO | CUPUAÇU(CP) | AÇAÍ(AC) |---')
print('---|    P    |   R$ 9.00   | R$ 11.00 |---')
print('---|    M    |   R$14.00   | R$ 16.00 |---')
print('---|    G    |   R$18.00   | R$ 20.00 |---')
print('-' * 42)


# Variáveis de controle de pedido
conta = 0
valor_final = 0

while True:

    # Recebendo o sabor e verificando se é válido
    sabor = input('Informe o sabor desejado (CP/AC): ').upper()
    if ((sabor != 'CP') and (sabor != 'AC')):
        print('Sabor inválido! Tente novamente!\n')
        continue

    # Recebendo o tamanho e verificando se é válido
    tamanho = input('Informe o tamanho desejado (P/M/G): ').upper()
    if ((tamanho != 'P') and (tamanho != 'M') and (tamanho != 'G')):
        print('Tamanho inválido! Tente novamente!\n')
        continue

    # Verificando o pedido
    if sabor == 'CP':
        sabor = 'Cupuaçu'
        if tamanho == 'P':
            conta = 9
        elif tamanho == 'M':
            conta = 14
        else:
            conta = 18
    else:
        sabor = 'Açai'
        if tamanho == 'P':
            conta = 11
        elif tamanho == 'M':
            conta = 16
        else:
            conta = 20
    # Informando o último pedido
    print(f'Você pediu {sabor} no tamanho {tamanho}: R$ {conta:.2f}')

    # Acumulador somando todo o pedido
    valor_final += conta

    # Verificando se deseja pedir mais algo
    pedido = input('\nDeseja pedir mais alguma coisa (S/N)? ').upper()
    if pedido != 'S':
        break

# Apresentando ao usuário o valor final a ser pago
print(f'O valor total a ser pago é: R$ {valor_final:.2f}')
print('Obrigado, volte sempre!')