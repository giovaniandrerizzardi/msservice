#pip install pymysql
#pip install peewee

from peewee import MySQLDatabase,CharField,IntegerField,Model,DoubleField,BooleanField,DateTimeField,fn
import datetime
import pymysql

mysql_db = MySQLDatabase('mestrado', user='root', password='root',
                         host='localhost')

        
class casa_info(Model):
    uuid = CharField()
    nr_residentes = IntegerField()
    corrente_nominal = DoubleField()
    public_building = BooleanField()
    tensao_nominal = DoubleField()
    latitude = CharField()
    longitude = CharField()
    cidade = IntegerField()

    class Meta:
        database = mysql_db

class city_infos(Model):
    city = CharField()
    nr_habitantes = IntegerField()

    class Meta:
        database = mysql_db

class consumo_dia(Model):
    data = DateTimeField(default=datetime.datetime.now)
    consumo = DoubleField()
    class Meta:
        database = mysql_db

class consumo_mes(Model):
    data = DateTimeField(default=datetime.datetime.now)
    consumo = DoubleField()
    class Meta:
        database = mysql_db

class iso_functionalities(Model):
    data = DateTimeField(default=datetime.datetime.now)
    func_one = DoubleField()
    func_two = DoubleField()
    func_three = DoubleField()
    func_five = DoubleField()
    func_six = DoubleField()
    func_seven = DoubleField()
    class Meta:
        database = mysql_db

class last_event(Model):
    uuid = CharField()
    nr_residentes = IntegerField()
    corrente_nominal = DoubleField()
    public_building = BooleanField()
    class Meta:
        database = mysql_db


def createTables():
    mysql_db.connect()
    casa_info.create_table()
    city_infos.create_tables()
    consumo_dia.create_table()
    consumo_mes.create_table()
    iso_functionalities.create_table()
    mysql_db.close()

def resetTables():
    mysql_db.connect()
    casa_info.drop_table()
    city_infos.drop_table()
    consumo_dia.drop_table()
    consumo_mes.drop_table()
    iso_functionalities.drop_table()

    casa_info.create_table()
    city_infos.create_table()
    consumo_dia.create_table()
    consumo_mes.create_table()
    iso_functionalities.create_table()
    mysql_db.close()


def addNewCasa(casaUuid, nrResidentes, correnteNominal, publicBuilding):
    mysql_db.connect()
    casa_info.insert(uuid=casaUuid, nr_residentes=nrResidentes, corrente_nominal=correnteNominal ,public_building=publicBuilding)
    casa_info.insert(UUIDField = casaUuid)

def addcasa_info(Uuid, nrResidentes, correnteNominal, publicBuilding,tensaoNominal,Nlatitude, Nlongitude):
    mysql_db.connect()
    casa_info.create(uuid = Uuid, nr_residentes=nrResidentes, corrente_nominal=correnteNominal ,public_building=publicBuilding, tensao_nominal = tensaoNominal, latitude = Nlatitude, longitude = Nlongitude)
    mysql_db.close()



#resetTables()
#addcasa_info('30b057a1-a28a-4460-8784-77ba0f0801f9',3,2,0,220,'lat:12345#lon:12345')
def getMysqlInstance():
    mysql_db.connect()
    return mysql_db
#query = casa_info.select()
#for casa in query:
#    print(casa.nr_residentes)

#city_infos.create(id=1, city='passo fundo', nr_habitantes = 200000)

def getById(uuid):
    mysql_db.connect()
    return casa_info.get_by_id(uuid)
    #mysql_db.close()