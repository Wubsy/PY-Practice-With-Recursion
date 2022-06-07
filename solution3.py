# Write code for algorithm 3 below

def print_fibonacci_sequence_until(num, curr=2, num_one=0, num_two=1):
    if curr-1 == num:
        print(num_two)
    elif curr-2 == num:
        print(num_one)
    else:
        num_one += num_two
        num_two += num_one
        curr += 2

        print_fibonacci_sequence_until(num, curr, num_one, num_two)


# Expected result 28657
print_fibonacci_sequence_until(23)

""" Solution code
# I'm not fond of how it relies on using the function to run a for loop
def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

n=6
for i in range(n):
    print(fibonacci(i))
"""
