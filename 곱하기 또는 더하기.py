// 곱하기 또는 더하기

input = list(map(int, list("567")))
answer = input[0]

for num in input[1:]:
    if num <= 1 or answer <= 1:
        answer += num 
    else:
        answer *= num 

print(answer)
