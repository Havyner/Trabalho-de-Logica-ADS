# Mensagem de Boas-vindas
print('Bem-vindo a Copiadora do Havyner Siqueira\n')

# Função para escolher o serviço
def escolha_servico():
    while True:
        print('DIG - Digitação')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        
        # Recebendo o serviço desejado
        servico = input('Informe o Serviço desejado: ').upper()
        if servico in {'DIG', 'ICO', 'IPB', 'FOT'}:
            return servico
        else: 
            # Caso a opção de serviço não esteja disponível
            print('\nOpção inválida! Tente novamente!\n')
            continue

# Função para definir o número de páginas
def num_pagina():
    while True:
        try:
            # Recebendo o número de páginas
            numero_paginas = int(input('Informe o número de páginas: '))
            # Limitando a quantidade de páginas
            if(numero_paginas >= 20000):
                print('Não aceitamos um número tão grande de Páginas\nLimite de: 19999')
                continue
            else:
                # Verificando desconto de acordo com a quantidade de páginas
                if(numero_paginas < 20):
                    return numero_paginas
                elif (numero_paginas >= 20 and numero_paginas < 200):
                    numero_paginas = round(numero_paginas - (numero_paginas * 0.15))
                    return numero_paginas
                elif(numero_paginas >= 200 and numero_paginas < 2000):
                    numero_paginas = round(numero_paginas - (numero_paginas * 0.20))
                    return numero_paginas
                elif (numero_paginas >= 2000 and numero_paginas < 20000):
                    numero_paginas = round(numero_paginas - (numero_paginas * 0.25))
                    return numero_paginas
        # Caso usuário informe um valor diferente de número
        except ValueError:
            print('Informe um valor válido!')
            continue

# Função para adicionar serviços extras
def servico_extra():

    valor_adicional = 0

    while True:
        try:

            print('\nServiços Extras Disponíveis')
            print('1 - Encardenação Simples = R$ 15.00')
            print('2 - Encardenação de Capa Dura = R$ 40.00')
            print('0 - Não desejo nenhum outro serviço')
            adicional = int(input('Deseja adicionar algum serviço? '))

            # Calculo de valor do serviço extra 
            if adicional == 1:
                return valor_adicional + 15
            elif adicional == 2:
                return valor_adicional + 40
            elif adicional == 0:
                return valor_adicional
            else:
                print('Opção inválida!\nTente novamente!')
        # Se o usúario informe um valor diferente de número (int)
        except ValueError:
            print('Informe um valor válido (1/2/0)')
            continue

# Programa principal main()
# Executa as funções e retorna o valor
servico = escolha_servico()
numero_paginas = num_pagina()
adicional = servico_extra()

# Atribui valor a cada serviço disponível
preco = {'DIG':1.10, 'ICO':1.00, 'IPB':0.40, 'FOT':0.20}

# Calculo do valor total
total = (preco[servico] * numero_paginas) + adicional

# Retornando ao usuário os serviços e custos
print(f'\nServiço: {servico} | Valor do Serviço: R$ {preco[servico]:.2f}')
print(f'Páginas: {numero_paginas:.0f}')
print(f'Serviço extra: R$ {adicional:.2f}')
print(f'Total: R$ {total:.2f}')