from flask import Flask, render_template, request, redirect, url_for
import datetime
from DATA import conexao

app = Flask(__name__)

@app.route('/')
def comentarios():
    # Consulta os comentários do banco de dados
    sql = "SELECT nome, data_hora, comentario FROM tb_comentarios ORDER BY data_hora DESC"
    conexao.cursor.execute(sql)
    comentarios = conexao.cursor.fetchall()  # Recupera todos os comentários da tabela

    # Passa os dados para o template
    return render_template('index.html', comentarios=comentarios)


@app.route('/post/comentario', methods=['POST'])
def getComentario():
    nomeUser = request.form['nome']
    comentarioUser = request.form['comentario']
    data_hora = datetime.datetime.today()

    sql = """
        INSERT INTO tb_comentarios(nome, data_hora, comentario)
        VALUES(%s,%s,%s)
    """

    valores = (nomeUser, data_hora, comentarioUser)

    conexao.cursor.execute(sql, valores)
    conexao.conn.commit()

    conexao.cursor.close()
    conexao.conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
