import re

# DATA
f = open("day_7_data.txt", "r")
data = f.readlines()
f.close()

def update_filepath(filepath: str, command: str) -> str:
    """
    Take a filepath and a linux file command as input: cd .. | cd {dir} | ls | cd /
    Return the updated filepath as a str
    """
    filepath_list = filepath.split("/") 
    operation = command[:2]
    match operation:
        case "ls":
            # ls has no impact on current folder 
            pass
        case "cd":
            _, param = command.split(" ")
            match param:
                case "..":
                    # Go one folder up - i.e. remove last folder in path
                    filepath_list = filepath_list[:-1] 
                case "/":
                    # Return to home
                    filepath_list = ["/"]
                case _:
                    # Add new folder to path
                    filepath_list.append(param)
    return "/".join(filepath_list).replace("//", "/")

def calculate_folder_size(terminal_input: list[str]) -> dict:
    """
    Take a Linux file command input log and map out the folder structure and each folder's associated file size
    Returns a dict in format {filepath:size}
    """
    folder_sizes = {}
    current_filepath = "/"
    command_regex = re.compile(r"(?:^\$ )([a-z \/\.]*)")
    filesize_regex = re.compile(r"^[0-9]+ ")
    for row in terminal_input:
        row = row.strip()
        if command_regex.match(row) is not None:
            # The command is a user command (e.g. "$ cd .."")
            # .group(1) makes sure we're just sending the actual command and excluding the $
            command = command_regex.match(row).group(1)
            current_filepath = update_filepath(filepath=current_filepath, command=command)
        if filesize_regex.match(row) is not None:
            # The command is a linux terminal output (e.g. "104564 dnbmm.bgc")
            filesize = int(filesize_regex.match(row).group(0))
            if current_filepath in folder_sizes:
                folder_sizes[current_filepath] += filesize
            else:
                folder_sizes[current_filepath] = filesize
    return folder_sizes

def roll_up_folder_size(size_by_folder: dict) -> dict:
    """
    Take a dict in format {filepath:size} and roll up the filesize so child folder size 
    count towards the size of parent folders. This approach assumes unique folder names!
    """
    rolled_up_folder_size = {}
    for key in size_by_folder.keys():
        # Loop through all known paths in file system
        # Exclude the first list item after split to exclude [""] (the left-hand side of home dir "/")
        # Otherwise the home directory gets double-counted 
        folder_path_parts = key.split("/")[1:]
        for i in range(1, len(folder_path_parts) + 1):
            # For each path - iterate through all folders in the path
            path_to_sum = "/".join(folder_path_parts[:i])
            if path_to_sum in rolled_up_folder_size:
                # We've already counted this path - let's not do it again
                # Otherwise we would count high-level paths like "/" multiple times and get the wrong size
                continue
            for key, value in size_by_folder.items():
                # For each folder - find all sub-folders and sum their size
                if path_to_sum in key:
                    # We've found a sub-folder - add its size to the current parent we're looping through
                    if path_to_sum in rolled_up_folder_size:
                        rolled_up_folder_size[path_to_sum] += value
                    else:
                        rolled_up_folder_size[path_to_sum] = value
    return rolled_up_folder_size

# PART 1 - Validated answer: 1543140
def part_1():
    size_by_folder = calculate_folder_size(data)
    size_by_folder_roll_up = roll_up_folder_size(size_by_folder)  
    small_folders = {k:v for k, v in size_by_folder_roll_up.items() if v < 100000}
    small_folders_sum = sum(small_folders.values())
    print(f"The sum of the size of all folders with a size below 100,000 is {small_folders_sum:,}")

# PART 1 - Validated answer: 1117448
def part_2():
    # Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update
    total_space = 70000000
    required_space_for_update = 30000000    
    size_by_folder = calculate_folder_size(data)
    used_space = sum(size_by_folder.values())
    available_space = total_space - used_space
    space_to_free_up = required_space_for_update - available_space

    size_by_folder_roll_up = roll_up_folder_size(size_by_folder)  
    deletable_folders = [v for v in size_by_folder_roll_up.values() if v > space_to_free_up]
    smallest_folder_size = min(deletable_folders)
    print(f"The smallest folder we can delete to fit in the system update has size {smallest_folder_size:,}")

if __name__ == "__main__":
    part_1()
    part_2()
