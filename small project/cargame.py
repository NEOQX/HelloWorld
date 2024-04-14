#start stop go left right back
speed = 0
car_stat = "off"
command = ["help","start","stop","slow","move","car_stat","car_speed"]


#console area

print("Hello driver! This is a car game!")
print("Type 'help' to ask for help and 'start' to start the game")

while car_stat == "off":
    x = input(">").lower()
    if x == "car_stat":
        print(f"Current car stat is {car_stat}")
    elif x == "car_speed":
        print(f"Car Speed is {speed} km/h")
    elif x == "help":
        print(f"Command available is {command}")
    elif x == "start" :
        engine = car_stat.replace("off", "on")
        print("The car is starting")
        print(f"Current Speed is {speed}")
        break
    else:
        print("how do you move a car without starting it? Type 'start' to start your journey")

#engine start
print("maybe 'move' will move the car?")
while engine == "on" :
    y = input(">").lower()
    if y == "move" :            #move
        speed = speed + 30
        print(f"Car is move at {speed}km/h")
        if speed == 120 :
            print("Slow Down! You are moving too fast!")
        elif speed >120:
            print("NOOOOOOOO You Crash into air!")
            break
        else:
            print("Keep going!")
    elif x == "car_stat":
        print(f"Current car stat is {car_stat}")
    elif x == "car_speed":
        print(f"Car Speed is {speed} km/h")
    elif x == "help":
        print(f"Command available is {command}")
    elif y == "stop":       #stop
        print("ok you stop the engine")
        break
    elif y == "slow":       #slow
        speed = speed -30
        if speed == 0:
            print("The car stopped!")
            break
        else:
            print(f"The car is moving at {speed}km/h")
    else:
        print("I dont know what you are saying!")
print("good game")






