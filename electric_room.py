lightning_gem = 0
doom_count = 0

def electric_room(power):
    global lightning_gem
    global doom_count
    high_voltage = power

    print("The room is full of flashing computer panels and electrical components, and at the back of the room is a heavy looking blast door.\nThere is a dangerously high-voltage power source on the wall which looks like it can be used to power the door mechanism.\nWhat do you do?")
    print("1. Connect power to door mechanism\n2. Connect power to transformer\n3. Play Doom on one of the computers\n4. Attack the door")
    print("high_voltage: ", high_voltage)
    choice = input("> ")

    if choice == "1" and high_voltage == True:
        dead("The door mechanism explodes due to the high voltage, and you are killed by shrapnel")

    elif choice == "1" and high_voltage == False:
        print("The mechanism comes to life, and with a whirr the door opens up. Behind the door was a doorway and a gem!")
        lightning_gem += 1
        print("You obtain a Lightning Gem. The doorway leads back to the starting room.")
        exit(0) #start()

    elif choice == "2" and high_voltage == True:
        print("You connect the power source to the transformer. It should be safe to connect the power to the door now.")
        high_voltage = False
        electric_room(False)

    elif choice == "3":
        if doom_count <= 3:
            print("You play some Doom on a nearby computer. You get distracted easily, don't you?")
            doom_count += 1
            electric_room(high_voltage)

        else:
            dead("You keep on playing until you die of starvation.")

    elif choice == "4":
        print("The door is unaffected.")
        electric_room(high_voltage)

    else:
        print("You cannot do that right now.")
        electric_room(high_voltage)

def dead(x):
    reason = str(x)
    print(reason, "\nYou are dead. Relaunch the game to restart.")
    exit(0)


electric_room(True)
