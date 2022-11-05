class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        this is a dinamic cording problem, solving it recursive works but takes a lot of time.
        also it solves same thing over and over again. for example imagine if there is only two steps
        that should be the same number of ways to climb of any n nuber last two steps. so solving this
        dinamicaly is the best way to do it.
        this is the same concept of fibanachi sequence
        """
        
        if n <= 2: return n
        x,y = 1,2
        for i in range(3,n):
            temp = y
            y = x+y
            x = temp
            
        return x+y
            
            
        
              
        
        

obj = Solution()

print(obj.climbStairs(40))               