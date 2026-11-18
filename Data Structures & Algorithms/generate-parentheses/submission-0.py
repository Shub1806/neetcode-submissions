class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        ans = []

        self.backtrack(0,0,n,"",ans)
        return ans
    
    def backtrack(self,open_count:int,close_count:int,n:int,    current: str, ans:list):

        if open_count == close_count == n:
            ans.append(current)
            return

         
        if open_count < n:
            self.backtrack(open_count + 1, close_count, n, current + '(', ans)
        
        if close_count < open_count:
            self.backtrack(open_count, close_count + 1, n, current + ')', ans)
