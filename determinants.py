def mat_input():
    n = int(raw_input("Enter the order of matrix:"))
    M = []
    for  i in range(n):
        M.append([])
        for j in range(n):
            M[-1].append(float(raw_input(str(i+1)+","+str(j+1)+"-->")))
    return M

def minor(i,j,M):
    N = []
    for m in range(len(M)):
        if m != i:
            N.append([])
            for n in range(len(M)):
                if n != j:
                    N[-1].append(M[m][n])
    return N

def det(M):
    if len(M) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    else :
        sum = 0
        for  i in range(len(M)):
            sum +=M[0][i]*(pow(-1,i))*det(minor(0,i,M))
        return sum
