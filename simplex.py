import numpy as np

# FASE 1: Inicialização
total_variaveis = 2  # Número de variáveis do problema
restricoes = 3  # Número de restrições (equivalente ao número de variáveis de folga)
interacao = 0

definir_eps = 1e-10  # Pequeno valor para evitar divisões por zero

f_objetivo = np.array([-3, -5, 0, 0, 0])  # Coeficientes da função objetivo

A = np.array([[3, 2, 1, 0, 0],
              [1, 0, 0, 1, 0],
              [0, 2, 0, 0, 1]])

b = np.array([18, 4, 12])

B = A[:, -restricoes:].copy()  # Matriz básica (colunas finais de A)
CB = f_objetivo[-restricoes:].copy()

N = A[:, :total_variaveis].copy()  # Matriz não básica (primeiras colunas de A)
CN = f_objetivo[:total_variaveis].copy()

# FASE 2: Método Simplex
while True:
    interacao += 1
    print(f'--------------- Iteração {interacao} ---------------')

    try:
        inversa_B = np.linalg.inv(B)
    except np.linalg.LinAlgError:
        print('A matriz B não é inversível. O algoritmo termina.\n')
        break

    XB = np.dot(inversa_B, b)  # Solução básica atual
    print(f'Solução Básica: {XB}')

    # PASSO 2.1: Cálculo de lambda_coef
    lambda_coef = np.dot(CB, inversa_B)

    # PASSO 2.2: Cálculo dos custos reduzidos
    CNk = [CN[j] - np.dot(lambda_coef, N[:, j]) for j in range(CN.size)]
    print(f'Custos reduzidos: {CNk}')

    # PASSO 2.3: Determinar variável que entra na base
    menor_valor = np.min(CNk)
    if menor_valor >= 0:
        print('Solução ótima encontrada!')
        print(f'Número de iterações: {interacao}')
        print(f'Solução ótima: {XB}')
        break
    indice_menor_valor = np.argmin(CNk)

    # PASSO 4: Cálculo do vetor direção y
    coluna_entrada = N[:, indice_menor_valor]
    y = np.dot(inversa_B, coluna_entrada)

    # PASSO 5: Determinar variável que sai da base
    if np.all(y <= 0):
        print('O problema não tem solução ótima finita!')
        break

    E = [(XB[i] / (y[i] if abs(y[i]) > definir_eps else float('inf'))) for i in range(y.size)]
    indice_menor_E = np.argmin(E)

    # PASSO 6: Atualização das bases
    B[:, indice_menor_E], N[:, indice_menor_valor] = N[:, indice_menor_valor].copy(), B[:, indice_menor_E].copy()
    CB[indice_menor_E], CN[indice_menor_valor] = CN[indice_menor_valor], CB[indice_menor_E]

    print(f'Nova matriz B:\n{B}')
    print(f'Nova matriz N:\n{N}')
