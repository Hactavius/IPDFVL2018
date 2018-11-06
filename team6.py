####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'Backstab'
strategy_name = 'Looks peaceful but it hurts.'
strategy_description = 'How does this strategy decide?'
betraytime = 0
didb = 0
bc = 0
def move(my_history, their_history, my_score, their_score):
    global betraytime
    global didb
    global bc
    if len(my_history) == 0:
        return 'c'
    if len(my_history) == 1:
        return 'c'
    if betraytime == 4:
        betraytime = 0
        return 'b'
    elif their_history[-1] == 'c':
        betraytime =betraytime + 1
        return 'c'
    elif their_history[-1]== 'b':
        didb += 1
        betraytime =betraytime +1
        if didb == 1:
            betraytime = betraytime +1
            return 'c'
        elif didb == 2:
            didb = 0
            betraytime =betraytime +1
            bc +=1
            if bc == 3:
                bc = 0
                return 'b'
            return 'b'