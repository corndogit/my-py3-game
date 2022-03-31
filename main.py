from sys import exit
import random

fire_gem = 0
water_gem = 0
lightning_gem = 0
win_state = False
correct_answers = 0
doom_count = 0

def lava_room():
    global fire_gem
    print("In the middle of the room is a huge pool of lava.\nAcross a path of stepping stones, you see a doorway and an alter with a gem.\nWhat do you do?\n1. Run across stepping stones.\n2. Look for a way around\n3. Jump into the lava.")

    action = input("> ")
    if action == "1":
        dead("You almost make it, but lose your footing on the last stepping stone.")

    elif action == "2":
        print("You see a precarious ledge that leads to the other side of the lava.\nNervously, you shimmy along and reach the other side.")
        fire_gem += 1
        print("You obtain a Fire Gem. The doorway leads back to the starting room.")
        start()

    elif action == "3":
        dead("You take a cannonball dive into the lava. You scream in agony as you sink into the fiery deep.")

    else:
        print("You cannot do that right now.")
        lava_room()


def water_room():
    global water_gem
    solved = False
    water_level = 0
    death_level = 5

    print("On entering the room, the door seals behind you and the sound of water can be heard.\nThere is a placard on the wall which says:\n\n\t\"YOU SHALL ANSWER 3 CORRECT QUESTIONS IN THIS EXERCISE\n\tOR IN A WATERY GRAVE YOU SHALL FIND YOUR DEMISE!\"\n")
    while solved == False:
        water_level += 1
        room_fill = (water_level / death_level) * 100

        if correct_answers >= 3:
            solved = True
            break

        elif water_level > death_level and correct_answers < 3:
            dead("You run out of breath and pass out.")
            exit(0)

        else:
            print("The room is ", room_fill, "% full.")
            question()

    if solved == True:
        print("A mechanical clunk can be heard, and grates in the floor open up.\nThe water drains away, and you escape with your life.\nA gem drops from the ceiling, and the doorway opens.")
        water_gem += 1
        print("You obtain a Water Gem. The doorway leads back to the starting room")
        start()

def question():
    global correct_answers
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = a + b
    number = correct_answers + 1

    print("Correct answers: ", correct_answers)
    print(f"ANSWER THE QUESTION: WHAT IS {a} + {b}?")
    answer = input("> ")

    if int(answer) == c:
        print("Correct!")
        correct_answers += 1

    else:
        print("Wrong, dumbass!")

def electric_room(power):
    global lightning_gem
    global doom_count
    high_voltage = power

    print("The room is full of flashing computer panels and electrical components, and at the back of the room is a heavy looking blast door.\nThere is a dangerously high-voltage power source on the wall which looks like it can be used to power the door mechanism.\nWhat do you do?")
    print("1. Connect power to door mechanism\n2. Connect power to transformer\n3. Play Doom on one of the computers\n4. Attack the door")
    choice = input("> ")

    if choice == "1" and high_voltage == True:
        dead("The door mechanism explodes due to the high voltage, and you are killed by shrapnel")

    elif choice == "1" and high_voltage == False:
        print("The mechanism comes to life, and with a whirr the door opens up. Behind the door was a doorway and a gem!")
        lightning_gem += 1
        print("You obtain a Lightning Gem. The doorway leads back to the starting room.")
        start()

    elif choice == "2" and high_voltage == True:
        print("You connect the power source to the transformer. It should be safe to connect the power to the door now.")
        high_voltage = False
        electric_room(high_voltage)

    elif choice == "3":
        if doom_count <= 2:
            print("You play some Doom on a nearby computer. You get distracted easily, don't you?")
            doom_count += 1
            electric_room(high_voltage)

        else:
            dead("You keep on playing Doom until you die of starvation.")

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

def start():
    gem_count = fire_gem + water_gem + lightning_gem
    print(f"In this room there is a locked golden chest, which opens with 3 gems (currently, you have {str(gem_count)}).\nAhead of you are three numbered doorways. How do you proceed?\n1. Enter room #1.\n2. Enter room #2.\n3. Enter room #3.")

    if gem_count == 3:
        print("4. Unlock the chest.")

    choice = input("> ")

    if choice == "1" and fire_gem == 0:
        lava_room()

    elif choice == "2" and water_gem == 0:
        water_room()

    elif choice == "3" and lightning_gem == 0:
        electric_room(True)

    elif choice == "4" and gem_count == 3:
        print("You place a gem into each of the slots and hear a click - the lock is disengaged.\nYou open the chest, and see that it's filled to the brim with priceless golden relics!\nYOU WIN! Good on you.")
        exit(0)

    else:
        print("You cannot do that now.")
        start()


print("You are an adventurer in a dungeon room.")
while win_state == False:
    
    start()
