class Solution(object):
    def reverse(self, x):

        """
        :type x: int
        :rtype: int
        """

        sum = 0
        sign = 1

        if x < 0 :
            sign = -1
            x= x*-1
        
        while x > 0:
            rem = x%10
            sum = sum*10 + rem
            x=x//10


        if not -2**31 < sum <  2**31 - 1:
            return 0


        return sum*sign


        