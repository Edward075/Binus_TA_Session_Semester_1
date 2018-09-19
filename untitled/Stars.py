print("Triangles app")
star=int(input("insert number:"))
temp1=star
temp2=star
temp3=star
print("")
print("(1)")
for n in range (0,star+1):
    print("*" * n)
print(" ")
print("(2)")
for n in range (0,star+1):
    print("*" * temp1)
    temp1-=1
print("(3)")
for n in range(0, star + 1):
    print(" " * n,"*" * temp2)
    temp2-=1
print("(4)")
for n in range(0, star + 1):
    print(" " * temp3,"*" * n)
    temp3-=1
print("(5)")
for n in range(0,star):
    for o in range(0,star-n):
        print(end=" ")
        print(end=" ")
    for o in range (0,n+1):
        print("*",end=" ")
    for o in range (0,n):
        print ("*",end=" ")
    print("")
print(" ")
print("(6)")
for n in range(0,star):
    for o in range(0, n+1):
        print(end=" ")
        print(end=" ")
    for o in range(0,star-n):
        print(" ",end="*")
    for o in range(0, star - n-1):
        print(" ",end="*")
    print("")
print("")
print("(7)")
for n in range(0, star):
    for o in range(0, star - n):
        print(end=" ")
        print(end=" ")
    for o in range(0, n + 1):
        print("*", end=" ")
    for o in range(0, n):
        print("*", end=" ")
    print("")
for n in range(0,star):
    for o in range(1):
        print(" ",end="")
    for o in range(0, n+1):
        print(end=" ")
        print(end=" ")
    for o in range(0,star-n-1):
        print(" ",end="*")
    for o in range(0, star - n-2):
        print(" ",end="*")
    print("")
print("")
#Teehee
