class Protected:
    def __init__(self):
        self.__privateVar = 13

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(26)
obj.getPrivate()

class Protected:
    def __init__(self):
        self.protectedVar = 0

obj = Protected()
obj._protectedVar = 45
print(obj._protectedVar)
