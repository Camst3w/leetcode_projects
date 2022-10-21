def kWeakestRows(mat: list, k):
    soldier_count, weakest_rows = 0, []
    while k != 0:
        for i in range(len(mat)):
            if mat[i].count(1) == soldier_count:
                weakest_rows.append(i)
                k -= 1
            if k == 0:
                return weakest_rows
        soldier_count += 1    


mat = [[1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]]
k = 3

print(kWeakestRows(mat, k))