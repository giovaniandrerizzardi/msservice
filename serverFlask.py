from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField, BooleanField
from processors import interscityManager,mapFuncionalities,isoFunctionalities, model
import json
from collections import namedtuple
from datetime import date, datetime, timedelta
#from js.momentjs import moment
#pip install moment

#import pandas as pd

import numpy as np
import operator

LOGIN_MAP = {}


app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

# Simple form handling using raw HTML forms
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        first_name = request.form['firstname']
        last_name = request.form['lastname']

        # Validate form data
        if len(first_name) == 0 or len(last_name) == 0:
            # Form data failed validation; try again
            error = "Please supply both first and last name"
        else:
            # Form data is valid; move along
            return redirect(url_for('thank_you'))

    # Render the sign-up page
    return render_template('sign-up.html', message=error)

# More powerful approach using WTForms


class RegistrationForm(Form):
    cpf = IntegerField('cpf')
    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    nr_residentes = IntegerField('Nr Residentes')
    corrente_nominal = TextField('Corrente Nominal')
    tensao_nominal = TextField('Tensao Nominal')
    public_building = BooleanField('Edificio Publico')
    latitude = TextField('Latitude')
    longitude = TextField('Longitude')
    cidade = SelectField(u'Programming Language', choices=[
                ('1', 'C++'), ('2', 'Python'), ('text', 'Plain Text')])

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        nr_residentes = form.nr_residentes.data
        corrente_nominal = form.corrente_nominal.data
        tensao_nominal = form.tensao_nominal.data
        public_building = form.public_building.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        cidade = form.cidade.data
        
        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            interscityManager.cadastraRecurso(form,0)
            return redirect(url_for('thank_you'))

    return render_template('register.html', form=form, message=error)

@app.route('/initialMap', methods=['GET'])
def attInitialMap():
    print(round(3.141592653589793, 2))
    #print(mapFuncionalities.initialMapData())
    datajson = [
                    {
                        "uuid": "432f.4234h.423fj4.555f",
                        "event_type": "EVENT_UP",
                        "energy_ativa": "0.9kWh",
                        "voltage_real_rms": "220V",
                        "phase_real_rms": "0.25A",
                        "lat": -28.26278,
                        "lon": -52.40667,
                        "alert_info": "none"
                    },
                    {
                        "uuid": "4324.423423.32423.423.44",
                        "event_type": "EVENT_DOWN",
                        "energy_ativa": "123",
                        "voltage_real_rms": "432",
                        "phase_real_rms": "123",
                        "lat": -28.27278,
                        "lon": -52.40667,
                        "alert_info": "Sobretensão"
                    }
                ]

    return json.dumps(mapFuncionalities.initialMapData())

@app.route('/dashboard1', methods=['GET'])
def attdashboard():
    sec71 = round(isoFunctionalities.func71(''),5)
    sec72 = isoFunctionalities.func72('passo fundo')
    sec73 = isoFunctionalities.func73()
    sec75 = round(isoFunctionalities.func75(),5)
    sec76 = isoFunctionalities.func76()
    sec77 = isoFunctionalities.func77('')
    print('seção 71 = ', sec71)
    print('seção 72 = ',sec72)
    print('seção 73 = ',sec73)
    print('seção 75 = ',sec75)
    print('seção 76 = ',sec76)
    print('seção 77 = ',sec77)
    response = {
        "s71" : sec71,
        "s72" : sec72,
        "s73" : sec73,
        "s75" : sec75,
        "s76" : sec76,
        "s77" : str(sec77)
    }
    
    return response



@app.route('/lasteventmui', methods=['GET'])
def getLastEventmui():
    args = request.args
    print(args)
    socketid = ''
    requestedUuid = ''
    try:
        socketid = args['socketid']
        requestedUuid = args['uuid']
        print(socketid)
        if socketid is '':
            print('socketId is null')
            return '0'
    except Exception:
        print('deu exeção')
        print('buscando uuid do socket id')
        requestedUuid = getUuidFromSocket(socketid)
    return '10'


    dados = interscityManager.getLastDataByUUID(requestedUuid)
    
    specificConsume = 0
    try:
        specificConsume = dados.specific_energy_ativa
    except AttributeError:
        specificConsume = dados.energy_ativa
    specificConsume = 0
    alerta = 'none'
    try:
        alerta = dados.alerta
    except AttributeError:
        print('nao tem alerta')

    datajson = {
        "event_type": dados.Event,
        "energy_ativa": round(dados.energy_ativa, 3),
        "voltage_real_rms": round(dados.rmsVoltage_real,2),
        "phase_real_rms": round(dados.rmsPhase_real,2),
        "alert_type": alerta,
        "specific_energy_ativa": specificConsume,
        #"timestamp": dados.
        "total_energy_daily": round(interscityManager.getDataDaily(requestedUuid),5)
    }
    print(datajson)
    return json.dumps(datajson)




