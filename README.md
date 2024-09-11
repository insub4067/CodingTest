# 코테 공부정리 (Python)

## 📚DFS

### ✔️ 설명
DFS(Depth-First Search, 깊이 우선 탐색)는 그래프나 트리의 모든 노드를 탐색할 때 사용하는 알고리즘입니다. DFS는 한 경로로 최대한 깊이 탐색한 후, 더 이상 갈 곳이 없으면 이전 정점으로 돌아가 다른 경로를 탐색하는 방식으로 작동합니다.

### ✔️ 특징
- 스택(Stack) 자료 구조를 기반으로 동작합니다. 이를 구현할 때 실제 스택을 사용할 수도 있지만, 재귀를 통해 스택을 대신할 수도 있습니다.
- 그래프 또는 트리의 모든 노드를 방문하는데 적합합니다.
- 깊이를 우선적으로 탐색하므로 특정 경로의 끝까지 도달한 후, 그 경로가 완료되면 다시 돌아가서 다른 경로를 탐색합니다.
- 방문한 노드를 기억하는 방문 배열(visited)을 사용하여 한 번 방문한 노드를 다시 방문하지 않도록 방지합니다.

### ✔️ 재귀방식 vs 스택방식
1) 재귀 방식
- 재귀 호출을 통해 스택의 역할을 대신하며, 파이썬의 함수 호출 스택을 사용합니다.
- ‼️중요‼️ 하지만 재귀 깊이가 깊어질 경우 스택 오버플로우가 발생할 수 있습니다. 따라서 탐색 깊이가 깊어지면 sys.setrecursionlimit()을 사용하여 재귀 한도를 늘리기도 합니다. 
- 코드는 간결하지만, 큰 그래프나 깊은 탐색에서는 위험할 수 있습니다.
2) 스택 방식
- 명시적인 스택 자료 구조를 사용하여 스택 오버플로우 문제를 해결합니다.
- 재귀 호출 없이도 구현 가능하며, 메모리 관리에 있어서 좀 더 효율적일 수 있습니다.
- 코드가 조금 더 복잡해질 수 있지만, 재귀를 피할 수 있는 장점이 있습니다.

### ✔️ 예시 (재귀) [🔗](https://www.acmicpc.net/problem/1012)
```python
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 좌우 상하
m, n, k = 10, 8, 17 # 농장의 (가로, 세로, 배추 갯수)

farm = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
visited = [[False] * m for _ in range(n)]  
answer = 0

def dfs(x, y, farm, visited):
    visited[y][x] = True
    
    for dx, dy in direction:
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < m and 0 <= ny < n:
            if farm[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny, farm, visited)

for y in range(n):
    for x in range(m):
        if not visited[y][x] and farm[y][x] == 1:
            dfs(x, y, farm, visited)
            answer += 1

print(answer) # 5
```

### ✔️ 예시 (스택) [🔗](https://www.acmicpc.net/problem/1012)
```python
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 좌우 상하
m, n, k = 10, 8, 17 # 농장의 (가로, 세로, 배추 갯수)

farm = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
visited = [[False] * m for _ in range(n)]  
answer = 0

def dfs(x, y): 
    stack = [(x, y)]
    visited[y][x] = True

    while stack:
        cx, cy = stack.pop()
        for dx, dy in direction:
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and farm[ny][nx] == 1:
                    visited[ny][nx] = True
                    stack.append((nx, ny))

for y in range(n):
    for x in range(m):
        if not visited[y][x] and farm[y][x] == 1:
            dfs(x, y)
            answer += 1

print(answer) # 5
```

## 📚BFS

### ✔️ 설명

### ✔️ 특징

### ✔️ 예시

## 📚deque

### ✔️ 설명
deque는 Python의 collections 모듈에서 제공하는 양방향 큐로, 리스트와 유사하지만 양쪽 끝에서 빠르고 효율적으로 요소를 추가하거나 제거할 수 있는 자료 구조입니다. deque는 Double-Ended Queue의 약자로, 큐의 양쪽 끝에서 요소를 추가하거나 제거하는 작업을 O(1) 시간 안에 수행할 수 있어, 리스트보다 효율적입니다.

### ✔️ 특징
- 양방향으로 삽입과 삭제가 가능합니다.
- 앞쪽에서 추가/삭제, 뒤쪽에서 추가/삭제 모두 지원합니다.
- 리스트는 양쪽 끝에서 요소를 추가하거나 삭제하는 데 O(n) 시간이 걸릴 수 있지만, deque는 O(1)의 시간 복잡도를 보장합니다.
- 큐, 스택, 덱 등 다양한 방식으로 활용 가능합니다.

```python
from collections import deque

l = [1,2,3,4]

dq = deque(l) # deque([1, 2, 3, 4])
dq.append(5) # deque([1, 2, 3, 4, 5])
dq.appendleft(6) # deque([6, 1, 2, 3, 4, 5])
first = dq.popleft() # 6
```

## 📚heapq

### ✔️ 설명
heapq는 Python에서 힙 큐(우선순위 큐)를 효율적으로 사용할 수 있도록 지원하는 모듈입니다. 힙은 이진 트리 기반의 자료 구조로, 최소값이나 최대값을 빠르게 찾아내기 위한 우선순위 큐를 구현할 때 유용합니다. heapq 모듈은 기본적으로 최소 힙(min-heap)을 제공합니다.


### ✔️ 예시
```python
import heapq

ints = [40, 50, 20]

heapq.heapify(ints) # [20, 50, 40]
min = heapq.heappop(ints) # 20
heapq.heappush(ints, 100) # [40, 50, 100]
```
