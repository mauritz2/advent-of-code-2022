# GET DATA
# Get container start
f = open("day_5_data_2.txt", "r")
container_start_raw = f.readlines()
f.close()

# Get moving instructions
f = open("day_5_data_1.txt", "r")
instructions = f.readlines()
f.close()

# PHASE 1 - Validated answer: CWMTGHBDW

def get_container_cols(lines: str) -> list[str]:
    result = []
    for col_num in range(9):
        row = []
        for x in lines:
            x_split = x.split(",")
            value = x_split[col_num]
            if value == "   ":
                continue
            value = value.replace("[", "").replace("]", "")
            value = value.strip()
            row.append(value)
        else:
            result.append(row)
    return result

def execute_instruction_1(container_state: dict, instruction: str) -> dict:
    instruction = instruction.strip()
    instruction_split = instruction.split(" ")
    amount_to_move = int(instruction_split[1])
    source = instruction_split[3]
    target = instruction_split[5]

    for _ in range(amount_to_move):
        container_to_move = container_state[source].pop(0)
        container_state[target].insert(0, container_to_move)

    return container_state


def main_phase_one():
    container_start = get_container_cols(container_start_raw)

    container_state = {}
    for col_num, col in enumerate(container_start, start=1):
        container_state[str(col_num)] = col

    for instruction in instructions:
        container_state = execute_instruction_1(container_state, instruction)
    
    top_containers = []
    for col in container_state.values():
        top_containers.append(col[0])
    
    print(("").join(top_containers))


# PHASE 2 - Validated answer: SSCGWJCRB
def execute_instruction_2(container_state: dict, instruction: str) -> dict:
    instruction = instruction.strip()
    instruction_split = instruction.split(" ")
    amount_to_move = int(instruction_split[1])
    source = instruction_split[3]
    target = instruction_split[5]

    container_to_move = container_state[source][:amount_to_move]
    del container_state[source][:amount_to_move]
    container_state[target] = container_to_move + container_state[target] 

    return container_state

def main_phase_two():
    container_start = get_container_cols(container_start_raw)

    container_state = {}
    for col_num, col in enumerate(container_start, start=1):
        container_state[str(col_num)] = col

    for instruction in instructions:
        container_state = execute_instruction_2(container_state, instruction)
    
    top_containers = []
    for col in container_state.values():
        top_containers.append(col[0])
    
    print(("").join(top_containers))

if __name__ == "__main__":
    main_phase_one()
    main_phase_two()