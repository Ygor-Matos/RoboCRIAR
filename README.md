# Robô Coletor de Celulares

## Setup

TODO: como instalar dependências e preparar o ambiente.

## Como rodar

TODO: como rodar a CLI e como rodar `pytest -v`.

## Decisões de projeto

TODO: decisões de design tomadas — em especial onde havia mais de um jeito
razoável de resolver (ex.: qual exceção recusa o conflito `fragil`+`urgente`,
Seção 2.4 do enunciado).
### Bandeja:
A bandeja será implementada como uma classe própria que pertence a RoboColetor
### Exceções:
um pedido com item inválido rejeta tudo, e um item com fragil=True e urgente=True ao mesmo tempo é pedido inválido
### Lote:
O lote disponível é representado por um dict no módulo de persistencia, o JSON informa o nome do lote e esse dict é utilizado para verificar se o codinome existe e se a quantidade solicitada esta disponível


## Mapeamento pra aulas da disciplina

TODO: uma tabela curta ligando cada mecanismo (descriptors, `__init_subclass__`,
os 5 design patterns, LPS, exceções, persistência, testes) ao arquivo/classe
correspondente — facilita a correção.
