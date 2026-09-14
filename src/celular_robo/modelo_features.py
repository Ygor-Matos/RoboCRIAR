from celular_robo.robo import RoboColetor
from celular_robo.robo_base import Robo
from celular_robo.estrategias import RotaColeta
from celular_robo.excecoes import ConfiguracaoInvalida


TIPOS_VALIDOS = set(Robo._registro)

ESTRATEGIAS_VALIDAS = {
    "direta",
    "dupla_conferencia",
}


REQUER = {
    "fragil": "dupla_conferencia",
    "urgente": "direta",
}


EXCLUI = {
    ("area_quarentena", "direta"),
}


AREAS_VALIDAS = {
    "centro_padrao",
    "area_quarentena",
}


def validar_configuracao(
    tipo_nome,
    estrategia_nome,
    area_nome,
):
    if tipo_nome not in TIPOS_VALIDOS:
        raise ConfiguracaoInvalida(
            f"Tipo de robô inválido: {tipo_nome}"
        )

    if estrategia_nome not in ESTRATEGIAS_VALIDAS:
        raise ConfiguracaoInvalida(
            f"Estratégia inválida: {estrategia_nome}"
        )

    if area_nome not in AREAS_VALIDAS:
        raise ConfiguracaoInvalida(
            f"Área inválida: {area_nome}"
        )

    if (area_nome, estrategia_nome) in EXCLUI:
        raise ConfiguracaoInvalida(
            f"A estratégia {estrategia_nome} não pode "
            f"ser usada na área {area_nome}"
        )

    return True
