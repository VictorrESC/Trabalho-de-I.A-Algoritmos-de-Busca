import random
import time
import pandas as pd
from busca_em_largura import busca_em_largura
from busca_em_profundidade import busca_em_profundidade
from custo_uniforme import busca_custo_uniforme
from busca_gulosa import busca_gulosa
from a_estrela import busca_a_estrela, heuristica_euclidiana, heuristica_manhattan, gerar_vizinhos

# Inicializar DataFrame para armazenar resultados
resultados_df = pd.DataFrame(columns=[
    "No_Inicial", "No_Final",
    "Algoritmo", "Funcao_Custo", "Funcao_Heuristica", 
    "Custo_Caminho", "Nos_Gerados", "Nos_Visitados", "Caminho_Encontrado", "Farmacias"
])

def salvar_resultados_pandas(nome_algoritmo, resultado, custo_fun, heuristica, no_inicial, no_final, estados_farmacias=None):
    global resultados_df
    nova_linha = pd.DataFrame([{
        "No_Inicial": no_inicial,
        "No_Final": no_final,
        "Algoritmo": nome_algoritmo,
        "Funcao_Custo": custo_fun.__name__ if custo_fun else 'N/A',
        "Funcao_Heuristica": heuristica.__name__ if heuristica else 'N/A',
        "Custo_Caminho": resultado['custo'],
        "Nos_Gerados": resultado['nos_gerados'],
        "Nos_Visitados": resultado['nos_visitados'],
        "Caminho_Encontrado": resultado['caminho'],
        "Farmacias": estados_farmacias if estados_farmacias else 'N/A'
    }])
    resultados_df = pd.concat([resultados_df, nova_linha], ignore_index=True)

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
                salvar_resultados_pandas("Busca em Largura", resultado, custo_func, None, estado_inicial, estado_objetivo)

                print(f"Executando Busca em Profundidade com custo {custo_func.__name__}")
                resultado = busca_em_profundidade(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos)
                salvar_resultados_pandas("Busca em Profundidade", resultado, custo_func, None, estado_inicial, estado_objetivo)

                print(f"Executando Busca de Custo Uniforme com custo {custo_func.__name__}")
                resultado = busca_custo_uniforme(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos)
                salvar_resultados_pandas("Busca de Custo Uniforme", resultado, custo_func, None, estado_inicial, estado_objetivo)
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
                salvar_resultados_pandas("Busca de Custo Uniforme", resultado, custo_func, None, estado_inicial, estado_objetivo)
                for heuristica in heuristicas:
                  print(f"Executando Busca A* com custo {custo_func.__name__} e heuristica {heuristica.__name__}")
                  resultado = busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, custo_func, heuristica)
                  salvar_resultados_pandas("Busca A*", resultado, custo_func, heuristica, estado_inicial, estado_objetivo)
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
             salvar_resultados_pandas("Busca Gulosa", resultado, custo_func, heuristica, estado_inicial, estado_objetivo)
           for custo_func in custo_funcs:
              print(f"Executando Busca A* com custo {custo_func.__name__} e heuristica {heuristica.__name__}")
              resultado = busca_a_estrela(estado_inicial, estado_objetivo, gerar_vizinhos, custo_func, heuristica)
              salvar_resultados_pandas("Busca A*", resultado, custo_func, heuristica, estado_inicial, estado_objetivo)
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
                salvar_resultados_pandas("Busca em Largura (Random)", resultado_largura_random, custo_func, None, estado_inicial, estado_objetivo)
          
                print(f"Executando Busca em Profundidade (Random) com custo {custo_func.__name__}")
                resultado_profundidade_random = busca_em_profundidade(estado_inicial, estado_objetivo, custo_func, gerar_vizinhos_aleatorios)
                salvar_resultados_pandas("Busca em Profundidade (Random)", resultado_profundidade_random, custo_func, None, estado_inicial, estado_objetivo)
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
                    salvar_resultados_pandas("Busca A* (Farmacia)", resultado_final, custo_func, heuristica, estado_inicial, estado_objetivo, farmacias)
        end_time = time.time()
        print(f"Tempo total da Busca: {end_time - start_time}")

# Função principal
def main():
    # Arquivos CSV para salvar resultados
    arquivo_csv1 = "resultados_experimento_1.csv"
    arquivo_csv2 = "resultados_experimento_2.csv"
    arquivo_csv3 = "resultados_experimento_3.csv"
    arquivo_csv4 = "resultados_experimento_4.csv"
    arquivo_csv5 = "resultados_experimento_5.csv"

    global resultados_df  # Garante que a função utilize o DataFrame global para armazenar resultados

    # Executa os experimentos e salva os resultados em CSV
    print("Executando experimento 1...")
    executar_experimentos_parte1(arquivo_csv1)
    resultados_df.to_csv(arquivo_csv1, index=False)
    resultados_df = pd.DataFrame(columns=resultados_df.columns)  # Limpa o DataFrame para o próximo experimento

    print("Executando experimento 2...")
    executar_experimentos_parte2(arquivo_csv2)
    resultados_df.to_csv(arquivo_csv2, index=False)
    resultados_df = pd.DataFrame(columns=resultados_df.columns)

    print("Executando experimento 3...")
    executar_experimentos_parte3(arquivo_csv3)
    resultados_df.to_csv(arquivo_csv3, index=False)
    resultados_df = pd.DataFrame(columns=resultados_df.columns)

    print("Executando experimento 4...")
    executar_experimentos_parte4(arquivo_csv4)
    resultados_df.to_csv(arquivo_csv4, index=False)
    resultados_df = pd.DataFrame(columns=resultados_df.columns)

    print("Executando experimento 5...")
    executar_experimentos_parte5(arquivo_csv5)
    resultados_df.to_csv(arquivo_csv5, index=False)
    resultados_df = pd.DataFrame(columns=resultados_df.columns)

    print("\nExperimentos concluídos. Resultados salvos nos arquivos CSV.")

if __name__ == "__main__":
    main()