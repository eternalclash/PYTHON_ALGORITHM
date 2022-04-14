class Solution:
    def reverse(self, x: int) -> int:
        reversed = str(x)[::-1] # reverse the casted string input
        
        if reversed.endswith("-"):
            reversed = -int(reversed[:-1]) # fix the negative sign ending.
            
        reversed = int(reversed) # cast back to int.
        
        if reversed >= (2**31)-1 or reversed <= -(2**31): # check if it fits within validity constraints.
            return 0
        
        return reversed
