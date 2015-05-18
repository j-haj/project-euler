// PE2: Find the sum of the even-valued Fibonacci numbers less than 4,000,000
// Solution: 4,613,732

import Foundation

func evenFibSum(n: Int, a: Int, b: Int) -> Int {
	let next = a + b
	if (next > n) {
		return 0
	} else {
		if (next % 2 == 0) {
			return next + evenFibSum(n, b, next)
		} else {
			return evenFibSum(n, b, next)
		}
	}
}

println("Answer: \(evenFibSum(4_000_000, 1, 1))")