// 문자열 재정렬.py

input = "K1KA5CB7"
input = "AJKDLSI412K4JSJ9D"

l = list(input)
l.sort()

s = ""
sum = 0

for i in l:
    if i.isdigit():
        sum += int(i)
    else:
        s += i
        
if sum > 0:
    s += str(sum)

print(s)
