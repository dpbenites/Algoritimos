'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example:

Input: strs = ["flower","flow","flight"]
Output: "fl"

'''

#strs = ["flower","flow","flight"]  # é uma lista

def LCP(strs:list):

    #ordena as strings em ordem de tamanho
    sorted_strs = sorted(strs, key=lambda x: len(x))
    min_str     = sorted_strs[0]  # no caso flow 
    low , high  = 0 , len(min_str) -1 
    mid   = (low + high) // 2

    #dont make anything




