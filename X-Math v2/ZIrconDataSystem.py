num = 0
array = []
scdn = []
create = []
an_create = []
specify = False
even = [2, 4, 6, 8, 0]
init = False

name = input("Name for file?\n")

f = open(name + ".txt", "a")

your_num = int(input("Max Number?\n"))
the_number = input("Choose one\n[a]Multiply Numbers By Themselves\n[b]Choose specific number\n")
if the_number == "b":
    other_num = int(input("Choose specific number.\n"))
    specify = True

while num < your_num:
    num += 1
    array.append(num)
    

input(array)
input(num)

for x in array:
    if specify == False:
        multiply = x * x
    if specify == True:
        multiply = x * other_num
    scdn.append(multiply)
    print(str(x) + ": " + str(multiply))
    f.write(str(x) + ": " + str(multiply) + "\n")

f.close()

summary = sum(scdn)
print("Sum: " + str(summary))

while True:
    look_up = int(input("Enter a number to look up\n"))

    if look_up not in array:
        break
    
    for x in array:
        if look_up == x:
            if specify == False:  #Looks up number in array you counted
                mult = x * x
            if specify == True:
                mult = x * other_num
            print(str(x) + ": " + str(mult))
            arg = input("add to array?\n")

            if arg.lower() == "yes":
                an_create.append(str(x) + ": " + str(mult))
                create.append(mult)

                ask = input("Show sum of array?\n")  #Shows sum of personal array

                if ask.lower() == "yes":
                    yr_sum = sum(create)
                    print(yr_sum)

                    yay = input("Add stuff to file?\n")

                    if yay.lower() == "yes":
                        fu = open(name + ".txt", "a")
                        fu.write("\nPERSONAL ARRAY:\n")
                        for why in an_create:
                            fu.write(why + "\n")

                        fu.write("Sum: " + str(yr_sum) + "\n")
                        fu.close()
                        


                






    









