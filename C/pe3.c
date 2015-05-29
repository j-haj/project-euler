// PE3 - find the largest prime factor of 600851475143
// Solution: 6857

#include <stdio.h>
#include <stdlib.h>

unsigned long largestPrimeFactor(unsigned long, unsigned long);

int main(int argc, char *argv[]) {
  unsigned long n = strtoul(argv[1], NULL, 0);
  printf("Solution: %lu\n", largestPrimeFactor(n, 2));
  return 0;
}

unsigned long largestPrimeFactor(unsigned long n, unsigned long x) {
  if (n == x) {
    return n;
  } else {
    if (n % x == 0) return largestPrimeFactor(n/x, x);
    else return largestPrimeFactor(n, x+1);
  }
}
