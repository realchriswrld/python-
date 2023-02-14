

class solution(object):
  def fizzbuzz(self, n):
    result =[]
    for i in range (1 , n+1) :
        if i%3 == 0 and i%5 == 0 :
            result.append("FizzBuzz")
        elif i%3 ==0:
            result.append("Fizz")
        elif i%5 == 0:
                result.append("Buzz")
        else:
                result.append(i)
    return result


ob1 = solution()
print(ob1.fizzbuzz(100))


