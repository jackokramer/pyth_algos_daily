## First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(num):
    return num[0] + len(num)

#print(first_plus_length([1,20,3,5,7,8,9,20]))

## Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(nums):
    new_list = []
    ## get the second value of the original list
    second = nums[1]
    #scan through the original list find the values greater then add them to the second list.
    for x in range (nums):    
        if nums[x] > second:
            new_list.append(nums[x])

    print(len(new_list))
    return new_list

#print(values_greater_than_second([1,2,29,3,0, 8,9]))

## This Length that Value - Write a function that accepts two inetgers as parameters : size and value. This function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def thisLengthThatValue(size, value):
    newly = []
    for y in range(size):
        newly.append(value)
    return newly

print(thisLengthThatValue(8,21))
