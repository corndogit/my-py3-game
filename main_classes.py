from sys import exit
from random import randint   # used in WaterRoom()
from textwrap import dedent


# todo for discord implementation, commands such as print, input, exit... need to use the respective equivalent
# to return info to the bot


class Scene(object):

    def enter(self):
        print("This scene is currently being implemented. Sorry!")
        return 'starting_room'

    def quit_game(self):
        """Should the Discord user want to stop playing the game, all scenes must inherit this function
        so the user can type a command which immediately ends the game."""
        print("Now exiting. Bye bye!")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map   # sets arg scene_map as an attribute of Engine self

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('treasure')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)   # set current scene to the next scene

        current_scene.enter()  # prints out the last scene


class Death(Scene):

    def enter(self):
        print("You are dead. Relaunch the game to restart.")
        exit(1)


class StartingRoom(Scene):

    def enter(self):
        print(dedent("""
        In this room there is a locked golden chest, which opens with 3 gems.
        Ahead of you are three numbered doorways. How do you proceed?
        1. Enter room #1.
        2. Enter room #2.
        3. Enter room #3."""))
        if all(value == 1 for value in Map.gems.values()):
            print("4. Unlock the golden chest")

        choice = input("> ")

        if '1' in choice and Map.gems['fire_gem'] == 0:
            return 'lava_room'

        elif '2' in choice and Map.gems['water_gem'] == 0:
            return 'water_room'

        elif '3' in choice and Map.gems['lightning_gem'] == 0:
            return 'electric_room'

        elif '4' in choice and all(value == 1 for value in Map.gems.values()):
            return 'treasure'

        elif 'quit' in choice:
            self.quit_game()

        else:
            print("You cannot do that right now.")
            return 'starting_room'


class LavaRoom(Scene):

    def enter(self):
        print(dedent("""
        In the middle of the room is a huge pool of lava.
        Across a path of stepping stones, you see a doorway and an alter with a gem.
        What do you do?
        
        1. Run across stepping stones.
        2. Look for a way around
        3. Jump into the lava."""))

        action = input("> ")

        if "1" in action:
            print("You almost make it, but lose your footing on the last stepping stone.")
            return 'death'

        elif "2" in action:
            print(dedent("""
            You see a precarious ledge that leads to the other side of the lava.
            Nervously, you shimmy along and reach the other side."""))
            Map.gems['fire_gem'] = 1
            print("You obtain a Fire Gem. The doorway leads back to the starting room.")
            return 'starting_room'

        elif "3" in action:
            print("You take a cannonball dive into the lava. You scream in agony as you sink into the fiery deep.")
            return 'death'
        else:
            print("You cannot do that right now.")
            return 'lava_room'


class WaterRoom(Scene):

    def enter(self):
        solved = False
        correct_answers = 0
        water_level = 0

        print(dedent("""
            On entering the room, the door seals behind you and the sound of water can be heard.
            There is a placard on the wall which says:
            
                \"YOU SHALL ANSWER 3 CORRECT QUESTIONS IN THIS EXERCISE
                OR IN A WATERY GRAVE YOU SHALL FIND YOUR DEMISE!\"
                """))
        while not solved:
            room_fill = (water_level / 6)

            if correct_answers >= 3:
                solved = True

            elif water_level > 5 and correct_answers < 3:
                break

            else:
                print(f"The room is {int(room_fill * 100)}% filled with water. Correct answers: {correct_answers}")
                correct_answers += self.question()
                water_level += 1

        if solved:
            print(dedent("""
            A mechanical clunk can be heard, and grates in the floor open up.
            The water drains away, and you escape with your life.
            A gem drops from the ceiling, and the doorway opens."""))
            Map.gems['water_gem'] = 1
            print("You obtain a Water Gem. The doorway leads back to the starting room")
            return 'starting_room'

        else:
            print("The room is completely filled with water.")
            return 'death'

    def question(self):
        a = randint(1, 100)
        b = randint(1, 100)
        c = a + b
        print(f"ANSWER THE QUESTION: WHAT IS {a} + {b}?")
        answer = input("> ")
        if int(answer) == c:
            print("Correct!")
            return 1
        else:
            print("Wrong, dumbass!")
            return 0


class ElectricRoom(Scene):

    def enter(self):
        doom_count = 0
        high_voltage = True
        print(dedent("""
        The room is full of flashing computer panels and electrical components, and at the back of the room is 
        a heavy looking blast door. There is a dangerously high-voltage power source on the wall which looks 
        like it can be used to power the door mechanism.
        What do you do?
        1. Connect power to door mechanism
        2. Connect power to transformer
        3. Play Doom on one of the computers
        4. Attack the door
        """))

        while True:
            choice = input("> ")

            if "1" in choice and high_voltage:
                print("The door mechanism explodes due to the high voltage, and you are killed by shrapnel")
                return 'death'

            elif "1" in choice and not high_voltage:
                print(dedent("""
                The mechanism comes to life, and with a whir the door opens up.
                Behind the door was a a gem!"""))
                Map.gems['lightning_gem'] = 1
                print("You obtain a Lightning Gem. The doorway leads back to the starting room.")
                return 'starting_room'

            elif "2" in choice and high_voltage:
                print("You connect the power source to the transformer. It should be safe to power the door now.")
                high_voltage = False

            elif "3" in choice:
                if doom_count <= 2:
                    print("You play some Doom on a nearby computer. You get distracted easily, don't you?")
                    doom_count += 1

                else:
                    print("You keep on playing Doom until you die of starvation.")
                    return 'death'
            elif choice == "4":
                print(dedent("""
                You strike the door in a rage.  After calming down you realise that perhaps 
                you can connect the power to the transformer to make it safely power the door?"""))


class Treasure(Scene):

    def enter(self):
        print(dedent("""
        You place a gem into each of the slots and hear a click - the lock is disengaged!
        You open the chest, and see that it's filled to the brim with priceless golden relics!
        
        YOU WIN! Good job."""))
        exit(0)


class Map(object):
    scenes = {
        'starting_room': StartingRoom(),
        'lava_room': LavaRoom(),
        'water_room': WaterRoom(),
        'electric_room': ElectricRoom(),
        'treasure': Treasure(),
        'death': Death()
    }

    gems = {
        'fire_gem': 0,
        'water_gem': 0,
        'lightning_gem': 0
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('starting_room')
a_game = Engine(a_map)
print("You are an adventurer in a dungeon room.")
a_game.play()
