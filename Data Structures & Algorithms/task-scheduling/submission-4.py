class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        #maxHeap is available tasks to perform, highest freq highest priority
        #q is tasks on cooldown, first cool first uncool and done
        while maxHeap or q:
            time += 1
            if maxHeap:
                #if we have available tasks, do lem
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    #if task still has more
                    q.append([cnt, time + n])
            else:
                time = time
                #no available tasks
                #could try doing nothing
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
            
        return time