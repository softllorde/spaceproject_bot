class Player:

    def __init__(self, user_id, name, balance):
    	self._user_id = user_id
    	self._name = name
    	self._balance = balance

    def getUserId(self):
    	return self._user_id

    def setUserId(self, inId):
    	self._user_id = inId

    def getUserName(self):
    	return self._name;

    def setUserName(self, inName):
    	self._name = inName

    def getUserBalance(self):
    	return self._balance

    def setUserBalance(self, inBalance):
    	self._balance = inBalance

    def __del__(self):
        print("Delete Player object")