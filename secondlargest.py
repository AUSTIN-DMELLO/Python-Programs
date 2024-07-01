def secondmax(l):
    (mymax, mysecondmax) = (0, 0)
    for i in range(len(l)):
        num = l[i]
        if num > mymax:
            mysecondmax = mymax
            mymax = num
        elif num > mysecondmax:
            mysecondmax = num
    return mysecondmax 
l = [5, 1, 4, 3, 2]
second_largest = secondmax(l)
print(f"Second largest value: {second_largest}")
