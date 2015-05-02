#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <vector>

using namespace std;

// Function prototypes
bool isPrime(const long long int &);
vector<int> primeFactors(const long long int &);
long largestPrime(const long long &);

// MAIN
int main(int argc, char *argv[]) {
    cout << isPrime(atoi(argv[1])) << endl;
    vector<int>primes = primeFactors(atoi(argv[1]));
    cout << "Largest prime factor is " << largestPrime(atoll(argv[1])) << endl;
    return 0;
}

// Function implementations
bool isPrime(const long long int &a) {
    for (long long int i = 2; i < (long long)(sqrt(a)) + 1; i++) {
        if (a % i == 0) {
            return false;
        }
    }
    return true;
}

vector<int> primeFactors(const long long int &a) {
    vector<int> primes;
    if (a % 2 == 0) {
        primes.push_back(2);
    }
    for (long long int i = 3; i < (long long)(sqrt(a)) + 1; i+= 2) {
        if (a % i == 0 && isPrime(i)){
            primes.push_back(i);
            if (isPrime(a/i)) {
                primes.push_back(a/i);
            }
        }
    }

    return primes;
}

long largestPrime(const long long &a) {
    long prime {2};
    while(!isPrime(a/prime) || a % prime != 0) {
        if(prime == 2){
            prime++;
        } else {
            prime += 2;
        }
    }

    return a/prime;
}
