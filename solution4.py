# Write code for algorithm 4 below

def exp_num(a, b):
    if b == 0:
        return 1
    else:
        return a * exp_num(a, b - 1)


print(exp_num(2, 4))
