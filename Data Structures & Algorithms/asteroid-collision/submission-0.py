class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
                continue
            if len(stack) > 0 and asteroids[i] < 0:
                while stack:
                    if stack[-1] < abs(asteroids[i]):
                        stack.pop()
                    elif stack[-1] == abs(asteroids[i]):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroids[i])

                
            else:
                stack.append(asteroids[i])
        return stack
                