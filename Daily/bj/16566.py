# 20분

from bisect import bisect_right
import sys

def sol_16566():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    li = sorted(map(int, input().split()))
    visited=[False] * len(li)
    cheol = list(map(int, input().split()))
    for c in cheol:
        i = bisect_right(li, c)
        while visited[i]:
            i += 1
        print(li[i])
        visited[i] = True

if __name__ == "__main__":
    sol_16566()



"""
others
"""

from sys import stdin

input = stdin.readline

# union find 찾기?

def solve():
    N, M, K = map(int, input().split())
    cards = sorted(map(int, input().split()))
    disjoint_set = [-1] * (M + 1)

    def union_find(a):
        if disjoint_set[a] == -1:
            return a
        disjoint_set[a] = union_find(disjoint_set[a])
        return disjoint_set[a]

    def bisect(x):
        lo, hi = 0, M
        while lo < hi:
            mid = (lo + hi) // 2
            if x < cards[union_find(mid)]:
                hi = mid
            else:
                lo = mid + 1

        return union_find(lo)

    for enemy in map(int, input().split()):
        idx = bisect(enemy)
        disjoint_set[idx] = union_find(idx+1)
        print(cards[idx])


if __name__ == '__main__':
    solve()