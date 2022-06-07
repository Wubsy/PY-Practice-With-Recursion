# Write code for algorithm 2 below
def print_to_number(num, curr=1):
    if num == curr:
        print(num)
    else:
        print(curr)
        print_to_number(num, curr+1)


print_to_number(18)
