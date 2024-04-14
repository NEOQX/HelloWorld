#黑塔转圈圈~

def herta(count):
    times = 0
    while times  +1 < count :
        print("kuru~ kuru~")
        times = times +1
    else:
        print("kuru~ rin~")


#console area
print("Welcome to herta simulation universe !Press 0 to exit...if you want.")
while True:
    count = int(input(">"))
    if count == 0:
        if input("Are u sure to exit? 'yes' or 'no' >").lower() == "yes":
            print("Goodbye Trailblazer! Have a good day :)")
            break
        else:
            print("Let's continue your journey! :)")
    elif count > 0:
        herta(count)
        count += 1
