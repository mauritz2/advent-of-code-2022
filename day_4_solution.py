## GET DATA
f = open("day_4_data.txt", "r")
data = f.readlines()
f.close()


## PART 1: Validated answer: 571

def find_start_end(cleaning_ids_str: str) -> list[list[int, int]]:
    """
    Takes a row of cleaning area assignments IDs ("80-80,25-80") and 
    returns the start, end of the cleaning zone IDs as ints ([[80, 80], [25, 80]])
    """
    cleaning_ids_start_end = []
    cleaning_ids_list = cleaning_ids_str.split(",")
    for ids in cleaning_ids_list:
        start, end = ids.split("-")
        cleaning_ids_start_end.append([int(start), int(end)])
    return cleaning_ids_start_end

def get_full_int_range(start: int, end: int) -> list[int]:
    full_int_range = [i for i in range(start, end + 1)]
    return full_int_range

def calculate_num_redundant_cleanings(cleaning_assignments: str):
    redundant_cleanings = 0
    for row in data:
        start_end_ints = find_start_end(row)
        cleaning_areas_left = set(get_full_int_range(start=start_end_ints[0][0], end=start_end_ints[0][1]))
        cleaning_areas_right = set(get_full_int_range(start=start_end_ints[1][0], end=start_end_ints[1][1]))
        # Check if one cleaning assignment is completely contained in another
        if (len(cleaning_areas_left - cleaning_areas_right) == 0) or (len(cleaning_areas_right - cleaning_areas_left) == 0):
            redundant_cleanings += 1
    return redundant_cleanings
            
## PART 2. Validated answer: 917.

def is_overlap(left_cleaning_ids: set, right_cleaning_ids: set) -> bool:
    intersect = left_cleaning_ids.intersection(right_cleaning_ids)
    return True if len(intersect) > 0 else False

def calculate_pairs_with_overlap(cleaning_assignments: str):
    pairs_with_overlap = 0
    for row in data:
        start_end_ints = find_start_end(row)
        cleaning_areas_left = set(get_full_int_range(start=start_end_ints[0][0], end=start_end_ints[0][1]))
        cleaning_areas_right = set(get_full_int_range(start=start_end_ints[1][0], end=start_end_ints[1][1]))
        if is_overlap(cleaning_areas_left, cleaning_areas_right):
            pairs_with_overlap += 1
    return pairs_with_overlap            

if __name__ == "__main__":
    print(calculate_num_redundant_cleanings(data))
    print(calculate_pairs_with_overlap(data))
