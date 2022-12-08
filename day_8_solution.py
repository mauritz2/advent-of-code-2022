import numpy as np

f = open("day_8_data.txt", "r")
data = f.readlines()
data = list(map(lambda x: x.strip(), data))
f.close()


def is_visible_in_one_direction(trees:list[str], variable_axis_start: list[str], range_direction:int, variable_axis:str, fixed_axis_val:str, tree_val:int):
    visible = False

    range_end = -1 if range_direction == -1 else max(variable_axis_start)

    #for index in range(variable_axis_start, range_end, range_direction):
    for index in range(variable_axis_start, range_end, range_direction):

        if variable_axis == "row":
            comparison_tree_val= int(trees[index][fixed_axis_val])
        elif variable_axis == "col":
            comparison_tree_val= int(trees[fixed_axis_val][index])
      
        print(f"Comparing: {comparison_tree_val} to {tree_val}")
        if comparison_tree_val >= tree_val:
            # Tree is not visible from this direction - 
            print("Breaking! Not visible")
            break
    else:
        print("Tree is visible")
        visible = True
    
    return visible


def is_visible(tree_val: int, tree_row: int, tree_col: int, trees: list[int]) -> bool:
    print(f"\n\nLooking into ({tree_row}, {tree_col}): {tree_val}")

    # Check if edge node 
    if ((tree_row == 0) or (tree_row == len(trees)) or (tree_col == 0) or (tree_col == len(trees[0]))):
        print("This is an edge node. It's visible")
        return True

    # Check up
    variable_axis_start = tree_row - 1
    range_direction = -1
    variable_axis = "row"
    fixed_axis_val = tree_col
    tree_val = tree_val

    visible_up = is_visible_in_one_direction(
        trees=trees,
        variable_axis_start=variable_axis_start,
        range_direction=range_direction,
        variable_axis=variable_axis,
        fixed_axis_val=fixed_axis_val,
        tree_val=tree_val)
    
    

    # Check down

    # Check left

    # Check right


def part_1(trees):
    visible = 0
    for row_index, tree_row in enumerate(trees):
        if row_index == 2:
            quit()
        print("New row\n\n")
        print(tree_row)
        print("\n\n")
        for col_index, tree_val in enumerate(tree_row):
            if is_visible(tree_val=int(tree_val), tree_row=row_index, tree_col=col_index, trees=trees):
                visible += 1            


if __name__ == "__main__":
    part_1(trees=data)
    