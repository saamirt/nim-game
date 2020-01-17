from Strategy import *
import time

class Nim:
    def __init__(self, strategy = unbeatable_strategy, init_count=12, max_turn = 3):
        self.__strategy = strategy
        self.__remaining = init_count
        self.__MAX_TURN = max_turn
        
    def player_turn(self, user_move):
        print(f'User has taken {user_move} items.')
        self.__remaining -= user_move
        if not self.__remaining:
            return 1
        return 0
    
    def robot_turn(self):
        robot_move = self.__strategy(self.__remaining, self.__MAX_TURN)
        time.sleep(0.5)
        print(f'Robot has taken {robot_move} items.')
        self.__remaining -= robot_move
        if not self.__remaining:
            return 2
        return 0

    def __get_input(self, question):
        while True:
            try:
                res = int(input(question))
                assert 1 <= res <= self.__MAX_TURN
                assert res <= self.__remaining
                return res
            except:
                print("Invalid response. Try again.")
            

    def play(self, bot_first = False):
        if bot_first:
            self.remaining += 1
            self.robot_turn()
        while True:
            user_move = self.__get_input(f'There are {self.__remaining} items left. How many items do you want? ')
            end = self.player_turn(user_move) or self.robot_turn()
            if end:
                if end == 1:
                    print("User has won.")
                elif end == 2:
                    print("Robot has won.")
                return end

if __name__ == '__main__':
    n = Nim(unbeatable_strategy)
    n.play()
