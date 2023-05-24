from __future__ import division
from math import atan,pi,sqrt
import matplotlib.pyplot as plt



# Calculate the arc Tan table once
ArcTanTable = []
for i in range(50):
  ArcTanTable.append(    atan( 2.0**(-1 * i) )    )
  
  
  
# Calculate the scaling factor K once
KN = []
value = 1.0
for i in range(50):
  value = value * sqrt(  1.0 + 2.0**(-2 * i)  )  
  KN.append(1.0 / value)
  
  
  

s=[]
c=[]
t=[]
co=[]
secant=[]
cosec=[]
iterations=50



#count=0
def tan():
	for i in range(0,361):
		if i==90 or i==270:
			#t.append(None)
			continue
		else:
			t.append(s[i]/c[i])
			secant.append(1/c[i])	
def cot():
	for i in range(0,361):
		if i==0 or i==180 or i==360:
			#t.append(None)
			continue
		else:
			co.append(c[i]/s[i])		
			cosec.append(1/s[i])

#calculating amplitudes of sin and cos in first quadrant	
for j in range(0,361):
	#count=j
	if j>270:
		j=j-360
	elif j>90:
		j=j-180
	
	beta = j* pi / 180.0

	
	Vx,Vy = 1.0 , 0.0

	for i in range(iterations):
		if beta < 0:
			Vx,Vy = Vx + Vy * 2.0**(-1 * i)  ,  Vy - Vx * 2.0**(-1 * i)
			beta = beta + ArcTanTable[i]
		else:
			Vx,Vy = Vx - Vy * 2.0**(-1 * i)  ,  Vy + Vx * 2.0**(-1 * i)
			beta = beta - ArcTanTable[i]

	Vx,Vy = Vx * KN[iterations - 1] , Vy * KN[iterations - 1] #Vx=cos amplitude ,#Vy=sin amplitude

	#t.append(Vy/Vx)
	
	if len(s)>90 and len(s)<=270: #for 2nd and 3rd quadrants
		s.append(-Vy)
		c.append(-Vx)
	else:				#for first and fourth quadrants
		s.append(Vy)
		c.append(Vx)
	#print ("Sin(%4.1f) = %14.12f  and  Cos(%4.1f) = %14.12f" % (count,s[count],count,c[count]))

tan()
cot()

##########   sin and cos ###########
plt.subplot(2,3,1)
plt.xlim([0,361])
plt.plot(s,'r',label='$sin(x)$') #sin
plt.plot(c,'g',label='$cos(x)$') #cos
plt.axhline(y = 0, color = 'k', linestyle = '-')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend()	

 ##########   tan ############
plt.subplot(2,3,2)
plt.xlim([0,361])
plt.plot(t,label='$tan(x)$')#tan
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend()		
plt.axhline(y = 0, color = 'k', linestyle = '-')


############# cot    ############
plt.subplot(2,3,3)
plt.xlim([0,361])
plt.plot(co,label='$cot(x)$')#tan
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend()		
plt.axhline(y = 0, color = 'k', linestyle = '-')

############# secant     ############
plt.subplot(2,3,4)
plt.xlim([0,361])
plt.plot(secant,label='$sec(x)$')#tan
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend()		
plt.axhline(y = 0, color = 'k', linestyle = '-')

############# cosec    ############
plt.subplot(2,3,5)
plt.xlim([0,361])
plt.plot(cosec,label='$cosec(x)$')#tan
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend()		
plt.axhline(y = 0, color = 'k', linestyle = '-')



plt.show()



	

