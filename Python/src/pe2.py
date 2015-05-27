def even_fib_sum_leq_n(n):
    """Returns the sum of even fibonacci numbers no greater than n"""

    sum_val = 2
    fib_val_new = 2
    fib_val_old = 1
    while fib_val_new <= n:
        temp = fib_val_new
        fib_val_new += fib_val_old
        fib_val_old = temp

        if fib_val_new % 2 == 0:
            sum_val += fib_val_new

    print("Sum of even Fibonacci numbers not exceeding 4M: {}".format(sum_val))


if __name__ == "__main__":
    # Main look
    even_fib_sum_leq_n(4000000)
