class GeoObejct(object):
	"""docstring for GeoObejct"""
	def __init__(self, arg):
		super(GeoObejct, self).__init__()
		self.arg = arg
		

class GeoPoint(GeoObejct):
	"""docstring for GeoPoint"""
	def __init__(self, arg):
		super(GeoPoint, self).__init__()
		self.arg = arg
		

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
		
