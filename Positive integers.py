NumList = []

Number=int(input("Total Number of List Elements: "))
for i in range(1, Number + 1):
    value =int(input())
    NumList.append(value)
for j in range(Number):
    if(NumList[j] >= 0):
        print(NumList[j], end = '   ')
Footer
