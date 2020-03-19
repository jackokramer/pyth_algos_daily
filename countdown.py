## Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def countDown(lst):
    countback = []
    for x in range (lst, -1, -1):
        countback.append(x)
    return countback
print(countDown(7))
print(countDown(12))

## Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_n_return(lst):
    print(lst[0])
    return lst[1]

print(print_n_return([7,12]))

