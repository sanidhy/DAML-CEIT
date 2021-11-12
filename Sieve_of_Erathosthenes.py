def sieve(n):
    l=[True for i in range(n+1)]
    l[0]=False
    l[1]=False

    i=2
    while(i*i<=n):
        if (l[i]==True):
            j=i*i
            while(j<=n):
                l[j]=False
                j+=i
        i+=1
    
    for i in range(n):
        if l[i]==True:
            print(i)

n=int(input('Enter no'))
sieve(n)