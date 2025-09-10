"""
Lab 3 - Functions

In THIS FILE you should write your code.
Compare with the solutions in `answers.py`.

Run with:
    python functions_lab_exercises.py
"""

# ----------------------
# Section 1: Basic functions
# ----------------------

import math

def ex_1_1():
    """
    Exercise 1.1 (1p)
    Create a function that returns the sum of all numbers between two chosen numbers.
    For example, 10 and 20 should return 10+11+12+...+20.
    """
    # TODO: Write your code here
    def sum_all_num(min_num, max_num):
        return sum(range(min_num, max_num + 1))
    return sum_all_num(22, 91)

def ex_1_2():
    """
    Exercise 1.2 (1p)
    Create a function that returns the color of a given fruit:
    banana -> yellow
    apple  -> green
    kiwi   -> green
    plum   -> red
    """
    # TODO: Write your code here
    # may also use a dictionary to give the value of color for each key (fruit as string)
    def fruit_color(fruit):
        fruit = ""
        if fruit == "banana":
            return "yellow"
        elif fruit == "apple" or "kiwi":
            return "green"
        elif fruit == plum:
            return "red"
    return fruit_color("plum")

def ex_1_3():
    """
    Exercise 1.3 (1p)
    Create a function that returns a comma-separated string of numbers from range_start to range_stop. """
    # TODO: Write your code here
    def string_of_num(range_start, range_stop):
        return ", ".join(str(i) for i in range(range_start, range_stop + 1))
    return string_of_num(25, 46)


def ex_1_4(): # !
    """
    Exercise 1.4 (1p)
    Create a function that returns a comma-separated string of numbers from range_start down to range_stop.    """
    # TODO: Write your code here
    def down_str_of_num(range_start, range_stop):
        return ", ".join(str(i) for i in range(range_start, range_stop-1, -1)) # range(start, stop, step)
    
    return down_str_of_num(46, 25)

def ex_1_5():
    """
    Exercise 1.5 (1p)
    Create a function that returns a comma-separated string of numbers between two values,
    handling both ascending and descending ranges.
    """
    # TODO: Write your code here
    def updown_list_str(range_start, range_stop):
        if range_start < range_stop:
            return ", ".join(str(i) for i in range(range_start, range_stop + 1))
        elif range_start > range_stop:
            return ", ".join(str(i) for i in range(range_start, range_stop-1, -1))
        else:
            return "these values are equal"
    return updown_list_str(25, 46)

def ex_1_6():
    """
    Exercise 1.6 (1p)
    Create a function that returns a string repeated a specified number of times.
    """
    # TODO: Write your code here
    def repeat_str(my_string, times):
        iter_print = 0
        while iter_print < times:
            print(my_string)
            iter_print += 1
    return repeat_str("grey", 12)

def ex_1_7():
    """
    Exercise 1.7 (1p)
    Create a function (that takes three arguments: range_start, range_stop, value) that returns True if a value is strictly between two given numbers,
    otherwise False.
    """
    # TODO: Write your code here
    def inbetween(a, num1, num2):
        if a > num1 and a < num2:
            return True
        elif a > num2 and a < num1:
            return True
        else:
            return False
    return inbetween(131, 547, 434)

def ex_1_8():
    """
    Exercise 1.9 (1p)
    Create a function called `degrees_to_radians()` that should take one
    argument, a degree value. The function should convert the value to radians
    and return the result with max 4 decimals    """
    # TODO: Write your code here
    def degrees_to_radians(val1):
        return round(math.radians(val1), 4)
    
    return degrees_to_radians(32)

def ex_1_9():
    """
    Exercise 1.10 (1p)
     Create a function called `fizz_buzz()` that takes two arguments `start` and
     `stop` and returns a comma-separated string.
    
     The arguments represents the starting point and stop point of the game
     `Fizz Buzz` (http://en.wikipedia.org/wiki/Fizz_buzz). The function should
     run from start to stop and add `Fizz`, `Buzz` or both to your
     result-variable at appropriate numbers.
    
     Each entry to your result should be comma-separated. If `stop` is equal or
     lower than `start`, the function should return an appropriate error
     message.
    """
    # TODO: Write your code here
    def fizz_buzz(start, stop):
        my_list = []
        if stop <= start:
            return "Stop must be greater than start."    
        for i in range(start, stop+1):
            if i % 15 == 0:
                my_list.append("Fizz Buzz")
            elif i % 3 == 0:
                my_list.append("Fizz")
            elif i % 5 == 0:
                my_list.append("Buzz")
            else:
                my_list.append(str(i))
                
        return ", ".join(my_list)

    return fizz_buzz(1, 30)


# ----------------------
# Section 2: Extra assignments
# ----------------------

def ex_2_1():
    """
    Exercise 2.1 (3p)
    
    Create a function that takes two variables: the sum of the player's hand 
    and the sum of the dealer's hand.
    
    Player's hand: 4, 10, 3
    Dealer's hand: 3, 6, 11
    
    The function should return a string in the format:
    'Player: 17, Dealer: 20'
    
    Test your function with these values.
    """
    # TODO: Write your code here
    def hand_tot(player_hand: list, dealer_hand: list):
        return f"Player: {sum(player_hand)}, Dealer: {sum(dealer_hand)}"
    return hand_tot([4, 10, 3], [3, 6, 11])

def ex_2_2():
    """
    Exercise 2.2 (3p)
    
    Create a function that takes two variables: the sum of the player's hand
    and the sum of the dealer's hand.
    
    Player's hand: 4, 10, 3
    Dealer's hand: 3, 6, 11
    
    Include a status check:
      - Player <21: "safe"
      - Player =21: "black jack"
      - Player >21: "busted"

      - Dealer <17: "safe"
      - Dealer >=17 and <21: "stop"
      - Dealer =21: "black jack"
      - Dealer >21: "busted"
    
    Return a string in the format: 'Player: safe, Dealer: busted'
    
    """
    # TODO: Write your code here
    def game_result(player_hand: list, dealer_hand: list):
        player_sum = sum(player_hand)
        dealer_sum = sum(dealer_hand)

        if player_sum < 21:
            player_status = "safe"
        elif player_sum == 21:
            player_status = "black jack"
        else:
            player_status = "busted"

        if dealer_sum < 21:
            dealer_status = "safe"
        elif dealer_sum == 21:
            dealer_status = "black jack"
        else:
            dealer_status = "busted"

        return f"Player: {player_status}, Dealer: {dealer_status}"

    return game_result([4, 10, 3], [3, 6, 11])

# ----------------------
# Helper runner for testing
# ----------------------

def _run_and_print(fn, label):
    try:
        result = fn()
        print(f"{label}: {result}")
    except NotImplementedError:
        print(f"{label}: (not implemented)")


def main():
    print("Running Lab 3 - Functions exercises...\n")
    _run_and_print(ex_1_1, "1.1")
    _run_and_print(ex_1_2, "1.2")
    _run_and_print(ex_1_3, "1.3")
    _run_and_print(ex_1_4, "1.4")
    _run_and_print(ex_1_5, "1.5")
    _run_and_print(ex_1_6, "1.6")
    _run_and_print(ex_1_7, "1.7")
    _run_and_print(ex_1_8, "1.8")
    _run_and_print(ex_1_9, "1.9")
    _run_and_print(ex_2_1, "2.1")
    _run_and_print(ex_2_2, "2.2")


if __name__ == "__main__":
    main()
