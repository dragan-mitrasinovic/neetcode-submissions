class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        stack = []

        for char in s:
            if char in "[({":
                stack.append(char)
                continue
            
            if not stack or stack[-1] != closed_to_open[char]:
                return False
            
            stack.pop()
        
        return len(stack) == 0
            