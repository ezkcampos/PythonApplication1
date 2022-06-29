from asyncio.log import logger
import logging
from shutil import ExecError
logger = logging.getLogger(__name__)

def calcular_pagamento(qtd_horas, valor_hora):
    try:
        logger.info("entering @calcular_pagamento")
        horas = float(qtd_horas)
        taxa = float(valor_hora)
        if horas <= 40:
            salario=horas*taxa
        else:
            h_excd = horas - 40
            salario = 40*taxa+(h_excd*(1.5*taxa))
        logger.info("Leaving @calcular pagamento")
        return salario
    except Exception as exc:
        logger.exception(f"no mapped error ocurred. {exc}")


print(calcular_pagamento(140,20))