num1=int(input("Enter first number"))
num2=int(input("Enter second number"))



for i in range (num1,num2):
    if i%3 ==0 and i%5 ==0:
        print(i,"FizzBuzz")
    elif i%3 ==0:
        print(i,"Fizz")
    elif i%5 ==0:
        print(i,"Buzz")


    else:print(i)