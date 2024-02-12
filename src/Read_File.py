import os
import time

def check_filename (filename):
    filename = f"./test/{filename}"
    print(os.path.abspath(filename))
    if not filename.endswith('.txt'):
        print("Error: Please input a .txt file\n")
        return False
    if not os.path.exists(filename):
        print(f"Error: There's not such file with name '{filename}' in the current directory.\n")
        return False
    
    return True
     

def start_time():
    return time.time()

def end_time():
    return time.time()


def output_solution():
    return

def write_solution():
    return
