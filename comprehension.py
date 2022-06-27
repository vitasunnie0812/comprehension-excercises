# This is a classic problem given in technical interviews.
# First solve the problem WITHOUT using list comprehension.
# "Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number.
# For Multiples of five print "Buzz".
# Finally, for numbers which are multiples of both three and five print "FizzBuzz".
# Include comments for each step of your script explaining the Pseudo code/what each line is doing.
# After you have solved it, write a second version of your script using list comprehension.

# version 1
fiz=[]
buz=[]
fizbuz=[]
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0 :
        fizbuz.append(n)
        # print(n,"FizzBuzz")
    elif n % 3 == 0 :
        # print(n,"Fizz")
        fiz.append(n)
    elif n % 5 == 0 :
        # print(n, "Buzz")
        buz.append(n)
    else :
        pass
print(fizbuz)
print(fiz)
print(buz)


# version 2

fizbuzprint=[ ('FizzBuzz' if n % 3 == 0 and n % 5 == 0 else ('Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n ))for n in range(1,101)]

print(fizbuzprint)