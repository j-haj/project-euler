// PE1: Sum multiples of 3 or 5 less than 1,000

func multipleOf3Or5(n: Int) -> Bool {
  let result = ((n % 3 == 0) || (n % 5 == 0))
  return result
}

func sumOfMultiplesLessThanN(n: Int) -> Int {
  if n = 1 {
    return 0
  }
  var sum: Int = 0
  if multipleOf3Or5(n - 1) {
    sum = n - 1
  }
  return sum + sumOfMultiplesLessThanN(n-2)
}
