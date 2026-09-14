# Observer — EquipeDeTestes, RegistroAuditoria — enunciado, Seção 2.3.
#
# Herde de `Observador` (observadores_base.py — ABC com registro automático):
#
#   from celular_robo.observadores_base import Observador
#
# TODO: implemente aqui. EquipeDeTestes(Observador) reage a "bandeja_pronta";
# RegistroAuditoria(Observador) loga todo evento (coleta, bandeja pronta,
# pedido rejeitado), pensando em trilha de auditoria, não só depuração.

from celular_robo.observadores_base import Observador
from celular_robo.modos import (
    ModoAguardandoVerificacao,
    ModoColetando,
)


class EquipeDeTestes(Observador):
    def atualizar(self, evento, **dados):
        robo = dados["robo"]

        if evento == "bandeja_pronta":
            print(
                f"[EQUIPE] Bandeja do robô "
                f"{robo.nome} está pronta para verificação."
            )

            robo.modo = ModoAguardandoVerificacao()


class RegistroAuditoria(Observador):
    def __init__(self):
        self.eventos = []

    def atualizar(self, evento, **dados):
        if evento in {
            "coleta",
            "bandeja_pronta",
            "pedido_rejeitado",
        }:
            self.eventos.append(
                {
                    "evento": evento,
                    "dados": dados,
                }
            )
