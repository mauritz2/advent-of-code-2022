import string

# GET DATA
f = open("day_3_data.txt", "r")
data = f.readlines()
f.close()

# PART 1 - Validated answer: 8139

# Generate the letters points dict
all_items = string.ascii_lowercase + string.ascii_uppercase
item_priority = {item:index + 1 for index, item in enumerate(all_items)}

def get_common_item(packing_data: list[str]) -> str:
    """
    Take a list of packing instruction strs, and return the common item (i.e. letter) between them
    """
    set_list = [set(packing_list) for packing_list in packing_data]
    common_item = list(set.intersection(*set_list))
    assert len(common_item) == 1 # Always one item missing
    return common_item[0]

def main_part_1():
    total_priority = 0
    for row in data:
        # Remove \n from the row
        row = row.strip()
        midway_point = len(row) // 2
        first_half = row[:midway_point]
        second_half = row[midway_point:]
        misplaced_item = get_common_item([first_half, second_half])
        total_priority += item_priority[misplaced_item]        
    print(f"Total priority for re-arrangement is {total_priority}")


# PART 2 - Validated answer 2668
def main_part_2():
    total_priority = 0
    group_of_elves = []
    for index, row in enumerate(data, start=1):
        row = row.strip()
        group_of_elves.append(row)

        if index % 3 == 0:
            badge_letter = get_common_item(group_of_elves)
            total_priority += item_priority[badge_letter]
            group_of_elves = []
    print(f"Total priority for badge re-labeling is {total_priority}")


if __name__ == "__main__":
    main_part_1()
    main_part_2()
    

