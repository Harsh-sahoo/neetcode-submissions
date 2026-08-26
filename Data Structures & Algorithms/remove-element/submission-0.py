class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []

        for i in nums:
            if (i!=val):
                temp.append(i)
        
        for index, value in enumerate(temp):
            nums[index] = value
        return len(temp)