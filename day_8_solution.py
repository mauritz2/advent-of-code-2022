import numpy as np

f = open("day_8_data.txt", "r")
data = f.readlines()
data = list(map(lambda x: x.strip(), data))
f.close()

def is_visible(tree_val: int, tree_row: int, tree_col: int, trees: list[int]) -> bool:
    # Check up

    visible = False

    print(f"\n\nLooking into ({tree_row}, {tree_col}): {tree_val}")

    first_row_above = tree_row - 1
    if first_row_above >= 0:
        # We need -1 instead of 0 because the end is non-inclusive
        for row_i in range(first_row_above, -1, -1):
            comparison_tree_val= int(trees[row_i][tree_col])
            print(f"Comparing: {comparison_tree_val} to {tree_val}")
            if comparison_tree_val >= tree_val:
                # Tree is not visible from this direction - 
                print("Breaking! Not visible")
                break
        else:
            print("This tree is visible")
            # Couldn't find a single tree in this direction that was taller
            visible = True
    else:
        # This is an edge tree
        print("This is an edge upwards so its visible")
        visible = True

    return visible

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
    