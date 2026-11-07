import plants

def traverse(direction):
	for i in range(get_world_size() - 1):
		move(direction)

		if i % 2 == 0:
			plants.bush()
		else:
			plants.tree()