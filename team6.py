####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'MasterChef'
strategy_name = 'Juke'
strategy_description = 'Checks past history and adjusts accordingly.'
betrays = 0
def move(my_history, their_history, my_score, their_score):
    global betrays
    if len(my_history) == 0:
        return 'c'
    if their_history[-1] == 'b':
        betrays += 1
    if their_history[-1] == 'b':
        for g in range(betrays):
            return 'b'
    elif their_history[-1] == 'c':
        return 'c'