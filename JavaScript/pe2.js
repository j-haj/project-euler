// Solution to PE2 - find the sum of the even-valued Fibonacci numbers less than
// 4,000,000
// Solution: 4,613,732

function evenFibSum(n, a, b) {
  next = a + b
  prev = b
  if(next > n) {
    return 0
  } else {
    if (next % 2 == 0) {
      return next + evenFibSum(n, prev, next)
    } else {
      return evenFibSum(n, prev, next)
    }
  }
}

console.log("Answer: " + evenFibSum(4000000, 1, 1))
