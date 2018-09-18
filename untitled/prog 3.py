star=int(input("Input a number:"))
n=int(1)
for n in range (star+1):
    print(" " * star,n * "*")
    n= n-1
    star=star-1

