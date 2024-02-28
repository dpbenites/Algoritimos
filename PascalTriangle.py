'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''


def Pascal(numRows:int):
    start = [1]
    seq   = []
    seq.append(start)
    rows = 1 

    while rows < numRows:

        row_list = seq[rows-1]
        rows += 1
        temp_list  = [0]*rows
        temp_list[0], temp_list[-1] = 1 , 1
        
        
        for k in range(1, len(temp_list)-1):
            temp_list[k] = row_list[k] + row_list[k-1]
        
        seq.append(temp_list)
    
    return seq



        
print(Pascal(numRows=6))


