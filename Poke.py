import random

map=[[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,2,2,2,0],[0,0,0,0,2,2,2,0],[0,0,2,2,2,2,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,2,2,0,0]]
tmap=[]
tmap=map
f=[]
def read():
	file=open("dat.txt","r")
	d=[]
	for r in file:
		raw=r.split(", ")
		d.append(raw[0])
		
		
	file.close()

def maps():
	for a in range(len(map)):
		for b in range(len(map)):
			if b%8==0:
				print("")
			print(map[a][b],end=" ")

		
		
	
n=0
read()
while n!=5:
	print(maps())
	
	for b in range(len(map)):
		for c in range(len(map)):
			if map[b][c]==1:
				f.extend([b,c])
	print("============")
	print("Menu")
	print("============")
	print("1. Move Up" )
	print("2. Move Down")
	print("3. Move Left")
	print("4. Move Right")
	print("5. Save and Exit")
	n=int(input( "Input : "))
	if n==1:
		f.append(f[0]-1)
		if f[2]<0:
			print("You cannot move that way!")
			print("")
				
		else:
			j=f[0]
			k=f[1]
			l=f[2]
			map[j][k], map[l][k]=map[l][k],map[j][k]
			if tmap[j][k]==2:
				map[j][k]=0
				if random.randint(1,101)<100:
					print("You encountered something!")

		
	elif n==2:
		f.append(f[0]+1)
		if f[2]>len(map)-1:
			print("You cannot move that way!")
			print("")
				
		else:
			j=f[0]
			k=f[1]
			l=f[2]
			print(f)
			map[j][k], map[l][k]=map[l][k],map[j][k]
			if tmap[j][k]==2:
				map[j][k]=0
				if random.randint(1,41)<100:
					print("You encountered something!")
			
			
		
	elif n==3:
		f.append(f[1]-1)
		if f[2]<0:
			print("You cannot move that way!")
			print("")
				
		else:
			j=f[0]
			k=f[1]
			l=f[2]
			map[j][k], map[j][l]=map[j][l],map[j][k]
			if tmap[j][k]==2:
				map[j][k]=0
				if random.randint(1,101)<100:
					print("You encountered something!")
	
	elif n==4:
		f.append(f[1]+1)
		if f[2]>len(map)-1:
			print("You cannot move that way!")
			print("")
		else:
			j=f[0]
			k=f[1]
			l=f[2]
			map[j][k], map[j][l]=map[j][l],map[j][k]
			if tmap[j][k]==2:
				map[j][k]==0
				if random.randint(1,101)<100:
					print("You encountered something!")
	elif n==5:
		temp=""
		file=open("dat.txt","w")
		temp=f[0],f[1]
		temp=str(temp)
		file.write(temp)
		file.close()
	
	else:
		print("Wrong input")
		
		