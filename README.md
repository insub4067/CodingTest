# CodingTest 공부정리 (Python)

## dfs

## bfs

## deque

deque는 Python의 collections 모듈에서 제공하는 양방향 큐로, 리스트와 유사하지만 양쪽 끝에서 빠르고 효율적으로 요소를 추가하거나 제거할 수 있는 자료 구조입니다. deque는 Double-Ended Queue의 약자로, 큐의 양쪽 끝에서 요소를 추가하거나 제거하는 작업을 O(1) 시간 안에 수행할 수 있어, 리스트보다 효율적입니다.

주요 특징: 양방향으로 삽입과 삭제가 가능합니다. 앞쪽에서 추가/삭제, 뒤쪽에서 추가/삭제 모두 지원합니다.
리스트는 양쪽 끝에서 요소를 추가하거나 삭제하는 데 O(n) 시간이 걸릴 수 있지만, deque는 O(1)의 시간 복잡도를 보장합니다.
큐, 스택, 덱 등 다양한 방식으로 활용 가능합니다.

```python
from collections import deque

l = [1,2,3,4]

dq = deque(l) # deque([1, 2, 3, 4])
dq.append(5) # deque([1, 2, 3, 4, 5])
dq.append(6) # deque([6, 1, 2, 3, 4, 5])
first = dq.popleft() # 6
```

## heapq

heapq는 Python에서 힙 큐(우선순위 큐)를 효율적으로 사용할 수 있도록 지원하는 모듈입니다. 힙은 이진 트리 기반의 자료 구조로, 최소값이나 최대값을 빠르게 찾아내기 위한 우선순위 큐를 구현할 때 유용합니다. heapq 모듈은 기본적으로 최소 힙(min-heap)을 제공합니다.

```python
import heapq

ints = [40, 50, 20]

heapq.heapify(ints) # [20, 50, 40]
min = heapq.heappop(ints) # 20
heapq.heappush(ints, 100) # [40, 50, 100]
```
