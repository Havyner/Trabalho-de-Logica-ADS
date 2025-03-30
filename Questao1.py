# A - print de boas-vindas 
print('Bem-vindo a Loja do Havyner Siqueira\n')

# B - Recebendo valor e quantidade de produto
valor_unitario = float(input('Informe o valor do produto: R$ '))
quantidade = int(input('Informe a quantidade: '))
'''
Realizando o calculo do valor total e implementando as condições
para receber o desconto.
'''
valor_total = valor_unitario * quantidade #Valor final da compra

# Calculando desconto de 4% para compras igual ou maior de 2.5k e menor que 6k 
if ((valor_total >= 2500) and (valor_total < 6000)):
    valor_desconto = valor_total - (valor_total * 0.04)
    print(f'\nO valor SEM desconto: R$ {valor_total:.2f}')
    print(f'O valor COM desconto: R$ {valor_desconto:.2f}')

# Calculando desconto de 7% para compras igual ou maior de 6k e menor que 10k
elif ((valor_total >= 6000) and (valor_total < 10000)):
    valor_desconto = valor_total - (valor_total * 0.07)
    print(f'\nO valor SEM desconto: R$ {valor_total:.2f}')
    print(f'O valor COM desconto: R$ {valor_desconto:.2f}')

# # Calculando desconto de 11% para compras igual ou maior de 11k
elif (valor_total >= 10000):
    valor_desconto = valor_total - (valor_total * 0.11)
    print(f'\nO valor SEM desconto: R$ {valor_total:.2f}')
    print(f'O valor COM desconto: R$ {valor_desconto:.2f}')

# Se a compra for menor que 2.5k
else:
    print('\nSua compra não atingiu o valor mínimo para conquistar desconto.')
    print(f'Valor total: R$ {valor_total:.2f}')