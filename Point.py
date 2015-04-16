class Point(object):
	"""docstring for Point"""
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = x
		self.y = y

	def __str__(self):
		""""""
		return 'point object at ({}, {})'.format(self.x, self.y)

	def __add__(self, other):
		""""""
		return self.x + other.x, self.y + other.y

	def distance(self, other):
		""""""
		from math import hypot
		math.hypot(self.x - other.x, self.y - other.y)
		# nice little comment here


##this is something that i want to change
# some rad shit 
