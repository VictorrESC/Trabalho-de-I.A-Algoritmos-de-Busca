import heapq

def busca_custo_uniforme(estado_inicial, estado_objetivo, custo_fun, gerar_vizinhos):
    fila_prioridade = [(0, estado_inicial, None, 0)]  # (custo, estado, pai, profundidade)
    visitados = set()
    nos_gerados, nos_visitados = 0, 0
    pilha_busca_custo_uniforme = {estado_inicial: None}
    profundidade_busca_custo_uniforme = {estado_inicial: 0}
    
    while fila_prioridade:
        custo_atual, estado_atual, pai_atual, prof_atual = heapq.heappop(fila_prioridade)
        nos_visitados += 1
        
        if estado_atual == estado_objetivo:
            caminho = []
            custo_total = 0
            while estado_atual is not None:
                caminho.append(estado_atual)
                if pilha_busca_custo_uniforme.get(estado_atual, None) is not None:
                    custo_total += custo_fun(pilha_busca_custo_uniforme[estado_atual], estado_atual, profundidade_busca_custo_uniforme[estado_atual])

                estado_atual = pilha_busca_custo_uniforme.get(estado_atual, None)
            caminho.reverse()
            return {"caminho": caminho, "custo": custo_total, "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}
       
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            for vizinho in gerar_vizinhos(estado_atual):
                if vizinho not in visitados:
                    novo_custo = custo_atual + custo_fun(estado_atual, vizinho, prof_atual+1)
                    heapq.heappush(fila_prioridade, (novo_custo, vizinho, estado_atual, prof_atual + 1))
                    nos_gerados += 1
                    pilha_busca_custo_uniforme[vizinho] = estado_atual
                    profundidade_busca_custo_uniforme[vizinho] = prof_atual+1
    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}