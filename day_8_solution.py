f = open("day_8_data.txt", "r")
data = f.readlines()
data = list(map(lambda x: x.strip(), data))
f.close()

def is_visible_in_direction(trees: list[str], direction: str, row: str, col: str):
    """
    Calculates if a tree is visible from a specific direction (i.e. if there are taller trees in that direction)
    Returns True if visible from the direction, otherwise False. 
    For part 2 - also calculates and returns the scenic score (i.e. how many trees you can see from the given tree)
    """
    ### For Part 2 ###
    scenic_score = 0
    ### End of Part 2 ### 

    # Check if edge node
    if ((row == 0) or (row == len(trees) - 1) or (col == 0) or (col == len(trees[0]) - 1)):
        ### For Part 2 ###
        scenic_score += 1
        ### End of Part 2 ###
        return True, scenic_score

    # Set variables 
    match direction:
        case "up":
            variable_axis_start = row - 1
            range_direction = -1
            variable_axis = "row"
            fixed_axis_val = col
            range_end = -1
        case "left":
            variable_axis_start = col - 1
            range_direction = -1
            variable_axis = "col"
            fixed_axis_val = row
            range_end = -1
        case "right":
            variable_axis_start = col + 1
            range_direction = 1
            variable_axis = "col"
            fixed_axis_val = row
            range_end = len(trees[0])
        case "down":
            variable_axis_start = row + 1
            range_direction = 1
            variable_axis = "row"
            fixed_axis_val = col
            range_end = len(trees)

    tree_val = int(trees[row][col])

    # Check visibility in the defined direction
    visible = True
    # Iterates over all the values in the defined direction
    for index in range(variable_axis_start, range_end, range_direction):
        ### For Part 2 ###
        scenic_score = scenic_score + 1
        ### End of Part 2 ###        
        if variable_axis == "row":
            comparison_tree_val= int(trees[index][fixed_axis_val])
        elif variable_axis == "col":
            comparison_tree_val= int(trees[fixed_axis_val][index])
        if comparison_tree_val >= tree_val:
            # We found a taller tree in this direction. Tree is not visible_trees from this direction.
            visible = False
            break
    
    return visible, scenic_score


def is_visible(row: int, col: int, trees: list[int]) -> bool:
    """
    Checks if a tree is visible_trees in all directions. Returns True if visible_trees in any direction, otherwise False 
    """
    # Check visibility
    is_visible_up, _ = is_visible_in_direction(trees=trees, direction="up", row=row, col=col)    
    is_visible_left, _ = is_visible_in_direction(trees=trees, direction="left", row=row, col=col)    
    is_visible_right, _ = is_visible_in_direction(trees=trees, direction="right", row=row, col=col)    
    is_visible_down, _ = is_visible_in_direction(trees=trees, direction="down", row=row, col=col)    
    # If tree is visible from any direction, return True. Otherwise return False.
    return True if True in [is_visible_up, is_visible_down, is_visible_left, is_visible_right] else False

# PART 1 - Validated answer: 1690
def part_1(trees):
    visible_trees = 0
    for row_index in range(len(trees)):
        for col_index in range(len(trees[0])):
            if is_visible(row=row_index, col=col_index, trees=trees):
                visible_trees += 1
    print(f"There are {visible_trees} visible trees!")            

# PART 1 - Validated answer: 535680
def part_2(trees):
    scenic_scores = []
    for row_index in range(len(trees)):
        for col_index in range(len(trees[0])):
            _, scenic_score_up = is_visible_in_direction(trees=trees, direction="up", row=row_index, col=col_index)
            _, scenic_score_down = is_visible_in_direction(trees=trees, direction="down", row=row_index, col=col_index)
            _, scenic_score_left = is_visible_in_direction(trees=trees, direction="left", row=row_index, col=col_index)
            _, scenic_score_right = is_visible_in_direction(trees=trees, direction="right", row=row_index, col=col_index)
            total_scenic = scenic_score_up * scenic_score_down * scenic_score_left * scenic_score_right
            scenic_scores.append(total_scenic)
    best_scenic = max(scenic_scores)
    print(f"The best scenic score is {best_scenic}!")

if __name__ == "__main__":
    part_1(trees=data)
    part_2(trees=data)

