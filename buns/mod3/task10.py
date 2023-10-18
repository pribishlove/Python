size = int(input())
matrix = [[str(j) for j in range(1, size + 1)] for i in range(size)]
for a in matrix:
    print(', '.join(a))
print()
for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for a in matrix:
    print(', '.join(a))