from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField, BooleanField
from processors import interscityManager,mapFuncionalities,isoFunctionalities
import json
from collections import namedtuple
import datetime
#from js.momentjs import moment
#pip install moment


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
            interscityManager.cadastraRecurso(form)
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
    sec71 = isoFunctionalities.func71('')
    sec72 = isoFunctionalities.func72('passo fundo')
    sec73 = isoFunctionalities.func73()
    sec75 = isoFunctionalities.func75()
    sec76 = isoFunctionalities.func76()
   # sec77 = isoFunctionalities.func77('')
    print(sec71)
    print(sec72)
    print(sec73)
    print(sec75)
    print(sec76)
    response = {
        "71" : sec71,
        "72" : sec72,
        "73" : sec73,
        "75" : sec75,
        "76" : sec76,
        "77" : "n ha"
    }
    
    return response


@app.route('/lastEvent', methods=['GET'])
def getLastEvent():
    args = request.args
    print(args['uuid'])
    requestedUuid = args['uuid']
    dados = interscityManager.getLastDataByUUID(requestedUuid)
    datajson = {
        "event_type": dados.Event,
        "energy_ativa": dados.energy_ativa,
        "voltage_real_rms": dados.rmsVoltage_real,
        "phase_real_rms": dados.rmsPhase_real,
        "alert_type": dados.alerta,
        #"timestamp": dados.
        "total_energy_daily": interscityManager.getDataDaily(requestedUuid)
    }

    return datajson

@app.route('/attdashboard', methods=['GET'])
def attdashboardgraft():
    args = request.args
    print(args['uuid'])
    print(args['start'])
    print(args['end'])
    response = 'sdsds'
    #response = interscityManager.getDataByRange(args['uuid'],args['start'],args['end'])
    #jsonBody = json.loads(str(request.json), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
   
    #print(jsonBody)
    
    #dateFrom = jsonBody.dateFrom
    #print(dateFrom)
    #dsd = '1571704042711'
    #print(moment.unix(int(dsd)))
    #dateFrom = time.strftime("%D %H:%M", time.localtime(int("1571093522494")))
    #dateTo = datetime.fromtimestamp(args.get('dateTo'))
    #print(dateFrom)
    return str(response)

# Run the application
app.run(debug=True, port= 4567)
