f = open('bigger_triangle.txt')
tri = []
for line in f:
        tri.append(list(map(int, line.split())))

# work from second bottom row to tip
for r in range(len(tri)-2, 0-1, -1):
        for c in range(0, r+1):
                tri[r][c] += max(tri[r+1][c], tri[r+1][c+1])

print(tri[0][0])