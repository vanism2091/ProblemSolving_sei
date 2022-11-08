# https://www.acmicpc.net/problem/1916
"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

dp가 틀린 풀이인게, arr dep cost일 때 arr가 dep보다 큰 경우가 있을 수 있음.

다익스트라 알고리즘
"""

def sol_1916_wrong():
    import sys
    from collections import deque, defaultdict
    input = sys.stdin.readline
    N = int(input())
    buses = defaultdict(list)
    for i in range(int(input())):
        dep, arr, cost = map(int, input().split())
        buses[arr].append((dep, cost))
    DEP, ARR = map(int, input().split())
    dp = [0] * (DEP+1) + [float('inf')] * (ARR - DEP)
    for i in range(DEP, ARR+1):
        for dep, cost in buses[i]:
            dp[i] = min(dp[dep]+cost, dp[i])
    return dp[ARR]
    
    pass


def sol_1916():
    import sys
    from collections import deque, defaultdict
    import heapq
    
    input = sys.stdin.readline
    N, B = int(input()), int(input())
    buses = defaultdict(list)
    for _ in range(B):
        dep, arr, cost = map(int, input().split())
        buses[dep].append((cost, arr))
    DEP, ARR = map(int, input().split())
    
    visited = [True] + [False] * N
    cost_dict = {}
    hq = [(0, DEP)]
    
    while hq:
        while hq and (cur := heapq.heappop(hq)) and visited[cur[1]]:
            continue
        cost_dict[cur[1]], visited[cur[1]] = cur[0], True
        if cur[1] == ARR: break
        for cost, cur_arr in buses[cur[1]]:
            heapq.heappush(hq, (cost+cur[0], cur_arr))
    
    return cost_dict[ARR]

if __name__ == "__main__":
    # sol_1916()
    print(sol_1916())
