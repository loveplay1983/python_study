## dictionary is key value pair in python, aka , associative array, mapping
#
#dic = {'a':1, 'b':2, 'c':3}
#print(dic['a'])
#
## add new entry
#dic['d'] = 100
#for i in dic:
#    print(i)
#
#en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
#print(en_de)
#print(en_de["red"])
#de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
#print("The French word for red is: " + de_fr[en_de["red"]])
#
## only immutable data types can be used as keys
#
## dictionary of dictionary
#en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
#de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
#
#dictionaries = {"en_de" : en_de, "de_fr" : de_fr }
#print(dictionaries["de_fr"]["blau"])
#
#"""
#Operator
#Explanation
#len(d)
#returns the number of stored entries, i.e. the number of (key,value) pairs.
#del d[k]
#deletes the key k together with his value
#k in d
#True, if a key k exists in the dictionary d
#k not in d
#True, if a key k doesn't exist in the dictionary d
#"""
#
## mapping of latin chars to morsecode
#morse = {
#        "A" : ".-",
#        "B" : "-...",
#        "C" : "-.-.",
#        "D" : "-..",
#        "E" : ".",
#        "F" : "..-.",
#        "G" : "--.",
#        "H" : "....",
#        "I" : "..",
#        "J" : ".---",
#        "K" : "-.-",
#        "L" : ".-..",
#        "M" : "--",
#        "N" : "-.",
#        "O" : "---",
#        "P" : ".--.",
#        "Q" : "--.-",
#        "R" : ".-.",
#        "S" : "...",
#        "T" : "-",
#        "U" : "..-",
#        "V" : "...-",
#        "W" : ".--",
#        "X" : "-..-",
#        "Y" : "-.--",
#        "Z" : "--..",
#        "0" : "-----",
#        "1" : ".----",
#        "2" : "..---",
#        "3" : "...--",
#        "4" : "....-",
#        "5" : ".....",
#        "6" : "-....",
#        "7" : "--...",
#        "8" : "---..",
#        "9" : "----.",
#        "." : ".-.-.-",
#        "," : "--..--"
#        }
#
#print(len(morse))
#print('a' in morse)
#
#########################################################################
## pop popitem
#
## pop
#a = {'a':1, 'b':2}
#b = a.pop('a')
#print(a, b)
#
#
## if the content to pop doesn't exist, we can add extra parameter to
## prevent error gets raised
#a = {'a':1, 'b':22, 'c':123, 'd':222}
#b = a.pop('f', 'default value')
#print(b)
#
## popitem - it is a method for dictionary which doesn't take any parameters and removes and returns an arbitrary (key,value) pair as 2-tuple.
#a = {'a':1, 'b':22, 'c':123, 'd':222}
#b = a.popitem()
#c = a.popitem()
#print(b, c)
#print(a)
#
## try to access a key which doesn't exist, you will error that's raised
## by using "in" key word to prevent such problem
#
#a = {'a':1, 2:1}
#print(a)
#
#if 3 in a:
#    print('3 is in a')
#else:
#    print('3 is not in a')
#
## using get method to avoid error that's raise for non-existed pair
## also get method allow to set up default value like popitem
#a = {'a':1, 'b':2}
#print(a.get('a'), a.get('c', 'default'))
#
###################################################################
## important method
########3############3#############################################
## copy
#a = {'a':1, 'b':2}
#b = a.copy()
#print(b['a'], a['a'])
#
## the above is shallow copy same as the shallow copy of list object
## if we use the shallow copy for simple dictionary is ok, but i will cause problem when confronting more complex structure where different dictionary variable references to the same dictionary object
#
#a ={
#    'A':{'a1':11,'a2':12, 'a3':13},
#    'B':{'b1':21, 'b2':22, 'b3':23}
#   }
#
#b = a.copy()
#a['A']['a1'] = 111
#print(b['A']['a1'])
#
## proper way to copy dictionary from preventing shallow copy issue
#
#a ={
#    'A':{'a1':11,'a2':12, 'a3':13},
#    'B':{'b1':21, 'b2':22, 'b3':23}
#   }
#
#b = a.copy()
#a['A'] = {'aa1':111,'aa2':222, 'aa3':333}
#print(a,'\n')
#print(b)
#
#
#
## clear the dictionary value by clear method
#a.clear()
#print(a)
#
## iterating and updating dictionary
## updating  -  merge the same key-val pair and put different element altogether
#a = {'a':1, 'b':2}
#A = {'a':1, 'B':2}
#a.update(A)
#print(a)
#
## iterating
#for k,v in a.items():
#    print(k,'-', v)
#
#
## performance comparison
#import time
#a = {'a':1, 'b':2, 'c':3}
#
#start = time.time()
#for val in a.values():
#    print(val)
#end = time.time() - start
#print('with values()', end)
#
#start = time.time()
#for k in a:
#    print(a[k])
#end = time.time() - start
#print('with dict[key] form', end)

##################################################################
# connection between list and dic
# l = {'a':1, 'b':2, 'c':3}
# print(list(l.items()))

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
# use zip() method to combine the 2 lists like a "zipper"
# turn the zip object into list by casting it with list
# finally turn the list object into dict by casting a dict()

dish_country_pair = zip(countries, dishes)
dish_country_list_pair = list(dish_country_pair)
dish_country_dict = dict(dish_country_list_pair)

for k, v in dish_country_dict.items():
    print(k, '-', v)

# the above code rather inefficient, we can apply dict function
# to zip object directly
a = [1,2,3,]
b = [11,22,33,a]
print(dict(zip(a,b)))

# everything in on step
# country_specialities_dict = dict(list(zip(["pizza", "sauerkraut", "paella", "hamburger"], ["Italy", "Germany", "Spain", "USA"," Switzerland"])))

# danger lurking
# python2.x zip object is a list where python3.x zip is an iterator which will exhaust themselves

a = [1,2,3]
b = ['a','b','c']
m = zip(a,b)

for i in m:
    print(i)
# each i in m gets printing out
for i in m:
    print(i)
# none print out



