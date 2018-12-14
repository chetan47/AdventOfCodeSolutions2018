#!/usr/bin/python

file = open("input.txt", "r")

sum = 0
numbers = []
myfrequency = set()
match = False


for line in file:
    numbers.append(int(line))


while not match:
    myfrequency.add(sum)
    for number in numbers:
        sum += number;
        if sum in myfrequency:
            match = True
            print sum
            break
        else:
            myfrequency.add(sum)
