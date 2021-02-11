import sys
import heapq

nums = int(input())
heap = []

for _ in range(nums):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)