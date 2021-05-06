from mysql.connector import connect

query_create_shema = "SHOW SCHEMAS" #SEMPRE USE LETRA MAIUSCULA
params = None

def execute (sql,params = None): # serve para insert,update,delet,create,alter,drop
    with connect(host="localhost", user ="root", password = "ga2468bi", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.executemany(sql,params)# colocando executemany aqui não é necessario a estrutura for nas funçoes q usam execute
            conn.commit()

def query(sql,params = None):# executa comando e retorna resultado
    with connect(host="localhost", user ="root", password = "ga2468bi", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,params)
            return cursor.fetchall() # qnd vou fazer o select tem q retornar algo, ou seja pega os valores q o bd retornou

def insert(tabela, colunas, valores):
     execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join('%s')})", valores)


def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])

def select(tabela, chave, valor_chave):
    query(f"SELECT * FROM {tabela} WHERE {chave} =%s", (valor_chave,)) #para retornar um valor sempre é usado o query
.