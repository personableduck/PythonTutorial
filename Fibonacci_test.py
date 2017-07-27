def get_fib(position):
    if (position == 0): 
        return 0; 
    if (position == 1): 
        return 1;
    
    first = 0
    second = 1
    count = 2
    
    def recursive_sum(first,second,count,position):
        if count >= position:
            #print first+second
            return first+second
        else:
            count+=1
            sol=recursive_sum(second,first+second,count,position)
            #print sol
            return sol

    sol = recursive_sum(first,second,count,position)
    
    return sol

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
