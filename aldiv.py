def conv(l):
    s = ""
    for i in l:
        if i[0] >= 0 :
            if i[1] ==1:
                if i[0]==1:
                    s += " + x"
                else:
                    s += " + "+str(i[0])+"x"
            elif i[1] ==0:
                s += " + "+str(i[0])
            else:
                if i[0]==1:
                    s += " + x^"+str(i[1])
                else:
                    s += " + "+str(i[0])+"x^"+str(i[1])
        if i[0] < 0 :
            if i[1] ==1:
                if i[0]==-1:
                    s += "  -x"
                else:
                    s += "  -"+str(-i[0])+"x"
            elif i[1] ==0:
                s += "  -"+str(-i[0])
            else:
                if i[0]==-1:
                    s += "  -x^"+str(i[1])
                else:
                    s += "  -"+str(-i[0])+"x^"+str(i[1])
    return s[2:]+" "

def div(D,d, var = "x"):
    D = [ [int(i.split("x^")[j]) for j in [0,1]]  for i in D.split()]
    d  = [ [int(i.split("x^")[j]) for j in [0,1]] for i in d.split()]
    Q = []
    c = D[0][0] / d[0][0]
    p = D[0][1]-d[0][1]
    while p >= 0:
        Q.append( [ c , p ] )
        r = []
        for m in range(len(d)):
            r.append([-c*d[m][0],p+d[m][1]])
        for j in range(len(r)):
            flag = False
            for k in range(len(D)):
                if r[j][1] == D[k][1]:
                    D[k][0] += r[j][0]
                    flag = True
                    break
            if not(flag):
                D.append(r[j])
        for n in range(len(D)):
            if D[n][0] == 0:
                D.pop(n)
                break
        for i in range(len(D)):
            lr = D[i][0]
            pos = i
            for j in range(i+1,len(D)):
                if lr < D[j][0]:
                    lr =D[j][0]
                    pos = j
            D[i],D[pos]=D[pos],D[i]
        c = D[0][0] / d[0][0]
        p = D[0][1] - d[0][1]
    return conv(Q),D[0][0]

D = raw_input(" > Enter dividend: ")
d = raw_input(" > Enter divisor : ")
v = div(D,d)
print "Quotient : ", v[0]
print "Remainder : " , v[1]
        
