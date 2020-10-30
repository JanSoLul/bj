def tsp(D):
    N = len(D)
    inf = float('inf')
    ans = inf
    VISITED_ALL = (1 << N) - 1 # 모든 도시를 방문했음을 의미하는 상수((1 << N)-1 은 N개의 비트를 모두 켠다와 같다.) -> 'N개의 도시를 모두 방문했다' 와 같다

    # 각 도시를 방문하는 재귀함수를 정의. visited는 방문 도시 집합 V를 의미
    def find_path(start, last, visited, tmp_dist):
        nonlocal ans
        # 각 방문에서 방문 도시 집합 visited가 모든 도시를 방문했음을 의미하는 상수 VISITED_ALL이면
        # 모든 도시를 방문했기 때문에 최소값을 경신하고 종료한다.
        if visited == VISITED_ALL:
            return_home_dist = D[last][start] or inf
            ans = min(ans, tmp_dist + return_home_dist)
            return

        # 아직 여행 중이면 방문하지 않은 각 도시를 방문한다. 모든 도시를 방문하는 것이 아니라
        # 다음 조건을 만족하는 도시를 선택해야 하는데:
        # 1. 아직 방문하지 않은 도시이며
        # 2. 마지막 방문 도시와 후보 도시가 이어져 있어야 한다.
        # if 문에서 두개의 조건식으로 이를 검증하는데, 첫 번째 조건 visited & (1 << city) == 0은
        # visited의 city번째 비트가 켜져있는지 검증하는 식이고, 두 번째 조건은 두 도시가 이어져 있지
        # 않으면 거리가 0이기 때문에 D[last][city] != 0으로 검증한다.
        fot city in range(N):
            if visited & (1 << city) == 0 and D[last][city] != 0:
                find_path(start, city, visited | (1 << city), tmp_dist + D[last][city])
                # 재귀호출에서 visited | (1 << city)로 visited를 경신하고 있는데, 이는 city번째
                # 도시를 방문했음을 알려준다.


    for c in range(N):
        find_path(c, c, 1<<c, 0)

    return ans
