import numpy as np
#importing the numpy for faster calculation
class linear_regression():
	def __init__(self,a,b):#a and b are two list data sets
		self.a=a
		self.b=b
		if len(a)!=len(b):#check weather the list lengths are same or not
			print('Warning list is length is not equal')
		a_mean=np.mean(a)#mean of a
		b_mean=np.mean(b)#mean of b
		self.a_mean=a_mean#mean of a
		self.b_mean=b_mean#mean of b
		num=0
		den=0
		for i in range(len(a)):#iteratring through a and b to calculate m value
			num+=(a[i]-a_mean)*(b[i]-b_mean)
			den+=(a[i]-a_mean)**2
		m=num/den#m value
		c=b_mean-(m*a_mean)#c value
		self.m=m#making it acsessible to whole class
		self.c=c#''''''
		#print('Value of m is:{0} Value of c is:{1}'.format(m,c))
	def r_sq(self):
		num=0
		den=0
		pr=[]
		k=0
		for i in range(len(self.a)):
			pr.append(self.a[i]*self.m+self.c)
		for z in range(0,len(self.a)):
			num+=(self.b[i]-self.b_mean)**2
			den+=(self.b[i]-pr[i])**2
		print('Value of r-square is :{}'.format(1-(den/num)))
		if num/den==1:
			print('Perfect Slope!!')
	def predict(self,x):
		print('Predicted value of :{0} is {1}'.format(x,self.m*x+self.c))


		



