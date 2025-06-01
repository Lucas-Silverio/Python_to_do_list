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
        print('Opção 1.')
    elif( opcao == 2):
        print('Opção 2.')
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

main()