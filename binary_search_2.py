def binary_search(input_array, value):
    
    endl=len(input_array)-1
    startl=0
    i=(endl-startl)/2
    if input_array[i] == value: 
        return i   
          
    while (i != 0 and i != endl):   
 
        if input_array[i] < value: 
            if endl-i == 1:
                i=i+1
            else:    
                i=(endl-i)/2+i

        else:
            i/=2 
        if input_array[i] == value: 
            return i
        
    return -1
    

test_list = [1,3,9,11,15,19]
test_val1 = 11
test_val2 = 19
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
