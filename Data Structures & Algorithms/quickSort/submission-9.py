# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs
    def quickSortHelper(self, arr: List[Pair], s:int, e:int) -> List[Pair]:
        if e-s+1<=1:
            return arr
        pivot = arr[e]
        k = s 
        for i in range(s,e):
            if arr[i].key < pivot.key:
                arr[k], arr[i] = arr[i], arr[k]
                k+=1
        arr[k], arr[e] = arr[e], arr[k]
        self.quickSortHelper(arr, s, k-1)
        self.quickSortHelper(arr, k+1, e)
        return arr


