a = [[0, 3, 1e7, 7],
     [8, 0, 2, 1e7],
     [5, 1e7, 0, 1],
     [2, 1e7, 1e7, 0]]
v = len(a)
for k in range(v):
    for i in range(v):
        for j in range(v):
            if a[i][k] + a[k][j] < a[i][j]:
                a[i][j] = a[i][k] + a[k][j]
print(a)
