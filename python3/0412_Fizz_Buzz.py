class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        solnList = []
        for i in range (1, n+1):
            if i%15 == 0:
                solnList.append("FizzBuzz")
            elif i%3 == 0:
                solnList.append("Fizz")
            elif i%5 == 0:
                solnList.append("Buzz")
            else:
                solnList.append(str(i))
        return solnList
