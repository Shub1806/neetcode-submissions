class Solution:
    # Recursive function to find all subsequences with the given target sum
    def func(self, v, i, sum, v2, ans):
        # Base case: if the sum is zero, add the current subsequence to the result
        if sum == 0:
            ans.append(v2[:])
            return
        
        # Base case: if the sum becomes negative or no elements are left
        if sum < 0 or i < 0:
            return
        
        # Exclude the current element and move to the next
        self.func(v, i - 1, sum, v2, ans)
        
        # Include the current element in the subsequence
        v2.append(v[i])
        
        # Recursively call the function with the included element
        self.func(v, i, sum - v[i], v2, ans)
        
        # Backtrack by removing the last added element
        v2.pop()

    # Main function to find all unique combinations of candidates that sum to the target
    def combinationSum(self, candidates, target):
        ans = []
        
        # Create a copy of the candidates list for easier manipulation
        v = candidates[:]
        
        # Start the recursive process
        self.func(v, len(v) - 1, target, [], ans)
        
        return ans