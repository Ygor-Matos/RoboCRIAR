from celular_robo.comandos_base import Comando


class ComandoColeta(Comando):
    def __init__(
        self,
        codinome,
        posicao,
        quantidade,
    ):
        self.codinome = codinome
        self.posicao = tuple(posicao)
        self.quantidade = quantidade
        self._executado = False

    def executar(self, robo):
        chegou = robo.estrategia.mover(
            robo,
            self.posicao,
        )

        if not chegou:
            raise RuntimeError(
                f"Não foi possível chegar ao item "
                f"{self.codinome}."
            )

        robo.bandeja.adicionar(
            self.codinome,
            self.quantidade,
            self.quantidade,
        )

        self._executado = True

        robo.notificar(
            "coleta",
            codinome=self.codinome,
            posicao=self.posicao,
            quantidade=self.quantidade,
        )

        robo.verificar_bandeja()

    def desfazer(self, robo):
        if not self._executado:
            return

        robo.bandeja.remover(
            self.codinome,
            self.quantidade,
        )

        self._executado = False

        robo.notificar(
            "coleta_desfeita",
            codinome=self.codinome,
            posicao=self.posicao,
            quantidade=self.quantidade,
        )

    def __repr__(self):
        return (
            f"ComandoColeta("
            f"{self.codinome!r}, "
            f"posicao={self.posicao}, "
            f"quantidade={self.quantidade}"
            f")"
        )
