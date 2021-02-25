num = 0
array = []
scdn = []
create = []

your_num = int(input())

while num < your_num:
    num += 1
    array.append(num)
    

input(array)
input(num)

for x in array:
    multiply = x * x
    scdn.append(multiply)
    print(str(x) + ": " + str(multiply))

summary = sum(scdn)
print("Sum: " + str(summary))

while True:
    look_up = int(input("Enter a number to look up?"))

    if look_up not in array:
        break
    
    for x in array:
        if look_up == x:
            mult = x * x
            print(mult)
            arg = input("add to array?")

            if arg == "yes":
                create.append(mult)

                ask = input("Show sum of array?")

                if ask == "yes":
                    yr_sum = sum(create)
                    print(yr_sum)

                






    








