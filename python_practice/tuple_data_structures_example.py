#Tuple
tup1 = (1, 2, 3, 4, 5)
tup2 = ("a", "b", "c")

#tuple can added only with tupple
tup3 = tup1 + tup2
print(tup3)

#few Basic operations
#len() for length
print("length", len(tup3))

#for concatenation '+'
print("tuple1 + tuple2", tup1 + tup2)

#to check contains or not returns boolean value
print(3 in tup2)

#iteration
for element in tup3:
	print (element)