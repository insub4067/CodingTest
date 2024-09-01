// 왕실의 나이트.py

input = "a1"
xStr = input[0]
y = int(input[1])

x = 0
match xStr:
    case "a":
        x = 1
    case "b":
        x = 2
    case "c":
        x = 3
    case "d":
        x = 4
    case "e":
        x = 5
    case "f":
        x = 6
    case "g":
        x = 7
    case "h":
        x = 8
        
answer = 0

xs = [-2, -1, 1, 2, 2, 1, -1, -2]
ys = [-1, -2, -2, -1, 1, 2, 2, -1]

for i in range(8):
    nxt_x = x + xs[i]
    nxt_y = y + ys[i]
    if 0 < nxt_x < 9 and 0 < nxt_y < 9:
        answer += 1
    
print(answer)