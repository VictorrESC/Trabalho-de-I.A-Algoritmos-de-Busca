import heapq
import math

def busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo, heuristica):

    # Fila de prioridade: (f(n), estado, pai, profundidade)
    fila_prioridade = [(heuristica(estado_inicial, estado_objetivo), estado_inicial, None, 0)]
    visitados = set()
    pais = {estado_inicial: None}
    custos = {estado_inicial: 0}
    profundidades = {estado_inicial: 0} # Keep track of the depth of each state
    nos_gerados = 0
    nos_visitados = 0

    while fila_prioridade:
        _, estado_atual, pai_atual, prof_atual = heapq.heappop(fila_prioridade)
        nos_visitados += 1

        if estado_atual == estado_objetivo:
            caminho = []
            while estado_atual is not None:
                caminho.append(estado_atual)
                estado_atual = pais[estado_atual]
            caminho.reverse()
            return {
                "caminho": caminho,
                "custo": custos[estado_objetivo],
                "nos_gerados": nos_gerados,
                "nos_visitados": nos_visitados,
            }

        if estado_atual in visitados:
            continue
        visitados.add(estado_atual)

        for vizinho in gerar_vizinhos(estado_atual):
            if pai_atual is not None:
                custo_g = custos[estado_atual] + calcular_custo(pai_atual, vizinho, prof_atual+1) # Passando a profundidade para calcular_custo
            else:
                 custo_g = custos[estado_atual] + calcular_custo(estado_atual, vizinho, prof_atual+1)

            custo_h = heuristica(vizinho, estado_objetivo)
            custo_f = custo_g + custo_h
            
            if vizinho not in visitados or custo_g < custos.get(vizinho, float("inf")):
                custos[vizinho] = custo_g
                pais[vizinho] = estado_atual
                profundidades[vizinho] = prof_atual + 1
                heapq.heappush(fila_prioridade, (custo_f, vizinho, estado_atual, prof_atual+1))
                nos_gerados += 1

    return {
        "caminho": None,
        "custo": float("inf"),
        "nos_gerados": nos_gerados,
        "nos_visitados": nos_visitados,
    }


def gerar_vizinhos(estado):
    """
    Gera os vizinhos válidos para um estado dado.

    Parâmetros:
        estado (tuple): Coordenadas atuais (x, y).

    Retorna:
        list: Lista de coordenadas vizinhas.
    """
    x, y = estado
    vizinhos = [
        (x - 1, y),  # Esquerda
        (x + 1, y),  # Direita
        (x, y - 1),  # Abaixo
        (x, y + 1),  # Acima
    ]
    # Filtra vizinhos fora do limite da cidade (0 a 30)
    return [(vx, vy) for vx, vy in vizinhos if 0 <= vx <= 30 and 0 <= vy <= 30]

# Heurísticas
def heuristica_euclidiana(estado, objetivo):
    x1, y1 = estado
    x2, y2 = objetivo
    return 10 * math.sqrt(abs((x1 - x2)) ** 2 + abs((y1 - y2)) ** 2)

def heuristica_manhattan(estado, objetivo):
    x1, y1 = estado
    x2, y2 = objetivo
    return 10 * (abs(x1 - x2) + abs(y1 - y2))