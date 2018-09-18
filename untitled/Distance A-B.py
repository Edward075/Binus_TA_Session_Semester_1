time=int(input("Insert Time:"))
acc=int(input("Insert Acceleration:"))
dist=int(input("Insert Distance:"))
u=int(0)
v=time*acc
maxdist=int(0.5 *acc* time*time)
limit=int(60)
for i in range(0,time+1):
     d= int(0.5 *acc* i*i)
     d= int(d/10)
     print("Duration",i,"Distance:",d*"*")
if v > limit :
    print("The person went over the speed limit.(The max speed was",v,"m/s")
else:
    print("The person did not went over the speed limit.(The max speed was",v,"m/s)")
if maxdist>= dist  :
    print("The person reached the destination.(Reached",maxdist,"m)")
else:
    print("The person did not reach the destination.(Reached",maxdist,"m)")
