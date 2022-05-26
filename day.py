'''
module to simulate your day
'''
import random

class My_Day:
    '''
    class which contain daily states
    '''
    def __init__(self):
        '''
        create states
        '''
        self.start_state = self.calm_state()
        self.final_state = self.final()
        self.eat = self.to_eat()
        self.sleep = self.to_sleep()
        self.work = self.to_work()
        self.sing = self.to_sing()
        self.teeth = self.brush_teeth()
        self.characteristics = ["happy", "healthy", "hungry", "dirty teeth", "alive"]
        self.deals = []
        self.current_state = self.start_state
        self.songs = ["I'm addicted to you\n\
Don't you know that you're toxic?", "Gimme, gimme (more)\nGimme (more)\n\
Gimme, gimme (more)", "Oops, I did it again\n\
I played with your heart, got lost in the game\n\
Oh baby, baby", "When I put on a show\n\
I feel the adrenaline moving through my veins\n\
Spotlight on me and I'm ready to break", "Womanizer, woman-womanizer, you're a womanizer\n\
Oh, womanizer, oh, you're a womanizer, baby", "My loneliness is killing me\n\
(And I) I must confess I still believe (Still believe)\n\
When I'm not with you, I lose my mind"]
        
    def prime(function):
        '''
        helper to send command to the module
        '''
        def wrapper(*args, **kwargs):
            v = function(*args, **kwargs)
            v.send(None)
            return v
        return wrapper
    
    def send(self, digit):
        '''
        send information about state
        '''
        self.current_state.send(digit)

    @prime
    def final(self):
        '''
        final state
        '''
        while True:
            state, hour = yield
            if state == "sleep":
                print("\ngood night, good day\n")
            else:
                print(f"\nit's not time to {state}, it's 12AM \n")
            print("your characteristics after the day: " + f"{self.characteristics}")
            self.current_state = self.final_state

    @prime
    def to_eat(self):
        '''
        eating state
        '''
        while True:
            state, hour = yield
            if state == "eat":
                print(f"\n{hour} hour:" )
                print("eat twice really?\nnow you're fat")
                if "healthy" in self.characteristics:
                    self.characteristics.remove("healthy")
                if "fat" not in self.characteristics:
                    self.characteristics.append("fat")
                if "hungry" in self.characteristics:
                    if "dirty teeth" not in self.characteristics:
                        self.characteristics.append("dirty teeth")
                    print("you eat")
                    self.current_state = self.eat
                else:
                    print("you are not hungry, try to do something else")

            elif state == "sleep":
                if "healthy" not in self.characteristics:
                    self.characteristics.append("healthy")
                if "tired" in self.characteristics:
                    self.characteristics.remove("tired")
                print(f"\n{hour} hour:" )
                if hour <= 6 or hour >= 22:
                    print("zzzzz...")
                print("you sleep")
                self.current_state = self.sleep

            elif state == "work":
                print(f"\n{hour} hour:" )
                print('you work')
                if "hungry" not in self.characteristics:
                    self.characteristics.append("hungry")
                self.current_state = self.work
            elif state == "brush_teeth":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) < 0.2:
                    print("oh there is no water, you can't brush your teeth now")
                else:
                    if "dirty teeth" in self.characteristics:
                        self.characteristics.remove("dirty teeth")
                    print('you brush teeth')
                    self.current_state = self.teeth
            elif state == "sing":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) > 0.3 and "healthy" in self.characteristics:
                    if "happy" not in self.characteristics:
                        self.characteristics.append("happy")
                    print("it's perfect time to sing a Britney's song\n")
                    print(random.choice(self.songs))
                    self.current_state = self.sing
                else:
                    print("you're too tired to sing :(")

    @prime
    def to_sleep(self):
        '''
        sleeping state
        '''
        while True:
            state, hour = yield
            if hour <= 6 or hour >= 22:
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) > 0.2:
                    print("zzzzzzzz")
                    self.current_state = self.sleep
                else:
                    print("stop procrastinating, work work work!")
                    self.current_state = self.work
            else:
                if state == "eat":
                    print(f"\n{hour} hour:" )
                    if random.uniform(0, 1) < 0.05:
                        print("somebody poisoned you, you die :(")
                        if "alive" in self.characteristics:
                            self.characteristics.remove("alive")
                        if "dead" not in self.characteristics:
                            self.characteristics.append("dead")
                        print(f"you die with characteristics like that: {self.characteristics}")
                        exit()
                    print('you eat')
                    if "dirty teeth" not in self.characteristics:
                            self.characteristics.append("dirty teeth")
                    self.current_state = self.eat
                elif state == "sleep":
                    if "healthy" not in self.characteristics:
                        self.characteristics.append("healthy")
                    print(f"\n{hour} hour:" )
                    if "tired" in self.characteristics:
                        self.characteristics.remove("tired")
                    print('you sleep')
                    if hour <= 6 or hour >= 22:
                        print("zzzzz...")
                    self.current_state = self.sleep
                elif state == "work":
                    if "hungry" not in self.characteristics:
                        self.characteristics.append("hungry")
                    print(f"\n{hour} hour:" )
                    print('you work')
                    self.current_state = self.work
                elif state == "brush_teeth":
                    print(f"\n{hour} hour:" )
                    if random.uniform(0, 1) < 0.2:
                        print("oh there is no water, you can't brush your teeth now")
                    else:
                        if "dirty teeth" in self.characteristics:
                            self.characteristics.remove("dirty teeth")
                        print('you brush teeth')
                        self.current_state = self.teeth
                elif state == "sing":
                    print(f"\n{hour} hour:" )
                    if random.uniform(0, 1) > 0.3 and "healthy" in self.characteristics:
                        if "happy" not in self.characteristics:
                            self.characteristics.append("happy")
                        print("it's perfect time to sing a Britney's song\n")
                        print(random.choice(self.songs))
                        self.current_state = self.sing
                    else:
                        print("you're too tired to sing :(")

    @prime
    def to_work(self):
        '''
        working state
        '''
        while True:
            state, hour = yield
            if state == "eat":
                print(f"\n{hour} hour:" )
                if "dirty teeth" not in self.characteristics:
                        self.characteristics.append("dirty teeth")
                print('you eat')
                self.current_state = self.eat

            elif state == "sleep":
                print(f"\n{hour} hour:" )
                if hour >= 6 and hour <=22:
                    print("no time for sleep\ngo to work")
                    self.current_state = self.work
                else:
                    if "healthy" not in self.characteristics:
                        self.characteristics.append("healthy")
                    if "tired" in self.characteristics:
                        self.characteristics.remove("tired")
                    print("zzzzzz")
                    self.current_state = self.sleep
            elif state == "work":
                if "hungry" not in self.characteristics:
                    self.characteristics.append("hungry")
                if "tired" not in self.characteristics:
                    self.characteristics.append("tired")
                print(f"\n{hour} hour:" )
                print('you work')
                self.current_state = self.work
            elif state == "brush_teeth":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) < 0.2:
                    print("oh there is no water, you can't brush your teeth now")
                else:
                    if "dirty teeth" in self.characteristics:
                        self.characteristics.remove("dirty teeth")
                    print('you brush teeth')
                    self.current_state = self.teeth
            elif state == "sing":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) > 0.3 and "healthy" in self.characteristics:
                    if "happy" not in self.characteristics:
                        self.characteristics.append("happy")
                    print("it's perfect time to sing a Britney's song\n")
                    print(random.choice(self.songs))
                    self.current_state = self.sing
                else:
                    print("you're too tired to sing :(")

    @prime
    def to_sing(self):
        '''
        singing state
        '''
        while True:
            state, hour = yield
            if state == "eat":
                print(f"\n{hour} hour:" )
                if "dirty teeth" not in self.characteristics:
                        self.characteristics.append("dirty teeth")
                print('you eat')
                self.current_state = self.eat
            elif state == "sleep":
                if "tired" in self.characteristics:
                    self.characteristics.remove("tired")
                if "healthy" not in self.characteristics:
                    self.characteristics.append("healthy")
                print(f"\n{hour} hour:" )
                if hour <= 6 or hour >= 22:
                    print("zzzzz...")
                print('you sleep')
                self.current_state = self.sleep
            elif state == "work":
                if "hungry" not in self.characteristics:
                    self.characteristics.append("hungry")
                if "tired" not in self.characteristics:
                    self.characteristics.append("tired")
                print(f"\n{hour} hour:" )
                print('you work')
                self.current_state = self.work
            elif state == "brush_teeth":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) < 0.2:
                    print("oh there is no water, you can't brush your teeth now")
                else:
                    if "dirty teeth" in self.characteristics:
                        self.characteristics.remove("dirty teeth")
                    print('you brush teeth')
                    self.current_state = self.teeth
            elif state == "sing":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) > 0.3 and "healthy" in self.characteristics:
                    if "happy" not in self.characteristics:
                        self.characteristics.append("happy")
                    print("it's perfect time to sing a Britney's song\n")
                    print(random.choice(self.songs))
                    if "tired" not in self.characteristics:
                        self.characteristics.append("tired")
                    self.current_state = self.sing
                else:
                    print("you're too tired to sing :(")
    @prime
    def brush_teeth(self):
        '''
        brushing your teeth state
        '''
        while True:
            state, hour = yield
            if state == "eat":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) > 0.6 and "hungry" in self.characteristics:
                    self.characteristics.remove("hungry")
                    if "dirty teeth" not in self.characteristics:
                        self.characteristics.append("dirty teeth")
                    print('you eat')
                    self.current_state = self.eat
                else:
                    print("You've just eaten")
            elif state == "sleep":
                if "healthy" not in self.characteristics:
                    self.characteristics.append("healthy")
                if "tired" in self.characteristics:
                    self.characteristics.remove("tired")
                print(f"\n{hour} hour:" )
                print('you sleep')
                self.current_state = self.sleep
            elif state == "work":
                if "hungry" not in self.characteristics:
                    self.characteristics.append("hungry")
                print(f"\n{hour} hour:" )
                print('you work')
                self.current_state = self.work
            elif state == "brush_teeth":
                print(f"\n{hour} hour:" )
                print("no way, you've just brush your teeth")
                if random.uniform(0, 1) < 0.2:
                    print("oh there is no water, you can't brush your teeth now")
                else:
                    if "dirty teeth" in self.characteristics:
                        self.characteristics.remove("dirty teeth")
                    self.current_state = self.teeth
            elif state == "sing":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) > 0.3 and "healthy" in self.characteristics:
                    if "happy" not in self.characteristics:
                        self.characteristics.append("happy")
                    print("it's perfect time to sing a Britney's song\n")
                    print(random.choice(self.songs))
                    self.current_state = self.sing
                else:
                    print("you're too tired to sing :(")

    @prime
    def calm_state(self):
        '''
        start state at 1 AM
        '''
        while True:
            state, _ = yield
            if state == "eat":
                print(f"\n{hour} hour:" )
                if "hungry" in self.characteristics:
                    if random.uniform(0, 1) < 0.2:
                        print("you wake up at night, go to fridge, fall down on banana\
 peel and die\nsorry :)")
                        self.characteristics.remove("alive")
                        self.characteristics.append("dead")
                        print(f"you die with characteristics like that: {self.characteristics}")
                        exit()
                        
                    print("oh you are night-eating liker")
                    self.characteristics.remove("hungry")
                    self.characteristics.append("tired")
                    print('you eat')
                    self.current_state = self.eat
                else:
                    print("you are not hungry, go to the bed")
                    self.current_state = self.sleep

            elif state == "sleep":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) < 0.2:
                    print('congratulation you unlocked achivement "Mary"')
                    print('you became pregnant in sleep')
                    self.characteristics.append("pregnant")
                print("zzzzzzz")
                self.current_state = self.sleep

            elif state == "work":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) < 0.5:
                    print("you missed your work")
                    self.current_state = self.sleep
                else:
                    print("stupid deadlines, you need to work")
                    self.characteristics.append("tired")
                    print('you work')
                    self.current_state = self.work

            elif state == "brush_teeth":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) < 0.2:
                    print("oh there is no water, you can't brush your teeth now")
                else:
                    self.characteristics.remove("dirty teeth")
                    print('you brush teeth, go to the bed')
                    self.characteristics.append("tired")
                    self.current_state = self.sleep

            elif state == "sing":
                print(f"\n{hour} hour:" )
                if random.uniform(0, 1) < 0.2 and "healthy" in self.characteristics:
                    print("it's perfect time to sing a song\n")
                    print("Upside, inside out\n\
She's livin' la vida loca\n\
She'll push and pull you down\n\
Livin' la vida loca")
                    self.characteristics.append("tired")
                    print('you sing, go to bed now')
                else:
                    print("you are too tired to sing")
                self.current_state = self.sleep
if __name__ == "__main__":
    simulator = My_Day()
    states = ["eat", "sleep", "work", "brush_teeth", "sing"]
    for hour in range(1, 25):
        state = random.choice(states)
        simulator.send((state, hour))
        if hour == 24:
            simulator.current_state = simulator.final_state
            simulator.send((state, hour))
    