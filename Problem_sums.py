## problema de programação e matematica

'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

'''
## a priori root = int(n**0.5)




def numSquares2(n):
    # pego a raiz do bixo 

    root    = int(n**0.5)
    ## n = (root)² + jk
    count_list = []


    ## comeco com o maior root para a metade: --> 

    for i in range(0, root + 1):
        jk      = (n - i**2) ## n = (root)² + (n - (root)²) -->  o resto = (n-(root)²) = jk 
        count   = 1

        while jk > 0 :
            count  += 1
            root_k = int(jk**0.5)
            jk     = jk -root_k ** 2 
        count_list.append(count)
    
    return count_list



def encontrar_menor_valor(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    menor_valor = lista[0]
    for elemento in lista:
        if elemento < menor_valor:
            menor_valor = elemento
    return menor_valor


def Solution(n): 
    return encontrar_menor_valor(numSquares2(n))



def numSquares(n):
    # Initialize a table to store the minimum number of perfect squares
    dp = [float('inf')] * (n + 1)
    
    # Base case: 0 requires 0 perfect squares
    dp[0] = 0
    
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Iterate over all possible perfect squares less than or equal to i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    
    return dp[n]

# Test cases
print(numSquares(12))  # Output: 3
print(numSquares(10))  # Output: 2

        