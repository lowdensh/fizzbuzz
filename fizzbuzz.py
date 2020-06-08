# FizzBuzz: One Simple Interview Question
# Tom Scott
# https://www.youtube.com/watch?v=QPZ0pIK_wsc


def fizzbuzz_shona(last):
    for i in range(1, last+1):
        if (i % 3 == 0) and (i % 5 == 0): print("fizzbuzz")
        elif i % 3 == 0: print("fizz")
        elif i % 5 == 0: print("buzz")
        else: print(i)


def fizzbuzz_tom(last):
    for i in range(1, last+1):
        output = ""
        if i % 3 == 0: output += "fizz"
        if i % 5 == 0: output += "buzz"
        if output == "": output += str(i)
        print(output)


fizzbuzz_tom(30)
