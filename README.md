# Implementação do Método Simplex em Python

Este código implementa o método Simplex para resolver problemas de programação linear. O método Simplex é um algoritmo iterativo que encontra a solução ótima para problemas de maximização linear sujeitos a restrições lineares.

## Descrição
O código utiliza a biblioteca NumPy para manipulação de matrizes e segue os seguintes passos:

1. **Inicialização**: Define a função objetivo, a matriz de restrições e as variáveis básicas e não básicas.
2. **Cálculo da Solução Básica**: Determina a solução básica viável inicial e verifica se é ótima.
3. **Determinação da Variável de Entrada**: Identifica a variável que entra na base com base nos custos reduzidos.
4. **Determinação da Variável de Saída**: Define a variável que sai da base através do critério de razão mínima.
5. **Atualização das Bases**: Atualiza a matriz básica e não básica e repete o processo até encontrar a solução ótima.
