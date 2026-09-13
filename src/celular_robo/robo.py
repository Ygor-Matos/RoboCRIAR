# RoboColetor + QuantidadeValida — enunciado, Seção 2.1.
#
# `Robo` (posição, __init_subclass__/_registro, avancar/girar, estrategia/modo,
# Observer) já vem pronto em robo_base.py — não precisa reescrever, só importar:
#
#   from celular_robo.robo_base import Robo, Coordenada
#
# TODO: implemente aqui.
# - RoboColetor(Robo): reaproveita Coordenada (x, y) por herança — não precisa
#   redeclarar. Adicione o que for específico da coleta (ex.: bandeja).
# - QuantidadeValida: descriptor novo (mesmo protocolo de Coordenada/Percentual
#   em robo_base.py), validando que a quantidade coletada de um item nunca é
#   negativa nem passa do pedido.
# - __str__/__repr__ (robô) e __len__ (bandeja — quantos itens já coletados).

from celular_robo.robo_base import Direcao, Robo, Coordenada
from bandeja import Bandeja;

class QuantidadeValida:
    def __set_name__(self, owner, name):
        self.nome_publico = name
        self.nome = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.nome]

    def __set__(self, instance, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError(
                f"{self.nome_publico} precisa ser um número"
            )

        if valor < 0:
            raise ValueError(
                f"{self.nome_publico} não pode ser negativa"
            )

        pedido = instance.pedido
        if valor > pedido:
            raise ValueError(
                f"{self.nome_publico}={valor} não pode passar "
                f"do pedido ({pedido})"
            )

        instance.__dict__[self.nome] = valor

class RoboColetor(Robo):
    def __init__(self, nome, pedido, **kwargs):
        super().__init__(nome, **kwargs)
        self.pedido = pedido
        self.bandeja = Bandeja()


    def __repr__(self):
        return (
            f"RoboColetor({self.nome!r}, "
            f"x={self.x}, y={self.y}, "
            f"direcao={self.direcao}, pedido={self.pedido!r})"
        )

    def __str__(self):
        return (
            f"{self.nome} em ({self.x}, {self.y}), "
            f"direção {self.direcao.name}, "
            f"pedido={self.pedido!r}"
        )
