def reader (self, file):
	self.file = file
with open (self.file, "r") as r:
	return r.readlines()
f = reader("poem.txt")
