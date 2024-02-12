
import os
import time
import datetime
from Matrix import *

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
     

def output_solution(matrix, width, height, seq_all, n_seq, total_time):
    sol = get_all_True(matrix, width, height)
    total = get_total_point(seq_all, n_seq)

    print(total) #Total point

    for i in range (0,len(sol),2): #Get Token
        print(sol[i], end=" ")
    print('\t')

    for i in range (1,len(sol),2): #Get koordinat
        print(f"{sol[i][0]},{sol[i][1]}")
    print('\n')

    print(f"{total_time} ms")


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
            filename = os.path.join("./test/", f"output_{current_time}.txt")
            with open(filename, 'w') as file:
                for i in solution_file:
                    file.write(str(i) + '\n')

            break
        elif (input_solusi == 'n'):
            break  


def start_time():
    return time.time()

def end_time():
    return time.time()

if __name__ == "__main__":
    print_solution([20, ['a','b', 'c', 'ef'], [[1,2], [2,3], [3,4], [2,4]]], 10)
    print_solution(None, 0)
