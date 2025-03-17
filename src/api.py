from flask import Flask, jsonify
from config import init_db
import os

app = Flask(__name__)
DB = init_db()

@app.route('/')
def hello():
    return f"Hello from container: HELL"


@app.route('/products')
def list_products():
    query = DB.fetch_all()
    return query

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')  # Valor padrão: '0.0.0.0'
    port = int(os.getenv('PORT', 5000))  # Valor padrão: 5000
    app.run(host=host, port=port)