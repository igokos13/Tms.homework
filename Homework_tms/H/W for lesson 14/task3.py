from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def speak(self):
        pass
    
    
class Dog(Animal):
        def speak(self):
            print('гав')
            
            
class Cat(Animal):
        def speak(self):
            print('мяу')
            
            
class AnimalFactory():
    def create_animal(self,type_animal):
        if type_animal== 'dog':
            return Dog()
        
        elif type_animal=='cat':
            return Cat()
        

factory = AnimalFactory()
dog = factory.create_animal('dog')
dog.speak()

cat= factory.create_animal('cat')
cat.speak()