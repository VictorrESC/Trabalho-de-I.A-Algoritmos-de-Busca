import heapq  # Usado para implementar a fila de prioridade
import math   # Necessário para cálculos de raiz quadrada

def busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo, tipo_heuristica="manhattan"):
    """
    Implementação do algoritmo A* com heurísticas.

    Parâmetros:
        estado_inicial (tuple): Coordenadas iniciais (x, y).
        estado_objetivo (tuple): Coordenadas objetivo (x, y).
        gerar_vizinhos (function): Função que gera os vizinhos de um estado dado.
        calcular_custo (function): Função que calcula o custo para mover entre dois estados.
        tipo_heuristica (str): Tipo de heurística ("manhattan" ou "euclidiana").

    Retorna:
        dict: Um dicionário com informações do resultado da busca.
    """
    # Escolha da heurística
    if tipo_heuristica == "euclidiana":
        def heuristica(estado, objetivo):
            x1, y1 = estado
            x2, y2 = objetivo
            return 10 * math.sqrt(abs((x1 - x2)) ** 2 + abs((y1 - y2)) ** 2)
    elif tipo_heuristica == "manhattan":
        def heuristica(estado, objetivo):
            x1, y1 = estado
            x2, y2 = objetivo
            return 10 * (abs(x1 - x2) + abs(y1 - y2))
    else:
        raise ValueError("Heurística inválida. Escolha 'manhattan' ou 'euclidiana'.")

    # Fila de prioridade
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, estado_inicial))  # (f(n), estado)

    visitados = set()
    pais = {estado_inicial: None}
    custos = {estado_inicial: 0}
    nos_gerados = 0
    nos_visitados = 0

    while fila_prioridade:
        _, estado_atual = heapq.heappop(fila_prioridade)
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
            custo_g = custos[estado_atual] + calcular_custo(estado_atual, vizinho)
            custo_h = heuristica(vizinho, estado_objetivo)
            custo_f = custo_g + custo_h

            if vizinho not in visitados or custo_g < custos.get(vizinho, float("inf")):
                custos[vizinho] = custo_g
                pais[vizinho] = estado_atual
                heapq.heappush(fila_prioridade, (custo_f, vizinho))
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

def calcular_custo(estado_atual, vizinho):
    """
    Calcula o custo de mover de um estado para outro.

    Parâmetros:
        estado_atual (tuple): Coordenadas atuais (x, y).
        vizinho (tuple): Coordenadas do vizinho (x, y).

    Retorna:
        int: O custo da ação.
    """
    return 10  # Exemplo: custo constante

# Teste simples
if __name__ == "__main__":
    estado_inicial = (0, 0)
    estado_objetivo = (7, 20)

    resultado = busca_a_estrela(
        estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo, tipo_heuristica="euclidiana"
    )

    print("Caminho encontrado:", resultado["caminho"])
    print("Custo do caminho:", resultado["custo"])
    print("Nós gerados:", resultado["nos_gerados"])
    print("Nós visitados:", resultado["nos_visitados"])
