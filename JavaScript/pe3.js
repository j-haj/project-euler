// PE3 - What is the largest prime factor of 600851475143?
// Solution: 6857

var largestPrimeFactor = function(n) {
  var i = 2
  var mid = Math.ceil(Math.sqrt(n))
  while (i < mid && i < n) {
    while (n % i == 0) {
      n /= i
    }
    i += 1
  }

  return n
}

console.log(largestPrimeFactor(600851475143))
