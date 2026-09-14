# Hierarquia de exceções — enunciado, Seção 2.5.
#
# TODO: implemente aqui. ErroColeta(Exception) como base;
# ConfiguracaoInvalida(ErroColeta) e PedidoInvalido(ErroColeta) como as duas
# subclasses (ver Seção 2.5 pra critério de qual usar em cada caso).


class ErroColeta(Exception):
    """Erro base do sistema de coleta."""


class ConfiguracaoInvalida(ErroColeta):
    """Erro na configuração do robô."""


class PedidoInvalido(ErroColeta):
    """Erro no conteúdo do pedido."""
