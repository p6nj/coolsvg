p = lambda x: print(x, end=" ")


def line(coords: tuple[tuple[int]]):
    return f"M {coords[0][0]} {coords[0][1]} L {coords[1][0]} {coords[1][1]}"


n = 5
for i in range(1, n):
    p(line(((i, 0), (n - i, n))))
    p(line(((0, i), (n, n - i))))

print()
