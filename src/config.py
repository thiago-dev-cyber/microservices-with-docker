from database import DataBase
import os

def init_db():
	host = 'db'
	user = 'root'
	port = int(os.getenv('MYSQL_PORT', 3306))
	database = os.getenv('MYSQL_DATABASE', 'api_database')
	password = os.getenv('MYSQL_ROOT_PASSWORD', '')

	return DataBase(
		host=host,
		user=user,
		port=port,
		database=database,
		password=password
	)

