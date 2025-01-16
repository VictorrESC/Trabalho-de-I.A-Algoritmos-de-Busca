def busca_em_profundidade(estado_inicial, estado_objetivo, gerar_vizinhos):
    """
    Implementação do algoritmo de Busca em Profundidade.

    Parâmetros:
        estado_inicial (tuple): Coordenadas iniciais (x, y).
        estado_objetivo (tuple): Coordenadas objetivo (x, y).
        gerar_vizinhos (function): Função que gera os vizinhos de um estado dado.

    Retorna:
        dict: Um dicionário com informações do resultado da busca.
    """
    # Pilha para armazenar os nós a serem explorados
    pilha = [estado_inicial]

    # Conjunto para evitar visitar estados repetidos
    visitados = set()
    visitados.add(estado_inicial)

    # Dicionário para reconstruir o caminho
    pais = {estado_inicial: None}

    # Contadores de nós gerados e visitados
    nos_gerados = 0
    nos_visitados = 0

    while pilha:
        # Remove o próximo estado da pilha
        estado_atual = pilha.pop()
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
                "custo": len(caminho) - 1,
                "nos_gerados": nos_gerados,
                "nos_visitados": nos_visitados,
            }

        # Gera os vizinhos do estado atual
        for vizinho in gerar_vizinhos(estado_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                pilha.append(vizinho)
                pais[vizinho] = estado_atual
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

# Teste simples
if __name__ == "__main__":
    estado_inicial = (0, 0)
    estado_objetivo = (5, 5)

    resultado = busca_em_profundidade(estado_inicial, estado_objetivo, gerar_vizinhos)

    print("Caminho encontrado:", resultado["caminho"])
    print("Custo do caminho:", resultado["custo"])
    print("Nós gerados:", resultado["nos_gerados"])
    print("Nós visitados:", resultado["nos_visitados"])
