M=int(raw_input("Enter value of M:"))
N=int(raw_input("Enter value of N:"))

while True:
    if N==0:
        print "Greatest common divisor:%d"% M
        break
    else:
        T=N
        N=M %N
        M=T
