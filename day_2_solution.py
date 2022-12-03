# GET DATA

# Rock = A or X
# Paper = B or Y
# scissors = C or Z   

f = open("day_2_data.txt", "r")
data = f.readlines()
f.close()

### PART 1 ###
# Confirmed correct

win = 6
draw = 3
loss = 0

match_outcome_points = {
    "AX": draw,
    "AY": win,
    "AZ": loss,
    "BX": loss,
    "BY": draw,
    "BZ": win,
    "CX": win,
    "CY": loss,
    "CZ": draw
}

shape_points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def calculate_points(strategy_guide):
    my_score = 0
    for row in data:
        my_move = row[2]
        their_move = row[0]
        my_score += shape_points[my_move]
        my_score += match_outcome_points[their_move + my_move]
    return my_score

calculate_points(data)

### PART 2 ###
# Confirmed correct

letter_to_shape = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

letter_to_match_outcome = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

outcome_points = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

shape_to_play = {
    "draw": {
        "rock":"rock",
        "paper":"paper",
        "scissors":"scissors"
    },
    "win": {
        "rock":"paper",
        "paper":"scissors",
        "scissors":"rock"
    },
    "lose": {
        "rock":"scissors",
        "paper":"rock",
        "scissors":"paper"
    }
}

shape_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def calculate_points_part_2(strategy_guide):
    total_score = 0
    for row in strategy_guide:
        # Add match outcome score
        match_outcome_letter = row[2]
        match_outcome = letter_to_match_outcome[match_outcome_letter]
        total_score += outcome_points[match_outcome]

        # Add shape score
        opponent_shape_letter = row[0]
        opponent_shape = letter_to_shape[opponent_shape_letter]
        my_shape = shape_to_play[match_outcome][opponent_shape]
        total_score += shape_points[my_shape]

    return total_score

print(calculate_points_part_2(data))


