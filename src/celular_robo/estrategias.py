from abc import ABC, abstractmethod


class RotaColeta(ABC):
    _registro_rotas = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        RotaColeta._registro_rotas[cls.__name__] = cls

    @abstractmethod
    def mover(self, robo, localizacao_item):
        ...


class RotaDireta(RotaColeta):
    def mover(self, robo, localizacao_item): 
        alvo_x, alvo_y = localizacao_item

        while robo.x != alvo_x:
            if robo.x < alvo_x:
                robo.girar_ate(
                    type(robo.direcao).LESTE
                )
            else:
                robo.girar_ate(
                    type(robo.direcao).OESTE
                )

            if not robo.avancar():
                return False

        while robo.y != alvo_y:
            if robo.y < alvo_y:
                robo.girar_ate(
                    type(robo.direcao).NORTE
                )
            else:
                robo.girar_ate(
                    type(robo.direcao).SUL
                )

            if not robo.avancar():
                return False

        return robo.posicao == localizacao_item


class RotaComDuplaConferencia(RotaColeta):
    def mover(self, robo, localizacao_item):
        chegou = self._ir_ate(
            robo,
            localizacao_item,
        )

        if not chegou:
            return False

        primeira_conferencia = (
            robo.posicao == localizacao_item
        )

        segunda_conferencia = (
            robo.posicao == localizacao_item
        )

        return (
            primeira_conferencia
            and segunda_conferencia
        )

    def _ir_ate(self, robo, localizacao_item):
        alvo_x, alvo_y = localizacao_item

        while robo.x != alvo_x:
            if robo.x < alvo_x:
                robo.girar_ate(
                    type(robo.direcao).LESTE
                )
            else:
                robo.girar_ate(
                    type(robo.direcao).OESTE
                )

            if not robo.avancar():
                return False

        while robo.y != alvo_y:
            if robo.y < alvo_y:
                robo.girar_ate(
                    type(robo.direcao).NORTE
                )
            else:
                robo.girar_ate(
                    type(robo.direcao).SUL
                )

            if not robo.avancar():
                return False

        return True


ESTRATEGIAS_VALIDAS = set(
    RotaColeta._registro_rotas
)
