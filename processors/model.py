#pip install pymysql
#pip install peewee

from peewee import *
import datetime
import pymysql

mysql_db = MySQLDatabase('mestrado', user='root', password='root',
                         host='localhost')

        
class casa_info(Model):
    uuid = CharField()
    nr_residentes = IntegerField()
    corrente_nominal = DoubleField()
    public_building = BooleanField()
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
    consumo_dia.create_table()
    consumo_mes.create_table()
    iso_functionalities.create_table()
    mysql_db.close()




def addNewCasa(casaUuid, nrResidentes, correnteNominal, publicBuilding):
    mysql_db.connect()
    casa_info.insert(uuid=casaUuid, nr_residentes=nrResidentes, corrente_nominal=correnteNominal ,public_building=publicBuilding)
    casa_info.insert(UUIDField = casaUuid)

mysql_db.connect()
casa_info.create(uuid = "dsdsadasddddasd", nr_residentes=1, corrente_nominal=11 ,public_building=0)
mysql_db.close()