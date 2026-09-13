# Strategy — RotaDireta, RotaComDuplaConferencia — enunciado, Seção 2.3.
# (Não confundir com estrategias_base.py — genérico do curso, não editar. Ao
# contrário de Command/Observer/State, aqui você NÃO herda de `Estrategia`:
# escreva sua própria base, ver TODO abaixo — motivo em estrategias_base.py.)
#
# TODO: implemente aqui. Considere uma base comum (RotaColeta) com
# __init_subclass__ registrando cada rota, ver Seção 2.2 (metaprogramação
# aplicada a uma segunda hierarquia).


from abc import ABC, abstractmethod

from celular_robo.robo_base import Direcao

class RotaColeta(ABC):
    _registro_rotas = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        RotaColeta._registro_rotas[cls.__name__] = cls

    @abstractmethod
    def mover(self, robo, localizacaoItem):
        ...

class RotaDireta(RotaColeta):
    def executar(self, robo, localizacaoItem):
        destino_x, destino_y = localizacaoItem

        atual_x, atual_y = robo.posicao

        if destino_x > atual_x:
            robo.girar_ate(Direcao.LESTE)
            robo.avancar_n(destino_x - atual_x)

        elif destino_x < atual_x:
            robo.girar_ate(Direcao.OESTE)
            robo.avancar_n(atual_x - destino_x)
        
        atual_y = robo.y

        if destino_y > atual_y:
            robo.girar_ate(Direcao.NORTE)
            robo.avancar_n(destino_y - atual_y)

        elif destino_y < atual_y:
            robo.girar_ate(Direcao.SUL)
            robo.avancar_n(atual_y - destino_y)
        #aqui eu realizaria robo.coletar
        return robo.posicao


class RotaComDuplaConferencia(RotaColeta):
    pass
    #ainda não entendi muito bem como implementar rotacomduplaconferencia, pois ainda não sei se
    #  vou usar robo.coletar dentro do método, vou implementar
    #  essa estrategia depois

ESTRATEGIAS_VALIDAS = set(RotaColeta._registro_rotas)
