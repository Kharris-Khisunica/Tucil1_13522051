
def get_token (matrix, x, y):
    return matrix[y][x][0]

def get_state (matrix,x,y):
    return matrix[y][x][1]

def get_absis (matrix, x,y):
    return matrix[y][x][3]

def get_ordinat (matrix,x,y):
    return matrix[y][x][2]

def get_all_True (matrix, width, height):
#Mengembalikan sebuah array berisi token yang dilalui beserta dengan koordinatnya
    sol = [] 
    for i in range (height):
        for j in range (width):
            if get_state(matrix,i,j):
                token = get_token(matrix,i,j)
                coor = []
                coor[0] = get_absis(matrix,i,j) #Absis
                coor[1] = get_ordinat(matrix,i,j) #Ordinat
                sol.append(token)
                sol.append(coor)
    
    return sol



def change_token_state (matrix, x, y):
    matrix[y][x][1] = not matrix[y][x][1]

def change_seq_state (seq_all, n):
    seq_all[n][2] = not seq_all[n][2]

def get_total_point (seq_all, n_seq):
    total = 0
    for i in range (n_seq):
        if seq_all[i][2] == True:
            total += seq_all[i][0]

def reset_state (matrix, width, height):
    for i in range (height):
        for j in range (width):
            matrix[i][j][1] = False

def best_solution (all_solution):
#mengambil nilai terbesar dari solution yang memiliki poin >= 0. 
    max = float('-inf')
    best = None
    for solution in all_solution:
        point = solution[0]
        if point >= max and point>=0:
            best = solution
    
    return best

if __name__ == "__main__":
    print(best_solution([[-3,2], [-2,3]]))




        