@app.route('/lastevent', methods=['GET'])
def getLastEvent():
    args = request.args
    print(args)
  
    requestedUuid = args['uuid']
    dados = interscityManager.getLastDataByUUID(requestedUuid)
    
    specificConsume = 0
    try:
        specificConsume = dados.specific_energy_ativa
    except AttributeError:
        specificConsume = dados.energy_ativa
    specificConsume = 0
    alerta = 'none'
    try:
        alerta = dados.alerta
    except AttributeError:
        print('nao tem alerta')

    datajson = {
        "event_type": dados.Event,
        "energy_ativa": round(dados.energy_ativa, 3),
        "voltage_real_rms": round(dados.rmsVoltage_real,2),
        "phase_real_rms": round(dados.rmsPhase_real,2),
        "alert_type": alerta,
        "specific_energy_ativa": specificConsume
        #"timestamp": dados.
        #"total_energy_daily": round(interscityManager.getDataDaily(requestedUuid),5)
    }
    print(datajson)
    return json.dumps(datajson)

# object to access data header
class _grafico:
    data = []
    labels = []
    series = []

def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__

@app.route('/attdashboard', methods=['GET'])
def attdashboardgraft():
    args = request.args
    print(args['uuid'])
    print(args['start'])
    print(args['end'])
    print(args['graphType'])

    infoConsumoList = interscityManager.getDataByRange(args['uuid'],args['start'],args['end'])

    if infoConsumoList is 0:
        print('erro no grafico')
        return 'me ajuda'
   
    

    graphType = args['graphType']
    data = []
    labels = []
    series = []
    print(graphType)
    if graphType == 'consumo':
        data,labels,series = generateConsumoType(infoConsumoList)
    elif graphType == 'tensao':
        data,labels,series = generateTensaoType(infoConsumoList)
    elif graphType == 'corrente':
        data,labels,series = generateCorrenteType(infoConsumoList)
        
    
    m = {
        'labels' : labels,
        'data' : [data],
        'series' : series
    }
    
    return m
    #return json.dumps(serialize(grafico))



def generateConsumoType(dados):
    data = []
    labels = []
    series = []
    for s in dados:
        specificConsume = 0
        try:
            specificConsume = s.specific_energy_ativa
        except AttributeError:
            specificConsume = s.energy_ativa

        data.append(round(specificConsume,5))
        labels.append(s.date)
    series.append('Consumo')
    return data,labels,series

def generateTensaoType(dados):
    data = []
    labels = []
    series = []
    for s in dados:
        try:
            data.append(round(s.rmsVoltage_real,2))
            labels.append(s.date)
        except AttributeError:
            print('Nao tem tensao pra esse evento')
    series.append('Tensão V')
    return data,labels,series

def generateCorrenteType(dados):
    data = []
    labels = []
    series = []
    for s in dados:
        try:
            data.append(round(s.rmsPhase_real,2))
            labels.append(s.date)
        except AttributeError:
            print('Nao tem corrente pra esse evento')
       
    series.append('Corrente A')
    return data,labels,series

#@app.route('/dashboard2', methods=['GET'])
def attdashboard2():
    
    #sec77 = isoFunctionalities.func77('')
    infoConsumoList = interscityManager.getDataByRange('9c0772b8-c809-4865-bec7-70dd2013bc37','2019-05-02 00:00:00','2019-11-04 23:59:59')
    grafico = _grafico()
    
    for s in infoConsumoList:
        #print('alo corno ',s.date)
        grafico.data.append(round(s.energy_ativa,5))
        grafico.labels.append(s.date)
    print(grafico)
    print(grafico.data)
    print(grafico.labels)
    return grafico

@app.route('/login', methods=['GET'])
def auth ():
    args = request.args
    print(args['uuid'])
    print(args['socketid'])

    socketId = args['socketid']
    uuid = args['uuid']
    password = args['password']
    try:
        logInfo = model.getByIdAndPass(uuid, password)
        print('retultados: ',logInfo.uuid)
        LOGIN_MAP[socketId] = str(uuid)
        print('login map = ' , LOGIN_MAP)
        print("logado com sucesso")
        return "0"
    except Exception:
        print("Erro")
        return "1"

@app.route('/logout', methods=['GET'])
def logout ():
    args = request.args
    print(args['socketid'])

    socketId = args['socketid']

    try:
        del LOGIN_MAP[socketId]
        print("deslogado com sucesso")
        return "0"
    except Exception:
        print("Erro ao tentar deslogar")
        return "1"



def getUuidFromSocket(socket):
    print(LOGIN_MAP)
    accountLog = LOGIN_MAP.get(socket)
    if accountLog is None:
        print('nada encontrado na lista para o socket' , socket)
        return None
    else:
        return accountLog

#attdashboard2()
# Run the application
app.run(debug=True, port= 4567)
