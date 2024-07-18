# -*- coding: utf-8 -*-
"""
Aula 2

Sequências de passos para conexão com Database Local MySql.
"""

# =============================================================================
# 1 - Pacotes
# =============================================================================
# 1.1 - Instala
#!pip install mysql-connector-python
#!pip install pandas

# 1.2 - Importa
import mysql.connector
import pandas as pd


# =============================================================================
# 2 - Realiza conexão
# =============================================================================
config = {
    'user': 'root',
    'password': 'my-secret-pw',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'sakila',
    'raise_on_warnings': True
}

try:
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print('Connected to MySQL successfully!')
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Databases:")
        for database in databases:
            print(database)
        cursor.close()
    else:
        print('Failed to connect to MySQL.')
except Error as err:
    print(f"Error: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
    
    
# =============================================================================
# 3 - Query em Dataframe
# =============================================================================
# Criação do cursor
cursor = conn.cursor()

# Escrevendo a query
query = "SELECT * FROM sakila.actor;"

# Executando a query
cursor.execute(query)

# Obtendo os resultados
resultados = cursor.fetchall()

 # Obtendo os nomes das colunas
colunas = cursor.column_names

# Transformando os resultados em um DataFrame do Pandas
df = pd.DataFrame(resultados, columns=colunas)

# =============================================================================
# =============================================================================
