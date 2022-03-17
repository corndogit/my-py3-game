from sys import exit
import random
water_gem = 0
correct_answers = 0

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
            print("The room is completely filled with water. You are dead")
            exit(0)

        else:
            print("The room is ", room_fill, "% full.")
            question()

    if solved == True:
        print("A mechanical clunk can be heard, and grates in the floor open up.\nThe water drains away, and you escape with your life.\nA gem drops from the ceiling, and the doorway opens.")
        water_gem += 1
        print("You obtain a Water Gem. The doorway leads back to the starting room")
        #start()

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


water_room()
