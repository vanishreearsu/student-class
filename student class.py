class Student:
    def __init__(self):
        self._name = ""
        self._rollNumber = ""

    def getName(self):
        pass
        return self._name

    def setName(self, name):
        pass
        self._name = name

    def getRollNumber(self):
        pass
        return self._rollNumber

    def setRollNumber(self, rollNumber):
        pass
        self._rollNumber = rollNumber
s = Student()
s.setName("Vanishree Arasu")
s.setRollNumber("20PS3045")
print(s.getName()) 
print(s.getRollNumber()) 
