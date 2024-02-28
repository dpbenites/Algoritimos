'''
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

'''

def solve(num):
    ## lista auxiliar
    L = [1 for _ in range(len(num))]

    for i in range(1, len(L)):
        subproblems = [ L[k] for k in range(i) if num[k] < num[i] ]
        L[i] = 1 + max(subproblems, default=0)

    return max(L, default=0)



print(solve(num=[2,3,7,101]))
