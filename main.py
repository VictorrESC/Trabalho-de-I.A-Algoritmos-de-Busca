import random
import time
from busca_em_largura import busca_em_largura
from busca_em_profundidade import busca_em_profundidade
from custo_uniforme import busca_custo_uniforme
from busca_gulosa import busca_gulosa
from a_estrela import busca_a_estrela, heuristica_euclidiana, heuristica_manhattan, gerar_vizinhos

# Funções de custo
def custo_c1(estado_atual, vizinho, profundidade):
    return 10

def custo_c2(estado_atual, vizinho, profundidade):
    return 10 if estado_atual[0] == vizinho[0] else 15

def custo_c3(estado_atual, vizinho, profundidade):
    return 10 if estado_atual[0] == vizinho[0] else 10 + (abs(15 - profundidade) % 6)

def custo_c4(estado_atual, vizinho, profundidade):
    return 10 if estado_atual[0] == vizinho[0] else 5 + (abs(10 - profundidade) % 11)

# Função de geração de vizinhos
def gerar_vizinhos_aleatorios(estado):
    vizinhos = gerar_vizinhos(estado)
    random.shuffle(vizinhos)
    return vizinhos

# Função para salvar resultados no arquivo
def salvar_resultados(nome_algoritmo, resultado, custo_fun, heuristica, arquivo, estados_farmacias = None):
    with open(arquivo, "a") as f:
        f.write(f"Algoritmo: {nome_algoritmo}\n")
        f.write(f"Funcao de Custo: {custo_fun.__name__ if custo_fun else 'N/A'}\n")
        f.write(f"Funcao Heuristica: {heuristica.__name__ if heuristica else 'N/A'}\n")
        if estados_farmacias:
            f.write(f"Farmacias: {estados_farmacias}\n")
        f.write(f"Custo do caminho: {resultado['custo']}\n")
        f.write(f"Nos gerados: {resultado['nos_gerados']}\n")
        f.write(f"Nos visitados: {resultado['nos_visitados']}\n")
        f.write(f"Caminho encontrado: {resultado['caminho']}\n")
        f.write("\n")

# Experimentos
def executar_experimentos_parte1(arquivo_resultados, num_repeticoes=50):
    
    custo_funcs = [custo_c1, custo_c2, custo_c3, custo_c4]

    for _ in range(num_repeticoes):
          x1, y1 = random.randint(0, 30), random.randint(0, 30)
          x2, y2 = random.randint(0, 30), random.randint(0, 30)
          estado_inicial = (x1, y1)
          estado_objetivo = (x2, y2)
          print(f"\n---Início da Busca: Estado Inicial {estado_inicial} Estado Objetivo: {estado_objetivo}---")
          start_time = time.time()
          for custo_func in custo_funcs:
                print(f"Executando Busca em Largura com custo {custo_func.__name__}")
                resultado = busca_em_largura(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos)
                salvar_resultados("Busca em Largura", resultado, custo_func, None, arquivo_resultados)

                print(f"Executando Busca em Profundidade com custo {custo_func.__name__}")
                resultado = busca_em_profundidade(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos)
                salvar_resultados("Busca em Profundidade", resultado, custo_func, None, arquivo_resultados)

                print(f"Executando Busca de Custo Uniforme com custo {custo_func.__name__}")
                resultado = busca_custo_uniforme(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos)
                salvar_resultados("Busca de Custo Uniforme", resultado, custo_func, None, arquivo_resultados)
          end_time = time.time()
          print(f"Tempo total da Busca: {end_time - start_time}")

