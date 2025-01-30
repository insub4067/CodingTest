import heapq

def solution(operations):
    stack = []

    for o in operations:
        o1, o2 = o.split()

        if o1 == "I":
            heapq.heappush(stack, int(o2))            
            continue
        if stack:
            if o1 == "D" and o2 == "1":
                stack.sort()
                stack.pop()
            elif o1 == "D" and o2 == "-1":
                heapq.heappop(stack)

    stack.sort()
    if stack:
        return [stack[-1], stack[0]]
    else:
        return [0, 0]