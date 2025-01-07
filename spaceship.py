class Spaceship:

	def __init__(self, id, name, type, hold_capacity):
		self._id = id
		self._name = name
		self._type = type
		self._hold_capacity = hold_capacity

	def getId(self):
		return self._id

	def setId(self, inId):
		self._id = inId

	def getName(self):
		return self._name

	def setName(self, inName):
		self._name = inName

	def getType(self):
		return self._type

	def setType(self, inType):
		self._type = inType

	def getHoldCapacity(self):
		return self._hold_capacity

	def setHoldCapacity(self, inHoldCapacity):
		self._hold_capacity = inHoldCapacity

	def __del__(self):
		print("Spaceship obj has been deleted")