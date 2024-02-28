'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example:

Input: strs = ["flower","flow","flight"]
Output: "fl"

'''


def longestCommonPrefix(strs):

    # Find the minimum length among the strings
    min_len = min(len(s) for s in strs)

    # Binary search in the interval (0...min_len)
    low, high = 0, min_len - 1

    while low <= high:
        mid = (low + high) // 2

        if all(strs[0][:mid + 1] == s[:mid + 1] for s in strs[1:]):
            # Common prefix found, go to the right half
            low = mid + 1
        else:
            # No common prefix, go to the left half
            high = mid - 1

    # Return the common prefix found
    return strs[0][:high + 1]

# Example usage:
strs = ["flower", "flow", "flight"]
output = longestCommonPrefix(strs)
print(output)  # Should print "fl"









    





