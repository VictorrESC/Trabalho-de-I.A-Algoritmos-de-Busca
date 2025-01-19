import heapq

def busca_gulosa(estado_inicial, estado_objetivo, heuristica, custo_fun, gerar_vizinhos):
    fila_prioridade = [(heuristica(estado_inicial, estado_objetivo), estado_inicial, None, 0)]  # (custo_h, estado, pai)
    visitados = set()
    nos_gerados, nos_visitados = 0, 0
    pilha_busca_gulosa = {estado_inicial: None}
    profundidade_busca_gulosa = {estado_inicial: 0}
    while fila_prioridade:
        custo_h, estado_atual, pai_atual, prof_atual = heapq.heappop(fila_prioridade)
        nos_visitados += 1
        if estado_atual == estado_objetivo:
            caminho = []
            custo = 0
            while estado_atual is not None:
                caminho.append(estado_atual)

                if pilha_busca_gulosa.get(estado_atual, None) is not None:
                   custo += custo_fun(pilha_busca_gulosa[estado_atual], estado_atual, profundidade_busca_gulosa[estado_atual])

                estado_atual = pilha_busca_gulosa.get(estado_atual, None)
            caminho.reverse()
            return {"caminho": caminho, "custo": custo, "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}
        
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            for vizinho in gerar_vizinhos(estado_atual):
                if vizinho not in visitados:
                 heapq.heappush(fila_prioridade, (heuristica(vizinho, estado_objetivo), vizinho, estado_atual, prof_atual+1))
                 nos_gerados += 1
                 pilha_busca_gulosa[vizinho] = estado_atual
                 profundidade_busca_gulosa[vizinho] = prof_atual + 1
    
    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}