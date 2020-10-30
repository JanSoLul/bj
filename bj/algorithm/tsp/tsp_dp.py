def tsp(dists):
    N = len(dists)
    VISITED_ALL = (1 << N) - 1

    cache = [[None] * (1 << N) for _ in range(N)]
    # dp를 위한 캐시를 초기화한다. range(N)을 통해 도시의 개수에 대응하고 (1<<N)을 통해 방문한 도시
    # 집합에 대응한다.

    INF = float('inf')

    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF
            # return에 or 연산자를 썼는데, 이 연산자를 통해 마지막 방문 도시와 0번째(시작 도시)
            # 사이의 경로가 존재하면(0이 아니라면) 이 경로 값을 return하고 이어져 있지 않다면(0이
            # 라면) 무한값을 return해서 절대 답이 될 수 없게 한다.

        if cache[last][visited] is not None:
            # 캐시의 초기값을 None으로 했기 때문에 None이 아니라는 것은 해당 last와 V에 대한 계산이
            # 이미 이루어졌고 지금은 중복 호출되었다는 뜻이기 때문에 다시 재계산하지 않고 값을 바로
            # 반환한다.
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])
        cache[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)
