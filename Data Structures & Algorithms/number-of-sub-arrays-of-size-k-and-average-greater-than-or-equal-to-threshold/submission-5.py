class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        for L in range(len(arr)-k+1):
            cur_sum = arr[L]
            for R in range(L+1, min(len(arr),L+k)):
                    cur_sum += arr[R]
            if cur_sum/k >= threshold:
                output +=1
        return output 
