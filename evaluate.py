#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np
steps = 10 		#measured steps
step = 10		#elements increased each step(kB)
iters =100		#measured iterations per step
sigma = 20
subprocess.Popen(['g++','PatternSearcher.cpp','-o','experimento']).communicate()
subprocess.Popen(['gcc','gentext.c','-w','-o','generador']).communicate()
#considero alfabeto fijo con tamaño 20
sizes  = range(step,(steps+1)*step,step)
x = np.array(sizes)
y = np.array([])
e = np.array([])
#mejor caso
kmpbm = np.array([])
bmbm = np.array([])
bfbm = np.array([])
kmpbe = np.array([])
bmbe = np.array([])
bfbe = np.array([])
#peor caso
kmpw = np.array([])
bmw = np.array([])
bfw = np.array([])
#texto natural
kmpn = np.array([])
bmn = np.array([])
bfn = np.array([])
#p = subprocess.Popen(['./generadorpat','patrones','10',str(sigma)],stdout = subprocess.PIPE)
out,err = p.communicate()
p = subprocess.Popen(['./generador','patron','1','1','1'],stdout = subprocess.PIPE)
out,err = p.communicate()
	
#mejor caso
for i in sizes:
	print(i)
	#texto
	p = subprocess.Popen(['./generador','texto',str(i),'1','0'],stdout = subprocess.PIPE)
	out,errorbarr = p.communicate()
	p = subprocess.Popen(['./experimento','texto','patrones',str(iters)],stdout = subprocess.PIPE)
	out,err = p.communicate()

	tiempos = map(float,out.split())
	tiempos = np.array(tiempos)
	kmp = tiempos[::3]
	bm = tiempos[1::3]
	bf = tiempos[2::3]
	kmpbm = np.append(kmpbm,np.mean(kmp))
	bmbm = np.append(bmbm,np.mean(bm))
	bfbm = np.append(bfbm,np.mean(bf))
	kmpbe = np.append(kmpbe,np.std(kmp))
	bmbe = np.append(bmbe,np.std(bm))
	bfbe = np.append(bfbe,np.std(bf))
plt.figure(1)
plt.title("Text size vs time")	
plt.xlabel("Text size [kB]")
plt.ylabel("Time [ms]")
plt.yscale('log')
#plt.ylim([1e-4,1e-2])
plt.errorbar(x,kmpbm,kmpbe,linestyle='-', marker='x',label='KMP')
plt.errorbar(x,bmbm,bmbe,linestyle='-', marker='x',label='Boyer Moore')
plt.errorbar(x,bfbm,bfbe,linestyle='-', marker='x',label='Brute Force')
plt.legend()
	

exit(0)
sizes = range(100,1001,100)
x2 = np.array(sizes)
p = subprocess.Popen(['./generador','texto','100',str(sigma)],stdout = subprocess.PIPE)
out,err = p.communicate()

for i in sizes:
	print(i)
	p = subprocess.Popen(['./generadorpat','patrones',str(i),str(sigma)],stdout = subprocess.PIPE)
	out,err = p.communicate()
	p = subprocess.Popen(['./experimento','texto','patrones',str(iters)],stdout = subprocess.PIPE)
	out,err = p.communicate()
	tiempos = map(float,out.split())
	tiempos = np.array(tiempos)
	sa = tiempos[1::3]
	bf = tiempos[2::3]

	#insert
	samm = np.append(samm,np.mean(sa))
	same = np.append(same,np.std(sa))
	bfmm = np.append(bfmm,np.mean(bf))
	bfme = np.append(bfme,np.std(bf))
print(samm)
print(same)
#insert plot
plt.figure(1)
plt.title("Text size vs time")	
plt.xlabel("Text size [kB]")
plt.ylabel("Time [ms]")
plt.yscale('log')
#plt.ylim([1e-4,1e-2])
plt.errorbar(x,sacm,sace,linestyle='-', marker='x',label='Suffix Array construction')
plt.errorbar(x,sanm,sane,linestyle='-', marker='x',label='Suffix Array total')
plt.errorbar(x,bfnm,bfne,linestyle='-', marker='x',label='Brute Force')
plt.legend()
#top plot
plt.figure(2)
plt.title("Pattern size vs search time")
plt.xlabel("Number of characters")
plt.ylabel("Time [ms]")
plt.errorbar(x2,samm,same,linestyle='-', marker='x',label='Suffix Array')
plt.errorbar(x2,bfmm,bfme,linestyle='-', marker='x',label='Brute Force')
plt.legend()
print("text size vs time")
print("N;SA total mean;SA total std;SA construction mean;SA construction std;BF mean;BF std")
for i in range(0,len(x)):
	print("%d;%g;%g;%g;%g;%g;%g"%(x[i],sanm[i],sane[i],sacm[i],sace[i],bfnm[i],bfne[i]))

print("pattern size vs time")
print("N;SA mean;SA std;BF mean;BF std")
for i in range(0,len(x)):
	print("%d;%g;%g;%g;%g;"%(x[i],samm[i],same[i],bfmm[i],bfme[i]))

plt.show()
