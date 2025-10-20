def Solve(n):
    n = int(n)
    smallest_base = 2
    current_base = 2
    while bin(n, current_base).count('1')!= len(bin(n, current_base)):
        current_base += 1
    return smallest_base