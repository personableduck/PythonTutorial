def recursive(input_n):
    if input_n <=0:
        return input_n
    else:
        output_n = recursive(input_n-1)
        print output_n
        return output_n

a=recursive(3)
