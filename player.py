class Player:

    def __init__(self, user_id, name, balance, spaceship):
        self._user_id = user_id
        self._name = name
        self._balance = balance
        self._spaceship = spaceship

    def getId(self):
    	return self._user_id

    def setId(self, inId):
    	self._user_id = inId

    def getName(self):
    	return self._name;

    def setName(self, inName):
    	self._name = inName

    def getBalance(self):
    	return self._balance

    def setBalance(self, inBalance):
    	self._balance = inBalance

    def getSpaceship(self):
        return self._spaceship

    def setSpaceship(self, inSpaceship):
        self._spaceship = inSpaceship

    def __del__(self):
        print("Player obj has been deleted")