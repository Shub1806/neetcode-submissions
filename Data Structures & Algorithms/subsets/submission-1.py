class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        current = []

        self.backtrack(0, len(nums), nums, current, ans)

        return ans
    
    def backtrack(self, index, n, nums, current, ans):
        if index == n:
            ans.append(current[:])
            return

        self.backtrack(index+1, n, nums, current, ans)

        current.append(nums[index])

        self.backtrack(index+1, n, nums, current, ans)

        current.pop()
        
        