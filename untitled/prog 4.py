star=int(input("Input a number:"))
n=0
m=1
for m in range (star+3):
    print(" " * star,"*"*m)
    star=star-1
    m=m+m-2
    print(" ")
