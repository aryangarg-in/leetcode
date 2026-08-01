# class Solution:
#     def fib(self, n: int) -> int:
        
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
        
#         return self.fib(n - 1) + self.fib(n - 2)
class Solution:
    def func(self , num):
        if num ==0 or num==1:
            return num

        return self.func(num-1) + self.func(num-2)

    def fib(self, n: int) -> int:
        return self.func(n)
        

         
        
       
        