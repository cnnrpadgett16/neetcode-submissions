class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        [2,2,2,2,5,5,5,8], k=3, threshold=4
        output = 3

        initialize a count to keep track of the sub-arrays and two pointers left (right is initilized in the for loop)
        initialize a set to keep track of elements in our window
        progress the right pointer
            if length of window == k: 
                avg = sum() / k
                if avg >= threshold:
                    increment count
            check to see if we are still in the window size k, if not we will remove the value at the left pointer
                increment the left pointer
            add the newest right value to the set

        return the count 
        '''
        count = 0
        window = deque()
        left = 0
        '''
         lr
        [2,2,2,2,5,5,5,8]
        window = set(2,2,2)
        '''
        # for right in range(len(arr)):
        #     window.append(arr[right])
        #     if right - left + 1 > k:
        #         window.popleft()
            
        #     if len(window) == k:
        #         avg = sum(window) / k
        #         if avg >= threshold:
        #             count += 1

        # return count
        count = 0
        curSum = sum(arr[:k - 1])

        for l in range(len(arr) - k + 1):
            curSum += arr[l + k - 1]
            if (curSum / k) >= threshold:
                count += 1
            curSum -= arr[l]
        return count
