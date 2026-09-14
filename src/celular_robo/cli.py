# CLI — enunciado, Seção 4.
#
# TODO: implemente aqui. Menu interativo (ou argparse, à sua escolha):
# listar pedido carregado, processar pedido, ver estado da bandeja,
# aprovar/rejeitar retirada da equipe de testes.
import json
from pathlib import Path

from celular_robo.persistencia import (
    montar_robo_de_config,
    montar_pedido_de_json,
)


CAMINHO_CONFIG = Path(
    "dados/config_robo_exemplo.json"
)

CAMINHO_PEDIDO = Path(
    "dados/pedido_coleta_exemplo.json"
)


def carregar_robo():
    with open(
        CAMINHO_CONFIG,
        "r",
        encoding="utf-8",
    ) as arquivo:
        config = json.load(arquivo)

    return montar_robo_de_config(config)


def mostrar_pedido(pedido):
    print("\n=== PEDIDO ===")
    print(f"Lote: {pedido['lote']}")

    for item in pedido["itens"]:
        print(
            f"- {item['codinome']}: "
            f"{item['quantidade']} unidade(s) "
            f"em {tuple(item['posicao'])} "
            f"(frágil={item['fragil']}, "
            f"urgente={item['urgente']})"
        )


def mostrar_bandeja(robo):
    print("\n=== BANDEJA ===")

    if len(robo.bandeja) == 0:
        print("Bandeja vazia.")
        return

    for item in robo.bandeja:
        print(
            f"- {item.codinome}: "
            f"{item.quantidade}"
        )

    print(
        f"Total de itens: {len(robo.bandeja)}"
    )


def main():
    robo = carregar_robo()
    pedido = montar_pedido_de_json(
        CAMINHO_PEDIDO
    )

    while True:
        print("\n=== ROBÔ COLETOR ===")
        print("1 - Listar pedido")
        print("2 - Processar pedido")
        print("3 - Ver estado da bandeja")
        print("4 - Aprovar retirada")
        print("5 - Rejeitar retirada")
        print("0 - Sair")

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        if opcao == "1":
            mostrar_pedido(pedido)

        elif opcao == "2":
            sucesso = robo.processar_pedido(
                pedido
            )

            if sucesso:
                print(
                    "Pedido processado."
                )

        elif opcao == "3":
            mostrar_bandeja(robo)

        elif opcao == "4":
            if robo.aprovar_retirada():
                print(
                    "Retirada aprovada."
                )

        elif opcao == "5":
            if robo.rejeitar_retirada():
                print(
                    "Retirada rejeitada. "
                    "Os itens permanecem na bandeja."
                )

        elif opcao == "0":
            print("Encerrando.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
