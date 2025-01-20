# Algoritmos de Busca - Projeto Prático

Este projeto implementa diversos algoritmos de busca para a disciplina de Inteligência Artificial, com o objetivo de analisar o comportamento, desempenho e características de cada um. O projeto é composto pelos seguintes arquivos:

*   `main.py`: Arquivo principal para executar os experimentos, definir as funções de custo e de gerar vizinhos, e chamar os algoritmos de busca com os parâmetros necessários. Também utiliza a biblioteca `pandas` para salvar os resultados em arquivos CSV.
*   `busca_em_largura.py`: Implementação do algoritmo de busca em largura.
*   `busca_em_profundidade.py`: Implementação do algoritmo de busca em profundidade.
*   `custo_uniforme.py`: Implementação do algoritmo de busca de custo uniforme.
*   `busca_gulosa.py`: Implementação do algoritmo de busca gulosa.
*   `a_estrela.py`: Implementação do algoritmo de busca A\*.

## Executando os Experimentos

1.  **Requisitos:**
    *   Python 3.10 instalado.
    *   Biblioteca `pandas` instalada. Instale utilizando: `pip install pandas`
2.  **Execução:**
    *   Navegue até o diretório do projeto no terminal.
    *   Execute o arquivo principal: `python main.py`
    *   Serão gerados 5 arquivos CSV (resultados_experimento_1.csv, resultados_experimento_2.csv, resultados_experimento_3.csv, resultados_experimento_4.csv e resultados_experimento_5.csv) contendo os resultados dos experimentos.

## Modificações nos Experimentos

As funções de experimentos (parte 1 até 5) foram modificadas para oferecer mais flexibilidade na definição dos parâmetros de teste.

*   **Geração de Estados Aleatórios:**
    *   Originalmente, os estados iniciais e objetivos eram gerados aleatoriamente utilizando `random.randint(0, 30)`.
    *   Essa parte do código está comentada nas funções, e ela pode ser utilizada caso o usuário queira executar o código de forma mais "genérica" e aleatória.

        ```python
           # x1, y1 = random.randint(0, 30), random.randint(0, 30)
           # x2, y2 = random.randint(0, 30), random.randint(0, 30)
           # estado_inicial = (x1, y1)
           # estado_objetivo = (x2, y2)
      
*  **Estados Fixos:**
    *   Caso o usuário queira definir quais são os estados iniciais e objetivos para executar o experimento, basta descomentar e mudar o código com estados desejados.
        ```python
        estado_inicial = (0, 0)
        estado_objetivo = (30, 5)
       

*   **Como usar:**
    1.  Para executar o código com os parâmetros aleatórios, comente a parte que tem o estado fixo, e descomente a parte dos estados aleatórios.
    2. Para executar com os parâmetros fixos, comente a parte do estado aleatório e descomente e altere a parte dos parâmetros fixos, caso necessário.

## Funções de Custo e Heurísticas

*   As funções de custo (C1, C2, C3, C4) estão definidas no arquivo `main.py`.
*   As funções heurísticas (Manhattan e Euclidiana) estão definidas no arquivo `a_estrela.py`.
*   A quantidade de repetições de cada experimento está configurada nas funções `executar_experimentos_parteX` do arquivo `main.py`.
*   As funções para gerar os vizinhos para cada nó estão definidas no arquivo `a_estrela.py` (função `gerar_vizinhos`) e no arquivo `main.py` (função `gerar_vizinhos_aleatorios`).
* Para as funções que utilizam a randomização dos vizinhos, é possível modificar a ordem das ações utilizando o código na função `gerar_vizinhos_aleatorios` do arquivo `main.py`.

## Saída dos Resultados

*   Os resultados de cada experimento são salvos em arquivos CSV separados (ex: `resultados_experimento_1.csv`, `resultados_experimento_2.csv`...).
*   Cada linha de um arquivo CSV representa o resultado de uma execução de um algoritmo de busca.
*   As colunas do CSV incluem informações como:
    *   `Algoritmo`: Nome do algoritmo de busca.
    *   `Funcao_Custo`: Nome da função de custo utilizada.
    *   `Funcao_Heuristica`: Nome da função heurística utilizada (se aplicável).
    *   `Custo_Caminho`: Custo total do caminho encontrado.
    *   `Nos_Gerados`: Número de nós gerados durante a busca.
    *   `Nos_Visitados`: Número de nós visitados durante a busca.
    *   `Caminho_Encontrado`: Caminho percorrido.
    *    `Farmacias`: Lista das farmácias no experimento (se aplicável).

## Observações

*   Este projeto foi desenvolvido para fins de estudo e demonstração dos algoritmos de busca.
*   Os resultados podem variar dependendo da configuração dos parâmetros e das entradas.
*   Sinta-se à vontade para modificar o código, testar diferentes abordagens e analisar os resultados gerados.

## Colaboradores

*   Kaynan Pereira de Sousa - 540864
*   Victor Emanuel de Sousa Costa - 535718
