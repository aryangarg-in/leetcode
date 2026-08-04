class Solution:
    def longestPalindrome(self, s: str) -> int:
       result = 0
       counter = defaultdict(int)

       for  char in s:
            counter[char]+=1

            if counter[char]%2 == 0:
                result+=2
            
       for count in counter.values():   
            if count%2 !=0:
                result+=1
                break

       return result



        

        