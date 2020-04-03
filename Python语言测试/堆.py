# import heapq
#
# a = set()
# a.add(1)
# a.add(2)
# print(a)

#

class Solution:
    def maxEvents(self,events):
        events.sort(key=lambda x:x[1],reverse=True)
        print(events)
        visited = {}
        for s,e in events:
            print()
            print()
            for day in range(e,s-1,-1):
                print(day)
                # if day not in visited:
                #     print(day)
                #     visited[day]=0
                #     break
        print(visited)
        return len(visited)

s = Solution()
s.maxEvents([[1,2],[2,2],[3,3],[3,4],[3,4]])