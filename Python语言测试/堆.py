import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(heapq.heappop(nums))
heapq.heappush(nums,-10)
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.nlargest(1,nums))
print(heapq.nlargest(1,nums))
