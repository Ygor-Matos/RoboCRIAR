# Configuração e persistência — enunciado, Seção 2.6.
#
# TODO: implemente aqui. montar_robo_de_config(config) e
# montar_pedido_de_json(caminho) — mesmo par de funções do capstone do curso
# (montar_robo_de_config/montar_frota_de_json), adaptado: um arquivo
# configura o robô (tipo, estratégia, área), outro traz o pedido de coleta.
import json

from celular_robo.excecoes import PedidoInvalido
from celular_robo.fabrica import criar_robo_configurado


# Lote disponível no laboratório.
# O JSON do pedido informa apenas o nome do lote.
import json

from celular_robo.excecoes import PedidoInvalido
from celular_robo.fabrica import criar_robo_configurado


LOTE_DISPONIVEL = {
    "Projeto Aurora": 10,
    "Projeto Vesper": 5,
    "Projeto Eclipse": 8,
    "Projeto Orion": 4,
}


def montar_robo_de_config(config):
    return criar_robo_configurado(
        tipo_nome=config["tipo_nome"],
        nome=config["nome"],
        estrategia_nome=config["estrategia_nome"],
        area_nome=config["area_nome"],
    )


def validar_item(item):
    campos_obrigatorios = {
        "codinome",
        "quantidade",
        "posicao",
        "fragil",
        "urgente",
    }

    if not campos_obrigatorios.issubset(item):
        raise PedidoInvalido(
            "Item possui campos obrigatórios ausentes."
        )

    codinome = item["codinome"]
    quantidade = item["quantidade"]

    if codinome not in LOTE_DISPONIVEL:
        raise PedidoInvalido(
            f"Codinome inexistente no lote: {codinome}"
        )

    if not isinstance(quantidade, int):
        raise PedidoInvalido(
            "A quantidade deve ser um inteiro."
        )

    if quantidade <= 0:
        raise PedidoInvalido(
            "A quantidade deve ser maior que zero."
        )

    if quantidade > LOTE_DISPONIVEL[codinome]:
        raise PedidoInvalido(
            f"Quantidade solicitada de {codinome} "
            "é maior que a disponível."
        )

    if (
        item["fragil"]
        and item["urgente"]
    ):
        raise PedidoInvalido(
            f"O item {codinome} não pode ser "
            "frágil e urgente ao mesmo tempo."
        )


def validar_pedido(pedido):
    if not isinstance(pedido, dict):
        raise PedidoInvalido(
            "O pedido precisa ser um dicionário."
        )

    if "lote" not in pedido:
        raise PedidoInvalido(
            "O pedido não possui lote."
        )

    if "itens" not in pedido:
        raise PedidoInvalido(
            "O pedido não possui itens."
        )

    itens = pedido["itens"]

    if not itens:
        raise PedidoInvalido(
            "O pedido não pode estar vazio."
        )

    for item in itens:
        validar_item(item)

    possui_urgente = any(
        item["urgente"]
        for item in itens
    )

    possui_fragil = any(
        item["fragil"]
        for item in itens
    )

    if possui_urgente and possui_fragil:
        raise PedidoInvalido(
            "O pedido não pode possuir itens "
            "urgentes e frágeis ao mesmo tempo."
        )

    return pedido


def montar_pedido_de_json(caminho):
    with open(
        caminho,
        "r",
        encoding="utf-8",
    ) as arquivo:
        pedido = json.load(arquivo)

    return validar_pedido(pedido)
