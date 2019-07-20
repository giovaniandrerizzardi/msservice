#pip install mysql-connector
#pip install peewee
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
    "CREATE TABLE casa_info (uuid VARCHAR(255), nr_residentes numeric(10), corrente_nominal numeric(10), public_building booelan, primary key (uuid))")
mycursor.execute(
    "CREATE TABLE consumoDia (data date, consumo numeric(10))")
mycursor.execute(
    "CREATE TABLE ConsumoMes (data date, consumo numeric(10))")

mycursor.execute(
    "CREATE TABLE iso_functionalities (data date, 7.1 numeric(10),7.2 numeric(10), 7.3 numeric(10), 7.5 numeric(10),7.6 numeric(10),7.7 numeric(10) )")

#insere dados
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()


print(mydb)
