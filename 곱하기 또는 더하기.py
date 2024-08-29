// 곱하기 또는 더하기

input = list(map(int, list("567"))) 

for idx, element in enumerate(input) :
    current = input[idx]
    hasNext = len(input) >= idx + 2 
    if hasNext:
        next = input[idx + 1]
        if current == 0 or next == 0:
            input[idx + 1] = current + next 
        else:
            input[idx + 1] = current * next 
    else:
        print(input[idx])