import heapq  # Usado para implementar a fila de prioridade

def busca_de_custo_uniforme(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo):
    """
    Implementação do algoritmo de Busca de Custo Uniforme.

    Parâmetros:
        estado_inicial (tuple): Coordenadas iniciais (x, y).
        estado_objetivo (tuple): Coordenadas objetivo (x, y).
        gerar_vizinhos (function): Função que gera os vizinhos de um estado dado.
        calcular_custo (function): Função que calcula o custo para mover entre dois estados.

    Retorna:
        dict: Um dicionário com informações do resultado da busca.
    """
    # Fila de prioridade para armazenar os nós a serem explorados
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, estado_inicial))  # (custo acumulado, estado)
    
    # Conjunto para evitar visitar estados repetidos
    visitados = set()
    
    # Dicionário para reconstruir o caminho
    pais = {estado_inicial: None}
    
    # Dicionário para rastrear o custo acumulado para cada estado
    custos = {estado_inicial: 0}

    # Contadores de nós gerados e visitados
    nos_gerados = 0
    nos_visitados = 0

    while fila_prioridade:
        # Remove o estado com menor custo acumulado
        custo_atual, estado_atual = heapq.heappop(fila_prioridade)
        nos_visitados += 1

        # Verifica se atingiu o objetivo
        if estado_atual == estado_objetivo:
            # Reconstrói o caminho
            caminho = []
            while estado_atual is not None:
                caminho.append(estado_atual)
                estado_atual = pais[estado_atual]
            caminho.reverse()

            return {
                "caminho": caminho,
                "custo": custo_atual,
                "nos_gerados": nos_gerados,
                "nos_visitados": nos_visitados,
            }

        # Evita revisitar estados
        if estado_atual in visitados:
            continue
        visitados.add(estado_atual)

        # Gera os vizinhos do estado atual
        for vizinho in gerar_vizinhos(estado_atual):
            novo_custo = custo_atual + calcular_custo(estado_atual, vizinho)
            if vizinho not in visitados or novo_custo < custos.get(vizinho, float('inf')):
                custos[vizinho] = novo_custo
                pais[vizinho] = estado_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
                nos_gerados += 1

    # Caso nenhum caminho seja encontrado
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
    estado_objetivo = (5, 5)

    resultado = busca_de_custo_uniforme(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo)

    print("Caminho encontrado:", resultado["caminho"])
    print("Custo do caminho:", resultado["custo"])
    print("Nós gerados:", resultado["nos_gerados"])
    print("Nós visitados:", resultado["nos_visitados"])
