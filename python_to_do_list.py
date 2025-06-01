def main():
    tarefas = []
    montar_menu()
    while(True):
        escolha = tratar_erro(int,'Digite o número da opção desejada: ')
        validar_escolha(escolha,tarefas)
        if(escolha == 6):
            print('Saindo do programa. Até mais!')
            break
def montar_menu():
    print('''
-----------------------
|        Menu         |
-----------------------
|      Opções:
|1 - Adicionar Tarefa | 
|2 - Listar Tarefas   |
|3 - Marcar Concluida |
|4 - Remover Tarefa   |
|5 - Pesquisar Tarefa |
|6 - Sair             |
-----------------------
''')
def tratar_erro(tipo, texto):
    while(True):
        try:
            entrada = tipo(input(texto))
            return entrada
        except:
            print('Entrada inválida.')
def validar_escolha(opcao,lista):
    if(opcao == 1):
        adicionar_tarefa(lista)
    elif( opcao == 2):
        listar_tarefas(lista)
    elif(opcao == 3):
        marcar_tarefa_concluida(lista)
    elif(opcao == 4):
        remover_tarefa(lista)
    elif(opcao == 5):
        pesquisar_tarefas(lista)
    elif(opcao == 6):
        print('Opção 6.')
    else:
        print('Opção Inválida.')
def selecionar_item(lista_de_tarefas,texto):
    while(True):
        item_escolhido = tratar_erro(int,texto)
        if item_escolhido <= 0 or item_escolhido > (len(lista_de_tarefas)):
            print('Item selecionado é inválido.')
        else:
            return item_escolhido - 1

def adicionar_tarefa(lista_de_tarefas):
    nome_tarefa = input('Digite o nome da tarefa: ')
    esta_tarefa = { 'nome': nome_tarefa, 'concluida' : False }
    lista_de_tarefas.append(esta_tarefa)
    print(f'Tarefa \' {esta_tarefa["nome"]} \' adicionada com sucesso!')
def listar_tarefas(lista_de_tarefas):
    if(lista_de_tarefas):
        montar_lista(lista_de_tarefas)
        input('Pressione Enter para continuar...')
    else:
        print('Não existe tarefas.')
def montar_lista(lista):
    print('---Lista de Tarefas---')
    contador = 1
    for i in lista:
        print(f'{contador}. {i["nome"]} {"CONCLUIDA" if i["concluida"] else "PENDENTE"}')
        contador+=1
    print('----------------------')
def remover_tarefa(lista_de_tarefas):
    if(lista_de_tarefas):
        montar_lista(lista_de_tarefas)    
        indicie_escolhido = selecionar_item(lista_de_tarefas,'Digite o número da tarefa a ser removida: ')
        try:
            print(f'Tarefa \'{lista_de_tarefas[indicie_escolhido]["nome"]}\' removida com sucesso!')
            del lista_de_tarefas[indicie_escolhido]
        except:
            print('Erro ao Deletar Tarefa.')
    else:
        print('A lista de tarefas está vazia...')
        return
def marcar_tarefa_concluida(lista_de_tarefas):
    if(lista_de_tarefas):
        montar_lista(lista_de_tarefas)
        indice_escolhido = selecionar_item(lista_de_tarefas,'Digite o número da tarefa a ser marcada como concluída: ')
        item_escolhido = lista_de_tarefas[indice_escolhido]
        if(item_escolhido["concluida"]):
            print('A Tarefa já esta concluída.')
        else:
            lista_de_tarefas[indice_escolhido]["concluida"] = True
            print(f'Tarefa \'{item_escolhido["nome"]}\' marcada como concluída!')
    else:
        print('A lista de tarefas está vazia...')
        return
def pesquisar_tarefas(lista_de_tarefas):
    item_pesquisado = input('Digite o que deseja pesquisar: ').lower()
    lista_aux = []
    for i in lista_de_tarefas:
        if item_pesquisado in i["nome"].lower():
            lista_aux.append(i)
    if(lista_aux):
        print('---Resultados:---')
        for i in lista_aux:
            print(f'Nome: \'{i["nome"]}\' Status: {"CONCLUIDA" if i["concluida"] else "PENDENTE"}')
        print('------------------')
    else:
        print('Não foi encontrado nenhuma Tarefa.')
main()