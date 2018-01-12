# Lists

aList = [1, 2, 3, 4]
aListOfStrings = ['Apples', 'Oranges', 'Mangoes', 'Cherries']

print('Some items in a list')
print(aList)
print(aList[0])
print(aList[2])
print()

print('Some items in a list of strings')
for item in aListOfStrings:
    print(item)
print()

# Sets

aListOfDuplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
aSet = set(aListOfDuplicates)
print('A list of duplicates and a set from that list')
print(aListOfDuplicates)
print(aSet)
print()

# Tuples

aTuple = (1, 2)
print('A tuple and the items in it')
print(aTuple)
print(aTuple[0], aTuple[1])
print()

aTupleOfTuples = ((1, 2), (3, 4))
print('A tuple of tuples')
print(aTupleOfTuples[0], aTupleOfTuples[1])
print()

aListOfTuples = [(1, 1), (2, 2, 2), (3, 3, 3)]
print('A list of tuples')
for item in aListOfTuples:
    print(item)
print()

# Dictionary

print('A Dictionary and its entries')
aDictionary = {'Apples' : 'Fruit', 'Broccoli' : 'Vegetable'}
print(aDictionary)
print(aDictionary['Apples'])
print(aDictionary['Broccoli'])
print()

anEmptyDictionary = {}
anEmptyDictionary['One'] = 1

print('A modified empty dictionary')
print(anEmptyDictionary['One'])