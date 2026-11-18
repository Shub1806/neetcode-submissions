class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = n

        if num < 0:
            return 1.0 / self.pow(x,-num)

        return self.pow(x,num)

    
    def pow(self, x, n):

        if n == 0:
            return 1.0

        if n == 1:
            return x

        if n%2 == 0:
            return self.pow(x*x, n//2)

        return x * self.pow(x, n-1)
        