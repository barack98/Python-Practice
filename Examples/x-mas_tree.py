rows = input('Enter the No. of rows: ')

rows = int(rows)

#get the starting space for the top of the tree
spaces = rows - 1

#There is one hash to start that will be incremented
hashes = 1

#save stump spaces till later
stump_spaces = rows - 1

#Make sure the right number of rows are printed
while rows != 0:
#print the spaces
	for i in range(spaces):
		print(' ', end="")

#print the hashes
	for i in range(hashes):
		print('#', end="")

#Newline after each row is printe
	print()

#spaces is decremented by 1 each time
	spaces -= 1

#hashes is incremented by 2 each time
	hashes += 2

#decrement tree height each time to jump out of the loop
	rows -= 1

#print the spaces before the stump and then the hash
for i in range(stump_spaces):
	print(' ', end="")

print("#")