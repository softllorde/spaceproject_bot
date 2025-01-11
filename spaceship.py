class Spaceship:

	def __init__(self, id, name, type, hold_capacity, attack, defence):
		self._id = id
		self._name = name
		self._type = type
		self._hold_capacity = hold_capacity
		self._attack = _attack
		self._defence = _defence

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

	def getAttack(self):
		return self._attack

	def setAttack(self, inAttack):
		self._attack = inAttack

	def getDefence(self):
		return self._defence

	def setDefence(self, inDefence):
		self._defence = inDefence

	def __del__(self):
		print("Spaceship obj has been deleted")