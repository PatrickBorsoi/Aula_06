def funcao_hello_world():
    return "Hello, World!"


funcao_hello_world()


def soma(valor_1, valor_2):
    return valor_1 + valor_2


resultado = soma(2, 3)
# print(resultado)

"""
Valores Padrão e Argumentos Nomeados
"""


def cumprimentar(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")


# cumprimentar(nome="Patrick", mensagem="Bem-vindo")

### EXERCÍCIOS

"""
01 - Calcular Média de Valores em uma lista
"""
from typing import List


# -> = 'Retorno da funcao
def calcular_valores_de_uma_lista(valores: List[float]) -> float:
    return sum(valores) / len(valores)


valores = [1, 2, 3.3, 4, 5]
# print(calcular_valores_de_uma_lista(valores=valores))

"""
02 - Filtrar dados acíma de um Limite
"""


def filtrar_dados_acima_de_um_limite(
    valores: List[float], limite: float
) -> List[float]:
    resultado = []
    for valor in valores:
        if valor >= limite:
            resultado.append(valor)
    return resultado


valores = [2, 4, 6]
limite = 2


# print(filtrar_dados_acima_de_um_limite(valores=valores, limite=limite))


"""
03 - Contar Valores Únicos em uma lista
"""


def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))


# print(contar_valores_unicos(lista=valores))

"""
04 - Converter Celsius para Fahrenheit em uma lista
"""


def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9 / 5) * temp + 32 for temp in temperaturas_celsius]


temperaturas = [32, 22, 40]

# print(celsius_para_fahrenheit(temperaturas))

"""
05 - Calcular Desvio Padrão de uma Lista
"""


def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia**0.5


# print(calcular_desvio_padrao(valores=valores))

"""
06 - Encontrar Valores Ausentes em uma Sequência
"""


def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))


sequencia = [4, 5, 8]
print(encontrar_valores_ausentes(sequencia=sequencia))
