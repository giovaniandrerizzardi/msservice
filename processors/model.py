#pip install pymysql
#pip install peewee

from peewee import MySQLDatabase,CharField,IntegerField,Model,DoubleField,BooleanField,DateTimeField,fn
import datetime
import pymysql

mysql_db = MySQLDatabase('mestrado', user='root', password='root',
                         host='localhost')

        
class casa_info(Model):
    uuid = CharField()
    senha = CharField()
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

class last_event(Model):
    #id_evento = BigAutoField()
    id_evento = DoubleField()
    uuid = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    total_consume = DoubleField()
    have_alert = BooleanField()
    class Meta:
        database = mysql_db




def createTables():
    mysql_db.connect()
    casa_info.create_table()
    city_infos.create_tables()
    consumo_dia.create_table()
    consumo_mes.create_table()
    last_event.create_table()
    mysql_db.close()

def resetTables():
    mysql_db.connect()
    casa_info.drop_table()
    city_infos.drop_table()
    consumo_dia.drop_table()
    consumo_mes.drop_table()

    casa_info.create_table()
    city_infos.create_table()
    consumo_dia.create_table()
    consumo_mes.create_table()
    mysql_db.close()


def addNewCasa(casaUuid, nrResidentes, correnteNominal, publicBuilding):
    mysql_db.connect()
    casa_info.insert(uuid=casaUuid, nr_residentes=nrResidentes, corrente_nominal=correnteNominal ,public_building=publicBuilding)
    casa_info.insert(UUIDField = casaUuid)

def addcasa_info(Uuid, password, nrResidentes, correnteNominal, publicBuilding,tensaoNominal,Nlatitude, Nlongitude,Ncidade):
    mysql_db.connect()
    casa_info.create(uuid=Uuid, senha = password, nr_residentes=nrResidentes, corrente_nominal=correnteNominal, public_building=publicBuilding, tensao_nominal=tensaoNominal, latitude=Nlatitude, longitude=Nlongitude, cidade=Ncidade)
    mysql_db.close()


def add_event(IDEvento,Uuid, TotalConsume, HaveAlert):
    #mysql_db.connect()
    last_event.create(id_evento=IDEvento, uuid=Uuid, total_consume=TotalConsume, have_alert=HaveAlert)
    #mysql_db.close()

#resetTables()
def getMysqlInstance():
    mysql_db.connect()
    return mysql_db
#query = casa_info.select()
#for casa in query:
#    print(casa.nr_residentes)

#city_infos.create(id=1, city='passo fundo', nr_habitantes = 200000)
#addcasa_info('9c0772b8-c809-4865-bec7-70dd2013bc37',3,2,0,220,'123','1234',1)

def getById(uuid):
    mysql_db.connect()
    return casa_info.get_by_id(uuid)
def getByIdAndPass(Suuid,password):
    
    return casa_info.select().where(casa_info.uuid == Suuid, casa_info.senha == password).get()

    #mysql_db.close()


#addcasa_info('d750d04e-b64f-4a56-9b02-6437f795cd84','123456789',1,0.3,1,220,'-28.27278','-52.416669999999996',1)
#addcasa_info('8a571135-9010-4f56-b930-59587de8167a','123456789',6,0.3,1,220,'-28.27278','-52.416669999999996',1)
#addcasa_info('c62824b8-8500-415a-87c8-b4b4906422e5','123456789',8,0.3,1,220,'-28.27278','-52.416669999999996',1)
#addcasa_info('cf7ab1dd-dfc2-400b-b772-d3c3fa4140da','123456789',6,0.3,1,220,'-28.29128','-52.430499999999995',1)