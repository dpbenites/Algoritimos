
## Binary Search algorithm implementation

def BinarySearch(sequence, item):
    
    start_index = 0 
    end_index   = len(sequence) - 1

    while start_index <= end_index:

        mid_point     =  start_index + (end_index - start_index)//2
        mid_point_val =  sequence[mid_point]

        if item == mid_point_val:
            return mid_point
        
        elif item < mid_point_val:
            end_index = mid_point - 1

        else:
            start_index = mid_point + 1
        
    return None

## vamos usar a funcao

lista_seq = [1, 4, 5 , 8, 10 , 14, 39, 41 , 45, 90 ,120 ,190 ,200]

index  = BinarySearch(sequence = lista_seq , item = 45)

print(f'O index do número procurado é : {index}')

    




