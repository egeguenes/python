s = "I am a String"

n = len(s)

#print(s) --> "I am a String"
#print(n) --> 13

# Lists can contain different types of elements
list1 = ["s", "e", "c"]
list2 = ["tu-braunschweig" , 20 , 1.9]
list3 = list1 + list2

list3[3] = "tu-bs"
list3[-1] = 19
list3[-6] = 27

print(list3) # len(l3) --> 6 | 6 - 6 --> 0 | list3[0] --> 27

# item with - index --> arrayName[ len(arrayName) - negativeIndex ] = wished variable

# Tuples are similer to lists but they are immutable - they can not be changed

tuple1 = ("tu-bs" , 13 , 22)

# tuple1[2] = 17 --> error bc an element of a tuple can not be implemented

# Dictionaries Sequences(Tulips and Arrays) are indexed by numbers | Dicts can be indexed by any (immutable) type
# There are keys and values in dicts

dict1 = { 1 : "sec" , "tu-bs" : "de" , 20 : 1.9 } # 1 | "tu-bs" | 20 are the keys for the following values : "sec" | "de" | 1.9

# dict1.keys()   --> [ 1 , "tu-bs" , 20 ]
# dict1.values() --> [ "sec" , "de" , 1.9 ]
# dict1.items()  --> [ (1,"sec") , ("tu-bs","de") , .....]
# dict1[1] --> "sec" | dict["tu-bs"] --> "de"

# For if we use : | same for the else : | if we use if and else in one line --> c = ( 'equal' if a == b else 'unequal')

# comparison equality and logical operators are the same, like other programming languages 




