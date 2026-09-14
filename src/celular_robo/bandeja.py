from celular_robo.robo import QuantidadeValida


class ItemBandeja:
    quantidade = QuantidadeValida()

    def __init__(self, codinome, quantidade_pedida):
        self.codinome = codinome
        self.quantidade_pedida = quantidade_pedida
        self.quantidade = 0

    def adicionar(self, quantidade):
        self.quantidade = self.quantidade + quantidade

    def remover(self, quantidade):
        nova_quantidade = self.quantidade - quantidade

        if nova_quantidade < 0:
            raise ValueError(
                "Não é possível remover mais itens do que foram coletados."
            )

        self.quantidade = nova_quantidade

    def __repr__(self):
        return (
            f"ItemBandeja("
            f"{self.codinome!r}, "
            f"quantidade={self.quantidade}, "
            f"pedido={self.quantidade_pedida}"
            f")"
        )


class Bandeja:
    def __init__(self):
        self.itens = {}

    def adicionar(self, codinome, quantidade, quantidade_pedida):
        if codinome not in self.itens:
            self.itens[codinome] = ItemBandeja(
                codinome,
                quantidade_pedida,
            )

        self.itens[codinome].adicionar(quantidade)

    def remover(self, codinome, quantidade):
        if codinome not in self.itens:
            return

        item = self.itens[codinome]
        item.remover(quantidade)

        if item.quantidade == 0:
            del self.itens[codinome]

    def limpar(self):
        self.itens.clear()

    def quantidade_de(self, codinome):
        if codinome not in self.itens:
            return 0

        return self.itens[codinome].quantidade

    def completa(self, pedido):
        for item in pedido["itens"]:
            codinome = item["codinome"]
            quantidade = item["quantidade"]

            if self.quantidade_de(codinome) < quantidade:
                return False

        return True

    def __len__(self):
        return sum(
            item.quantidade
            for item in self.itens.values()
        )

    def __iter__(self):
        return iter(self.itens.values())

    def __repr__(self):
        return f"Bandeja({self.itens!r})"

    def __str__(self):
        if not self.itens:
            return "Bandeja vazia"

        partes = [
            f"{item.codinome}: {item.quantidade}"
            for item in self.itens.values()
        ]

        return "Bandeja(" + ", ".join(partes) + ")"

