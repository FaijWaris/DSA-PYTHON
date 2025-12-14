class Solution:
    @staticmethod
    def func(num):
        if num == 0 or num == 1:
            return num
        return Solution.func(num - 1) + Solution.func(num - 2)

    def fibonacci(self, n):
        answer = Solution.func(n)
        return answer
print(Solution().fibonacci(6))