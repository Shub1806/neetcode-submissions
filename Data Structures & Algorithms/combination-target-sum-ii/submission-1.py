class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.ans=[]
        self.func(0,target, [], candidates)
        return self.ans 


    def func(self, ind, sum, nums, candidates):

        if sum == 0:
            self.ans.append(nums[:])
            return 
        if sum < 0 or ind == len(candidates):
            return

        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > sum:
                break
            nums.append(candidates[i])
            self.func(i + 1, sum - candidates[i], nums, candidates)
            nums.pop()