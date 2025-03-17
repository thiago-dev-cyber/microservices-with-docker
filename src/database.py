import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Any, Optional

class DataBase:
    def __init__(self, host: str, user: str, port: int, database: str, password: str):
        """
        Inicializa a classe DataBase com as configurações de conexão.

        :param host: Endereço do servidor do banco de dados.
        :param user: Usuário do banco de dados.
        :param port: Porta do banco de dados.
        :param database: Nome do banco de dados.
        :param password: Senha do banco de dados.
        """
        self.database_config = {
            "host": host,
            "port": port,
            "user": user,
            "database": database,
            "password": password
        }

    def get_connect(self):
        """
        Estabelece uma conexão com o banco de dados.

        :return: Conexão com o banco de dados.
        :raises: Error se a conexão falhar.
        """
        try:
            conn = mysql.connector.connect(**self.database_config)
            if conn.is_connected():
                print("Conexão ao banco de dados realizada com sucesso!")
                return conn
        except Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            raise

    def fetch_all(self, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """
        Executa uma consulta e retorna todos os resultados.

        :param query: Consulta SQL a ser executada.
        :param params: Parâmetros para a consulta (opcional).
        :return: Lista de dicionários contendo os resultados.
        """
        conn = None
        cursor = None
        try:
            conn = self.get_connect()
            cursor = conn.cursor(dictionary=True)  # Retorna resultados como dicionários
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Error as err:
            print(f"Erro ao executar a consulta: {err}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
                print("Conexão ao banco de dados encerrada.")

    def fetch_one(self, query: str, params: Optional[tuple] = None) -> Optional[Dict[str, Any]]:
        """
        Executa uma consulta e retorna o primeiro resultado.

        :param query: Consulta SQL a ser executada.
        :param params: Parâmetros para a consulta (opcional).
        :return: Um dicionário contendo o primeiro resultado ou None.
        """
        conn = None
        cursor = None
        try:
            conn = self.get_connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            return cursor.fetchone()
        except Error as err:
            print(f"Erro ao executar a consulta: {err}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
                print("Conexão ao banco de dados encerrada.")

    def execute(self, query: str, params: Optional[tuple] = None) -> None:
        """
        Executa uma consulta que não retorna resultados (INSERT, UPDATE, DELETE).

        :param query: Consulta SQL a ser executada.
        :param params: Parâmetros para a consulta (opcional).
        """
        conn = None
        cursor = None
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            conn.commit()  # Confirma a transação
        except Error as err:
            print(f"Erro ao executar a consulta: {err}")
            if conn:
                conn.rollback()  # Reverte a transação em caso de erro
            raise
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
                print("Conexão ao banco de dados encerrada.")