from services.database import cursor, conexao


def Incluir(cliente):
    comando = f'INSERT INTO cliente (cliNome, cliIdade, cliProfissao) VALUES ("{cliente.nome}", "{cliente.idade}", "{cliente.profissao}")'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
