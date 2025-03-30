# Mensagem de Boas-vindas
print('Bem-vindo a Livraria do Havyner Siqueira')

lista_livro = []
id_global = 0

# Função que realiza o cadastro de livros
def cadastrar_livro(id):
    print('-'*56)
    print('-'*17, 'MENU CADASTRAR LIVRO', '-'*17)
    # Recebendo as informações para cadastro do livro
    print(f'Id do livro: {id}')
    nome = input('Informe o nome do livro: ')
    autor = input('Informe o autor do livro: ')
    editora = input('Informe a editora do livro: ')
    # Criando um dicionário dos livros
    livro = {"id":id, "nome":nome, "autor":autor, "editora":editora}
    # Add livro na lista
    lista_livro.append(livro)# Correto seria lista_livro.append(livro.copy())
    print('Livro cadastrado!')

# Função de consultar livro
def consultar_livro():
    if lista_livro: # Verificando se a lista está vazia
        while True:
            # Menu com as opções de consultas
            print('\n' + '-'*56)
            print('-'*17, 'MENU CONSULTAR LIVRO','-'*17)
            print('1 - Consultar todos')
            print('2 - Consultar por Id')
            print('3 - Consultar por autor')
            print('4 - Retornar ao menu')
            op_consultar = int(input('Informe a opção desejada: '))
            try:
                if op_consultar == 1: # Apresenta todos os livros cadastrados
                    for livro in lista_livro:
                        print(f'\nId: {livro["id"]}' + 
                            f'\nNome: {livro["nome"]}' + 
                            f'\nAutor: {livro["autor"]}' + 
                            f'\nEditora: {livro["editora"]}')
                elif op_consultar == 2: # Verifica o livro pelo Id informado
                    consulta_id = int(input('Informe o Id que deseja consultar: '))
                    verifica_id = False # Verifica se possui o id
                    for livro in lista_livro:
                        if livro["id"] == consulta_id:
                            print(f'\nId: {livro["id"]}' + 
                                f'\nNome: {livro["nome"]}' + 
                                f'\nAutor: {livro["autor"]}' + 
                                f'\nEditora: {livro["editora"]}')
                            verifica_id = True
                    if not verifica_id: # Se o Id informado não for identificado
                        print('Id não encontrado!')
                elif op_consultar == 3: # Verifica o livro pelo nome do autor
                    consulta_autor = input('Informe o nome do autor: ').lower()
                    verifica_autor = False # Verifica se possui o autor
                    for livro in lista_livro:
                        if livro["autor"].lower() == consulta_autor:
                            print(f'\nId: {livro["id"]}' + 
                                f'\nNome: {livro["nome"]}' + 
                                f'\nAutor: {livro["autor"]}' + 
                                f'\nEditora: {livro["editora"]}')
                            verifica_autor = True
                    if not verifica_autor: # Se o autor não for identificado
                        print('Autor não encontrado!')
                elif op_consultar == 4: # Retorna ao menu principal
                    break
                else:
                    print('Opção inválida!')
            except ValueError: # Se o usuário usar algo diferente das opções
                print('Informe uma opção válida!')
                continue
    else: # Se não tiver nenhum livro cadastrado
        print('Não possui nenhum livro cadastrado!')

# Função para remover um livro através de seu Id
def remover_livro():
    if lista_livro: # Verifica se a lista está vazia
        print('\n' + '-'*56)
        print('-'*18, 'MENU REMOVER LIVRO','-'*18)
        try:
            remove_id = int(input('Informe o Id do livro que deseja remover: '))
            verifica_id = False # Verifica se possui o id
            for livro in lista_livro:
                if livro["id"] == remove_id:
                    lista_livro.remove(livro) # remove o livro
                    print('Livro removido!')
                    verifica_id = True
            if not verifica_id: # Se não tiver o id informado
                print('Livro não encontrado!')
        except ValueError: # Valor diferente de int
            print('Valor inválido, tente novamente!')
    else: # Se a lista estiver vazia
        print('Nenhum livro cadastrado!')

# Main()
while True:
    # Menu principal
    print('\n' + '-'*56)
    print('-'*20, 'MENU PRINCIPAL', '-'*20)
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    try:
        op = int(input('Informe uma opção: ')) # Recebendo a opção desejada pelo usuário
        if op == 1:
            id_global += 1 # Inclementa o id para um novo cadastro
            cadastrar_livro(id_global)
        elif op == 2:
            consultar_livro()
        elif op == 3:
            remover_livro()
        elif op == 4: # Finalizando o programa
            print('Obrigado!')
            break
        else:
            print('Opção inválida!')
    except ValueError:
        print('Valor inválido, tente novamente!')