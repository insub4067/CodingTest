# 코테 공부정리 (Python)

1. [DFS](#DFS)
2. [BFS](#BFS)
3. [DFS vs BFS](#DFS-vs-BFS)
4. [이분매칭](#이분매칭)
5. [deque](#deque)
6. [heapq](#heapq)

## 📚DFS <a name="DFS"></a>
### ✔️ 설명
**DFS**(Depth-First Search, 깊이 우선 탐색)는 그래프나 트리의 모든 노드를 탐색할 때 사용하는 알고리즘입니다. DFS는 한 경로로 최대한 깊이 탐색한 후, 더 이상 갈 곳이 없으면 이전 정점으로 돌아가 다른 경로를 탐색하는 방식으로 작동합니다.

### ✔️ 특징
- 스택(Stack) 자료 구조를 기반으로 동작합니다. 이를 구현할 때 실제 스택을 사용할 수도 있지만, 재귀 호출 시 내부적으로 스택이 사용됩니다.
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

### ✔️ 활용 예시 (재귀) [문제: 유기농 배추](https://www.acmicpc.net/problem/1012)
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
    
    for dy, dx in direction:
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

### ✔️ 활용 예시 (스택) [문제: 유기농 배추](https://www.acmicpc.net/problem/1012)
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
        for dy, dx in direction:
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

## 📚BFS <a name="BFS"></a>
### ✔️ 설명
**BFS**(Breadth-First Search)는 그래프 또는 트리에서의 탐색 알고리즘 중 하나로, 너비 우선 탐색 방법을 사용합니다. BFS는 먼저 시작 노드에서 가까운 노드를 탐색한 후 점차 멀리 있는 노드로 이동합니다. 이를 위해 큐(Queue)를 사용하여 현재 탐색 중인 노드의 이웃을 차례대로 저장하고 탐색합니다.

### ✔️ 특징
- 최단 경로 탐색: BFS는 가중치가 없는 그래프에서 두 노드 간의 최단 경로를 보장합니다.
- FIFO 큐 사용: 방문할 노드를 큐에 저장하고, 먼저 들어온 노드를 먼저 탐색합니다.

### ✔️ 동작순서
1. 시작 노드를 큐에 삽입합니다.
2. 큐에서 노드를 하나 꺼내고 해당 노드를 방문합니다.
3. 방문한 노드에 연결된 인접 노드를 모두 큐에 삽입합니다.
4. 큐가 빌 때까지 이 과정을 반복합니다.

### ✔️ 활용 예시 [문제: 숨바꼭질](https://www.acmicpc.net/problem/1697)
```python
from collections import deque

 # 현재 위치, 목표 도달 위치
N, K = 5, 17
visited = [False] * 100001  
visited[N] = True  

def bfs():
    q = deque([(N, 0)])
    while q:
        n, sec = q.popleft()
        if n == K:
            # 목표 도달시 출력 후 종료
            print(sec) 
            break
        # 현재 위치에서 (-1, +1, *2) 3가지 가능성이 있는 케이스를 계산한다.
        for next in (n - 1, n + 1, n * 2):
            # 방문처리와 재방문 방지
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = True  
                q.append((next, sec + 1)) 

bfs()
```

## 📚DFS vs BFS <a name="DFS-vs-BFS"></a>
### ✔️ 탐색 방식의 차이
**DFS**는 하나의 경로를 끝까지 탐색한 후 다시 돌아와서 다른 경로를 탐색합니다. 즉, 깊이 우선으로 탐색을 진행합니다. 이를 위해 스택(Stack) 자료 구조나 재귀 함수 호출을 사용합니다.
먼저 깊이(depth)를 우선으로 탐색하므로, 한 노드에서 갈 수 있는 경로를 모두 탐색한 뒤에야 다른 경로로 돌아옵니다.

**BFS**는 먼저 시작 노드에서 가까운 노드를 탐색하고, 그 다음으로 멀리 있는 노드를 탐색합니다. 즉, 너비 우선으로 탐색을 진행합니다. 이를 위해 큐(Queue) 자료 구조를 사용합니다.
먼저 동일한 레벨(level)의 모든 노드를 탐색한 후, 다음 레벨로 이동합니다.

### ✔️ 자료 구조
**DFS**는 주로 스택(재귀 호출 시 시스템 스택)을 사용하여 가장 최근에 방문한 노드를 기준으로 다음 탐색을 진행합니다.  
**BFS**는 주로 큐를 사용하여 먼저 들어온 노드부터 차례로 탐색합니다.

### ✔️ 사용 예시
1) DFS 사용 예시
    - 경로 탐색: 특정 노드에서 특정 노드로 가는 경로를 찾거나, 미로 탐색 등의 문제에 적합합니다.
    - 백트래킹: 가능한 모든 경우를 시도해야 할 때 사용됩니다. 예를 들어, 퍼즐 문제, 조합/순열 문제 등에서 DFS가 유용합니다.
    - 사이클 탐지: DFS는 그래프에서 사이클이 존재하는지를 확인하는 데 적합합니다.

2) BFS 사용 예시
    - 최단 경로 탐색: 가중치가 없는 그래프에서 두 노드 간의 최단 경로를 찾는 데 적합합니다.
    - 계층 탐색: 한 레벨씩 순차적으로 탐색해야 하는 문제에 유용합니다. 예를 들어, 소셜 네트워크에서 친구 관계를 탐색할 때 같은 레벨의 사람들부터 차례로 탐색하는 것이 유리합니다.
    - 레벨 탐색: 트리의 각 레벨에서 노드를 순차적으로 탐색하는 경우 BFS가 적합합니다.

## 📚이분매칭 <a name="이분매칭"></a>
### ✔️ 설명
이분 그래프에서 두 개의 독립된 집합 사이에서 가능한 최대 매칭을 찾는 문제입니다. 이분 그래프는 두 개의 집합으로 정점들이 나뉘어 있으며, 각 간선은 서로 다른 집합의 정점 사이에서만 연결됩니다.

### ✔️ 특징
- 매칭(Matching): 이분 매칭에서 "매칭"은 간선의 부분집합으로, 각 정점이 최대 하나의 간선에만 포함되도록 선택됩니다. 즉, 각 정점이 한 번만 매칭에 참여할 수 있습니다.
- 최대 매칭(Maximum Matching): 가능한 한 최대한 많은 간선을 선택하여 매칭을 구성하는 것을 말합니다. 최대 매칭을 구하는 것이 이분 매칭 문제의 핵심입니다.
- DFS와 BFS의 활용: 이분 매칭을 해결하는 일반적인 방식은 깊이 우선 탐색(DFS)을 사용해 교환 경로를 탐색하는 것입니다. 경우에 따라 BFS(너비 우선 탐색)도 보조적으로 사용됩니다.
  
### ✔️ 예시
- 구인/구직 매칭: 두 집합 중 하나를 구직자, 다른 하나를 일자리로 설정하여 각각의 구직자와 일자리가 연결된 경우, 가능한 최적의 매칭을 찾을 수 있습니다.
- 작업 할당 문제: 작업을 수행할 수 있는 기계나 사람과 각 작업 간의 최적 할당을 찾는 데 사용됩니다.
- 대학 입시, 파티 구성: 학생-전공 매칭, 파티나 그룹을 구성하는 등의 문제에도 이분 매칭 알고리즘이 사용됩니다.

### ✔️ 예시 [열혈강호](https://www.acmicpc.net/problem/11375)
```python
import sys

sys.setrecursionlimit(100000)

# 작업자, 작업
N, M = map(int, input().split()) 

tasks = {}
assigned = [None] * (M + 1) # 매칭 상태를 기록

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    tasks[i] = line[1:]

# 매칭을 수행
def assign(staff, visited): 
    for task in tasks[staff]:
        if visited[task]:  
            continue
        visited[task] = True
        # 작업자가 할당되어 있지 않거나 이미 할당되어있다면 해당 작업자가 다른 작업으로 양보할 수 있는지 확인한다.
        if assigned[task] is None or assign(assigned[task], visited): 
            assigned[task] = staff 
            return True
    return False

for i in range(1, N + 1):
    # 작업자를 순화할때 마다 작업 visited를 초기화한다.
    visited = [False] * (M + 1) 
    assign(i, visited)

print(sum(1 for a in assigned if a != None))
```

## 📚deque <a name="deque"></a>
### ✔️ 설명
**deque**는 Python의 collections 모듈에서 제공하는 양방향 큐로, 리스트와 유사하지만 양쪽 끝에서 빠르고 효율적으로 요소를 추가하거나 제거할 수 있는 자료 구조입니다. deque는 Double-Ended Queue의 약자로, 큐의 양쪽 끝에서 요소를 추가하거나 제거하는 작업을 O(1) 시간 안에 수행할 수 있어, 리스트보다 효율적입니다.

### ✔️ 특징
- 양방향으로 삽입과 삭제가 가능합니다.
- 앞쪽에서 추가/삭제, 뒤쪽에서 추가/삭제 모두 지원합니다.
- 리스트는 양쪽 끝에서 요소를 추가하거나 삭제하는 데 O(n) 시간이 걸릴 수 있지만, deque는 O(1)의 시간 복잡도를 보장합니다.
- 큐, 스택, 덱 등 다양한 방식으로 활용 가능합니다.

### ✔️ 간단 사용방법
```python
from collections import deque

l = [1,2,3,4]

dq = deque(l) # deque([1, 2, 3, 4])
dq.append(5) # deque([1, 2, 3, 4, 5])
dq.appendleft(6) # deque([6, 1, 2, 3, 4, 5])
first = dq.popleft() # 6
last = dq.pop() # 5
print(dq) # deque([1, 2, 3, 4])
```

## 📚heapq <a name="heapq"></a>
### ✔️ 설명
**heapq**는 Python에서 힙 큐(우선순위 큐)를 효율적으로 사용할 수 있도록 지원하는 모듈입니다. 힙은 이진 트리 기반의 자료 구조로, 최소값이나 최대값을 빠르게 찾아내기 위한 우선순위 큐를 구현할 때 유용합니다. heapq 모듈은 기본적으로 최소 힙(min-heap)을 제공합니다.

### ✔️ 예시
```python
import heapq

ints = [40, 50, 20]

heapq.heapify(ints) # [20, 50, 40]
min = heapq.heappop(ints) # 20
heapq.heappush(ints, 100) # [40, 50, 100]
```
