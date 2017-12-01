# class MathDojo(object):
# 	def __init__(self):
# 		self.total = 0

# 	def add(self, *args):
# 		for i in args:
# 			self.result += i
# 		return self
	
# 	def subtract(self, *args):
# 		for i in args:
# 			self.result -= i
# 		return self

# md = MathDojo()
# md.add(2).add(2,5).subtract(3,2).result


class MathDojo(object):
	def __init__(self):
		self.result = 0
	def add(self, *args):
		for i in args:
			if type(i) == list or type(i) == tuple:
				for k in i:
					self.result += k
			else:
				self.result += i
		return self
	def subtract(self, *args):
		for i in args:
			if type(i) == list or type(i) == tuple:
				for k in i:
					self.result -= k
			else:
				self.result -= i
		return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result	