fire_gem = 0

def lava_room(x):
    fire_gem = x
    print("In the middle of the room is a huge pool of lava.\nAcross a path of stepping stones, you see a doorway and an alter with a gem.\nWhat do you do?\n1. Run across stepping stones.\n2. Look for a way around\n3. Jump into the lava.")

    action = input("> ")
    if action == "1":
        dead("You almost make it, but lose your footing on the last stepping stone.")

    elif action == "2":
        print("You see a precarious ledge that leads to the other side of the lava.\nNervously, you shimmy along and reach the other side.")
        fire_gem += 1
        print("You obtain a Fire Gem. The doorway leads back to the starting room.")
        return fire_gem

    elif action == "3":
        dead("You take a cannonball dive into the lava. You scream in agony as you sink into the fiery deep.")
    else:
        print("You cannot do that right now.")
        lava_room(0)

def dead(x):
    reason = str(x)
    print(reason, "\nYou are dead. Relaunch the game to restart.")
    exit(0)


lava_room(0)
print("Gem count: ", fire_gem)
