from banco import conexao

def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tb_livros (titulo, autor, isbn, disponivel) VALUES (%s, %s, %s, %s)",
        (titulo, autor, isbn, True)
    )
    conexao.commit()

def listar_livros():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tb_livros")
    resultado = cursor.fetchall()
    for livro in resultado:
        print(f"ID: {livro[0]}\nTítulo: {livro[1]}\nAutor: {livro[2]}\nISBN: {livro[3]}\nDisponÍvel: {livro[4]}\n")

def buscar_livro():
    id_livro = int(input("Digite o ID do livro: "))
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM tb_livros WHERE id = %s",
        (id_livro,)
    )
    resultado = cursor.fetchone()

    if resultado:
        print(
            f"ID: {resultado[0]}\nTítulo: {resultado[1]}\nAutor: {resultado[2]}\nISBN: {resultado[3]}\nDisponível: {resultado[4]}\n")
    else:
        print("Livro não encontrado")

def atualizar_livro():
    id_livro = int(input("Digite o ID do livro: "))
    titulo_livro = input("Qual o novo titulo do livro?")
    autor_livro = input("Qual o novo autor?")
    isbn_livro = input("Qual o novo isbn?")

    cursor = conexao.cursor()
    cursor.execute(
        """
        UPDATE tb_livros
        SET titulo = %s,
            autor  = %s,
            isbn   = %s
        WHERE id = %s
        """, (titulo_livro, autor_livro, isbn_livro, id_livro)
    )
    linhas_alteradas = cursor.rowcount
    conexao.commit()
    if linhas_alteradas > 0:
        print(f"Foram alterados {linhas_alteradas} livro(s)")
        print("Livro alterado com sucesso")
    else:
        print("Livro não encontrado")

def excluir_livro():
    id_livro = int(input("Digite o ID do livro: "))
    cursor = conexao.cursor()
    cursor.execute(
        """
        DELETE FROM tb_livros
        WHERE id = %s
        """, (id_livro,)
    )
    linhas_deletadas = cursor.rowcount

    conexao.commit()
    if linhas_deletadas > 0:
        print(f"{linhas_deletadas} livro(s) excluído(s) com sucesso")
    else:
        print("Livro não encontrado")

