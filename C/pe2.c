#include <stdio.h>
#include <stdbool.h>


// Returns a fibonacci sequence whose terms don't exceed n
int *fibonacciSequence(int);

int main(int argc, char *argv[]) {
    
    int sum = 2;
    int fibValNew  = 2;
    int fibValOld = 1;
    int temp;
    while(fibValNew <= 4000000) {
        temp = fibValNew;
        fibValNew += fibValOld;
        fibValOld = temp;

        if (fibValNew % 2 == 0)
            sum += fibValNew;
    }

    printf("Sum of even Fibonacci numbers not exceeding 4M: %d\n", sum);

    return 0;
}

    
