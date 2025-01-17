from collections import deque

def busca_em_largura(estado_inicial, estado_objetivo, custo_fun, gerar_vizinhos):
    fila = deque([estado_inicial])
    visitados = {estado_inicial}
    pais = {estado_inicial: None}
    profundidade = {estado_inicial: 0}
    nos_gerados = 0
    nos_visitados = 0
    
    while fila:
        estado_atual = fila.popleft()
        nos_visitados +=1
        
        if estado_atual == estado_objetivo:
            caminho = []
            custo = 0
            while estado_atual is not None:
                caminho.append(estado_atual)
                
                if pais[estado_atual] is not None:
                   custo += custo_fun(pais[estado_atual], estado_atual, profundidade[estado_atual])
                
                estado_atual = pais[estado_atual]
            
            caminho.reverse()
            return {"caminho": caminho, "custo": custo, "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}
        
        
        for vizinho in gerar_vizinhos(estado_atual):
             if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                pais[vizinho] = estado_atual
                profundidade[vizinho] = profundidade[estado_atual] + 1
                nos_gerados += 1
           
    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}