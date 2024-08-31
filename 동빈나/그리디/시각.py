// 시각

n = 5
answer = 0

def find(x):
    return "3" in str(x)

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if find(h) or find(m) or find(s):
                answer += 1
    
print(answer)