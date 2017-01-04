# Create a list.
elements = []
#loop variables
i=0
j=0

# Append empty lists in first two indexes.
elements.append([])
elements.append([])

# Add elements to empty lists.
elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)

# Display top-left element.
print(elements[0][0])

# Display entire list.
print(len(elements))

while ( i < len(elements) ):
	i=i+1
	while ( j < len(elements) ):
		j=j+1
		print elements[i][j]
