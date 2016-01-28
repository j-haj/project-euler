import sys


def find_multiples_below_n(a, b, n):
    '''Returns multiples of a or b that are less than n'''
    multiples = []
    for i in range(n):gtest
        if (i%a)==0 and (i%b)==0:
            multiples.append(i)
        elif (i%a)==0 and (i%b)!=0:
            multiples.append(i)
        elif (i%a)!=0 and (i%b)==0:
            multiples.append(i)
    return multiples

if __name__ == "__main__":
    # Main loop
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    n = int(sys.argv[3])
    multiples = find_multiples_below_n(a, b, n)
    print(sum(multiples))

