

from Sequence import *
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

filename = f"./Tucil1_13522051/test/{filename}"
input_file = open(filename, 'r')

#Input dari file ke array
isi_file = [line.strip() for line in input_file.readlines()]


#Ekstrak variabel dari array isi_file
n_buffer = int(isi_file[0])
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
start_time = time.time()

"""
row_best = [] #Menyimpan total poin[0], isi buffer[1], dan koordidnat token[2] dengan poin terbaik untuk koordinat (i,1)
buffer = []
koordinat = []
best = None


for i in range (1,matrix_width+1):
  posisi_buffer = 0
  all_solution = [] #Inisiasi array yang menampung total poin[0], seluruh token True[1], dan Koordiat token[2]
  
  
  #input token (i,1)
  posisi_buffer += 1
  if posisi_buffer <= n_buffer:
    mark_token(matrix, i, 1, buffer, koordinat)


  for j in range (1, n_seq+1) :
    first = get_nth_token_a_sequence(seq, 1, j)
    if first == get_token(matrix,i,1):
      #lanjut first_found
    
      best_first_found = first_found()
    else:
      #lanjut first_not_found
      
      best_first_not_found = first_not_found()

    
    seq_best = 

    


  row_best.append(seq_best)


#Dapatkan Solusi Terbaik
best = best_solution(row_best)

"""
end_time = time.time()

total_time = (end_time - start_time)*1000


#Output Solusi ke layar dan keluarkan prompt apakah mau menyimpan ke dalam .txt
#print_solution(best, total_time)
print_solution(None, total_time)




input_file.close()


