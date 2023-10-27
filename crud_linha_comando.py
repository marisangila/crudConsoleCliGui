import mysql.connector

conexao = None
cursor = None

def mostrarMenu():
    opcao = 0
    while opcao != 6:
        print("[1] Inserir Filme")
        print("[2] Listar Filmes")
        print("[3] Listar Filme")
        print("[4] Editar Filme")
        print("[5] Excluir Filme")
        print("[6] Sair")
        print("Escolha uma opção:")
        opcao = int(input())  # Converte a entrada para um número inteiro

        if opcao == 1:
            inserir_filme()
        elif opcao == 2:
            listar_filmes()
        elif opcao == 3:
            listar_filme()
        elif opcao == 4:
            editar_filme()
        elif opcao == 5:
            excluir_filme()
        elif opcao == 6:
            print("Saindo...")
        else:
            print("Opção Inválida!")

# Conectar ao servidor MySQL (certifique-se de substituir os valores com suas próprias credenciais)
def fazer_conexao():
    global conexao, cursor
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="filmes"
    )
    cursor = conexao.cursor()

def inserir_filme():
    print('--------------------------------------')
    print('Inserir de Filmes:')
    nome = input("Digite o nome do filme: ")
    ano_lancamento_filme = input("Digite o ano de lançamento do filme: ")

    sql = 'INSERT INTO filme (nome_filme, ano_lancamento_filme) VALUES (%s, %s);'

    dados = (nome, ano_lancamento_filme)
    cursor.execute(sql, dados)
    conexao.commit()

    print(f'Filme "{nome}" foi inserido com sucesso!')

def listar_filmes():
    cursor.execute('SELECT * FROM filme;')
    filmes = cursor.fetchall()
    print('--------------------------------------')
    print('Visualizar Filmes:')
    for filme in filmes:
        print('--------------------------------------')
        print(f'Código: {filme[0]}')
        print(f'Nome: {filme[1]}')
        print(f'Data de Lançamento: {filme[2]}')

def listar_filme():
    print('--------------------------------------')
    print('Visualizar Filme:')
    nome = input("Digite o nome do filme que você quer visualizar: ")
    
    sql = 'SELECT * FROM filme WHERE nome_filme = %s;'

    cursor.execute(sql, (nome,))
    filme = cursor.fetchone()

    if filme:
        print('Filme:')
        print(f'Código: {filme[0]}')
        print(f'Nome: {filme[1]}')
        print(f'Ano de Lançamento: {filme[2]}')
    else:
        print("Filme não encontrado.")

def editar_filme():
    print('--------------------------------------')
    print('Editar de Filme:')
    pk_filme = input("Digite o código do filme que você quer editar: ")
    novo_nome_filme = input("Digite o novo nome do filme: ")
    novo_ano_lancamento_filme = input("Digite o novo ano de lançamento do filme: ")

    sql = 'UPDATE filme SET nome_filme = %s, ano_lancamento_filme = %s WHERE PK_filme = %s;'
    dados = (novo_nome_filme, novo_ano_lancamento_filme, pk_filme)
    cursor.execute(sql, dados)
    conexao.commit()
    print(f'Filme com código {pk_filme} foi atualizado com sucesso!')

def excluir_filme():
    print('--------------------------------------')
    print('Excluir de Filme:')
    pk_filme = input("Digite o código do filme que você quer excluir: ")

    sql = 'DELETE FROM filme WHERE PK_filme = %s;'
    cursor.execute(sql, (pk_filme,))
    conexao.commit()
    print(f'Filme com código {pk_filme} foi deletado com sucesso!')

# Inicio da Execução
if __name__ == '__main__':
    fazer_conexao()
    mostrarMenu()
    conexao.close()
