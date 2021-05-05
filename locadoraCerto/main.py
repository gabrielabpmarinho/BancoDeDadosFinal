from mysql.connector import connect

query_create_shema = "SHOW SCHEMAS" #SEMPRE USE LETRA MAIUSCULA
params = None

def execute (sql,params = None): # serve para insert,update,delet,create,alter,drop
    with connect(host="localhost", user ="root", password = "ga2468bi", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,params)
            conn.commit()

def query(sql,params = None):# executa comando e retorna resultado
    with connect(host="localhost", user ="root", password = "ga2468bi", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,params)
            return cursor.fetchall() # qnd vou fazer o select tem q retornar algo, ou seja pega os valores q o bd retornou

