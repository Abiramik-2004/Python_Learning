from abc import ABC, abstractclassmethod
class Calculator(ABC):
    @abstractclassmethod
    def calculate(self,a,b):
        pass
class Addition(Calculator):
    def calculate(self,a,b):
        return a+b

class Subraction(Calculator):
    def calculate(self, a, b):
        return a-b

class Multiplication(Calculator):
    def calculate(self, a, b):
        return a*b

class Division(Calculator):
    def calculate(self, a, b):
        return a/b