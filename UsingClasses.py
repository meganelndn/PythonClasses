from MyClasses import Counter 
from MyClasses import Owner
from MyClasses import Dog
from MyClasses import Fish

# intellicence not always working - known error (it will not always tell/suggest us the functions/variables we have been using, but they are still there)

# Counter example

mycounter = Counter()
mycounter.count()
mycounter.count()
print("Value = ", mycounter.getValue())
mycounter.reset()
print("Value = ", mycounter.getValue())
mycounter.count()
print("Value = ", mycounter.getValue())


# Dog and Owner example

owner1 = Owner(1, "Jack")
print("First owner = number ", owner1.getOwnerid(), " : ", owner1.getOwnername())
owner2 = Owner(2.5, "Jill")
print("Second owner =", owner2.toString())

# dogs

dog1 = Dog("Fido", owner1)
print("First dog = number ", dog1.getDogid(), " ", dog1.getDogname(), "with owner name", dog1.getOwner().getOwnername())

dog2 = Dog(owner = owner1, dogname = "Pluto")
print("Second dog = number ", dog2.getDogid(), " ", dog2.getDogname(), "with owner name", dog2.getOwner().getOwnername())
# change owner object
dog2.setOwner(owner2)
print("Second dog = number ", dog2.getDogid(), " ", dog2.getDogname(), "with owner name", dog2.getOwner().getOwnername())

dog3 = Dog(owner = owner2)
print("Third dog = number ", dog3.getDogid(), " ", dog3.getDogname(), "with owner name", dog3.getOwner().getOwnername())
# change dog name
dog3.setDogname("Lady")
print("Third dog = number ", dog3.getDogid(), " ", dog3.getDogname(), "with owner name", dog3.getOwner().getOwnername())
print("Third dog =", dog3.toString())
print()


# fish with state examples

myfish = Fish("Gold fish")
print(myfish.toString())

# a little intermediate experiment
print()
dog4 = Dog("King", myfish)
print("Fourth dog = number ", dog4.getDogid(), " ", dog4.getDogname(), "with owner name", dog4.getOwner())
print("Fourth dog = number ", dog4.getDogid(), " ", dog4.getDogname(), "with owner name", dog4.getOwner().toString())

dog5 = Dog("Queen", 25)
print("Fourth dog = number ", dog5.getDogid(), " ", dog5.getDogname(), "with owner name", dog5.getOwner()) 
print()

# continue with fish
print(myfish.toString())
print(myfish.getType(), myfish.eat())
print(myfish.getType(), myfish.swim())
print(myfish.getType(), myfish.swim())
print(myfish.toString())
print(myfish.getType(), myfish.eat())
print(myfish.getType(), myfish.swim())
print(myfish.toString())
print(myfish.getType(), myfish.eat())
print(myfish.toString())
print(myfish.getType(), myfish.eat())