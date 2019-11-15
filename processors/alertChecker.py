from processors import model, environmentVariables

def checkForAlert(dados):

    query = model.casa_info.select().where(model.casa_info.uuid == dados.uuid)
    for casa in query:
        rmsPhase = float(casa.corrente_nominal)
        rmsTensao = float(casa.tensao_nominal)
        if (rmsPhase + (rmsPhase * environmentVariables.PORCENTAGEM_CORRENTE / 100)) < dados.rmsPhase_real:
            return 'SOBRECORRENTE'
        if (rmsTensao + (rmsTensao * environmentVariables.PORCENTAGEM_TENSAO / 100)) < dados.rmsVoltage_real:
            return 'SOBRETENSÃO'
        if (rmsTensao - (rmsTensao * environmentVariables.PORCENTAGEM_TENSAO / 100)) > dados.rmsVoltage_real:
            return 'SUBTENSÃO'
    return 'none'


