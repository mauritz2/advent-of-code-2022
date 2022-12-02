# GET DATA
f = open("day_1_data.txt", "r")
data = f.readlines()
f.close()

# PART 1
# Validated answer as correct

def get_calories_by_elf(calories):
    calories_sum_by_elf = []
    current_elf_sum = 0
    for line in calories:
        if line == "\n":
            calories_sum_by_elf.append(current_elf_sum)
            current_elf_sum = 0
        else:
            current_elf_sum += int(line)
    return calories_sum_by_elf

calories_by_elf = get_calories_by_elf(data)
print(max(calories_by_elf))

# PART 2
# Validated answer as correct

calories_by_elf.sort(reverse=True)
top_three = calories_by_elf[:3]
print(sum(top_three))