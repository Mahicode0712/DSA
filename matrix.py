def display(mat,title=""):
    if title:
        print(f"{title}:")
        for row in mat:
            print("" + "".join(f"{x:>4}" for x in row))

def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def add_matrix(A,B):
    return [[A[i][j] + B[i][j] 
             for j in range(len(A[0]))] 
             for i in range(len(A))]

def multiply_matrix(A,B):
    m,k,n = len(A), len(A[0]), len(B[0])
    C= [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for l in range(k):
                C[i][j] += A[i][l] * B[l][j]
    return C

def rotate_90_clockwise(mat):
    n= len(mat)
    for i in range(n):
        for j in range (i+1,n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for row in mat:
        row.reverse()
    return mat

def is_symmetric(mat):
    n=len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != mat[j][i]:
                return False
    return True

def sparse_to_list(mat):
    return [(i,j,mat[i][j])
            for i in range(len(mat)) 
            for j in range(len(mat[0])) 
            if mat[i][j] != 0]  
#__________________________DEMO___________________________#
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
c = [[1,2,3],[4,5,6],[7,8,9]]
symm = [[1,2,3],[2,4,5],[3,5,6]]
sparse = [[0,0,3],[0,0,0],[7,0,0]]
display(A,"Matrix A")
display(B,"Matrix B")
display(transpose(A),"Transpose of A")
display(add_matrix(A,B),"A + B")
display(multiply_matrix(A,B),"A * B")
display(rotate_90_clockwise(A),"A rotated 90 degrees clockwise")
print(f"Is  symmetric?, {is_symmetric(symm)}")
print(f"Sparse representation of A: {sparse_to_list(A)}")

            

