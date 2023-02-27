

colors = ['Blue', 'Green', 'Yellow']

for i in colors:
    print(i)

print("-------------------------------------------------------------")
numbers = [45,98,75,65,24,88,74,56,75]

for i in range(0,len(numbers)):
    if numbers[i]<=50:
        print(numbers[i], "-- is correct number")
    else:
        print(numbers[i], "-- Number is greater than 50")