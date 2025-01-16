import heapq  # Usado para filas de prioridade
import math
from collections import deque

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

def heuristica_euclidiana(estado, objetivo):
    """
    Calcula a heurística baseada na distância Euclidiana.

    Parâmetros:
        estado (tuple): Coordenadas atuais (x, y).
        objetivo (tuple): Coordenadas do objetivo (x, y).

    Retorna:
        float: O valor heurístico.
    """
    x1, y1 = estado
    x2, y2 = objetivo
    return 10 * math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def heuristica_manhattan(estado, objetivo):
    """
    Calcula a heurística baseada na distância de Manhattan.

    Parâmetros:
        estado (tuple): Coordenadas atuais (x, y).
        objetivo (tuple): Coordenadas do objetivo (x, y).

    Retorna:
        float: O valor heurístico.
    """
    x1, y1 = estado
    x2, y2 = objetivo
    return 10 * (abs(x1 - x2) + abs(y1 - y2))

# Algoritmo: Busca em Largura
def busca_em_largura(estado_inicial, estado_objetivo, gerar_vizinhos):
    fila = deque([estado_inicial])
    visitados = set()
    visitados.add(estado_inicial)
    pais = {estado_inicial: None}
    nos_gerados, nos_visitados = 0, 0

    while fila:
        estado_atual = fila.popleft()
        nos_visitados += 1
        if estado_atual == estado_objetivo:
            caminho = []
            while estado_atual is not None:
                caminho.append(estado_atual)
                estado_atual = pais[estado_atual]
            caminho.reverse()
            return {"caminho": caminho, "custo": len(caminho) - 1, "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

        for vizinho in gerar_vizinhos(estado_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                pais[vizinho] = estado_atual
                nos_gerados += 1

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Algoritmo: Busca em Profundidade
def busca_em_profundidade(estado_inicial, estado_objetivo, gerar_vizinhos):
    pilha = [estado_inicial]
    visitados = set()
    visitados.add(estado_inicial)
    pais = {estado_inicial: None}
    nos_gerados, nos_visitados = 0, 0

    while pilha:
        estado_atual = pilha.pop()
        nos_visitados += 1
        if estado_atual == estado_objetivo:
            caminho = []
            while estado_atual is not None:
                caminho.append(estado_atual)
                estado_atual = pais[estado_atual]
            caminho.reverse()
            return {"caminho": caminho, "custo": len(caminho) - 1, "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

        for vizinho in gerar_vizinhos(estado_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                pilha.append(vizinho)
                pais[vizinho] = estado_atual
                nos_gerados += 1

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Algoritmo: Busca de Custo Uniforme
def busca_de_custo_uniforme(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, estado_inicial))
    visitados = set()
    pais = {estado_inicial: None}
    custos = {estado_inicial: 0}
    nos_gerados, nos_visitados = 0, 0

    while fila_prioridade:
        custo_atual, estado_atual = heapq.heappop(fila_prioridade)
        nos_visitados += 1

        if estado_atual == estado_objetivo:
            caminho = []
            while estado_atual is not None:
                caminho.append(estado_atual)
                estado_atual = pais[estado_atual]
            caminho.reverse()
            return {"caminho": caminho, "custo": custo_atual, "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

        if estado_atual in visitados:
            continue
        visitados.add(estado_atual)

        for vizinho in gerar_vizinhos(estado_atual):
            novo_custo = custo_atual + calcular_custo(estado_atual, vizinho)
            if vizinho not in visitados or novo_custo < custos.get(vizinho, float("inf")):
                custos[vizinho] = novo_custo
                pais[vizinho] = estado_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
                nos_gerados += 1

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Algoritmo: Busca A*
def busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo, tipo_heuristica="manhattan"):
    if tipo_heuristica == "euclidiana":
        heuristica = heuristica_euclidiana
    elif tipo_heuristica == "manhattan":
        heuristica = heuristica_manhattan
    else:
        raise ValueError("Heurística inválida.")

    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, estado_inicial))
    visitados = set()
    pais = {estado_inicial: None}
    custos = {estado_inicial: 0}
    nos_gerados, nos_visitados = 0, 0

    while fila_prioridade:
        _, estado_atual = heapq.heappop(fila_prioridade)
        nos_visitados += 1

        if estado_atual == estado_objetivo:
            caminho = []
            while estado_atual is not None:
                caminho.append(estado_atual)
                estado_atual = pais[estado_atual]
            caminho.reverse()
            return {"caminho": caminho, "custo": custos[estado_objetivo], "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

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

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Função principal
def main():
    estado_inicial = (0, 0)
    estado_objetivo = (5, 5)

    print("Busca em Largura:")
    print(busca_em_largura(estado_inicial, estado_objetivo, gerar_vizinhos))

    print("\nBusca em Profundidade:")
    print(busca_em_profundidade(estado_inicial, estado_objetivo, gerar_vizinhos))

    print("\nBusca de Custo Uniforme:")
    print(busca_de_custo_uniforme(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo))

    print("\nBusca A* (Heurística Manhattan):")
    print(busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo, "manhattan"))

    print("\nBusca A* (Heurística Euclidiana):")
    print(busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo, "euclidiana"))

if __name__ == "__main__":
    main()
