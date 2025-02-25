from flask import Flask, render_template, request, redirect, url_for
import datetime
from DATA import conexao

app = Flask(__name__)

@app.route('/')
def comentarios():

    conn = conexao.get_conexao()
    cursor = conn.cursor()

    # Consulta os comentários do banco de dados
    sql = "SELECT nome, data_hora, comentario FROM tb_comentarios ORDER BY data_hora DESC"
    cursor.execute(sql)
    comentarios = cursor.fetchall()  # Recupera todos os comentários da tabela

    conexao.close_conexao(conn, cursor)

    # Passa os dados para o template
    return render_template('index.html', comentarios=comentarios)


@app.route('/post/comentario', methods=['POST'])
def getComentario():
    nomeUser = request.form['nome']
    comentarioUser = request.form['comentario']
    data_hora = datetime.datetime.today()

    conn = conexao.get_conexao()
    cursor = conn.cursor()

    sql = """
        INSERT INTO tb_comentarios(nome, data_hora, comentario)
        VALUES(%s,%s,%s)
    """

    valores = (nomeUser, data_hora, comentarioUser)

    cursor.execute(sql, valores)
    conn.commit()

    conexao.close_conexao(conn, cursor)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
