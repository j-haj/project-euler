import random
import math
import sys

"""
    !headerdoc!

    @brief Returns a tuple containing a prime factorization a*b of a given integer

    @description This method uses Dixon's factorization method to find
    two

    @param n
        The number to be decomposed into prime factors

    @param B
        The bound for the factor base used in the decomposition
"""
def dixon_factorization(n, B):
    # Generate base-B factor base
    B_base = factor_base(B)

    # Find two numbers whose squares are B-smooth
    B_flag = 0
    lower_bound = math.ceil(math.sqrt(n))
    A = 0
    B = 0
    while B_flag < 2:
        test_num = random.randint(lower_bound, n)
        test_num = modular_pow(test_num, 2, n)
        if is_B_smooth(test_num, B_base):
            if B_flag == 0:
                A = test_num
                B_flag += 1
            else:
                B = test_num
                B_flag += 1
    x = A*B % n
    y = find_square_congruence(x, n)
    print("(x, y) -> ({}, {})".format(x, y))
    (f1, f2) = (gcd(x+y, n), gcd(x-y, n))
    print("(f1, f2) -> ({}, {})".format(f1, f2))

"""
    !headerdoc!

    @brief Returns a number y such that x**2 = y**2 mod n

    @description This method finds a number that is a square congruence.
    This is used in the Dixon factorization method.

    @param x
        Known value

    @param n
        The base of the modulo
"""
def find_square_congruence(x, n):
    z = modular_pow(x, 2, n)
    result = 0
    for i in range(n):
        if i == x:
            continue
        result = modular_pow(i, 2, n)
        if result ==z:
            break
    return result

"""
    !headerdoc!

    @brief Determines whether the specified number is B-smooth

    @description This method runs through the factor base bound by B
    and determines if there exists a combination of elements from the
    factor base bound by B that can be combined, via multiplication, to
    yield n.

    @param n
        The test number

    @param B
        The bound on the respective factor base
"""
def is_B_smooth(n, B):
    for x in B:
        while n % x == 0:
            n /= x
    if n == 1:
        return True
    return False

"""
    !headerdoc!

    @brief Returns a factor base for a given bound B

    @description Returns a list less than or equal to B such that all
    elements of the list are prime. This list is referred to as a factor
    base and used in algorithms such as Dixon's factorization, the qudratic
    sieve, and the number field sieve.

    @param B
        The bound of the factor base
"""
def factor_base(B):
    # Do nothing
    factor_base = []
    for i in range(2,B+1):
        if is_prime(i, 21):
            factor_base.append(i)
    print(factor_base)
    return factor_base

"""
    !headerdoc!

    @brief Determines whether the given number is prime

    @description Uses the Miller-Rabin primality test to determine
    the primality of the passed argument. This test doesn't
    determine with 100% certainty that a number is prime, just that it is either
    definitely not prime or likely prime. The likelihood of a number being prime
    depends on the parameters k and a.

    See wikipedia.org/wiki/Miller-Rabin_primality_test
    for a detailed description of the algorithm.

    @param n
        The integer for which primality will be determined

    @param k
        A parameter that determines the likelihood of the test being correct
        The larger this parameter gets, the more likely the test will be correct
        but it will also increase the runtime of the test.

    @param a
        A parameter that determines the likelihood of the test being corred.
        The larger this parameter gets, the more likely the test will be correct
        but it will also increase the runtime of the test.

"""
def is_prime(n, k):
    if n == 1 or n == 2 or n == 3 or n == 5 or n == 7:
        return True
    else:
        # Use the Miller-Rabin test
        (s, d) = s_d_constructor(n-1)
        for i in range(k):
            a = random.randint(2, n-2)
            x = modular_pow(a, d, n)
            if x == 1 or x == n-1:
                continue
            for j in range(s - 1):
                x = x**2 % n
                if x == 1:
                    return False
                if x == n - 1:
                    break
            else:
                return False
        return True


"""
    !headerdoc!

    @brief Find s and d such that n = d * 2**s

    @description The main purpose of this method is to get the proper form for
    n - 1 in the Miller-Rabin test.

    @param n
        Number to be re-written in d * 2**s form
"""
def s_d_constructor(n):
    s = 0
    d = n
    while d % 2 == 0:
        d /= 2
        s += 1

    return (s, int(d))

"""
    !headerdoc!

    @brief Returns the result of a**b mod m

    @description This method uses a memory efficient method to compute the
    modular arithmetic a**b mod m. See wikipedia.org/wiki/Modular_exponentiation
    for details.

    @param a
        The base of the exponental term

    @param b
        The exponent of the exponential term

    @param m
        The number that specifies what the modulo of a**b should be
"""
def modular_pow(a, b, m):
    c = 1
    for i in range(1, int(b)):
        c = (a * c) % m
    return c

"""
    !headerdoc!

    @brief Returns the GCD of two numbers using the Euclidean algorithm

    @param a
        One of two comparison numbers

    @param b
        One of two comparison numbers
"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(is_prime(n, 5))
    print(gcd(228, 4256))
    print(is_B_smooth(1620, [2,3,5]))
    dixon_factorization(84923, 7)
