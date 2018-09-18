sal=float(input("enter salary:"))
if sal>=40000:
    print("$",sal*0.30)
elif sal>=30000 and sal<40000:
    print("$",sal*0.25)
elif sal>=20000 and sal <30000:
    print(sal*0.20)
elif sal>=10000 and sal <20000:
    print ("$,",sal*0.15)
elif sal>=5000 and sal<10000:
    print ("$",sal*0.06)
elif sal>=0 and sal<5000:
    print("$",sal*0)
else:
    print("wrong input")
