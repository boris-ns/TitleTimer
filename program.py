import sys
import os.path
from datetime import datetime
from datetime import timedelta

def load_file_content(file_name):
    content = None
    with open(file_name, encoding="latin-1") as file:
        content = file.readlines()

    return content

def is_time_format(line):
    try:
        line_split = line.split("-->")
        start_time = datetime.strptime(line_split[0].strip(), "%H:%M:%S,%f")
        end_time = datetime.strptime(line_split[1].strip(), "%H:%M:%S,%f")
    except ValueError:
        return None, None

    return start_time, end_time

def time_to_str(time):
    return datetime.strftime(time, "%H:%M:%S,%f")[:-3]

def change_time(content, seconds):
    for line in content:
        start_time, end_time = is_time_format(line)
        
        if start_time == None and end_time == None:
            continue

        start_time += timedelta(seconds=seconds)
        end_time += timedelta(seconds=seconds)
        content[content.index(line)] = time_to_str(start_time) + " --> " + time_to_str(end_time) + "\n"


def save_changes(content, file_name):
    with open(file_name[:-4] + "-new_version.srt", "w") as file:
        for line in content:
            file.write(line)

def print_error_msg(msg):
        print(msg)
        print("Please run the program with 'python program.py srt-file num-of-seconds'")
        print("Example: python program.py my-title.srt 12.421")

def is_float(num):
    try:
        float(num)
    except ValueError:
        return False

    return True

def load_arguments():
    # 3 because first arguments is name of python file
    if len(sys.argv) != 3:
        print_error_msg("There are some missing/surplus arguments.")
        return []

    if not os.path.isfile(sys.argv[1]):
        print_error_msg("File '" + sys.argv[1] + "' doesn't exist!")    
        return []

    if not is_float(sys.argv[2]):
        print_error_msg("Invalid seconds format!")
        return []

    return sys.argv

if __name__ == "__main__":
    arguments = load_arguments()
    if len(arguments) == 0:
        sys.exit(0)
    
    file_name = arguments[1]
    seconds = float(arguments[2])
    file_content = load_file_content(file_name)
    
    change_time(file_content, seconds)
    save_changes(file_content, file_name)