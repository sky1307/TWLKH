import numpy as np 

n = 30
m = 72

xh = np.random.randint(100,size=n)
yh = np.random.randint(100,size=n)
vh = np.random.randint(int(60*n/5+1),int(100*n/5+1),size=n)

xc = np.random.randint(100,size=m)
yc = np.random.randint(100,size=m)
vc = np.random.randint(int(20*n/5+1),int(30*n/5+1),size=m)

data = "{} {}\n".format(n,m)
for i in range(n):
    temp = "{} {} {}\n".format(xh[i],yh[i],vh[i])
    data += temp
for j in range(m):
    temp = "{} {} {}\n".format(xc[j],yc[j],vc[j])
    data += temp

with open("Data test/data_test_{}_{}.txt".format(n,m),"w+") as f:
    f.write(data)