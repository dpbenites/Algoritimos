
'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

## lets start with a function that give us the solutions

def Solution(n:int):

    dp = [0 for _ in range(n+1)]
    dp[-1]= 1
    dp[-2] = 1
    index = n -2

    while dp[0] == 0:
        dp0 , dp1 = dp[index +1] , dp[index +2]
        val = dp0 + dp1
        dp[index] = val
        index = index  -1
    
    return dp[0]





print(Solution(5))