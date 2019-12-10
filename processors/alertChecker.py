from processors import model, environmentVariables

def checkForAlert(dados):

    query = model.casa_info.select().where(model.casa_info.uuid == dados.uuid)
    for casa in query:
        rmsPhase = float(casa.corrente_nominal)
        rmsTensao = float(casa.tensao_nominal)
        #o disjuntor usa o valo maximo de corrente que pode utilizar, no do matheus é 15A
        # entao, se o rmsPhase chegar a 90% de 15A entao é sobrecorrente
        if (rmsPhase + (rmsPhase * environmentVariables.PORCENTAGEM_CORRENTE / 100)) < dados.rmsPhase_real:
            return 'SOBRECORRENTE'
        if (rmsTensao + (rmsTensao * environmentVariables.PORCENTAGEM_TENSAO / 100)) < dados.rmsVoltage_real:
            return 'SOBRETENSÃO'
        if (rmsTensao - (rmsTensao * environmentVariables.PORCENTAGEM_TENSAO / 100)) > dados.rmsVoltage_real:
            return 'SUBTENSÃO'
        if dados.rmsDiff_real > 0.003:
            return 'FUGA'
    return 'none'


