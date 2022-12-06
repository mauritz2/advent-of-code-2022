import re

f = open("day_6_data.txt", "r")
signal_data = f.readlines()[0]
f.close()

# PHASE 1 - Validated answer: 1909
def get_marker_pos(received_signal: str, marker_len: int) -> int:
        regex = "(.)"
        for i in range(1, marker_len):
            # The regex below matches 4 chars where each char is not the same as any previously matched char:
            # (.)(?!\1)(.)(?!(\1\2))(.)(?!(\1\2\3))(.)
            # But writing this out for a 14 char marker is a lot of manual work
            # I can't find a regex way to reference "all previous capturing group"
            # Therefore creating the regex through a loop to avoid having to create a super long regex manually
            regex += "".join([f"(?!\{num})" for num in range(1, i + 1)])  
            regex += "(.)"
        marker_re = re.compile(regex)
        match_pos = re.search(marker_re, received_signal)
        return match_pos.end(0)

def phase_one(): 
    first_start_of_packet_pos = get_marker_pos(received_signal=signal_data, marker_len=4)
    print(f"The first packet start is at {first_start_of_packet_pos}")

# PHASE 2: Validated answer 3380
def phase_two(): 
    first_start_of_msg_pos = get_marker_pos(received_signal=signal_data, marker_len=14)
    print(f"The first message start is at {first_start_of_msg_pos}")

if __name__ == "__main__":
    phase_one()
    phase_two()