#pip install mysql-connector
import mysql.connector
#cria conexao
mydb = mysql.connector.connect(
    user='root', 
    password='root',
    host='localhost', 
    database='mestrado',
)

mycursor = mydb.cursor() 

#cria database
#mycursor.execute("CREATE DATABASE mestrado")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
mycursor.execute("use mestrado")
#cria tabela
mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


#insere dados
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()


print(mydb)
