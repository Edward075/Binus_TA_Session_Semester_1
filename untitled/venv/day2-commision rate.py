#num=input("Enter yo numbah:")
#ame= input ("Enter yo name:")
#comm=float(input("Enter sales volume:"))
#if comm>=0 and comm<=200:
    #print("$",comm *0.05 )
#elif comm > 200 and comm <=1000:
    #print((200*0.05)+((comm-200)*0.08))
#elif comm > 1000 and comm <=2000:
    #print ((200*0.05)+(800)*0.08+((comm-1000)*0.10))
#elif comm > 2000 :
    #print ((200*0.05)+(800)*0.08+((1000)*0.10)+(comm-2000)*0.12)
#else:
    #print( "wrong value")

star=int(input("insert number:"))
x=1
while x<star+1:
    print("*")
    x=x+1
    while x<star+1:
        print("*"*x)
        x=x+1

