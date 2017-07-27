def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

get_fib(9)
get_fib(11)
get_fib(0)
