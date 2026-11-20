class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        v = nums[:]

        self.func(v, len(v) -1, target, [], ans)

        return ans 


    def func(self, v, i, sum, v2, ans):

        if sum == 0:
            ans.append(v2[:])
            return
        
        if sum < 0 or i < 0:
            return

        self.func(v, i-1, sum, v2, ans)

        v2.append(v[i])

        self.func(v, i, sum - v[i], v2, ans)

        v2.pop()