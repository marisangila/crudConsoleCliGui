import mysql.connector
import PySimpleGUI as sg

conexao = None
cursor = None
layout = None
window = None

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

def inserir_filme(nome, ano_lancamento_filme):
    sql = 'INSERT INTO filme (nome_filme, ano_lancamento_filme) VALUES (%s, %s);'
    dados = (nome, ano_lancamento_filme)
    cursor.execute(sql, dados)
    conexao.commit()
    sg.popup(f'Filme "{nome}" foi inserido com sucesso!')

def listar_filmes():
    cursor.execute('SELECT * FROM filme;')
    filmes = cursor.fetchall()
    resultado = ''
    for filme in filmes:
        resultado += f'Código: {filme[0]}\n'
        resultado += f'Nome: {filme[1]}\n'
        resultado += f'Data de Lançamento: {filme[2]}\n\n'
    return resultado

def listar_filme(pk_filme):
    sql = 'SELECT * FROM filme WHERE id_filme = %s;'
    cursor.execute(sql, (pk_filme,))
    filme = cursor.fetchone()
    if filme:
        return f'Código: {filme[0]}\nNome: {filme[1]}\nData de Lançamento: {filme[2]}\n'
    else:
        return 'Filme não encontrado.'

def editar_filme(pk_filme, nome, ano_lancamento_filme):
    sql = 'UPDATE filme SET nome_filme = %s, ano_lancamento_filme = %s WHERE id_filme = %s;'
    dados = (nome, ano_lancamento_filme, pk_filme)
    cursor.execute(sql, dados)
    conexao.commit()
    sg.popup(f'Filme com código {pk_filme} foi atualizado com sucesso!')

def excluir_filme(pk_filme):
    sql = 'DELETE FROM filme WHERE id_filme = %s;'
    cursor.execute(sql, (pk_filme,))
    conexao.commit()
    sg.popup(f'Filme com código {pk_filme} foi deletado com sucesso!')

# Definir o layout da interface
def definir_tela():
    global layout
    layout = [
        [sg.Text("Gerenciamento de Filmes")],
        [sg.Button("Inserir Filme"), sg.Button("Listar Filmes")],
        [sg.Text("Código do Filme:"), sg.InputText(key='codigo')],
        [sg.Button("Listar Filme"), sg.Button("Editar Filme"), sg.Button("Excluir Filme")],
        [sg.Output(size=(50, 10), key='output')],
        [sg.Button("Sair")]
    ]
    global window
    window = sg.Window("Filmes", layout)

# Inicio da Execução
if __name__ == '__main__':
    
    definir_tela()
    fazer_conexao()
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            break

        if event == 'Inserir Filme':
            nome = sg.popup_get_text("Digite o nome do filme:")
            ano_lancamento_filme = sg.popup_get_text("Digite o ano de lançamento do filme:")
            inserir_filme(nome, ano_lancamento_filme)

        if event == 'Listar Filmes':
            resultado = listar_filmes()
            window['output'].update(resultado)

        if event == 'Listar Filme':
            codigo = values['codigo']
            resultado = listar_filme(codigo)
            window['output'].update(resultado)

        if event == 'Editar Filme':
            codigo = values['codigo']
            nome = sg.popup_get_text("Digite o novo nome do filme:")
            ano_lancamento_filme = sg.popup_get_text("Digite o novo ano de lançamento do filme:")
            editar_filme(codigo, nome, ano_lancamento_filme)

        if event == 'Excluir Filme':
            codigo = values['codigo']
            excluir_filme(codigo)

    conexao.close()
    window.close()
