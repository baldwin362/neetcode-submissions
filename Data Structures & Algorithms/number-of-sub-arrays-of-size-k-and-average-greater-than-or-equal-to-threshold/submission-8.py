class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cur_sum = sum(arr[:k-1])
        for L in range(len(arr)-k+1):
            cur_sum += arr[L+k-1]
            if cur_sum/k>=threshold:
                res +=1
            cur_sum -=  arr[L]
        return res 

        #Here instead of having two pointers, we just traverse the array once 
        # then we just substract the last value in the "slicing" (we're actually summing the slice)
        # in order to simulate the fact that the window in getting smaller from the left side 
        # in order to extend it to the right side
        # the slicing method insures that the values we are considering always englobe k values 