def executar_experimentos_parte2(arquivo_resultados, num_repeticoes=50):    
    custo_funcs = [custo_c1, custo_c2, custo_c3, custo_c4]
    heuristicas = [heuristica_euclidiana, heuristica_manhattan]

    for _ in range(num_repeticoes):
           x1, y1 = random.randint(0, 30), random.randint(0, 30)
           x2, y2 = random.randint(0, 30), random.randint(0, 30)
           estado_inicial = (x1, y1)
           estado_objetivo = (x2, y2)
           print(f"\n---Início da Busca: Estado Inicial {estado_inicial} Estado Objetivo: {estado_objetivo}---")
           start_time = time.time()
           for custo_func in custo_funcs:
                print(f"Executando Busca de Custo Uniforme com custo {custo_func.__name__}")
                resultado = busca_custo_uniforme(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos)
                salvar_resultados("Busca de Custo Uniforme", resultado, custo_func, None, arquivo_resultados)
                for heuristica in heuristicas:
                  print(f"Executando Busca A* com custo {custo_func.__name__} e heuristica {heuristica.__name__}")
                  resultado = busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, custo_func, heuristica)
                  salvar_resultados("Busca A*", resultado, custo_func, heuristica, arquivo_resultados)
           end_time = time.time()
           print(f"Tempo total da Busca: {end_time - start_time}")


def executar_experimentos_parte3(arquivo_resultados, num_repeticoes=50):
    
    custo_funcs = [custo_c1, custo_c2, custo_c3, custo_c4]
    heuristicas = [heuristica_euclidiana, heuristica_manhattan]
    
    for _ in range(num_repeticoes):
        x1, y1 = random.randint(0, 30), random.randint(0, 30)
        x2, y2 = random.randint(0, 30), random.randint(0, 30)
        estado_inicial = (x1, y1)
        estado_objetivo = (x2, y2)
        print(f"\n---Início da Busca: Estado Inicial {estado_inicial} Estado Objetivo: {estado_objetivo}---")
        start_time = time.time()
        for heuristica in heuristicas:
           print(f"Executando Busca Gulosa com heuristica {heuristica.__name__}")
           resultado = busca_gulosa(estado_inicial, estado_objetivo, heuristica, custo_c1, gerar_vizinhos)
           for custo_func in custo_funcs:
             resultado['custo'] = 0
             for i in range(1, len(resultado['caminho'])):
                 resultado['custo'] += custo_func(resultado['caminho'][i-1], resultado['caminho'][i], i)
             salvar_resultados("Busca Gulosa", resultado, custo_func, heuristica, arquivo_resultados)
           for custo_func in custo_funcs:
              print(f"Executando Busca A* com custo {custo_func.__name__} e heuristica {heuristica.__name__}")
              resultado = busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, custo_func, heuristica)
              salvar_resultados("Busca A*", resultado, custo_func, heuristica, arquivo_resultados)
        end_time = time.time()
        print(f"Tempo total da Busca: {end_time - start_time}")


def executar_experimentos_parte4(arquivo_resultados, num_repeticoes = 20):
    custo_funcs = [custo_c1, custo_c2, custo_c3, custo_c4]
    
    for _ in range(num_repeticoes):
        x1, y1 = random.randint(0, 30), random.randint(0, 30)
        x2, y2 = random.randint(0, 30), random.randint(0, 30)
        estado_inicial = (x1, y1)
        estado_objetivo = (x2, y2)
        print(f"\n---Início da Busca: Estado Inicial {estado_inicial} Estado Objetivo: {estado_objetivo}---")
        start_time = time.time()
        for _ in range(10):
            for custo_func in custo_funcs:
                print(f"Executando Busca em Largura (Random) com custo {custo_func.__name__}")
                resultado_largura_random = busca_em_largura(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos_aleatorios)
                salvar_resultados("Busca em Largura (Random)", resultado_largura_random, custo_func, None, arquivo_resultados)
          
                print(f"Executando Busca em Profundidade (Random) com custo {custo_func.__name__}")
                resultado_profundidade_random = busca_em_profundidade(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos_aleatorios)
                salvar_resultados("Busca em Profundidade (Random)", resultado_profundidade_random, custo_func, None, arquivo_resultados)
        end_time = time.time()
        print(f"Tempo total da Busca: {end_time - start_time}")

        
