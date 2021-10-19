i=0
n1=0
n2=1
while (i<50):
    if(i<=1):
        next = i
    else:
        next = n1+n2
        n1=n2
        n2=next
    print(next)
    i=i+1