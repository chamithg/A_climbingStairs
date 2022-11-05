class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        output =0
        

        def climb(steps,output):
            
            if steps>= 1:
                output +=1
                steps-=1
                climb(steps,output)
            if steps>=2:
                output+=1
                steps -=2
                climb(steps,output)
            if steps == 0:
                print(output)
                return
        climb(n,output)
        print(output)  
        return output
              
        
        
    
obj = Solution()

obj.climbStairs(40)               