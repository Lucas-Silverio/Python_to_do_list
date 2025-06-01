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
        print('Opção 3.')
    elif(opcao == 4):
        print('Opção 4.')
    elif(opcao == 5):
        print('Opção 5.')
    elif(opcao == 6):
        print('Opção 6.')
    else:
        print('Opção Inválida.')
def adicionar_tarefa(lista_de_tarefas):
    nome_tarefa = input('Digite o nome da tarefa: ')
    esta_tarefa = { 'nome': nome_tarefa, 'concluida' : False }
    lista_de_tarefas.append(esta_tarefa)
    print(f'Tarefa \' {esta_tarefa["nome"]} \' adicionada com sucesso!')
def listar_tarefas(lista_de_tarefas):
    if(lista_de_tarefas):
        print('---Lista de Tarefas---')
        contador = 1
        for i in lista_de_tarefas:
            print(f'{contador}. {i["nome"]} {"CONCLUIDA" if i["concluida"] else "PENDENTE"}')
            contador+=1
        print('----------------------')
        input('Pressione Enter para continuar...')
    else:
        print('Não existe tarefas.')
main()