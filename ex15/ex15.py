tamanho = 20

grid = [[1] * (tamanho + 1) for _ in range(tamanho + 1)]

for i in range(1, tamanho + 1):
    for j in range(1, tamanho + 1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

resultado = grid[tamanho][tamanho]

print(resultado)

"""
Descobre a quantidade de caminhos possiveis para chegar do topo esquerdo de uma grid 20x20,
até o inferior direito
"""