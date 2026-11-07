import plants
import alttraverse

world_size = get_world_size() - 1
directions = [North, South]

		
def next_column():
	move(East)
	task()

def main():
	while True:
		plants.tree()
		
		# the traversal with plant
		for i in range(get_world_size()):
			direction = directions[i % 2]
			
			alttraverse.traverse(direction)
			
			if i < world_size:
				move(East)
				if i % 2 == 0:
					plants.tree()
				else:
					plants.bush()
			
		# Reset
		for i in range(world_size):
			move(West)
			if can_harvest():
				harvest()

if __name__ == "__main__":
	main()