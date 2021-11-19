# counter

class Counter : 
    # constructor
    def __init__(self) : # self is a parameter
        self._value = 0
    # count method
    def count(self) :
        self._value = self._value + 1 # variables start with an underscore
    # reset
    def reset(self) : 
        self._value = 0
    # show value 
    def getValue(self) : 
        return self._value


# owner

class Owner :
    # constructor
    def __init__(self, ownerid, ownername) :
        self._ownerid = ownerid
        self._ownername = ownername
    # get 
    def getOwnerid(self) :
        return self._ownerid
    def getOwnername(self) : 
        return self._ownername
    # toString
    def toString(self) :
        return self.getOwnername() + " has id " + str(self.getOwnerid())

# dog

class Dog :
    # class variable
    _dogcounter = 0; # no self, so does not belong to object but to class Dog
    # constructor
    def __init__(self, dogname = "No name yet", owner = None) :
        Dog._dogcounter = Dog._dogcounter + 10
        self._dogid = Dog._dogcounter
        self._dogname = dogname
        self._owner = owner
    # get & set
    def getDogid(self) :
        return self._dogid
    def getDogname(self) :
        return self._dogname
    def getOwner(self) :
        return self._owner
    def setDogname(self, name) :
        self._dogname = name
    def setOwner(self, owner) :
        self._owner = owner
    # toString
    def toString(self) :
        return self.getDogname() + " has id " + str(self.getDogid()) + " and owner " + self.getOwner().getOwnername()


# fish

class Fish :
    # class variables - state values 
    NOT_HUNGRY = 0  # capitals : do not change value!
    LITTLE_HUNGRY = 1
    VERY_HUNGRY = 2
    # constructor 
    def __init__(self, type) :
        self._type = type
        self._hungry = Fish.NOT_HUNGRY
    # get
    def getType(self) :
        return self._type
    # swim 
    def swim(self) :
        if self._hungry < Fish.VERY_HUNGRY :
            self._hungry = self._hungry + 1
        return "swims"
    # eat
    def eat(self) :
        if self._hungry == Fish.NOT_HUNGRY :
            return "does not eat"
        elif self._hungry == Fish.LITTLE_HUNGRY :
            self._hungry =  Fish.NOT_HUNGRY
            return "eats a little"
        else : 
            self._hungry = Fish.NOT_HUNGRY
            return "eats a lot"
    # toString
    def toString(self) :
        return self.getType() + " is in hungry-state " + str(self._hungry)