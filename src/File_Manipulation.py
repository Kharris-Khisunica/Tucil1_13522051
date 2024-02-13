
import os
import time
import datetime
from Matrix import *

def check_filename (filename):
    filename = f"./Tucil1_13522051/test/{filename}"
    if not filename.endswith('.txt'):
        print("Error: Please input a .txt file\n")
        return False
    if not os.path.exists(filename):
        print(f"Error: There's not such file with name '{filename}' in the current directory.\n")
        return False
    
    return True
     



def print_solution (best_solution, total_time):
    solution_file =  []
    if best_solution != None:

        point = best_solution[0]
        token = best_solution[1]
        koordinat = best_solution[2]

        print(point) #Total point terbaik >= 0
        solution_file.append(point)

        print(' '.join(token))
        solution_file.append(' '.join(token))

        for i in koordinat:
            solution_file.append(','.join(map(str, i)))
            print(','.join(map(str, i))) 

    else: #Tidak ditemukan solusi yang point >=0
        print("Tidak Ada Solusi")
        solution_file.append("Tidak ada Solusi")
    
    print('\t')
    solution_file.append("")

    print(f"{total_time} ms")
    solution_file.append(f"{total_time} ms")

    print('\t')
    
    
    write_solution(solution_file)

def write_solution(solution_file):
    while True:
        input_solusi = input("Apakah ingin menyimpan solusi? (y/n): ")
        print("\t")
        if (input_solusi == 'y'):
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join("./test/", f"solusi_{current_time}.txt")
            with open(filename, 'w') as file:
                for i in solution_file:
                    file.write(str(i) + '\n')

            break
        elif (input_solusi == 'n'):
            break  


