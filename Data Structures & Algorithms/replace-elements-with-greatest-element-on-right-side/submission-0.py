class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for index, value in enumerate(arr):
            if(index==len(arr)-1):
               arr[index] = -1
            else:
                arr[index]= max(arr[index+1:len(arr)])
        return arr