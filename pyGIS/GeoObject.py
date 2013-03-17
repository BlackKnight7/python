class GeoObejct(object):
	"""docstring for GeoObejct"""
	def __init__(self, arg):
		super(GeoObejct, self).__init__()
		self.arg = arg
		

class GeoPoint(GeoObejct):
	"""docstring for GeoPoint"""
	x=0.0
	y=0.0
	def __init__(self, x,y):
		super(GeoPoint, self).__init__()
		self.x=x
		slef.y=y
		

class GeoLine(GeoObejct):
	"""docstring for GeoLine"""
	def __init__(self, arg):
		super(GeoLine, self).__init__()
		self.arg = arg


class GeoPolygon(GeoObejct):
	"""docstring for GeoPolygon"""
	def __init__(self, arg):
		super(GeoPolygon, self).__init__()
		self.arg = arg
		
class GeoMultiPoints(GeoObejct):
	"""docstring for GeoMultiPoints"""
	def __init__(self, arg):
		super(GeoMultiPoints, self).__init__()
		self.arg = arg
		
