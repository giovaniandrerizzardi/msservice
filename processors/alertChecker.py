from processors import model

def checkForAlert(dados):

    query = model.casa_info.select().where(model.casa_info.uuid == dados.uuid)
    for casa in query:
        rmsPhase = float(casa.corrente_nominal)
        rmsTensao = float(casa.tensao_nominal)
        if (rmsPhase + (rmsPhase * 5 / 100)) < dados.rmsPhase_real:
            return 'SOBRECORRENTE'
        if (rmsTensao + (rmsTensao * 5 / 100)) > dados.rmsVoltage_real:
            return 'SOBRETENSÃO'
        if (rmsTensao - (rmsTensao * 5 / 100)) < dados.rmsVoltage_real:
            return 'SUBTENSÃO'
    return 'none'


