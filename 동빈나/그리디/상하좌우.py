// 상하좌우

n = 5
input = "R R R U D D"
commands = list(map(str, input.split()))

x, y = 1, 1

for c in commands: 
    match c:
        case "L":
            if y > 1:
                y -= 1
        case "R":
            if 5 > y:
                y += 1
        case "U":
            if x > 1:
                x -= 1
        case "D":
            if 5 > x:
                x += 1

print(x, y)