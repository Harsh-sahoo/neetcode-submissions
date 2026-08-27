class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp_arr = []
        for i in operations:
            
            if i not in ["+", "C", "D"]:
                temp_arr.append(int(i))
            elif(i=="+"):
                temp_arr.append(temp_arr[-1]+temp_arr[-2])
            elif(i=="C"):
                temp_arr.pop()    
            else:
                temp_arr.append(temp_arr[-1]*2)
        return sum(temp_arr)