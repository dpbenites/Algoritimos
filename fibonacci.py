class Solution:
    def fib(self, n: int):

        f0, f1   = 0,1 
        list_seq = []
        list_seq.append(f0)
        list_seq.append(f1)

        if n == 0:
            return 0 
        elif n ==1:
            return 1
        else:
            for i in range(2,n+1):
                fn = list_seq[i-1] + list_seq[i-2]
                list_seq.append(fn)
            
            return list_seq[-1]
        
    def tribonacci(self, n: int) -> int:
        ## tribonacci sequence
        ## start with a start list

        start_list = [0,1,1]


        if n<3:
            return start_list[n]
        
        else:
            for n in range(3, n+1):
                Tn = start_list[n-1] + start_list[n-2] + start_list[n-3]
                start_list.append(Tn)
            
            return start_list[-1]
            



x = Solution()
x = x.fib(n = 10)
print(x)