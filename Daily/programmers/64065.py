# 18:10
"""
# n-tuple
중복된 원소 있을 수 있음
순서가 있음. 순서가 다르면 서로 다른 튜플
원소의 개수는 유한

중복이 없는 원소는 소집합? { ,..., } 로 표현 가능
특정 튜플을 표현하는 집합이 담긴 문자열을 받았을 때,
S가 표현하는 튜플을 배열에 담아 return하기
"""
# 순서가 있음 ^^

def solution(s):
    s = s[1:-1]
    left, right = 0, 1
    res_dict = {}
    res = []
    while right < len(s):
        if s[right] == "}":
            cur = s[left+1:right]
            res_dict[len(cur)] = map(int,cur.split(","))
            left = right + 2
            right += 3
        else:
            right += 1
    for key in sorted(res_dict.keys()):
        res.append(list(filter(lambda x: x not in res, res_dict[key]))[0])
    return res

if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print()
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print()
    print(solution("{{20,111},{111}}"))
    print()
    print(solution("{{123}}"))
    print()
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
    print("---")