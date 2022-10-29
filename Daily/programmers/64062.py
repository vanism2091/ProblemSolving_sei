# 22:50 - 11:07
def solution(stones, k):
    # minimun = - float("inf")
    minimum = float("inf")
    i = 0
    while i < len(stones)-k+1:
        cur_i, cur_max = list(filter(lambda x: x[1] == max(stones[i:i+k]), list(zip(range(i, i+k), stones[i:i+k]))))[0]
        print(i, cur_i, cur_max)
        if minimum > cur_max:
            minimum = cur_max
        i = cur_i + 1
        
    # for i in range(len(stones)-k):
    #     cur_max = max(stones[i:i+k])
    #     if minimun > cur_max:
    #         minimum = cur_max        
    return minimum

# 결과
# 테스트 1, 테스트 3 실패(런타임 에러, 값 틀림)
# 시간 초과

# 11:15 정확도 모두 통과
# 문제는 k+1을 안해줬던 것


# 22:50 - 11:07

# 11:20 효율성 1개 실패 :(
def solution(stones, k):
    # minimun = - float("inf")
    minimum = float("inf")
    i = 0
    while i < len(stones)-k+1:
        cur_i, cur_max = i, 0
        for j in range(i, i+k):
            if cur_max < stones[j]:
                cur_i, cur_max = j, stones[j]
        if minimum > cur_max:
            minimum = cur_max
        i = cur_i + 1
    return minimum

# 11:22 효율성 1개 실패 :(
def solution(stones, k):
    minimum = float("inf")
    i = 0
    while i < len(stones)-k+1:
        cur_i, cur_max = i, 0
        for j in range(i, i+k):
            if cur_max <= stones[j]:
                cur_i, cur_max = j, stones[j]
        if minimum > cur_max:
            minimum = cur_max
        i = cur_i + 1
    return minimum

stones = [2, 4, 5, 3, 2, 1, 1, 2, 5, 1]	
k = 3
print(solution(stones, k))

# 13이 어떤 케이스일까? 아마 내림차순으로 정렬된 배열 같은데
# 재귀로 한 후 하나는 reverse array에 대해?

# 11: 34
# stones.reverse()만 추가 했더니 다른건 매우 쉽게 통과, 14는 시간초과.
# 즉, 14는 오름차순 정렬된 배열인 것. 이렇게 완전 오름차순, 완전 내림차순 정렬은 그럼 어떻게 해야할까?
# 둘 다 병렬로 한 후 둘 중 빨리 끝나는걸 하는 방법이 없을까 :(

def solution(stones, k):
    min1, min2 = float("inf"), float("inf")
    i1, i2 = 0, 0
    stones_reversed = reversed(stones)
    while i1 < len(stones)-k+1 and i2 < len(stones)-k+1:
        i1, min1 = get_idx_min(stones, i1, min1)
        i2, min2 = get_idx_min(stones_reversed, i2, min2)
    
    def get_idx_min(li, i, cur_min):
        cur_i, cur_max = i, 0
        for j in range(i, i+k):
            if cur_max <= li[j]:
                cur_i, cur_max = j, li[j]
            minimum = cur_max if cur_min > cur_max else cur_min
            return cur_i+1, minimum
    return min1 if i1 > i2 else min2

# 어거지로 풀었다..
# 11:48
def solution(stones, k):
    min1, min2 = float("inf"), float("inf")
    i1, i2 = 0, 0
    stones_reversed = list(reversed(stones))
    def get_idx_min(li, i, cur_min):
        cur_i, cur_max = i, 0
        for j in range(i, i+k):
            if cur_max <= li[j]:
                cur_i, cur_max = j, li[j]
        minimum = cur_max if cur_min > cur_max else cur_min
        return cur_i+1, minimum
    while i1 < len(stones)-k+1 and i2 < len(stones)-k+1:
        i1, min1 = get_idx_min(stones, i1, min1)
        i2, min2 = get_idx_min(stones_reversed, i2, min2)
    return min1 if i1 > i2 else min2