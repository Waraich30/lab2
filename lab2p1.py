c=input("x")

x=[4,6,9,12,17,22,27,33,44]
for i in range(0,9):
    if (x[i]>x[i+1]):
     c=x[i]
    x[i]=x[x+1]
    x[x+i]=c
