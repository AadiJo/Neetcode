class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")",
                    "[" : "]",
                    "{" : "}"}
        stack = []
        if (len(s) % 2) != 0:
            return False
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            elif i in brackets.values():
                try:
                    if brackets.get(stack.pop()) != i:
                        return False
                except IndexError:
                    return False
        if len(stack) > 0:
            return False
        return True