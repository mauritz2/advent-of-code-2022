
def update_head(head_coords: tuple[int, int], direction: str) -> tuple[int, int]:
    """
    Updates the coordinate of the head based on the instruction (e.g. R 12 is move right 12 locations)
    """ 
    x, y = head_coords

    match direction:
        case "U":
            y = y - 1 
        case "D":
            y = y + 1 
        case "R":
            x = x + 1 
        case "L":
            x = x - 1
    new_head_pos = (x, y)

    # Verify that we didn't end up with negative coords
    assert x >= 0
    assert y >= 0

    return new_head_pos


def update_tail(head_coords: tuple[int, int], tail_coords: tuple[int, int]) -> tuple[int, int]:
    """
    Takes a head and tail coordinate pair as input and returns the updated tail position based on the head position.
    """
    # Get the coordinate diff between head and tail as a tuple, e.g. (-2, 1)
    diff = tuple(int(x) - int(y) for x, y in zip(head_coords, tail_coords))
    x_diff, y_diff = diff

    if (abs(x_diff) <= 1 and abs(y_diff) <= 1):
        # Tail is already adjacent to head - no movement necessary
        return tail_coords

    # Adjust the x or y axis one step closer to head if they have a higher diff than 0
    new_x, new_y = tail_coords

    if y_diff > 0:
        new_y =  new_y + 1
    elif y_diff < 0:
        new_y =  new_y - 1
    
    if x_diff > 0:
        new_x =  new_x + 1
    elif x_diff < 0:
        new_x =  new_x - 1

    return (new_x, new_y)


def create_board(board_dimension: int) -> list[list[str]]:
    board = []
    for _ in range(board_dimension):
        row = [" "] * board_dimension
        board.append(row) 
    return board


def part_1(data):
    coords_set = set()
    start = 1000 // 2
    head_coords = (start, start)
    tail_coords = (start, start)
    for instruction in data:
            direction, num_moves = instruction.split(" ")
            num_moves = int(num_moves)
            for _ in range(num_moves):
                head_coords = update_head(head_coords, direction)
                tail_coords = update_tail(head_coords=head_coords, tail_coords=tail_coords)
                coords_set.add(tail_coords)
    print(f"The tail visited {len(coords_set)} locations")

def part_2(data):
    coords_set = set()
    # rope_pieces[0] = head
    # rope_pieces[-1] = tail
    rope_pieces = [(250, 250) for _ in range(10)]
    board = create_board(500)
    for instruction in data:
            # For each instruction (e.g. U 12) to move the head of the rope
            direction, num_moves = instruction.split(" ")
            num_moves = int(num_moves)
            for i in range(num_moves):
                # Execute each head movement one step at a time
                rope_pieces[0] = update_head(rope_pieces[0], direction)
                for i, rope_piece in enumerate(rope_pieces[1:], 1):
                    # Adjust each rope piece in relation to the one closest up ahead
                    rope_pieces[i] = update_tail(rope_pieces[i - 1], rope_piece)
                    if i == len(rope_pieces[1:]):
                        # Update the new tail (last rope piece) position 
                        board[rope_pieces[i][1]][rope_pieces[i][0]] = "X"
                        coords_set.add(rope_pieces[i])

    print(f"The tail passed through {len(coords_set)} locations. See positions below:")
    for row in board:
        print("|".join(row))

if __name__ == "__main__":
    f = open("day_9_data.txt", "r")
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))
    f.close()

    part_1(data) # Validated answer 6089
    part_2(data) # Validated answer 2493

