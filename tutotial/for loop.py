numbers = [5,2,5,2,2]

for count in numbers:  #first count is 5 second is 2
    output = ""        #clear variable in inner loop
    for x_count in range(count):  #range(5) = 0,1,2,3,4 = work 5 times
        output += "x"  #since the loop work five time, output add "x" five times
    print(output)


print("")

print("The feature python have")

for count in numbers:
    print(count * "x")