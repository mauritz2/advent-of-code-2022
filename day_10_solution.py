def create_screen(row_num: int, col_num: int) -> list[list[str]]:
    """
    Return a 2D list representing the screen
    """
    screen = []
    for _ in range(row_num):
        screen.append([" "] * col_num)
    return screen

def get_signal_strength_by_cycle(instructions: list[str]) -> dict[int, int]:
    """
    Return a dictionary of the signal strength at each cycle count
    X is an input needed to calc signal strength (X * cycle num)
    """
    x = 1
    cycle_num = 1
    x_by_cycle = {}
    queue = [0]
    available = True
    instructions = instructions.copy()
    while len(queue) > 0:        
        if available:
            # Device is ready for another instruction
            if (len(instructions) == 0):
                # There are no more instructions to process
                break

            instruction = instructions.pop(0)
            if "noop" in instruction:
                # Add a 0 - i.e. no effect on signal strength this cycle 
                queue.append(0)
            elif "addx" in instruction:
                _, value_to_queue = instruction.split(" ")
                value_to_queue = int(value_to_queue)
                # Add the signal strength adjustment (V) and a 0 so it takes two cycles to add V 
                queue.append(0)
                queue.append(value_to_queue)
                available = False
        else:
            # An addx takes two cycles - if one cycle was skipped addx is complete by the next
            available = True

        cycle_value = queue.pop(0)
        x += cycle_value
        x_by_cycle[cycle_num] = x
        cycle_num += 1

    return x_by_cycle

def get_pixel_to_coord_mapping():
    """
    Return a mapping between screen pixel coordinates (0,0 to 5,39) and their index (1-240)
    """
    pixel_to_coord_map = {}
    pixel_num = 0
    for i in range(6):
        for j in range(40):
            pixel_num += 1
            pixel_to_coord_map[pixel_num] = (i, j)
    return pixel_to_coord_map

def part_1(data):
    total = 0
    x_by_cycle = get_signal_strength_by_cycle(data)
    cycles_of_interest = [20, 60, 100, 140, 180, 220]
    for cycle in cycles_of_interest:
        total += (x_by_cycle[cycle] * cycle)
    print(f"The sum of the signal strengths is {total}")

def part_2(data):
    screen = create_screen(6, 40)
    signal_strength_by_cycle = get_signal_strength_by_cycle(data)
    pixel_to_coord_map = get_pixel_to_coord_mapping()

    for pixel_num in range(1, 241):
        # Loop through 1-240 (there are 240 pixels and 240 cycles)
        pixel_coords = pixel_to_coord_map[pixel_num]
        row_num, col_num = pixel_coords
        current_signal_strength = signal_strength_by_cycle[pixel_num]

        if col_num in [current_signal_strength - 1, current_signal_strength, current_signal_strength + 1]:
            # Pixel is lit
            screen[row_num][col_num] = "#"
        else:
            # Pixel is dark 
            screen[row_num][col_num] = "."

    print("These are the spelled out letters on the screen:")        
    for row in screen:
        print(" ".join(row))

if __name__ == "__main__":
    f = open("day_10_data.txt")
    data = f.read().strip().split("\n")
    part_1(data)
    part_2(data)
