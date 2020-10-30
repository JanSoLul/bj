from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    adj = [list(map(int, read().split())) for _ in range(N)]

    def tsp(dists, N):
        VISITED_ALL = (1 << N) - 1
        cache = [[None] * (1 << N) for _ in range(N)]
        INF = float('inf')

        def find_path(last, visited):
            if visited == VISITED_ALL:
                return dists[last][0] or INF
            if cache[last][visited] is not None:
                return cache[last][visited]
            tmp = INF
            for city in range(N):
                if visited & (1 << city) == 0 and dists[last][city] != 0:
                    tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])
            cache[last][visited] = tmp
            return tmp
        return find_path(0, 1 << 0)

    print(tsp(adj, N))

if __name__  == '__main__':
    solve()