def executar_experimentos_parte5(arquivo_resultados, num_repeticoes = 25):
    
    custo_funcs = [custo_c1, custo_c2, custo_c3, custo_c4]
    heuristicas = [heuristica_euclidiana, heuristica_manhattan]

    for _ in range(num_repeticoes):
        x1, y1 = random.randint(0, 30), random.randint(0, 30)
        x2, y2 = random.randint(0, 30), random.randint(0, 30)
        
        farmacias = []
        while len(farmacias) < 4:
            x_farmacia = random.randint(0,30)
            y_farmacia = random.randint(0,30)
            farmacia_coord = (x_farmacia, y_farmacia)
            if farmacia_coord not in farmacias and farmacia_coord != (x1, y1) and farmacia_coord != (x2, y2):
                farmacias.append(farmacia_coord)

        estado_inicial = (x1, y1)
        estado_objetivo = (x2, y2)
        print(f"\n---Início da Busca: Estado Inicial {estado_inicial} Estado Objetivo: {estado_objetivo}---")
        start_time = time.time()
        for custo_func in custo_funcs:
            for heuristica in heuristicas:
                 
                melhor_caminho = None
                melhor_custo = float('inf')
                nos_gerados_total, nos_visitados_total = 0, 0
                 
                for f in farmacias:
                    print(f"Executando Busca A* com custo {custo_func.__name__} e heuristica {heuristica.__name__} para farmacia {f}")
                    resultado = busca_a_estrela(estado_inicial, f, gerar_vizinhos, custo_func, heuristica)
                    
                    if resultado['caminho']:
                        resultado_2 = busca_a_estrela(f, estado_objetivo, gerar_vizinhos, custo_func, heuristica)
                    else:
                        continue
                    
                    if resultado_2['caminho']:
                       
                        caminho_total = resultado['caminho'][:-1] + resultado_2['caminho']
                        
                        custo_total = 0
                        for i in range(1, len(caminho_total)):
                            custo_total += custo_func(caminho_total[i-1], caminho_total[i], i)

                        if custo_total < melhor_custo:
                            melhor_custo = custo_total
                            melhor_caminho = caminho_total
                            nos_gerados_total = resultado['nos_gerados'] + resultado_2['nos_gerados']
                            nos_visitados_total = resultado['nos_visitados'] + resultado_2['nos_visitados']
                if melhor_caminho:
                    resultado_final = {"caminho": melhor_caminho, "custo": melhor_custo, "nos_gerados": nos_gerados_total, "nos_visitados": nos_visitados_total}
                    salvar_resultados("Busca A* (Farmacia)", resultado_final, custo_func, heuristica, arquivo_resultados, farmacias)
        end_time = time.time()
        print(f"Tempo total da Busca: {end_time - start_time}")

# Função principal
def main():
    
    arquivo_resultados1 = "resultados_busca_experimento_1.txt"
    arquivo_resultados2 = "resultados_busca_experimento_2.txt"
    arquivo_resultados3 = "resultados_busca_experimento_3.txt"
    arquivo_resultados4 = "resultados_busca_experimento_4.txt"
    arquivo_resultados5 = "resultados_busca_experimento_5.txt"

    # Limpa o arquivo de resultados
    with open(arquivo_resultados1, "w") as f:
        f.write("Resultados das buscas do experimento 1:\n\n")

    with open(arquivo_resultados2, "w") as f:
        f.write("Resultados das buscas do experimento 2:\n\n")

    with open(arquivo_resultados3, "w") as f:
        f.write("Resultados das buscas do experimento 3:\n\n")

    with open(arquivo_resultados4, "w") as f:
        f.write("Resultados das buscas do experimento 4:\n\n")

    with open(arquivo_resultados5, "w") as f:
        f.write("Resultados das buscas do experimento 5:\n\n")

    # Executa os experimentos
    print("Executando experimento 1...")
    executar_experimentos_parte1(arquivo_resultados1)

    print("Executando experimento 2...")
    executar_experimentos_parte2(arquivo_resultados2)

    print("Executando experimento 3...")
    executar_experimentos_parte3(arquivo_resultados3)
    
    print("Executando experimento 4...")
    executar_experimentos_parte4(arquivo_resultados4)

    print("Executando experimento 5...")
    executar_experimentos_parte5(arquivo_resultados5)
    print("\nExperimentos concluídos. Resultados salvos em resultados_busca.txt")

if __name__ == "__main__":
    main()