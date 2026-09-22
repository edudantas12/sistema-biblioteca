from livros import cadastrar_livro, listar_livros, buscar_livro, atualizar_livro, excluir_livro
from usuarios import cadastrar_usuario, listar_usuario, buscar_usuario, atualizar_usuario, excluir_usuario
from emprestimos import realizar_emprestimo, devolver_livro

opcao = -1
while opcao != 0:
    print("---- MENU -----")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Atualizar livro")
    print("5 - Excluir livro")
    print("6 - Cadastrar usuario")
    print("7 - Listar usuarios")
    print("8 - Buscar usuarios")
    print("9 - Atualizar usuario")
    print("10 - Excluir usuario")
    print("11 - Realizar emprestimo")
    print("12 - Devolver livro")
    print("0 - Sair")
    try:
        opcao = int(input("Escolha: "))
    except ValueError:
        print("Digite apenas números")
        continue


    if opcao == 1:
        cadastrar_livro()
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        buscar_livro()
    elif opcao == 4:
        atualizar_livro()
    elif opcao == 5:
        excluir_livro()
    elif opcao == 6:
        cadastrar_usuario()
    elif opcao == 7:
        listar_usuario()
    elif opcao == 8:
        buscar_usuario()
    elif opcao == 9:
        atualizar_usuario()
    elif opcao == 10:
        excluir_usuario()
    elif opcao == 11:
        realizar_emprestimo()
    elif opcao == 12:
        devolver_livro()
    elif opcao != 0:
        print("Opção invalida. Escolha uma opção de 0 a 12.")

