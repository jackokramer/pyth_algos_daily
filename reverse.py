def reverseList(lst):
    halfway = int(len(lst)/2)
    for x in range(halfway):
        temp = lst[x]
        lst[x] = lst[len(lst)-1-x]
        lst[len(lst)-1-x] = temp
    return lst
test = [1,4,2,6,1,10]
test2 =[2,1,4,5,6,10,35]

print(reverseList(test))
print(reverseList(test2))

def reverseList(listy):
    half = int(len(listy)/2)
    for t in range(half):
        listy[t], listy[len[listy]-1-t] = listy[len[listy]-1-t], listy[t]
        ## This is another way to do the assignment and its called Multi-Variable Assignment. where you compare one to one.