
from celular_robo.robo_base import Robo


class QuantidadeValida:
    def __set_name__(self, owner, name):
        self.nome = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self.nome]

    def __set__(self, instance, valor):
        if not isinstance(valor, int):
            raise TypeError("A quantidade deve ser um inteiro.")

        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        quantidade_pedida = getattr(instance, "quantidade_pedida", None)

        if (
            quantidade_pedida is not None
            and valor > quantidade_pedida
        ):
            raise ValueError(
                "A quantidade coletada não pode passar "
                "da quantidade pedida."
            )

        instance.__dict__[self.nome] = valor


from celular_robo.bandeja import Bandeja

class RoboColetor(Robo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bandeja = Bandeja()
        self.pedido_atual = None
        self.quantidade_pedida = None

        from celular_robo.modos import ModoColetando

        self.modo = ModoColetando()

    def __repr__(self):
        return (
            f"RoboColetor("
            f"{self.nome!r}, "
            f"x={self.x}, "
            f"y={self.y}, "
            f"direcao={self.direcao}"
            f")"
        )

    def __str__(self):
        return (
            f"{self.nome} em ({self.x}, {self.y}), "
            f"direção {self.direcao.name}, "
            f"bandeja={self.bandeja}"
        )

    def coletar_item(
        self,
        codinome,
        posicao,
        quantidade,
    ):
        from celular_robo.modos import ModoColetando
        from celular_robo.comandos import ComandoColeta

        if not isinstance(self.modo, ModoColetando):
            print(
                f"{self.nome} não pode iniciar uma coleta "
                "enquanto aguarda verificação."
            )
            return False

        self.quantidade_pedida = quantidade

        comando = ComandoColeta(
            codinome,
            posicao,
            quantidade,
        )

        comando.executar(self)

        self._historico_comandos.append(comando)

        return True

    def processar_pedido(self, pedido):
        from celular_robo.modos import ModoColetando

        if not isinstance(self.modo, ModoColetando):
            print(
                f"{self.nome} não pode processar um novo pedido."
            )
            return False

        self.pedido_atual = pedido

        for item in pedido["itens"]:
            sucesso = self.coletar_item(
                codinome=item["codinome"],
                posicao=tuple(item["posicao"]),
                quantidade=item["quantidade"],
            )

            if not sucesso:
                return False

        return True

    def verificar_bandeja(self):
        if self.pedido_atual is None:
            return False

        if self.bandeja.completa(self.pedido_atual):
            self.notificar(
                "bandeja_pronta",
                pedido=self.pedido_atual,
            )
            return True

        return False

    def aprovar_retirada(self):
        from celular_robo.modos import (
            ModoAguardandoVerificacao,
            ModoColetando,
        )

        if not isinstance(
            self.modo,
            ModoAguardandoVerificacao,
        ):
            print(
                "A bandeja não está aguardando verificação."
            )
            return False

        self.notificar(
            "retirada_aprovada",
            pedido=self.pedido_atual,
        )

        self.bandeja.limpar()
        self.pedido_atual = None
        self.quantidade_pedida = None
        self.modo = ModoColetando()

        return True

    def rejeitar_retirada(self):
        from celular_robo.modos import (
            ModoAguardandoVerificacao,
            ModoColetando,
        )

        if not isinstance(
            self.modo,
            ModoAguardandoVerificacao,
        ):
            print(
                "A bandeja não está aguardando verificação."
            )
            return False

        self.notificar(
            "pedido_rejeitado",
            pedido=self.pedido_atual,
        )

        self.modo = ModoColetando()

        return True
