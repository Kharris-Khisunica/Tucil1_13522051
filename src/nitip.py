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




