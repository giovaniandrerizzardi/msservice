from processors import model

def checkForAlert(dados):

    query = model.casa_info.select().where(model.casa_info.uuid == dados.uuid)
    for casa in query:
        
        if float(casa.corrente_nominal)< dados.rmsPhase_real:
            return 'SOBRECORRENTE'
        if float(casa.tensao_nominal)< dados.rmsVoltage_real:
            return 'SOBRETENSÃO'
    return 'none'


