class Point():
	"""docstring for Point"""
	def __init__(self, x,y):	
		self.x=x
		self.y=y

	def __eq__(self,that):
		if not isinstance(that,Point):
			return False
		return self.x==that.x and self.y==that.y

	def __hash__(self):
		return 22*(12*self.x+self.y)

if __name__=='__main__':
	p1=Point(1,2)
	p2=Point(1,2)
	pset={p1:1,p2:2}
	for x in pset.items():
		print x
	