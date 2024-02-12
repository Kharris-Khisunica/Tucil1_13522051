

from Movement import *
from File_Manipulation import *
from Matrix import *

#Kamus
Mark = "."



#Show Greeting
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


#ekstrak matriks dari array isi_file ke matriks
matrix = []
for i in range (matrix_height):
  row = []
  for j in range (matrix_width):
    element = []
    element.append(isi_file[2+i].split()[j]) #Token
    element.append(False) #Flag untuk menentukan apakah suatu token sudah dilalui atau belum
    element.append(j+1) #Absis token
    element.append(i+1) #Ordinat token
    row.append(element) 
  matrix.append(row)
  
  
#Ekstrak banyak sequence dan sequence+poin ke dalam suatu array
idx = matrix_height + 2 #Idx baru

n_seq = int(isi_file[idx])
print(n_seq)

idx = idx + 1 #Update
seq_all = []
for i in range (0,2*n_seq,2):
  temp = []
  point = int(isi_file[idx+1]) #Point suatu sequence
  seq = isi_file[idx].split() #Sequence
  seq.append(Mark) #Input Mark untuk menentukan akhir sequence
  temp.append(point)
  temp.append(seq)
  idx = idx+2
  temp.append(False) #Initial state, seq belum ditemukan. 
  seq_all.append(temp)

#Proses
start_time = start_time()

all_solution = [] #Inisiasi array yang menampung total poin[0], seluruh token True[1], dan Koordiat token[2]

#Cek apakah ada starter sequence dalam row pertama


if check_starter_exist_at_first_row(matrix, matrix_width, matrix_height, seq_all, n_seq):
  #Starter ditemukan di row pertama

  #Ambil semua seq yang memenuhi syarat

  first_row_seq_all = starter_exist_at_first_row(matrix, matrix_width, matrix_height, seq_all, n_seq)

  #Cek token apakah ada token ke-2 di bawahnya. 
  for first_row_seq in first_row_seq_all: #Cek per avail_seq [[absis,ordinat], [seqs yang mengandung]]
    for seq in first_row_seq[1]:
      #cek token ke-2 ada atau Mark (size == 1)
      if seq[1][1] != Mark: #Seq_size > 1
        Cek = check_vertical(matrix, seq[1][1], first_row_seq[0][0], first_row_seq[0][1], matrix_width, matrix_height)

        if Cek: #Ditemukan 
          #Ubah State 

          #Masukin Seq ke list kalau dia masuk itungan -> lanjut ke hitung ke-n


      else:
        temp = []
        point = seq[0]
        temp.append(point)
        


  #Didapat seq yang memiliki
  #Cek token next sampai Mark lewat check_all_direction


  

#Cek kasus kalau tidak ditemukan dalam row pertama
else: 
  " "











#Dapatkan Solusi Terbaik
best = best_solution(all_solution)


end_time = end_time()

total_time = (end_time - start_time)*1000


#Output Solusi ke layar dan keluarkan prompt apakah mau menyimpan ke dalam .txt
print_solution(best, total_time)






if __name__ == "__main__":
  print(f"Isi file: {isi_file}")
  print(f"Banyak Buffer: {buffer}")
  print(f"Matrix Width: {matrix_width}")
  print(f"Matrix Height: {matrix_height}")
  print(f"Matriks: {matrix}")
  print(f"Sequence all: {seq_all}")
  print(f"Total time: {total_time} ms")

input_file.close()


