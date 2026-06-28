class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # m = heap length
        # BRUTE FORCE Idea :
        #
        # if you sort you have TC : O (nlogn), SC : O(1)
        #
        # Optimal Idea :
        # Use a min heap
        # putting a value is TC : O (log k) and SC : O (k)
        # TC : O ( n*logk )
        # SC : O( k )
        #
        
        min_heap = []

        for number in nums:
            heapq.heappush(min_heap, number) # TC : O(logk)

            if len(min_heap) > k:
                heapq.heappop(min_heap) # TC : O(logk)
        
        
        return min_heap[0]
