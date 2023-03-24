class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        newList = []
        for i in digits:
            i = str(i)
            number = ''.join((number,str(i)))
        number = int(number)
        number = number + 1
        number = str(number)
        for i in number:
            i = int(i)
            newList.append(i)
        return newList
