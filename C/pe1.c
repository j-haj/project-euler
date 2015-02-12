#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int *findMultiplesBelowN(int, int, int);

int main(int argc, char *argv[]){
    // Get command line input
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int n = atoi(argv[3]);
    int *result = findMultiplesBelowN(a, b, n);
    
    int idx = 0; // Array index
    int sum = 0; // Sum of array elements
    while(result[idx] != 0) {
        sum += result[idx];
        idx++;
    }
    printf("%d\n", sum);
    free(result);
    return 0;
}

int *findMultiplesBelowN(int a, int b, int n) {
    // Find min of a and b to aid in memory allocation
    int minFactor = fmin(a, b);
    
    // Alocate memory for factor array
    int *multiples = malloc(n * sizeof(int));
    
    // Set array elements to 0
    memset(multiples, 0, n * sizeof(int));
    
    int index = 0; // Array index

    // Count up to n, storing factors as apprporiate
    for (int i = 1; i < n; i++) {
        if ((i % a) == 0 && (i % b) == 0) {
            multiples[index] = i;
            index ++;
        } else if ((i % a) == 0 && (i % b) != 0) {
            multiples[index] = i;
            index++;
        } else if ((i % a) != 0 && (i % b) == 0) {
            multiples[index] = i;
            index++;
        }
    }

    return multiples;
}
