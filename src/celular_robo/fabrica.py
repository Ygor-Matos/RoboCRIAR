# Factory — criar_robo_coletor, criar_robo_configurado — enunciado, Seção 2.3.
# (Ver fabrica_base.py — genérico do curso, não editar: criar_robo("RoboColetor",
# ...) já funciona, pode chamar direto ou usar como modelo.)
#
# TODO: implemente aqui. criar_robo_coletor(tipo_nome, ...) a partir do
# _registro (Seção 2.2); criar_robo_configurado combina isso com a validação do
# modelo de features (Seção 2.4).
#
# Contrato mínimo exigido por tests/test_00_fornecido.py (não altere a
# assinatura abaixo sem também atualizar aquele arquivo):
#
#   criar_robo_configurado(tipo_nome, nome, estrategia_nome=..., area_nome=...)


from celular_robo.robo_base import Robo
from celular_robo.estrategias import (
    RotaDireta,
    RotaComDuplaConferencia,
)
from celular_robo.modelo_features import (
    validar_configuracao,
)
from celular_robo.excecoes import ConfiguracaoInvalida


def criar_robo_coletor(
    tipo_nome,
    nome,
    estrategia_nome="direta",
    area_nome="centro_padrao",
    **kwargs,
):
    if tipo_nome not in Robo._registro:
        raise ConfiguracaoInvalida(
            f"Tipo de robô não registrado: {tipo_nome}"
        )

    classe_robo = Robo._registro[tipo_nome]

    if estrategia_nome == "direta":
        estrategia = RotaDireta()
    elif estrategia_nome == "dupla_conferencia":
        estrategia = RotaComDuplaConferencia()
    else:
        raise ConfiguracaoInvalida(
            f"Estratégia inválida: {estrategia_nome}"
        )

    if area_nome == "centro_padrao":
        obstaculos = {}

    elif area_nome == "area_quarentena":
        obstaculos = {
            (4, 4),
            (4, 5),
            (4, 6),
        }

    else:
        raise ConfiguracaoInvalida(
            f"Área inválida: {area_nome}"
        )

    return classe_robo(
        nome=nome,
        estrategia=estrategia,
        obstaculos=obstaculos,
        **kwargs,
    )


def criar_robo_configurado(
    tipo_nome,
    nome,
    estrategia_nome="direta",
    area_nome="centro_padrao",
    **kwargs,
):
    validar_configuracao(
        tipo_nome,
        estrategia_nome,
        area_nome,
    )

    return criar_robo_coletor(
        tipo_nome=tipo_nome,
        nome=nome,
        estrategia_nome=estrategia_nome,
        area_nome=area_nome,
        **kwargs,
    )
