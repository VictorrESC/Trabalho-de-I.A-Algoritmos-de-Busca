def busca_em_profundidade(estado_inicial, estado_objetivo, custo_fun, gerar_vizinhos):
    pilha = [(estado_inicial, None, 0)]
    visitados = set()
    nos_gerados = 0
    nos_visitados = 0
    pilha_busca_profundidade = {}
    profundidade_busca_profundidade = {}
    while pilha:
        estado_atual, pai_atual, prof_atual = pilha.pop()
        nos_visitados += 1
        if estado_atual == estado_objetivo:
             caminho = []
             custo = 0
             while estado_atual is not None:
                caminho.append(estado_atual)

                if pilha_busca_profundidade.get(estado_atual, None) is not None:
                   custo += custo_fun(pilha_busca_profundidade[estado_atual], estado_atual, profundidade_busca_profundidade[estado_atual])

                estado_atual = pilha_busca_profundidade.get(estado_atual, None)

             caminho.reverse()
             return {"caminho": caminho, "custo": custo, "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

        if estado_atual not in visitados:
            visitados.add(estado_atual)
            
            for vizinho in gerar_vizinhos(estado_atual):
                if vizinho not in visitados:
                    pilha.append((vizinho, estado_atual, prof_atual+1))
                    nos_gerados += 1
                    pilha_busca_profundidade[vizinho] = estado_atual
                    profundidade_busca_profundidade[vizinho] = prof_atual

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}