import mysql.connector


#Função responsavel por estabelecer conexão ao banco de dados
def conectar():
    #passando as informações para conectar ao banco MySQL hostlocal
    try:
        conexao = mysql.connector.connect(
            host="localhost",  
            user="root",    
            password="akitaariel12345!enrique",   
            database="biblioteca"
            )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        return None