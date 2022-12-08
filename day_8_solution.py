import numpy as np

f = open("day_8_data.txt", "r")
data = f.readlines()
data = list(map(lambda x: x.strip(), data))
f.close()

def is_visible_in_direction(trees:list[str], direction: str, row: str, col: str):

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

    for index in range(variable_axis_start, range_end, range_direction):
        if variable_axis == "row":
            comparison_tree_val= int(trees[index][fixed_axis_val])
        elif variable_axis == "col":
            comparison_tree_val= int(trees[fixed_axis_val][index])
        #print(f"Comparing: {comparison_tree_val} to {tree_val}")
        if comparison_tree_val >= tree_val:
            # Tree is not visible from this direction because it's blocked
            visible = False
    
    return visible


def is_visible(tree_val: int, row: int, col: int, trees: list[int]) -> bool:
    print(f"\n\Checking visibility of ({row}, {col}): {tree_val}")

    # Check if edge node 
    if ((row == 0) or (row == len(trees) -1 ) or (col == 0) or (col == len(trees[0]) - 1)):
        print("This is an edge node. It's visible")
        return True

    # Check directional visibility
    is_visible_up = is_visible_in_direction(trees=trees, direction="up", row=row, col=col)    
    print(f"Upwards visibility: {is_visible_up}")
    is_visible_left = is_visible_in_direction(trees=trees, direction="left", row=row, col=col)    
    print(f"Leftwards visibility: {is_visible_left}")
    is_visible_right = is_visible_in_direction(trees=trees, direction="right", row=row, col=col)    
    print(f"Rightwards visibility: {is_visible_right}")
    is_visible_down = is_visible_in_direction(trees=trees, direction="down", row=row, col=col)    
    print(f"Downwards visibility: {is_visible_down}")

    # If tree is visible from any direction, return True. Otherwise False.
    return True if True in [is_visible_up, is_visible_down, is_visible_left, is_visible_right] else False

# PART 1 - Validated answer: 1690

def part_1(trees):
    visible = 0
    for row_index, tree_row in enumerate(trees):
        for col_index, tree_val in enumerate(tree_row):
            if is_visible(tree_val=int(tree_val), row=row_index, col=col_index, trees=trees):
                print("This one is visible - incrementing by 1!")
                visible += 1
    print(f"There are {visible} visible trees!")            

if __name__ == "__main__":
    part_1(trees=data)
    