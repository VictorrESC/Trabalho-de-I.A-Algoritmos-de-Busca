import heapq
import math
from collections import deque

# Funções de custo
def custo_c1(estado_atual, vizinho, profundidade):
    return 10

def custo_c2(estado_atual, vizinho, profundidade):
    return 10 if estado_atual[0] == vizinho[0] else 15

def custo_c3(estado_atual, vizinho, profundidade):
    return 10 if estado_atual[0] == vizinho[0] else 10 + (abs(5 - profundidade) % 6)

def custo_c4(estado_atual, vizinho, profundidade):
    return 10 if estado_atual[0] == vizinho[0] else 5 + (abs(10 - profundidade) % 11)

# Heurísticas
def heuristica_euclidiana(estado, objetivo):
    x1, y1 = estado
    x2, y2 = objetivo
    return 10 * math.sqrt(abs((x1 - x2)) ** 2 + abs((y1 - y2)) ** 2)

def heuristica_manhattan(estado, objetivo):
    x1, y1 = estado
    x2, y2 = objetivo
    return 10 * (abs(x1 - x2) + abs(y1 - y2))

# Função de geração de vizinhos
def gerar_vizinhos(estado):
    x, y = estado
    vizinhos = [
        (x - 1, y),  # Esquerda
        (x + 1, y),  # Direita
        (x, y - 1),  # Abaixo
        (x, y + 1),  # Acima
    ]
    return [(vx, vy) for vx, vy in vizinhos if 0 <= vx <= 30 and 0 <= vy <= 30]

# Função para salvar resultados no arquivo
def salvar_resultados(nome_algoritmo, resultado, cenarios_custo, arquivo):
    with open(arquivo, "a") as f:
        f.write(f"Algoritmo: {nome_algoritmo}\n")
        f.write(f"Cenário de custo: {cenarios_custo}\n")
        f.write(f"Custo do caminho: {resultado['custo']}\n")
        f.write(f"Nós gerados: {resultado['nos_gerados']}\n")
        f.write(f"Nós visitados: {resultado['nos_visitados']}\n")
        caminho = resultado['caminho']
        f.write(f"Caminho encontrado: {caminho[:5]}{'...' if len(caminho) > 5 else ''}\n")
        f.write("\n")

# Algoritmos de busca (adapte o restante conforme necessário)
def busca_em_largura(estado_inicial, estado_objetivo, gerar_vizinhos):
    fila = deque([estado_inicial])
    visitados = set()
    visitados.add(estado_inicial)
    pais = {estado_inicial: None}
    profundidade = {estado_inicial: 0}
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
                profundidade[vizinho] = profundidade[estado_atual] + 1
                nos_gerados += 1

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Busca em Profundidade
def busca_em_profundidade(estado_inicial, estado_objetivo, gerar_vizinhos):
    pilha = [estado_inicial]
    visitados = set()
    visitados.add(estado_inicial)
    pais = {estado_inicial: None}
    profundidade = {estado_inicial: 0}
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
                profundidade[vizinho] = profundidade[estado_atual] + 1
                nos_gerados += 1

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Busca de Custo Uniforme
def busca_de_custo_uniforme(estado_inicial, estado_objetivo, gerar_vizinhos, calcular_custo):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, estado_inicial))
    visitados = set()
    pais = {estado_inicial: None}
    custos = {estado_inicial: 0}
    profundidade = {estado_inicial: 0}
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
            novo_custo = custo_atual + calcular_custo(estado_atual, vizinho, profundidade[estado_atual])
            if vizinho not in visitados or novo_custo < custos.get(vizinho, float("inf")):
                custos[vizinho] = novo_custo
                profundidade[vizinho] = profundidade[estado_atual] + 1
                pais[vizinho] = estado_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
                nos_gerados += 1

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Busca A*
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
    profundidade = {estado_inicial: 0}
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
            custo_g = custos[estado_atual] + calcular_custo(estado_atual, vizinho, profundidade[estado_atual])
            custo_h = heuristica(vizinho, estado_objetivo)
            custo_f = custo_g + custo_h
            if vizinho not in visitados or custo_g < custos.get(vizinho, float("inf")):
                custos[vizinho] = custo_g
                profundidade[vizinho] = profundidade[estado_atual] + 1
                pais[vizinho] = estado_atual
                heapq.heappush(fila_prioridade, (custo_f, vizinho))
                nos_gerados += 1

    return {"caminho": None, "custo": float("inf"), "nos_gerados": nos_gerados, "nos_visitados": nos_visitados}

# Função principal
def main():
    estado_inicial = (0, 0)
    estado_objetivo = (5, 5)
    cenarios_custo = [custo_c1, custo_c2, custo_c3, custo_c4]
    arquivo_resultados = "resultados_busca.txt"

    # Limpa o arquivo de resultados
    with open(arquivo_resultados, "w") as f:
        f.write("Resultados das buscas:\n\n")

    for i, custo_func in enumerate(cenarios_custo, start=1):
        print(f"\n--- Cenário C{i} ---")

        with open(arquivo_resultados, "a") as f:
            f.write(f"\n==== Cenário C{i} ====" + "\n")
        
        resultado_largura = busca_em_largura(estado_inicial, estado_objetivo, gerar_vizinhos)
        print(f"Busca em Largura: Custo: {resultado_largura['custo']}, Nós Gerados: {resultado_largura['nos_gerados']}, Nós Visitados: {resultado_largura['nos_visitados']}")
        salvar_resultados("Busca em Largura", resultado_largura, f"C{i}", arquivo_resultados)

        resultado_profundidade = busca_em_profundidade(estado_inicial, estado_objetivo, gerar_vizinhos)
        print(f"Busca em Profundidade: Custo: {resultado_profundidade['custo']}, Nós Gerados: {resultado_profundidade['nos_gerados']}, Nós Visitados: {resultado_profundidade['nos_visitados']}")
        salvar_resultados("Busca em Profundidade", resultado_profundidade, f"C{i}", arquivo_resultados)

        resultado_custo_uniforme = busca_de_custo_uniforme(estado_inicial, estado_objetivo, gerar_vizinhos, custo_func)
        print(f"Busca de Custo Uniforme: Custo: {resultado_custo_uniforme['custo']}, Nós Gerados: {resultado_custo_uniforme['nos_gerados']}, Nós Visitados: {resultado_custo_uniforme['nos_visitados']}")
        salvar_resultados("Busca de Custo Uniforme", resultado_custo_uniforme, f"C{i}", arquivo_resultados)

        resultado_a_estrela = busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, custo_func, "manhattan")
        print(f"Busca A*: Custo: {resultado_a_estrela['custo']}, Nós Gerados: {resultado_a_estrela['nos_gerados']}, Nós Visitados: {resultado_a_estrela['nos_visitados']}")
        salvar_resultados("Busca A*", resultado_a_estrela, f"C{i}", arquivo_resultados)

        resultado_a_estrela_euclidiana = busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, custo_func, "euclidiana")
        print(f"Busca A* (Euclidiana): Custo: {resultado_a_estrela_euclidiana['custo']}, Nós Gerados: {resultado_a_estrela_euclidiana['nos_gerados']}, Nós Visitados: {resultado_a_estrela_euclidiana['nos_visitados']}")
        salvar_resultados("Busca A* (Euclidiana)", resultado_a_estrela_euclidiana, f"C{i}", arquivo_resultados)        

if __name__ == "__main__":
    main()
