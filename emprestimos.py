from banco import conexao
from datetime import date

def realizar_emprestimo():
    id_usuario = int(input("Informe o seu id: "))
    id_livro = int(input("Informe o id do seu livro: "))

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM tb_usuarios WHERE id = %s", (id_usuario,)
    )
    resultado = cursor.fetchone()
    if not resultado:
        print("Usuário não encontrado")
        return

    cursor.execute(
        "SELECT * FROM tb_livros WHERE id = %s", (id_livro,)


    )
    resultado = cursor.fetchone()
    if not resultado:
        print("Livro não encontrado")
        return
    if not resultado[4]:
        print("Livro não está disponível")
        return

    cursor.execute(
        "INSERT INTO tb_emprestimos (id_usuario, id_livro, dt_emprestimo, devolvido) VALUES (%s, %s, %s, %s)",
        (id_usuario, id_livro, date.today(), False)
    )

    cursor.execute(
        """
        UPDATE tb_livros
        SET disponivel = FALSE
        WHERE id = %s
        """, (id_livro,)
    )

    conexao.commit()
    print("Empréstimo realizado com sucesso!")


def devolver_livro():
    id_livro = int(input("Informe o id do livro que está sendo devolvido: "))
    cursor = conexao.cursor()
    cursor.execute(
        """
        SELECT * FROM tb_emprestimos 
        WHERE id_livro = %s
        AND devolvido = FALSE
        """, (id_livro,)
    )
    resultado = cursor.fetchone()
    if resultado:
        print(
            f"ID: {resultado[0]}\n")
    else:
        print("Nenhum empréstimo ativo encontrado para este livro")
        return

    cursor.execute(
        """
        UPDATE  tb_emprestimos
        SET devolvido = True
        WHERE   id = %s
        """, (resultado[0],)
    )

    cursor.execute(
        """
        UPDATE tb_livros
        SET disponivel = True
        WHERE id = %s
        """, (id_livro,)
    )

    conexao.commit()
    print("Livro devolvido com sucesso!")


