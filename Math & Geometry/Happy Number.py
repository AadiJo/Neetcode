class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        result = 0
        dInput = n

        while seen.get(dInput) == None and result != 1:
            result = 0
            for i in str(dInput):
                i = int(i)
                result += (i**2)
                
            seen.update({dInput: result})
            dInput = result
            
            

        if result == 1:
            return True
        else:
            return False
            