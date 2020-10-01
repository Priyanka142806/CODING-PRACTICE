n= int(input())
while(n):
    d=c=0
    int_nos =input()
    ar=int_nos.split()
    d=abs(int(ar[0])-int(ar[1]))
    c=int(d/10)
    if(d%10>=1):
        c=c+1
    print(c)
    n=n-1  
