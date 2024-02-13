
from Matrix import *

def check_vertical (matrix, token_yang_dicari, absis, ordinat, width, height):
    i = 0
    Flag = False
    while (i<=height and not Flag):
        if matrix[i-1][absis-1][0] == token_yang_dicari and (i != ordinat):
            Flag = True
    #i == height+1 or Flag
    if Flag:
        return True
    else:
        return False

def check_horizontal (matrix, token_yang_dicari, absis, ordinat, width, height):
    j = 1
    Flag = False
    while (j<=width and not Flag):
        if matrix[ordinat-1][j-1][0] == token_yang_dicari and (j != absis):
            Flag = True
        j += 1
    #i == width+1 or Flag
    if Flag:
        return True
    else:
        return False
    

def check_first (matrix, token, absis, ordinat, width, height):
#Mengecek apakah dibawah row pertama ditemukan lanjutan, untuk token ke-2
#untuk kasus 1 = starter ditemukan di row pertama atau token ke-1
#untuk kasus 2 = starter tidak ditemukan di row pertama. Jika ditemukan maka 
#akan mengembalikan nilai True
    found_vertical = check_vertical (matrix, token, absis, ordinat, height)

    if found_vertical:
        change_token_state(matrix,absis,ordinat)
        return True


def check_starter_exist_at_first_row (matrix, width, height, seq_all, n_seq):
#Fungsi yang mengecek apakah ada token ke-1 dari salah satu atau lebih sequencer dalam row pertama
    
    for i in range (width):
        token = matrix[0][i][0] #token di koordinat (i,1)
        for k in range (n_seq):
            if seq_all[k][1][0] == token: #Jika starter sequencer == token
                return True
    return False

    

def starter_exist_at_first_row (matrix, width, height, seq_all, n_seq):
#Fungsi untuk mengambil data setiap sequencer yang token pertamanya ditemukan dalam baris pertama matriks. 

    avail_seq = [] #Array berisi sequencer-sequencer yang token pertamanya memiliki koordinat (i,1) dan token 
    #[[[absis,ordinat], [seq1, seq2, ... ]], [token2, [seq1, seq2, ... ]], ..., [token-n, [seq1, seq2, ... ]]]
    #seq1 = [point, [token...Mark], F/T]
    for i in range (width):
        row = []
        seq = [] #Array yang berisi Sequence yang token pertamanya koordinat (i, 1)
        token_absis = i
        token_ordinat = 0
        token = matrix[token_ordinat][i][0] #token di koordinat (i,1)
        
        for k in range (n_seq):
            if seq_all[k][1][0] == token: #Token pertama seq ke-k == token koordinat (i,1)
                seq.append(seq_all[k])
        row.append(token_absis)
        row.append(token_ordinat)
        row.append(seq)
        avail_seq.append(row)
    
    return avail_seq


def get_nth_token_a_sequence (seq, nth, nseq):
#Mendapatkan token ke-n dari sequence ke-nseq
    return seq[nseq-1][1][nth-1]


def mark_token (matrix, x,y, buffer, koordinat):
#Mencopy token dan koordinat lalui mengubah state token menjadi telah dilalui. 
    buffer.append(get_token(matrix, x, y))
    change_token_state(matrix,x,y)
    koordinat.append([get_absis(matrix, x,y), get_ordinat(matrix, x,y)])


def first_found (matriks, x, y, seq, nseq, posisi_buffer, n_buffer, buffer, koordinat):
    n_start = 2
    n = n_start

    
            


