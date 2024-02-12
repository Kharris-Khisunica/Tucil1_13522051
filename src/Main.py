#Show Greeting

from Move import *
from Read_File import *
import os


print("====================================")
print("Welcome to my first STIMA project")
print("Kharris Khisunica - 13522051")
print("====================================")
print(""" 
  _____           _                  _   ____                      _     
 |  __ \         | |                | | |  _ \                    | |    
 | |__) | __ ___ | |_ ___   ___ ___ | | | |_) |_ __ ___  __ _  ___| |__  
 |  ___/ '__/ _ \| __/ _ \ / __/ _ \| | |  _ <| '__/ _ \/ _` |/ __| '_ \ 
 | |   | | | (_) | || (_) | (_| (_) | | | |_) | | |  __/ (_| | (__| | | |
 |_|   |_|  \___/ \__\___/ \___\___/|_| |____/|_|  \___|\__,_|\___|_| |_|
                                                                              
""")                                                                     

print("====================================\n")

                                                                                                                                                                                             


"Clear Terminal Windows dan Linux"

"Minta Input Nama File. Harus .txt"

#Get Data From File

#Input nama file dan validasi
while True:
  filename = input("Please input the input's .txt file: ")
  
  if check_filename(filename):
    print(f"Horray ! The file '{filename}' has been found. Let's Proceed !")
    break


input_file = open(filename, 'r')

#Input dari file ke array
isi_file = [line.strip() for line in input_file.readlines()]


#Ekstrak variabel dari array isi_file
buffer = int(isi_file[0])
matrix_width = int(isi_file[1].split()[0])
matrix_height = int(isi_file[1].split()[1])


#ekstrak matriks dari array ke matriks
matrix = []
element = []
row = []
for i in range (matrix_height):
  for j in range (matrix_width):
    element.append(isi_file[2+i].split()[j])
    element.append(False)
    element.append(j+1) #Absis token
    element.append(i+1) #Ordinat token
    row.append(element)
    element = []
  matrix.append(row)
  row = []
  

idx = matrix_height + 2 #Idx baru

n_seq = int(isi_file[idx])
print(n_seq)

idx = idx + 1 #Update
seq_all = []
for i in range (0,2*n_seq,2):
  temp = []
  point = int(isi_file[idx+1])
  seq = isi_file[idx].split()
  temp.append(point)
  temp.append(seq)
  idx = idx+2
  seq_all.append(temp)
 

print(seq_all)


#Proses
start_time = start_time()











end_time = end_time()

total_time = (end_time - start_time)*1000

#output ke layar

while True:
  input_solusi = input("Apakah ingin menyimpan solusi? (y/n): ")
  print("\t")
  if (input_solusi == 'y'):
    write_solution()
    break
  elif (input_solusi == 'n'):
    break  




if __name__ == "__main__":
  print(f"Isi file: {isi_file}")
  print(f"Banyak Buffer: {buffer}")
  print(f"Matrix Width: {matrix_width}")
  print(f"Matrix Height: {matrix_height}")
  print(f"Matriks: {matrix}")
  print(f"Total time: {total_time} ms")

input_file.close()


