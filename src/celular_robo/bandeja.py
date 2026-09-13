class Bandeja:
    def __init__(self):
        self.itens = {}

    def adicionar(self, codinome, quantidade):
        self.itens[codinome] = quantidade

    def __len__(self):
        return sum(self.itens.values())

    def __repr__(self):
        return f"Bandeja({self.itens!r})"
