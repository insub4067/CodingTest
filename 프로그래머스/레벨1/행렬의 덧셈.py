# 행렬의 덧셈

def solution(arr1, arr2):
    i = len(arr1)
    answer = [[] for _ in range(i)]

    for i in range(i):
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])

    return answer

print(solution([[1,2],[2,3]]	, [[3,4],[5,6]]	))