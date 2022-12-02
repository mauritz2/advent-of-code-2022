# Validated as correct solution
with open("data.txt", "r") as f:
    calorie_sum = []
    data = f.readlines()
    current_elf_sum = 0
    for line in data:
        if line == "\n":
            calorie_sum.append(current_elf_sum)
            current_elf_sum = 0
        else:
            current_elf_sum += int(line)
    print(max(calorie_sum))

