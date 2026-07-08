# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs,0,len(pairs)-1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e:int)->List[Pair]:
        if (e-s+1)<=1:
            return pairs
        m = (e+s)//2 # m : int 
        self.mergeSortHelper(pairs,s,m)
        self.mergeSortHelper(pairs, m+1,e)
        self.merge(pairs, s, m, e)
        return pairs
    
    def merge(self, arr: list[Pair], s:int, m: int, e: int)->None:
        # [1,2] and [0]
        # k = 0
        # i = s
        # j = m+1
        k = s
        i = 0
        j = 0
        left_half = arr[s:m+1]
        right_half = arr[m+1:e+1]
        while i<len(left_half) and j<len(right_half):
            if left_half[i].key<=right_half[j].key:
                arr[k] = left_half[i]
                i+=1
                
            else:
                arr[k] = right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
            arr[k] = left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            arr[k] = right_half[j]
            j+=1
            k+=1
        


        

