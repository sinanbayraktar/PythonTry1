class Animal:
    __name = ""
    __height = 0
    
    #constructor
    def __init__(self, name1, height1):
        self.__name = name1
        self.__height = height1
        
    def set_name (self, name1):
        self.__name = name1
        
    def get_name (self):
        return self.__name
    
    def set_height (self, height1):
        self.__height = height1
        
    def get_height (self):
        return self.__hight
    
    def type (self):
        print ("Animal")
        
    def speak (self):
        print ("my name is " + self.__name + " and i am " + str(self.__height) + " cm tall")
        
donkey = Animal ("ali", 10)
donkey.type()
donkey.speak()

class Bird(Animal):
    __sound = ""
    
    def __init__(self, name1, height1, sound1):
        self.__sound = sound1
        super(Bird, self).__init__(name1, height1)
        
    def set_sound (self, sound1):
        self.__sound = sound1
    
    def get_sound (self):
        return self.__sound
    
    def type (self):
        print ("Bird")
        
    def speak (self):
        return ("my name is " + self.__name + " and i am " + str(self.__height) + " cm tall and i say " + self.__sound)        
    
eagle = Bird ("ayşe", 5, "cik cik")
print (eagle.get_name())
print (eagle.get_sound())
eagle.type()
print (eagle.speak())
