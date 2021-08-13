class idol(object):
	'''偶像类的创建例子'''
	
	def __init__ (self, name, place, rank):
		self.name = name
		self.place = place
		self.rank = rank
		
	def __str__ (self):
		return f"<偶像名：{self.name}({self.place},排名第{self.rank})>"
		
	def dance(self):
		print("O(∩_∩)O哈哈~")
		print(self.name)
		print(self.place)
		print(self.rank)

if __name__ == '__main__':
	Air = idol('Air','BJ',14)
	print(Air.name)
	print(Air.place)
	print(Air.rank)
	print(Air)
	Air.dance()