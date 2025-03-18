from flask import Flask, jsonify, request
from config import init_db
import os

app = Flask(__name__)
DB = init_db()

@app.route('/produtos/por-preco', methods=['GET'])
def pegar_produtos():
    valor_minimo = request.args.get('min_preco')
    valor_maximo = request.args.get('max_preco')

    if valor_minimo is None or valor_maximo is None:
        return jsonify({"erro": "Parâmetros 'min_preco' e 'max_preco' são obrigatórios"}), 400

    query = DB.fetch_all(
        "SELECT * FROM Products WHERE preco_compra BETWEEN %s AND %s", 
        (valor_minimo, valor_maximo)
        )

    return query, 200 if query else jsonify({"response: Nenhum produto por intervalo especificado"}), 401


@app.route('/produtos')
def listar_produtos():
    query = DB.fetch_all("SELECT * FROM Products", ())
    return (query, 200) if query else ({""}, 404)

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')  # Valor padrão: '0.0.0.0'
    port = int(os.getenv('PORT', 5000))  # Valor padrão: 5000
    app.run(host=host, port=port)