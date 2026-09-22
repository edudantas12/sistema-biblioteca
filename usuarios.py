from banco import conexao

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tb_usuarios (nome, email) VALUES (%s, %s)",
        (nome, email)
    )
    conexao.commit()

def listar_usuario():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tb_usuarios")
    resultado = cursor.fetchall()
    for usuario in resultado:
        print(f"ID: {usuario[0]}\nNome: {usuario[1]}\nEmail: {usuario[2]}\n")

def buscar_usuario():
    id_usuario = int(input("Digite o ID do usuário: "))
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM tb_usuarios WHERE id = %s",
        (id_usuario,)
    )
    resultado = cursor.fetchone()

    if resultado:
        print(
            f"ID: {resultado[0]}\nNome: {resultado[1]}\nEmail: {resultado[2]}\n")
    else:
        print("Usuário não encontrado")

def atualizar_usuario():
    id_usuario = int(input("Digite o ID do usuário: "))
    nome_usuario = input("Atualize o nome: ")
    email_usuario = input("Atualize o email: ")

    cursor = conexao.cursor()
    cursor.execute(
        """
        UPDATE tb_usuarios
        SET nome = %s,
            email  = %s
        WHERE id = %s
        """, (nome_usuario, email_usuario, id_usuario)
    )
    linhas_alteradas = cursor.rowcount
    conexao.commit()
    if linhas_alteradas > 0:
        print(f"Foram alterados {linhas_alteradas} usuário(s)")
        print("Usuário alterado com sucesso")
    else:
        print("Usuário não encontrado")

def excluir_usuario():
    id_usuario = int(input("Digite o ID do usuário: "))
    cursor = conexao.cursor()
    cursor.execute(
        """
        DELETE FROM tb_usuarios
        WHERE id = %s
        """, (id_usuario,)
    )
    linhas_deletadas = cursor.rowcount

    conexao.commit()
    if linhas_deletadas > 0:
        print(f"Foram deletados {linhas_deletadas} usuário(s)")
    else:
        print("Usuário não encontrado")
