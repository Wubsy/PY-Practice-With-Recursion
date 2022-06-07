# Write code for algorithm 1 below

def print_to_zero(num):
    if num == 0:
        print(0)
    else:
        print(num)
        print_to_zero(num-1)


print_to_zero(10)
