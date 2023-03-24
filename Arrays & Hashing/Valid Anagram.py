class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strList1 = [*s]
        strList2 = [*t]

        strList1 = sorted(strList1)
        strList2 = sorted(strList2)

        if strList1 != strList2:
            return False
        else:
            return True