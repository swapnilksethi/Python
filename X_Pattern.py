from __future__ import print_function
i=0
j=6
for row in range(7):
	for col in range(7):
		if row==i and col==j:
			print("*",end="")
			i=i+1
			j=j-1
		elif row==col:
			print("*",end="")
		else:
			print(end=" ")
	print("\n")
print()