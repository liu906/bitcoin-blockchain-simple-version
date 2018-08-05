import numpy as np
import matplotlib.pyplot as plt

sum = 21000000
revenue = 50
time = 0
block = 0
begin = [2008,]

year_revenue = [50,]
year_total = [21000000,]
while sum<0.0001 :
	if (block==210000) :
	    revenue = revenue/2
	    block = 0
	if( time%525600==0) :
		begin.append(begin[-1]+1)
		year_revenue.append(revenue)
		year_total.append(sum)

	#print("time = ",time)
	#print("sum = ",sum)
	time = time+10
	block = block + 1
	sum -= revenue

print("result is ",time)

plt.figure()
plt.plot(begin,year_revenue,'-',blue)
plt.plot(begin,year_total,'-',red)
plt.show()



