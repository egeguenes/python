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

# one can also compare 3 numbers : a < b <= c

# there are no switch statements, rather we are using elif (else if)

# there are also no break statements in if statements!!!, which we are using in java and C

# for i in range[1,2,3] --> for statement rather than an array also ,,for i in range (1,4)'' can be used. 4 nicht enthalten!

# while a == 0 : --> while statement

# in loops it is allowed to use break and continue!

# functions can be identified with the key word "def"

# def functionName( a , b , c = None ) : --> None means that the function can be called only with the a and b variables

# class ClassName( InheritedClassName1 , InheritedClassName2 ) : 
# def __init__(self , a , b , c ): --> self always the first argument
# self.a = a --> public | self._a = a --> protected | self.__a = private 
# def functionInTheClass(self , a , b) : "nextLine" return x * y + self.__c

# try: "nextLine" raise PatatesError("That is a PatatesError")
# except: 

# try: "nextLine" 1/0
# except zeroDivisionError es e: "nextLine" print("Divided by zero: {}".format(e)) --> an exception can be catched with the keyword as | the first e is then used in the format(e)

# Each .py file is one module
# import foo
# f = foo.Foo( 0 , 1 , 2 )
# x = f.functionName(4 , 2 )

# importing specific functions/classes only
# from foo import Foo
# f = Foo( 0 , 1 , 2 )
# x = f.functionName( 4 , 2 )

# modules are organized as packages | packages are ,,folders'' containing modules
# must contain a __init__.py module

# Phyton offers a huge standart library
# import os.path as path
# fileName = path.basename("/usr/bin/python")
# pypath = path.join( "" , "usr" , "bin" , filename )

# use a dedicated main function --> def main() : 
# if __name__ == "__main__" : "nextLine" main()

""" this is a comment, that i can have for more than one line
		line 2
		line 3
		line 4 and its gonna end here """

# end of the comment codes and i hope i will be using these information and use python effectively with its help
























